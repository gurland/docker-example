from settings import TOKEN, CHANNEL_NAME
from celeryconfig import broker_url, result_backend
from models import Tweet
from time import sleep

from telegram import TelegramApi
from celery import Celery


tg_api = TelegramApi(TOKEN)
celery_app = Celery('tasks', broker=broker_url, backend=result_backend)


@celery_app.task
def post_tweets():
    tweets = Tweet.select()
    for tweet in tweets:
        tg_api.send_message(chat_id=CHANNEL_NAME, text=tweet.text)
        tweet.delete_instance()
        sleep(1)
