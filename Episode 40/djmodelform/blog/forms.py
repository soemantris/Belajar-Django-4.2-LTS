from django import forms


from .models import Artikel


# class ArtikelForm(forms.Form):
#     judul = forms.CharField(max_length=100)
#     isi = forms.CharField(widget=forms.Textarea())
#     kategori = forms.CharField(max_length=20)

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = "__all__"
        # fields = ['tag', 'penulis', 'judul', 'isi', 'kategori']
