# todoapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoItemForm

def todo_list(request):
    todos = TodoItem.objects.all()
    form = TodoItemForm()

    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')

    return render(request, 'todoapp/todo_list.html', {'todos': todos, 'form': form})

def delete_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    todo.delete()
    return redirect('todo_list')

def mark_completed(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')
