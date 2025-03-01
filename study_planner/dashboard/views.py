# dashboard/views.py
from django.shortcuts import render, redirect
from .models import Note, Homework, Todo
from .forms import NoteForm, HomeworkForm, TodoForm

def dashboard(request):
    notes = Note.objects.all()
    homeworks = Homework.objects.all()
    todos = Todo.objects.all()

    # Instantiate empty forms (for modals) by default
    note_form = NoteForm()
    homework_form = HomeworkForm()
    todo_form = TodoForm()

    if request.method == 'POST':
        # Determine which form was submitted
        if 'note_submit' in request.POST:
            note_form = NoteForm(request.POST)
            if note_form.is_valid():
                note_form.save()
                return redirect('dashboard')

        elif 'homework_submit' in request.POST:
            homework_form = HomeworkForm(request.POST)
            if homework_form.is_valid():
                homework_form.save()
                return redirect('dashboard')

        elif 'todo_submit' in request.POST:
            todo_form = TodoForm(request.POST)
            if todo_form.is_valid():
                todo_form.save()
                return redirect('dashboard')

    context = {
        'notes': notes,
        'homeworks': homeworks,
        'todos': todos,
        'note_form': note_form,
        'homework_form': homework_form,
        'todo_form': todo_form,
    }
    return render(request, 'dashboard/home.html', context)
