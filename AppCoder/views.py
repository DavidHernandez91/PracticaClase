from django.shortcuts import render
from AppCoder.models import Tarea,Persona
from AppCoder.forms import PersonaForm, BuscarPersonasForm
from django.views.generic import ListView

def mostrar_mi_template(request, nombre, apellido):
    context = {
        "nombre" : nombre,
        "apellido" : apellido,
        "notas": [5,6,7,8,9,10]
    }
    return render(request, "AppCoder/index.html", context)

def mostrar_tareas(request,criterio):
        if criterio == "todo":
            tareas = Tarea.objects.all()
        elif criterio:
            tarea = Tarea.objects.filter(nombre=criterio).all()
        return render(request,"AppCoder/tareas.html",{"tareas":tareas})

def mostrar_personas(request):

        personas = Persona.objects.all()
        total_personas = len(personas)
        context = {
            "personas":personas,
            "total_personas":total_personas,
            "form": PersonaForm(),
        }
        return render(request,"AppCoder/personas.html",context)

def cargar_personas(request):

    f = PersonaForm(request.POST)
    context= {
        "form":f
    }

    if f.is_valid():
        Persona(nombre=f.data["nombre"], apellido=f.data["apellido"],
        fecha_nacimiento=f.data["Fecha_nacimiento"] ).save()
        context['form'] = PersonaForm()
    
    context["Personas"] = Personas.objects.all()
    context["Total_de_Personas"] =len(Total_de_Personas)
    return render(request,"AppCoder/personas.html",context)

class BuscarPersonas(ListView):
    model = Persona
    context_objec_name="personas"

    def get_query(self):
        f = BuscarPersonasForm(self.request.GET)
        if f.is_valid():
            return persona.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Personas.objects.none()
    



    


