from background_task import background
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def contact_mail(name,email):
    ctx = {
        'user': name
    }

    subject, from_email, to = 'Contact Mail!',"Choreography Club<settings.EMAIL_HOST_USER>", [email,]
    text_content = 'This is an Contact message.'
    html_content = get_template('contact_mail.html').render(ctx)
    msg = EmailMultiAlternatives(subject, text_content,from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print(name + " contacted us")


@background(schedule=10)
def register_mail(name,email):
    ctx = {
        'user': name
    }

    subject, from_email, to = 'Signup Mail!',"Abhivyakti 22<settings.EMAIL_HOST_USER>", [email,]
    text_content = 'This is an Contact message.'
    html_content = get_template('email/signupMail.html').render(ctx)
    msg = EmailMultiAlternatives(subject, text_content,from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.attach_file('ABHIVYAKTI_2k22_BROCHURE.pdf')
    msg.send()
    print("mail sent to " + name)


@background(schedule=20)
def event_register_mail(name,email,event,date,cell):
    ctx = {
        'user': name,
        'event':event,
        'date':date,
        'cell':cell,
    }

    subject, from_email, to = 'Confirmation Mail!',"Abhivyakti 22<settings.EMAIL_HOST_USER>", [email,]
    text_content = 'This is an Contact message.'
    html_content = get_template('email/eventMail.html').render(ctx)
    msg = EmailMultiAlternatives(subject, text_content,from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.attach_file('ABHIVYAKTI_2k22_BROCHURE.pdf')
    msg.send()
    print("mail sent to " + name, 'for event', event)