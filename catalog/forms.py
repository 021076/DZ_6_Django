from django import forms
from django.forms import BooleanField, ModelForm

from catalog.models import Product


class StyleMixin(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleMixin, forms.ModelForm):
    lock_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')
        for word in cleaned_data.lower().split(" "):
            if word in self.lock_words:
                raise forms.ValidationError('Ошибка, запрещенное слово названии')
        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data.get('product_description')
        for word in self.lock_words:
            if word in cleaned_data.lower().split(" "):
                raise forms.ValidationError('Ошибка, запрещенное слово в описании')
        return cleaned_data
