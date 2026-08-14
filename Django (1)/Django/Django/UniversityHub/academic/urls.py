from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# 1.Create a router 
router = DefaultRouter()

# 2.Register our viewsets with the router
# 'courses' is the URL prefix
router.register(r'courses', views.CourseViewSet)
router.register(r'students', views.StudentViewSet)


urlpatterns = [
   # path('students/', views.student_list),
   #path(route,view,name)
    path('hello/', views.hello_world, name='hello'),
    path('courses/', views.course_list, name='course_list'),
    #path("department/<int:id>/", views.department_detail, name="department_detail"),
    path("register-student/", views.student_create, name="student_create"),
    path("register/", views.register_user, name="register"),
    path("delete-student/<int:id>/", views.delete_student),
    path("profile/<int:id>/", views.student_profile),
    #path("api/courses/", views.api_course_list),
   #-------------DRF ROUTER----------------
   path('api/', include(router.urls)),


] 