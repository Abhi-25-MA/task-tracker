from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# HOME (SEARCH + FILTER FIXED)
@login_required
def home(request):
    query = request.GET.get('q', '')
    filter_type = request.GET.get('filter', '')

    tasks = Task.objects.filter(user=request.user)

    # SEARCH
    if query:
        tasks = tasks.filter(title__icontains=query)

    # FILTER (completed / pending)
    if filter_type == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_type == 'pending':
        tasks = tasks.filter(completed=False)

    # DASHBOARD COUNTS (IMPORTANT FIX: use same user filter)
    total_tasks = Task.objects.filter(user=request.user).count()
    completed_tasks = Task.objects.filter(user=request.user, completed=True).count()
    pending_tasks = Task.objects.filter(user=request.user, completed=False).count()

    context = {
        'tasks': tasks,
        'query': query,
        'filter_type': filter_type,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
    }

    return render(request, 'home.html', context)


# ADD TASK
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')

        if title:
            Task.objects.create(
                user=request.user,
                title=title,
                due_date=due_date if due_date else None
            )
    return redirect('/')


# DELETE TASK (SAFE VERSION)
@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('/')


# TOGGLE COMPLETE
@login_required
def toggle_complete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('/')


# EDIT TASK
@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('/')

    return render(request, 'edit.html', {'task': task})


# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('/login/')


# SIGNUP
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(username=username, password=password)
        return redirect('/login/')

    return render(request, 'signup.html')