from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    """
    Displays the list of tasks.
    """
    tasks = Task.objects.all()
    return render(request, 'tasks/dashboard.html', {'tasks': tasks})

def add_task(request):
    """
    Handles POST request to create a new task.
    """
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        
        if title:
            Task.objects.create(title=title, description=description)
            
    return redirect('task_list')

def complete_task(request, pk):
    """
    Marks a specific task as completed.
    """
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('task_list')

def delete_task(request, pk):
    """
    Deletes a specific task.
    """
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
