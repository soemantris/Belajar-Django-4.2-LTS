from django import forms

JENIS_KELAMIN = (
    ('p','Pria'),
    ('w','Wanita'),
)

TAHUN = range(1993, 2011,1)

class KontakForms(forms.Form):
    nama = forms.CharField(max_length=25)
    email = forms.EmailField(required=False,label='Alamat Email', help_text='Tolong masukan masukan email yang benar')
    no_telp = forms.IntegerField(required=False)
    tgl_lahir = forms.DateField(
        widget = forms.SelectDateWidget(years=TAHUN)
    )
    jenkel = forms.ChoiceField(
        choices=JENIS_KELAMIN,
        label='Jenis Kelamin',
        widget = forms.RadioSelect,
    )
    subjek = forms.CharField(required=False)
    pesan = forms.CharField(required=False)
    alamat = forms.CharField(
        widget = forms.Textarea,
        required=False
    )
    aggre = forms.BooleanField()


    
