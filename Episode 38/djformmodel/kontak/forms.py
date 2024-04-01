from django import forms


class KontakForm(forms.Form):
    nama = forms.CharField(max_length=25)
    email = forms.EmailField()
    pesan = forms.CharField(
        widget=forms.Textarea(),
    )
