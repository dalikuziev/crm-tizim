from django.urls import path
from .views import (
    HomeView,
    SubjectListView, SubjectDetailView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView,
    TeacherListView, TeacherDetailView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('subjects/create/', SubjectCreateView.as_view(), name='subject_create'),
    path('subjects/<int:pk>/update/', SubjectUpdateView.as_view(), name='subject_update'),
    path('subjects/<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/update', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/delete', TeacherDeleteView.as_view(), name='teacher_delete'),
]
