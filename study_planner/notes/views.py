# notes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Note
from .forms import NoteForm

def notes(request):
    # 1) Searching
    query = request.GET.get('q', '')
    
    # 2) Filtering by category
    category_filter = request.GET.get('category', '')

    # 3) Sorting (newest or oldest)
    sort_order = request.GET.get('sort', 'newest')  # 'newest' or 'oldest'

    # Base queryset
    note_qs = Note.objects.all()

    # Apply search
    if query:
        note_qs = note_qs.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    # Apply category filter
    if category_filter:
        note_qs = note_qs.filter(category=category_filter)

    # Sorting
    if sort_order == 'oldest':
        note_qs = note_qs.order_by('created_at')
    else:
        note_qs = note_qs.order_by('-created_at')

    # 4) Pagination
    paginator = Paginator(note_qs, 6)  # 6 notes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 5) Modal form to create new notes
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = NoteForm()

    context = {
        'page_obj': page_obj,
        'form': form,
        'query': query,
        'category_filter': category_filter,
        'sort_order': sort_order,
    }
    return render(request, 'notes/notes.html', context)


def notes_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/notes_detail.html', {'note': note})


def notes_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes-detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/notes_form.html', {'form': form, 'note': note})


def notes_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    return render(request, 'notes/notes_confirm_delete.html', {'note': note})
