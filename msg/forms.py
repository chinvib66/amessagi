from django import forms
from .models import Message
from django.utils.translation import gettext_lazy as _

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['rec_add','title', 'message']
        labels = {
            'rec_add': _("Reciever's a_Messagi Address"),
            'message': _("Your Message"),
        }
        help_texts = {
            'message': _("Please refrain from using any kind of abusive language"),
            
        }