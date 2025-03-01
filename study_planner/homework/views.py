# homework/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Homework
from .forms import HomeworkForm

def homework_list(request):
    # 1) Optional: Searching by subject/title/description
    query = request.GET.get('q', '')
    homeworks = Homework.objects.all()

    if query:
        homeworks = homeworks.filter(
            Q(subject__icontains=query) |
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    # Separate into pending vs. completed
    pending_homeworks = homeworks.filter(is_finished=False)
    completed_homeworks = homeworks.filter(is_finished=True)

    # 2) If user posts a new homework form
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homework')
    else:
        form = HomeworkForm()

    context = {
        'pending_homeworks': pending_homeworks,
        'completed_homeworks': completed_homeworks,
        'form': form,
        'query': query,  # So we can keep the search text in the input
    }
    return render(request, 'homework/homework.html', context)

def homework_update(request, pk):
    homework = get_object_or_404(Homework, pk=pk)
    if request.method == 'POST':
        form = HomeworkForm(request.POST, instance=homework)
        if form.is_valid():
            form.save()
            return redirect('homework')
    else:
        form = HomeworkForm(instance=homework)
    return render(request, 'homework/homework_form.html', {'form': form})

def homework_delete(request, pk):
    homework = get_object_or_404(Homework, pk=pk)
    if request.method == 'POST':
        homework.delete()
        return redirect('homework')
    return render(request, 'homework/homework_confirm_delete.html', {'homework': homework})

def homework_complete(request, pk):
    """
    Simple view to mark homework as finished.
    """
    homework = get_object_or_404(Homework, pk=pk)
    homework.is_finished = True
    homework.save()
    return redirect('homework')
