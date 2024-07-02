from django.http import HttpResponse
import datetime
from django.template import Template, Context

#clase persona
class Persona(object):
    def __init__(self,nombre, apellido): #init indica que es un constructor
        self.nombre = nombre
        self.apellido = apellido



def index(request): # Primera vista

    p1 = Persona("juan", "perez")


    fecha_ahora = datetime.datetime.now()

    doc_externo = open("C:/Users/tleon/Desktop/django yt/djangoyt/djangoyt/templates/index.html") #esto lo que hace es abrir el archivo html
    
    
    plt = Template(doc_externo.read()) #esto lo que hace es leer el archivo html
    doc_externo.close() #esto lo que hace es cerrar el archivo html para que no se quede abierto
    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "fecha": fecha_ahora, "temas":["Lenguaje", "Matematicas", "Ciencias"]}) #esto lo que hace es crear un contexto para el archivo html que se va a renderizar
    documento = plt.render(ctx) #esto lo que hace es renderizar el archivo html
    return HttpResponse(documento)

def despedida(request): # Segunda vista
    return HttpResponse("Hasta luego")

def dameFecha(request): # Tercera vista
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)  # Devuelve la fecha y hora actuales

def calculaEdad(request, agno, edad): # Cuarta vista
    periodo = agno - 2024
    edadFutura = edad + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años" % (agno, edadFutura)
    return HttpResponse(documento)