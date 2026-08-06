from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views import View
from .models import Subject, Teacher, Student
from .forms import SubjectForm, TeacherForm, StudentForm

class HomeView(View):
    def get(self, request):
        return render(
            request,
            'course/home.html',
        )

class SubjectListView(View):
    def get(self, request):
        subjects = Subject.objects.all()
        return render(
            request,
            'course/subject/subject_list.html',
            {
                'subjects': subjects,
            }
        )
class SubjectCreateView(View):
    def get(self, request):
        form = SubjectForm()
        return render(
            request,
            'course/subject/subject_create.html',
            {
                'form': form,
            }
        )
    def post(self, request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
        return render(
            request,
            'course/subject/subject_create.html',
            {
                'form': form,
            }
        )

class SubjectTeacher(View):
    def get(self, request, pk):
        subject = get_object_or_404(Subject, pk=pk)
        return render(
            request,
            'course/subject/subject_teacher.html',
            {
                "subject": subject,
            }
        )

class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(
            request,
            'course/teacher/teacher_list.html',
            {
                'teachers': teachers,
            }
        )
class TeacherDetailView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        return render(
            request,
            'course/teacher/teacher_detail.html',
            {
                'teacher': teacher,
            }
        )
class TeacherCreateView(View):
    def get(self, request):
        form = TeacherForm()
        return render(
            request,
            'course/teacher/teacher_create.html',
            {
                'form': form,
            }
        )
    def post(self, request):
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
        return render(
            request,
            'course/teacher/teacher_create.html',
            {
                'form': form,
            }
        )
class TeacherUpdateView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        form = TeacherForm(instance=teacher)
        return render(
            request,
            'course/teacher/teacher_update.html',
            {
                'form': form,
            }
        )
    def post(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
        return render(
            request,
            'course/teacher/teacher_update.html',
            {
                'form': form,
            }
        )
class TeacherDeleteView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        return render(
            request,
            'course/teacher/teacher_delete.html',
            {
                'teacher': teacher,
            }
        )
    def post(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        teacher.delete()
        return redirect('teacher_list')

class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(
            request,
            'course/student/student_list.html',
            {
                'students': students,
            }
        )
class StudentCreateView(View):
    def get(self, request):
        form = StudentForm()
        return render(
            request,
            'course/student/student_create.html',
            {
                'form': form,
            }
        )
    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        return render(
            request,
            'course/student/student_create.html',
            {
                'form': form,
            }
        )
