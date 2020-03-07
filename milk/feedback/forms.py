from django import forms


# Модель формы обратной связи
class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', max_length=100)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)
    from_email = forms.EmailField(label='Email')
    name = forms.CharField(label='Имя', required=False)
    copy = forms.BooleanField(label='Отправить копию себе', required=False)
