from celery import Celery
from flask import Flask, request
from flask_restful import Api, Resource
from mail_config import server_mapping_table

REDIS_CONFIG = 'redis://localhost:6379'

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = REDIS_CONFIG

api = Api(app) 

celery = Celery('mail', broker=REDIS_CONFIG)
celery.conf.update(app.config)

@celery.task()
def send_email(mail):
    recipient = mail.pop('recipient')
    server_type = recipient.split('@')[-1]
    server = server_mapping_table.get(server_type)
    server.send_mail(recipient, mail)

class Mail(Resource):
    def post(self):
        mail = request.form
        send_email.delay(mail)
        return '', 201

api.add_resource(Mail, '/')

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
