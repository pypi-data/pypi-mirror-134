from aioredis import Redis
from fastapi import Depends, HTTPException, Body
from secrets import token_hex
from starlette import status

from jwtserver.Google.Recaptcha_v3 import Recaptcha
from jwtserver.functions.SMSC import SMSCRULES
from jwtserver.app import app
from pydantic import BaseModel

from jwtserver.functions.init_redis import redis_conn

smsc = SMSCRULES()


class CheckCodeResponseModel(BaseModel):
    reg_token: str


@app.post("/api/v1/check_code/",
          description="User authorization by login and password",
          # response_description=response_description,
          response_model=CheckCodeResponseModel,
          tags=["Registration"]
          )
async def check_code(
        telephone: str = Body(...),
        code: int = Body(...),
        redis: Redis = Depends(redis_conn),
        recaptcha: Recaptcha = Depends(Recaptcha)
):
    """Checking the code from SMS or Call
    :param str telephone: Telephone number in international format
    :param int code: 4 digit verification code
    :param redis: Redis client
    :param recaptcha: Validate Google recaptcha_v3.md v3 [return True or HTTPException]
    :return: one-time token for registration
    """
    await recaptcha.set_action_name('SignUpPage/CheckCode').greenlight()

    code_method = await redis.get(telephone)
    if code_method:
        from_redis_code, method = code_method.decode('ascii').split(":")
        if int(from_redis_code) == code:
            reg_token = token_hex(16)
            await redis.set(f"{telephone}_reg_token", reg_token, 60 * 60)
            return {"reg_token": reg_token}

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Неверный код",
        )
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Нужно запросить новый код ",
    )
