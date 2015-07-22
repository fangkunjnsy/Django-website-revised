#from celery.registry import Task
from __future__ import absolute_import
from celery.task import Task
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from celery import Celery
from celery import shared_task
from django.core.mail import EmailMultiAlternatives



@shared_task
def run(self, to_email):
	subject, from_email, to = 'hello', 'danielkunfang@ciloud.com', to_email
	text_content = 'This is an important message.'
	html_content = '<p>This is an <strong>important</strong> message.</p>'
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()
	print "executed email sending task successfully!"


