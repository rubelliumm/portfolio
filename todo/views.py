from django.shortcuts import redirect, render
from todo.models import Todo
from todo.forms import TodoForm
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def todo_home(request):
    todo = Todo.objects.all()
    form = TodoForm()
    imp_todo = todo.order_by("-importance")[:5]
    return render(
        request,
        "todo/todo_home.html",
        {"todo": todo, "form": form, "imp_todo": imp_todo},
    )


def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo added successfully")
        last_todo = list(Todo.objects.values().order_by("created"))
        return JsonResponse({"todo": last_todo})
    else:
        return redirect("todo:homepage_url")


def remove_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect("todo:homepage_url")


def edit_todo(request, pk):
    todo_obj = Todo.objects.get(pk=pk)
    form = TodoForm()
    form.initial["name"] = todo_obj.name
    form.initial["detail"] = todo_obj.detail
    todo = Todo.objects.all()
    imp_todo = todo.order_by("-importance")[:5]
    return render(
        request,
        "todo/todo_home.html",
        {"form": form, "id": pk, "imp_todo": imp_todo, "todo": todo},
    )


def todo_details(request, pk):
    pass
