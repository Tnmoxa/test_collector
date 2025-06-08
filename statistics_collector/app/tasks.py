from datetime import datetime
import requests

from cele.celery_app import celery_app
from app.models import StatRecord
from tarot.dependencies import sync_database


@celery_app.task
def parser():
    zodiacs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo',
               'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
    with sync_database() as db:
        for zodiac in zodiacs:
            response = requests.get('https://horo.mail.ru/prediction/' + zodiac + '/today/')
            stats = StatRecord()
            db.add(horoscope)
        db.commit()


if __name__ == '__main__':
    parser()