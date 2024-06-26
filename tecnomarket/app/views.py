from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required



# Create your views here.
def home(request):
    
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'app/home.html', data)
#@login_required  restringir si el usuairo no esta registrado y no dejara que entre a la pestaña en este caso a galeria, no lo dejara amenos que tenga un registro
def galeria(request):
    return render(request, 'app/galeria.html')

def contacto(request):
    data = {
        'form' : ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
            
    return render(request, 'app/contacto.html',data)

@permission_required('app.add_producto')
def agregar_producto(request):
    
    data = {
        'form' : ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto guardado")
        else:
            data["form"] = formulario
    return render(request, 'app/producto/agregar.html',data)

@permission_required('app.view_producto')
def listar_productos(request):
    
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404("No existe la pagina")
    
    data = {
        'entity' : productos,
        'paginator': paginator
    }
    return render(request, 'app/producto/listar.html',data)

@permission_required('app.change-producto')
def modificar_productos(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    
    data = {
        'form' : ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            return redirect(to="listar_productos")
        data["form"] = formulario     
    
    return render(request, 'app/producto/modificar.html',data)

@permission_required('app.delete_producto')
def eliminar_productos(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    
    messages.success(request, "Producto eliminado correctamente")
    
    return redirect(to="listar_productos")


def registro(request):
    
    data = {
        'form' : CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        else:
            data["form"] = formulario
            
    return render(request, 'registration/registro.html',data)