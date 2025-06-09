import asyncio
import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from alembic.config import Config
from alembic import command
from apscheduler.triggers.cron import CronTrigger


from statistics_collector.app.parcer import parse_stat

def run_migrations():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    alembic_ini_path = os.path.join(base_dir, '..', 'alembic.ini')

    alembic_cfg = Config(alembic_ini_path)
    alembic_cfg.set_main_option("script_location", os.path.join(base_dir, 'database', 'alembic'))

    command.upgrade(alembic_cfg, 'head')

async def main():
    run_migrations()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(parse_stat, CronTrigger(minute=0))
    scheduler.start()

    try:
        while True:
            await asyncio.sleep(3600)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

if __name__ == "__main__":
    asyncio.run(main())