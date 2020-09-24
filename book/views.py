from django.shortcuts import render, redirect
from .models import Book,Student
from .forms import BookCreate,StudentCreate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/library.html', {'shelf':shelf})
    
def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{url : 'index'}}">reload</a>""")
    else:
        return render(request, 'book/upload_form.html', {'upload_form':upload})
        

def update_book(request, book_id):
    book_id  = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
        
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    
    return render(request, 'book/upload_form.html',{'upload_form': book_form})
    
def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')
    


def student_index(request):
    bench = Student.objects.all()
    return render(request, 'book/student.html', {'bench':bench})
    
def upload_student(request):
    upload = StudentCreate()
    if request.method == 'POST':
        upload = StudentCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('student_index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{url : 'student_index'}}">reload</a>""")
    else:
        return render(request, 'book/upload_student_form.html', {'upload_student_form':upload})
        

def update_student(request, student_id):
    student_id  = int(student_id)
    try:
        student_sel = Student.objects.get(id = student_id)
    except Student.DoesNotExist:
        return redirect('student_index')
        
    student_form = StudentCreate(request.POST or None, instance = student_sel)
    if student_form.is_valid():
        student_form.save()
        return redirect('student_index')
    
    return render(request, 'book/upload_student_form.html',{'upload_student_form': student_form})
    
def delete_student(request, student_id):
    student_id = int(student_id)
    try:
        student_sel = Student.objects.get(id = student_id)
    except Student.DoesNotExist:
        return redirect('student_index')
    student_sel.delete()
    return redirect('student_index')