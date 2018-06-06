import os
import zmail
from flask import Flask, request
from celery import Celery

REDIS_CONFIG = 'redis://localhost:6379'
MAIL_SERVER = zmail.server(
    os.environ.get('MAIL_USERNAME'), 
    os.environ.get('MAIL_PASSWORD')
)

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = REDIS_CONFIG
# app.config['CELERY_RESULT_BACKEND'] = REDIS_CONFIG
 
celery = Celery(app.import_name, broker=REDIS_CONFIG)
celery.conf.update(app.config)

@celery.task
def send_async_mail(mail):
    to = mail.pop('to')
    MAIL_SERVER.send_mail(to, mail)

@app.route('/', methods=['POST'])
def mail():
    mail = request.data
    send_async_mail.delay(mail)
    return ''


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)