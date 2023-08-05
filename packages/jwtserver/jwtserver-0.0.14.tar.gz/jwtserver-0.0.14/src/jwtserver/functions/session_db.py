from jwtserver.database import AsyncSessionLocal


async def async_db_session():
    """Databases pool fabric connection, auto close connection"""
    async with AsyncSessionLocal() as session:
        yield session
