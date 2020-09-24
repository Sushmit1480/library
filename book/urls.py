from django.urls import path
from .import views
from libraryapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book),
    path('student/', views.student_index, name = 'student_index'),
    path('upload_student/', views.upload_student, name = 'upload-student'),
    path('student/update_student/<int:student_id>', views.update_student),
    path('student/delete_student/<int:student_id>', views.delete_student),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)