from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ToDo

def todo_list(request):
    todos = ToDo.objects.all().order_by('-created_at')
    return render(request, 'todo_list.html', {'todos': todos})

def todo_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        ToDo.objects.create(title=title, description=description)
        messages.success(request, 'Todo added successfully!')
        return redirect('todo_list')
    return render(request, 'todo_form.html')

def todo_update(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST.get('description', '')
        todo.save()
        messages.success(request, 'Todo updated successfully!')
        return redirect('todo_list')
    return render(request, 'todo_form.html', {'todo': todo})

def todo_delete(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    messages.success(request, 'Todo deleted successfully!')
    return redirect('todo_list')

def todo_toggle(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    status = "completed" if todo.completed else "re-opened"
    messages.success(request, f'Todo marked as {status}!')
    return redirect('todo_list')