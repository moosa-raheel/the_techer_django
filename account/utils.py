from threading import Thread
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from decouple import config

class EmailThread(Thread):
    def __init__(self,email):
        self.email = email
        Thread.__init__(self)
        
    def run(self):
        self.email.send()
        
def send_email(user,user_email,activation_link):
    from_email = config("ADMIN_EMAIL")
    subject = "Activate your TheTecher account"
    html_message = render_to_string("emailTemplate.html",context={"user_name":user,"activation_link" : activation_link})
    text_message = strip_tags(html_message)
    email = EmailMultiAlternatives(from_email=from_email, to=[user_email],subject=subject, body=html_message)
    email.content_subtype = 'html'
    email.attach_alternative(text_message, "text/plain")
    EmailThread(email).start()
