from django import forms


class KontakForms(forms.Form):
    nama = forms.CharField(
        label="Nama Lengkap",
        max_length=25,
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Masukan nama lengkap Anda."}
        ),
    )
    email = forms.EmailField(
        help_text="Masukan email Anda dengan benar. contoh: user@email.com",
    )
    jenkel = forms.ChoiceField(
        label="Jenis Kelamin",
        widget=forms.RadioSelect(
            attrs={
                "class": "form-check-input",
            }
        ),
        choices=[
            ("p", "Pria"),
            ("w", "Wanita"),
        ],
    )
    tgl_lahir = forms.DateField(
        label="Tanggal Lahir",
        widget=forms.SelectDateWidget(
            years=range(1985, 2014, 1),
            attrs={
                "class": "form-select",
            },
        ),
    )
    pesan = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Masukan pesan Anda.",
            }
        )
    )
    agree = forms.BooleanField()

    email.widget.attrs.update(
        {
            "class": "form-control",
            "placeholder": "Masukan email Anda.",
        }
    )
