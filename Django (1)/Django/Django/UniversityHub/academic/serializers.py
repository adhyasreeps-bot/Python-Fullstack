from rest_framework import serializers
from .models import Department, Course, Student 

# 1.Department Serializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        #'__all__' is a shortcut to include all fields in the model
        fields = '__all__'

# 2.Course Serializer
class CourseSerializer(serializers.ModelSerializer):
    # Nested Serializer: Instead of just showing the Dept ID (1),
    # we can show the Dept Nmae by being clever here.
    # For now, let's keep it simple and just show the Dept ID.
    class Meta:
        model = Course
        fields = ['id', 'name', 'code', 'department', 'credits', 'syllabus','semester']
# 3.Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email','profile_pic','courses']