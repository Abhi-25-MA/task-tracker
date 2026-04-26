from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count

@login_required
def home(request):
    query = request.GET.get('q', '')  # 🔍 search input

    tasks = Task.objects.filter(user=request.user)

    # SEARCH FILTER
    if query:
        tasks = tasks.filter(title__icontains=query)

    total_tasks = Task.objects.filter(user=request.user).count()
    completed_tasks = Task.objects.filter(user=request.user, completed=True).count()
    pending_tasks = Task.objects.filter(user=request.user, completed=False).count()

    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'query': query,
    }

    return render(request, 'home.html', context)
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

@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.delete()
    return redirect('/')

@login_required
def toggle_complete(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('/')

@login_required
def edit_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
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
    request.session.flush()   
    return redirect('/login/')

# SIGNUP
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(username=username, password=password)
        return redirect('/login/')

    return render(request, 'signup.html')