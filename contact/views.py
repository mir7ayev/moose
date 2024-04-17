from django.shortcuts import render, redirect
from .models import Contact
import requests


def contact_view(r):
    if r.method == 'POST':
        Contact.objects.create(name=r.POST['name'],
                               message=r.POST['message']).save()

        contact = Contact.objects.filter().last()

        token = '6486746634:AAHgQKInguR3FxhT-46JB5ap2M-L-XeYTD8'
        requests.get(f"""
                                https://api.telegram.org/bot{token}/sendMessage?chat_id=-4175535863
                                &text=Moose
                                \nname: {contact.name.title()}\nmessage: {contact.message}
                                """)

        return redirect('/contact/')

    return render(r, 'contact.html')
