import re
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render
from .models import Task

#def home(request):
 #   return HttpResponse("Hello, Django!")

def tasks(request):
    if request.method == "POST":

        if "add_task" in request.POST:
            title = request.POST.get("title")
            description = request.POST.get("description")
            completed = request.POST.get("completed") == "on"
            task = Task(title=title, description=description, completed=completed)
            task.save()

        if "edit_task" in request.POST:
            task_id = request.POST.get("task_id")
            task = Task.objects.filter(id=task_id).first()

            if task:
                task.title = request.POST.get("title")
                task.description = request.POST.get("description")
                task.completed = request.POST.get("completed") == "on"
                task.save()

        if "delete_task" in request.POST:
            task_id = request.POST.get("task_id")
            task = Task.objects.filter(id=task_id).first()

            if task:
                task.delete()

        if "clear_all" in request.POST:
            Task.objects.all().delete()

    tasks = Task.objects.all()

    return render(request, "tasks/tasks.html", {
        "date": timezone.now(),
        "tasks": tasks, 
        "task_count": tasks.count()
    })
    #now = datetime.now()
    #formatted_now = now.strftime("%a, %d %b, %y at %x")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    #match_object = re.match("[a-zA-Z]+", name)

    #if match_object:
    #    clean_name = match_object.group(0)
    #else:
    #    clean_name = "Friend"

    #content = "Hello there, " + clean_name + "! It's " + formatted_now
    #return HttpResponse(content)
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'tasks/tasks.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )