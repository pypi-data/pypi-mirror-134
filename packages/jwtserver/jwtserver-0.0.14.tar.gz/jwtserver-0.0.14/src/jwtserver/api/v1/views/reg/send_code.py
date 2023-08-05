from aioredis import Redis
from fastapi import Depends, HTTPException
from loguru import logger
from starlette import status

from jwtserver.functions.SMSC import SMSCRULES
from jwtserver.functions.init_redis import redis_conn
from jwtserver.app import app
from jwtserver.functions.config import load_config
from pydantic import BaseModel

smsc = SMSCRULES()
config_server = load_config().server
config_sms = load_config().sms


class Data(BaseModel):
    telephone: str


class ResponseSendCodeModel(BaseModel):
    send: bool
    time: int
    method: str


@app.post("/api/v1/send_code/",
          response_model=ResponseSendCodeModel,
          tags=["Registration"],
          description="Sending a code through a call or SMS",
          )
async def call_code(data: Data, redis: Redis = Depends(redis_conn), ):
    """Последние цифры номер это код"""
    if config_sms.ignore_attempts:
        await redis.delete(f"{data.telephone}_try_count")

    try_count = await redis.incr(f"{data.telephone}_try_count")
    block_ttl = await redis.ttl(f"{data.telephone}_try_count")
    code_is_send = await redis.get(data.telephone)

    if try_count <= config_sms.try_call:
        method_func = smsc.call
        next_method_name = "call"
    else:
        method_func = smsc.send_sms
        next_method_name = "sms"

    if try_count < (config_sms.try_call + config_sms.try_sms):
        if code_is_send:
            code, method = code_is_send.decode('ascii').split(":")

            ttl = await redis.ttl(data.telephone)
            logger.info("code is send")
            return {"send": True, "time": ttl, "method": method}
        code, time, error = await method_func(telephone=data.telephone)
        if error:
            logger.error(error)
            return {"send": False}

        await redis.set(data.telephone, f"{code}:{next_method_name}", time)
        await redis.expire(f"{data.telephone}_try_count", config_sms.block_time_minutes)
        return {"send": True, "method": next_method_name, "time": time}
    else:
        if not code_is_send:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail={"error": "Превышен лимит запросов", 'block_time': block_ttl}
            )

        code, method = code_is_send.decode('ascii').split(":")
        ttl = await redis.ttl(data.telephone)
        logger.info("code is send")
        return {"send": True, "time": ttl, "method": method}
