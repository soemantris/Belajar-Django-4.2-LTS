from django import forms

from .models import Artikel


class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = "__all__"
        # fields = ['tag', 'penulis', 'judul', 'isi', 'kategori']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['judul'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan judul artikel', })
        self.fields['isi'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan isi artikel', })
        self.fields['kategori'].widget.attrs.update(
            {'class': 'form-select', 'placeholder': 'Masukan kategori artikel', })
        self.fields['penulis'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan penulis artikel', })
        self.fields['tag'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan tag artikel', })
        self.fields['penerbit'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan penerbit artikel', })
