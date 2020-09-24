from django import forms
from .models import Book,Student

class BookCreate(forms.ModelForm):
	class Meta:
		model = Book
		fields = '__all__'
        
class StudentCreate(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'