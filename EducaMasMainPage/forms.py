from django import forms
from EducaMasMainPage import models


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        #fields = ('Titulo', 'Descripcion', 'Foto', ) # o todos y exclude = ['campo1', 'campo2']
        exclude = ['uploaded_at', 'id_int']
        widgets = {
            'Descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 5})
        }