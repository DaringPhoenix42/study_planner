# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Todo
from .forms import TodoForm

def todo(request):
    # 1) Search
    query = request.GET.get('q', '')
    todos_qs = Todo.objects.all()

    if query:
        todos_qs = todos_qs.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    # Separate pending vs. completed
    pending_todos = todos_qs.filter(is_finished=False)
    completed_todos = todos_qs.filter(is_finished=True)

    # 2) Handle create form (modal)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm()

    context = {
        'pending_todos': pending_todos,
        'completed_todos': completed_todos,
        'form': form,
        'query': query,  # keep search text in the input
    }
    return render(request, 'todo/todo.html', context)

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})

def todo_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_finished = True
    todo.save()
    return redirect('todo')
