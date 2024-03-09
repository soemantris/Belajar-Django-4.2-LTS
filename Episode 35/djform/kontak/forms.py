# ? Membuat class form

from django import forms


class KontakForm(forms.Form):
    nama = forms.CharField()
    email = forms.EmailField()
    subjek = forms.CharField()
    pesan = forms.CharField()
