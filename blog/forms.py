from django import forms


class TicketForm(forms.Form):
    SUBJECT_CHOICES = (
        ('پیشنهاد', 'پیشنهاد'),
        ('انتقاد', 'انتقاد'),
        ('گزارش', 'گزارش'),
    )
    message = forms.CharField(widget=forms.Textarea, requrired=True)
    name = forms.CharField(max_length=250, requrired=True)
    email = forms.EmailField()
    phone = forms.CharField(max_length=11,  requrired=True)
    subject = forms.CharField(max_length=250)
