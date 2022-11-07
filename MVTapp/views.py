from django.http import HttpResponse
from MVTapp.models import *
from django.template import loader


def Padre(request):

    for obj in Familia.objects.all():
        if obj.id == 1:
            nombre = obj.nombre
            apellido = obj.apellido
            edad = obj.edad
            adn = obj.adn.strftime('el %d del mes %m del año 19%y')


            datos = {'parentezco': 'Padre', 'nombre': nombre, 'apellido': apellido, 'edad': edad, 'adn': adn}

            plantilla = loader.get_template('MVTtemplate.html')
            doc = plantilla.render(datos)

            return HttpResponse(doc)
        
def Madre(request):

    for obj in Familia.objects.all():
        if obj.id == 2:
            nombre = obj.nombre
            apellido = obj.apellido
            edad = obj.edad
            adn = obj.adn.strftime('el %d del mes %m del año 19%y')

            datos = {'parentezco': 'Madre', 'nombre': nombre, 'apellido': apellido, 'edad': edad, 'adn': adn}

            plantilla = loader.get_template('MVTtemplate.html')
            doc = plantilla.render(datos)

            return HttpResponse(doc)


def Hermano(request):
    
    for obj in Familia.objects.all():
        if obj.id == 3:
            nombre = obj.nombre
            apellido = obj.apellido
            edad = obj.edad
            adn = obj.adn.strftime('el %d del mes %m del año 19%y')

            datos = {'parentezco': 'Hermano', 'nombre': nombre, 'apellido': apellido, 'edad': edad, 'adn': adn}

            plantilla = loader.get_template('MVTtemplate.html')
            doc = plantilla.render(datos)

            return HttpResponse(doc)