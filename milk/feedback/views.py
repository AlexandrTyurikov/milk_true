from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ContactForm


class ContactFormsView(View):

    def get(self, request):
        form = ContactForm()
        return render(request, 'feedback/form.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            # context = form.cleaned_data
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            name = form.cleaned_data['name']
            copy = form.cleaned_data['copy']

            recepients = ['987tav@gmail.com']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(from_email)
            try:
                send_mail(subject, message, f'{name} {from_email}', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return HttpResponseRedirect('/feedback/thanks/')
            # return render(request, 'feedback/form.html', context)
        else:
            return render(request, 'feedback/error.html', {'error': form.errors})


def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'feedback/thanks.html', {'thanks': thanks})

