from django.shortcuts import render
from api.models import Info


# Create your views here.


def add(request):
    FirstName = request.POST.get('FirstName')
    LastName = request.POST.get('LastName')
    email = request.POST.get('email')
    number = request.POST.get('number')
    choose = request.POST.get('choose')
    print(choose)
    Info.objects.create(FirstName=FirstName, LastName=LastName, email=email, number=number, choose=choose)
    results = Info.objects.all()
    return render(request, 'index.html', context={'data': results})


def delinfo(request):
    id = request.GET.get('id')
    Info.objects.filter(id=id).delete()
    results = Info.objects.all()
    return render(request, 'index.html', context={'data': results})


def edit(request):
    id = request.POST.get('id')
    FirstName = request.POST.get('FirstName')
    LastName = request.POST.get('LastName')
    email = request.POST.get('email')
    number = request.POST.get('number')
    choose = request.POST.get('choose')
    Info.objects.filter(id=id).update(FirstName=FirstName, LastName=LastName, email=email, number=number, choose=choose)
    results = Info.objects.all()
    return render(request, 'index.html', context={'data': results})


def infoshow(request):
    results = Info.objects.all()
    return render(request, 'index.html', context={'data': results})


def add_page(request):
    return render(request, 'add.html')


def edit_page(request):
    id = request.GET.get('id')
    results = Info.objects.get(id=id)
    return render(request, 'edit.html', context={'data': results})
