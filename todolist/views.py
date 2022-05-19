from django.shortcuts import render, HttpResponse, redirect
from .forms import Task_Form
from .models import Task

# Create your views here.


def index(request):
    # return HttpResponse("Hello World!!")
    form = Task_Form()

    if request.method == "POST":
        # Get the posted form
        form = Task_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")

    tasks = Task.objects.all() # add this
    return render(request, "index.html", {"task_form": form, "tasks": tasks})

#Updation

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = Task_Form(instance=task)
    if request.method == "POST":
        form = Task_Form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "update_task.html", {"task_edit_form": form})


#delete task
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")