from django import forms
from .models import *
from django.core.validators import MinLengthValidator

class AddPost(forms.Form):
    title = forms.CharField(max_length=255, min_length=3,
                            label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'})
                            , error_messages= {
            'min_length': 'Слишком короткий заголовок',
            'required': 'Без заголовка никак'
        })
    slug = forms.SlugField(max_length=255, validators=[MinLengthValidator(5)])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows': 5}), required=False)
    is_published = forms.BooleanField(required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False)


