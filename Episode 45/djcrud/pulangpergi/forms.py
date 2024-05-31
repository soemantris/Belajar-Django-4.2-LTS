from django import forms

from .models import Tujuan


class TujuanForm(forms.ModelForm):
    class Meta:
        model = Tujuan
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nm_penumpang'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan nama penumpang anda.'})
        self.fields['nm_pengemudi'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan nama pengemudi anda.'})
        self.fields['tujuan'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan tujuan anda.'})
