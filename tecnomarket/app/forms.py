from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        #fields = ["nombre", "coreo", "tipo_consulta", "mensaje", "avisos"] #aca se listan 1 x 1 los campos de la clase Contacto
        fields = '__all__' # aca se toma todos los campos de la clase Contacto
        
        
    
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'
        
        widgets = {
            "fecha_fabricacion" : forms.SelectDateWidget()
        }
        
class CustomUserCreationForm(UserCreationForm):
    pass