from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from todo.models import Todo
from todo.forms import TodoForm


def todo_home(request):
    todo = Todo.objects.all()
    form = TodoForm()
    imp_todo = todo.order_by('-importance')[:5]
    return render(request, 'todo/todo_home.html', {'todo': todo, 'form': form, 'imp_todo': imp_todo})


def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        todo = Todo.objects.all()
        form = TodoForm()
        return redirect('todo:todo_homepage_url')
    else:
        return redirect('todo:todo_homepage_url')


def remove_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todo:todo_homepage_url')


def edit_todo(request, pk):
    todo_obj = Todo.objects.get(pk=pk)
    form = TodoForm()
    form.initial['name'] = todo_obj.name
    form.initial['detail'] = todo_obj.detail
    todo = Todo.objects.all()
    imp_todo = todo.order_by('-importance')[:5]
    return render(request, 'todo/todo_home.html', {'form': form, 'id': pk, 'imp_todo': imp_todo, 'todo': todo})
    # return redirect('todo_homepage_url')
