from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import Course, Person
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonCreationForm

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/new')
        else:
            return redirect('/login')
    return render(request,'login.html')

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('/login')
        else:
            messages.info(request,'password not matching')
            return redirect('/register')
        return redirect('/')
    return render(request,'register.html')

def new(request):
    form=PersonCreationForm()
    if request.method == 'POST':
        return redirect('/add')
    return render(request,'new.html',{'form':form})

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        return redirect('/new3')
    return render(request, 'form.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        form.save()
        return redirect('/')
    return render(request, 'form.html', {'form': form})

# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def new3(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        return redirect('/')
    return render(request, 'new3.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')