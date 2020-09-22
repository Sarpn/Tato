from django.shortcuts import render, redirect
from .models import Producto

def index(request):

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '-1')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('precio')
        comentario = request.POST.get('comentario')  
        if nombre != '-1':     
            Producto(nombre=nombre,cantidad=cantidad,precio=precio,comentario=comentario).save()
        else:
            csv = request.FILES['csv'].read().decode('utf-8')
            
            for i in csv.split('\n'):
                row = i.split(',')
                try:
                    Producto(nombre=row[0],cantidad=row[1],precio=row[2],comentario=row[3]).save()
                except:
                    pass



    context = {'productos':Producto.objects.all()}
    return render(request,'index.html', context=context)

def delete(request,id):
    obj = Producto.objects.get(id=id)
    obj.delete()
    return redirect('index')


def edit(request,id):

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('precio')
        comentario = request.POST.get('comentario')

        pro = Producto.objects.get(id=id)

        pro.nombre = nombre
        pro.cantidad = cantidad
        pro.precio = precio
        pro.comentario = comentario

        pro.save()

        return redirect('index')

    obj = Producto.objects.get(id=id)
    return render(request,'edit.html', context={'data':obj})