from __future__ import absolute_import

import os

from celery import Celery

##test import parts:
from celery.decorators import task
import time
import random

##Email functionalities import:
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail

##Gmail imports:
import smtplib

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_ecommerce.settings')

from django.conf import settings

app = Celery('django_ecommerce', broker='amqp://guest@localhost//')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
		CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend',
	)

##email configuration part:


@task()
def run(to_email):
	subject, from_email, to = 'hello', 'danielkunfang@ciloud.com', to_email
	text_content = 'This is an important message.'
	html_content = '<p>This is an <strong>important</strong> message.</p>'
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	print "executed email sending task successfully!"

@task()
def runemail(to_email):
	send_mail('Welcome to Quinn', 'Here is the message', '353246394@qq.com',
				[to_email], fail_silently=False)

@task()
def gmail_sender():
	fromaddr = 'woshidaniu999@gmail.com'
	toaddrs = 'danielkunfang@icloud.com'

	msg = 'first test sending email through gmail'

	username = 'woshidaniu999@gmail.com'
	password = 'woshishen999'

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username, password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()

@task()
def addtest(x, y):
	delay = random.randint(1,60)
	time.sleep(delay)
	print x + y
	return x + y


@task()
def send_email():
            import smtplib

            gmail_user = "woshidaniu999@gmail.com"
            gmail_pwd = "woshishen999"
            FROM = 'woshidaniu999@gmail.com'
            TO = ['zhenyugood25@gmail.com'] #must be a list
            SUBJECT = "Quinn's application"
            TEXT = "Quinn's application's trying to reach you, bro!"

            # Prepare actual message
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
                #server = smtplib.SMTP(SERVER) 
            server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
                #server.quit()
            server.close()


@app.task(bind=True)
def debug_task(self):
	print('Request: {0!r}'.format(self.request))