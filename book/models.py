from django.db import models

Available = [
    ('Yes','Yes'),
    ('No','No')
]

Language = [
    ('English','English'),
    ('Marathi','Marathi'),
    ('Hindi','Hindi')
]

Branch = [
    ('IT','IT'),
    ('CSE','CSE'),
    ('MECH','MECH'),
    ('PROD','PROD'),
    ('CHEM','CHEM'),
    ('CIVIL','CIVIL'),
    ('TEXT','TEXT'),
    ('EXTC','EXTC'),
    ('ELECT','ELECT'),
    ('INSTRU','INSTRU')
]
class Book(models.Model):
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 40, default = 'anonymos')
    isbn = models.CharField(max_length = 12)
    total_copies = models.IntegerField(default = 0)
    remaining = models.IntegerField(default = 0)
    available = models.CharField(max_length = 3, choices = Available)
    language = models.CharField(max_length = 7, choices = Language)
    
    def __str__(self):
        return self.name
        
class Student(models.Model):
    student_name = models.CharField(max_length = 30)
    book_assign = models.ForeignKey(Book, on_delete = models.CASCADE,blank=True, null=True)
    reg_no = models.CharField(max_length = 15, default = '***')
    branch = models.CharField(max_length = 6, choices = Branch, default = 'IT')
    assign_date = models.DateField('book assign')
    due_date = models.DateField('Due on')
    fine = models.DecimalField(max_digits = 5, decimal_places = 2)
    
    def __str__(self):
        return str(self.student_name)+ "Rs." + str(self.fine)