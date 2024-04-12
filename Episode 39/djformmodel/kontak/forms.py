from django import forms


class KontakForm(forms.Form):
    nama = forms.CharField(max_length=45)
    email = forms.EmailField()
    pesan = forms.CharField(
        widget=forms.Textarea(),
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if 'tri@dj.com' in email:
            raise forms.ValidationError(
                f'Email {email} ini sudah pernah kirim pesan!')

        return email
