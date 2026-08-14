from django.http import HttpResponse
from django.shortcuts import render
from .models import Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Type 1: Simple HTTP Response
def hello_world(request):
    # This returns raw text, not HTML
    return HttpResponse("Welcome to University Hub!")


# Type 2: Data-Driven View
def course_list(request):
    # 1. Fetch data from DB
    all_courses = Course.objects.all()

    # 2. Context: dictionary mapping template variables to Python objects
    context = { 
        'courses': all_courses,
        'page_title': 'Available Courses'
    }

    # 3. Render template with data
    return render(request, 'academic/course_list.html', context)

from django.shortcuts import render,redirect
from .forms import StudentForm

def student_create(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():

            # get login fields safely
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '').strip()
            email = request.POST.get('email', '').strip()

            # validate login fields first
            if not username or not password or not email:
                return render(request,'academic/student_form.html',{
                    'form': form,
                    'error': 'All login fields required'
                })

            # prevent duplicate username crash
            if User.objects.filter(username=username).exists():
                return render(request,'academic/student_form.html',{
                    'form': form,
                    'error': 'Username already exists'
                })

            # create user first
            # create user first
            user = User.objects.create_user(
                   username=username,
                   password=password,
                   email=email
            )

            # THEN create student object
            student = form.save(commit=False)
            student.user = user
            student.save()

            form.save_m2m()

            return redirect('course_list')

    else:
        form = StudentForm()

    return render(request, 'academic/student_form.html', {'form': form})

def register_user(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .models import Course,Student

# 1. The @login_required Decorator
# If a guest tries to access this, they are redirected to the login page automatically.
@login_required
def course_list(request):
    # Logic remains the same...
    courses = Course.objects.all()

    return render(
        request,
        "academic/course_list.html",
        {"courses": courses}
    )

# 2. Custom Permission Checks
# Define a check function: Returns True if user is a staff member
def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def delete_student(request, id):
    # Only staff can reach this code
    student = Student.objects.get(id=id)

    if student.user:
        student.user.delete()
    else:
        student.delete()

    return redirect('course_list')

@login_required
def student_profile(request, id):
    # 1. Fetch the requested profile
    profile = Student.objects.get(id=id)

    # 2. Check if the logged-in user matches the profile owner
    # (Assuming we linked the Student model to the User model)
    if request.user != profile.user:
        return HttpResponseForbidden("You are not authorized to view this profile.")

    return HttpResponse("Profile allowed")

    # JSON
from django.http import JsonResponse

def api_course_list(request):
    
    # 1. Get data
    courses = Course.objects.all()

    # 2. Convert Python Objects to Dictionary (Serialization)
    # We cannot send Python objects directly over the internet.
    data = {
        'count': courses.count(),
        'results': list(courses.values('name', 'code', 'credits'))
    }

    # 3. Return JSON Response (Not HTML)
    return JsonResponse(data)

from rest_framework import viewsets
from .models import Course, Student
from .serializers import CourseSerializer, StudentSerializer
from rest_framework.permissions import IsAuthenticated
#This ONE class handles GET (List), GET (Detail), POST, PUT, DELETE for Courses
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes =[IsAuthenticated]