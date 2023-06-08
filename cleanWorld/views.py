from datetime import date

import requests
from decouple import config
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from account.forms import ContactForm


def home(request):
    if request.method == "GET":
        form = ContactForm(request.GET)
        if form.is_valid():
            form.save()

            mail_subject = "ارتباط باما | پیغام جدید"
            message = render_to_string(
                "registration/contactus_email.html",
                {
                    "name": form.cleaned_data["name"],
                    "email": form.cleaned_data["email"],
                    "text": form.cleaned_data["text"],
                    "page_title": "Clean The World",
                },
            )
            email_from = settings.EMAIL_HOST_USER
            email = EmailMessage(mail_subject, message, email_from, to=[config("EMAIL_HOST_USER")])
            email.content_subtype = "html"
            email.send()

            context = {
                "title": "ارتباط با ما",
                "message": "پیام شما با موفقیت ارسال شد.",
                "type": "success",
            }
            return render(request, "registration/registration_messages.html", context=context)
    form = ContactForm()
    context = {"form": form, "current_year": date.today().year}
    return render(request, "cleanWorld/index.html", context=context)


def robots(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Sitemap: https://daryaban.tk/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
