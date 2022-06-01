from distutils.file_util import move_file
from tabnanny import verbose
from django.db import models
 
class user_model(models.Model):
    staff = 1
    teacher = 2
    student  = 3
    accountant  = 4
    parents = 5
 
    designation = (
        ('staff',"Staff"),
        ('teacher',"Teacher"),
        ('student',"Students"),
        ( 'parents' , 'parents'),
        ( 'accountant' , 'accountant'),    
    )

    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200,unique = True)
    address = models.CharField(max_length=200)
    role = models.CharField(max_length=200,choices = designation,default="1")
    password = models.CharField(max_length=200,unique = True)

    class Meta:
        verbose_name = 'user_model',
        verbose_name_plural = 'user_models'

class classes_model(models.Model):
 classroom = (
     ("1", "I"),
     ("2", "II"),
     ("3","III"),
     ("4", "IV"),
     ("5","V"),
     ("6","VI"),
     ("7","VII"),
     ("8","VIII"),
     ("9","IX"),
     ("10","X"),
     ("11","XI"),
     ("12","XII")
 )
 name = models.CharField(max_length=20,choices = classroom,unique=True)

class student_realtions(models.Model):
    sections =(
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D')
    )
    student = models.OneToOneField(user_model,null = True,on_delete=models.CASCADE,related_name="student")
    parent = models.OneToOneField(user_model, null = True,on_delete=models.CASCADE,related_name="parents")
    classes = models.OneToOneField(classes_model, null = True,on_delete=models.CASCADE,related_name="classes")
    section =  models.CharField(max_length=20,choices = sections,default ='A')

    class Meta:
        verbose_name ="student_realtions"
        verbose_name_plural = "student_realtions"
 
class attendence(models.Model):
    attendance = (
        ('present',"Present"),
        ('absent', "Absent"),
    )
    status = models.CharField(max_length=20,choices = attendance,default="absent")
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name="user")

    class Meta:
        verbose_name = "attendence"
        verbose_name_plural = "attendence"
 
class subject(models.Model):
    subjects = (
        ("En","English"),
        ("Math","Maths"),
        ("Hi","Hindi"),
        ("Sci","Science"),
        ("Ss","Social Science"),
        ('Skt','Sanskrit'),
        ('Env',"Environment"),
        ('Spt',"Sports"),
        ('Evs',"Environmental Studies or Environmental Sciences"),
        ("Computer","Computer"),
    )
    name = models.CharField(max_length=20,choices= subjects,unique=True)
    class Meta:
        verbose_name = "subject"
        verbose_name_plural = "subjects"


 
class teacher_relations(models.Model):
    subject = models.ForeignKey(subject,on_delete=models.CASCADE,related_name="subject")
    classes = models.ForeignKey(classes_model,on_delete=models.CASCADE,related_name="cla")
    teacher = models.ForeignKey(user_model,on_delete=models.CASCADE,related_name="teacher")
    class Meta:
        verbose_name = "teacher_relation"
        verbose_name_plural = "teacher_relations"

        