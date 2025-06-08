from statistics_collector.dependencies import database

from sqlalchemy import delete

async def clear_table(model):
    async with database() as session:
        await session.execute(delete(model))
        await session.commit()

async def save_stat_record(data: dict, model: any) -> None:
    async with database() as session:
        try:
            record = model(**data)
            session.add(record)
            await session.commit()
        except Exception as e:
            print(e)