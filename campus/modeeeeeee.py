from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from datetime import datetime
import uuid
# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    college_name = models.CharField(max_length =100, default="BVM")

# class Admin(models.Model):
#     username = models.CharField(unique=True,primary_key=True,max_length=20)
#     # name= models.CharField(max_length = 100)
#     # mobile_no = models.CharField(max_length=12)
#     # email_id = models.CharField(max_length = 100)
#     password = models.CharField(max_length=100)
#     # college_name = models.CharField(max_length =100, default="BVM")

#     # class Meta:
#     #     db_table = "admin"


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True,unique=True)
    college_name= models.CharField(max_length = 100, default="BVM")
    dept_name = models.CharField(max_length=100)
    # dept_hod = models.CharField(max_length = 100)
    # no_of_faculty = models.CharField(max_length=10)
    # est_year = models.CharField(max_length=5)

    def __str__(self):
        return self.dept_name

    # class Meta:
    #     db_table = "departments"


class Students(models.Model):
    boolChoice = (
        ("Male","Male"),("Female","Female")
        )
    boolrchoice = (
        ("Student","Student"),("Staff","Staff")
    )
    booldchoice  = (
        ("Mechanical","Mechanical"),
        ("EC","EC"),
        ("Civil","Civil"),
        ("IT","IT"),("EL","EL"),("EE","EE"),("Production","Production")
    )
    student_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fname = models.CharField(max_length=100,null=True)
    lname = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=10,choices=boolChoice,null=True)
    dob = models.DateField(null=True)
    email = models.EmailField(max_length = 254,null=True)
    mobile = models.CharField(max_length=12,null=True)
    role = models.CharField(max_length = 10,choices=boolrchoice,null=True)
    batch_id = models.CharField(max_length=10)
    # dept_name = models.CharField(max_length = 10,choices=booldchoice,null=True)
    depart_name = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dept_name')
    # city = models.CharField(max_length = 100)
    # residential_addr = models.CharField(max_length = 255)
    # permanant_addr = models.CharField(max_length=255)
    # ssc_marks = models.CharField(max_length = 10,default = '0')
    # hsc_marks = models.CharField(max_length=10,default = '0')
    # sem_1 = models.CharField(max_length = 10,default = '0')
    # sem_2 = models.CharField(max_length=10,default = '0')
    # sem_3 = models.CharField(max_length = 10,default = '0')
    # sem_4 = models.CharField(max_length=10,default = '0')
    # sem_5 = models.CharField(max_length = 10,default = '0')
    # sem_6 = models.CharField(max_length=10,default = '0')
    # sem_7 = models.CharField(max_length = 10,default = '0')
    # sem_8 = models.CharField(max_length=10,default = '0')
    # dept_id = models.CharField(max_length=5)
    # batch_id = models.CharField(max_length=5)
    college_name = models.CharField(max_length =100, default="BVM")

    def __str__(self):
        return self.student_id
    # class Meta:
    #     db_table = "students"



class Faculties(models.Model):
    # faculty_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    faculty_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    faculty_name = models.CharField(max_length = 100)
    mobile_no = models.CharField(max_length=12)
    email_id = models.CharField(max_length = 100)
    date_join = models.DateField()
    depart_name = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dept_name')
    college_name = models.CharField(max_length =100, default="BVM")

    # class Meta:
    #     db_table = "faculties"

    def __str__(self):
        return self.faculty_name





class Subjects(models.Model):
    subject_id = models.CharField(max_length=100,  primary_key=True, unique=True)
    subject_name = models.CharField(max_length = 100)
    semester = models.CharField(max_length=3)
    teach_year = models.CharField(max_length = 5)
    faculty_id = models.ForeignKey(Faculties, on_delete=models.CASCADE, related_name='faculty_name')
    depart_name = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dept_name')
    college_name = models.CharField(max_length =100, default="BVM")


    def __str__(self):
        return self.subject_name



class Achievements(models.Model):
    achieve_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    achieve_name= models.CharField(max_length = 100)
    stud_name = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='student_name')
    field_name = models.CharField(max_length = 100)
    company_name = models.CharField(max_length = 100)
    issue_date = models.DateField()
    college_name = models.CharField(max_length =100, default="BVM")

    # class Meta:
    #     db_table = "achievements"




class Events(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    event_name = models.CharField(max_length=200)
    facultyy_name = models.ForeignKey(Faculties, on_delete=models.CASCADE, related_name='faculty_name')
    depart_name = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dept_name')
    college_name = models.CharField(max_length =100, default="BVM")
    event_date = models.DateField()

    def __str__(self):
        return self.event_id


class Exams(models.Model):
    exam_choice=(
        ("Mid","Mid"),
        ("External","External")
    )
    exam_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_name')
    stud_name = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='student_name')
    exam_type = models.CharField(max_length=10,choices=exam_choice)
    obtain_marks = models.CharField(max_length=10)
    total_marks = models.CharField(max_length=10)


    def __str__(self):
        return self.exam_id







class College(models.Model):
    index_no = models.CharField(max_length=100,primary_key=True)
    name= models.CharField(max_length = 100, default="BVM")
    university = models.CharField(max_length=100)
    city = models.CharField(max_length = 100)
    address = models.CharField(max_length=255)
    email_id = models.CharField(max_length=100)
    helpline_no = models.CharField(max_length =100)

    # class Meta:
    #     db_table = "college"




class Comapnies(models.Model):
    company_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    company_name = models.CharField(max_length = 100)
    field_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length = 100)
    coming_date = models.DateField()
    job_description = models.CharField(max_length=255)
    # required_student = models.IntergerField()
    # placed_student = models.IntergerField()
    college_name = models.CharField(max_length =100, default="BVM")

    # class Meta:
    #     db_table = "companies"








class Projects(models.Model):
    project_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    facultyy_name = models.ForeignKey(Faculties, on_delete=models.CASCADE, related_name='faculty_name')
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_name')
    student_name = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='student_name')
    definition = models.CharField(max_length = 255)
    project_sem = models.CharField(max_length=4)
    project_year = models.CharField(max_length = 5)
    source = models.CharField(max_length=100)
    due_date = models.DateField()
    rating_star = models.CharField(max_length =3)
    college_name = models.CharField(max_length =100, default="BVM")

    # class Meta:
    #     db_table = "projects"











    # class Meta:
    #     db_table = "subjects"





class Timetable(models.Model):
    time_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    semester = models.CharField(max_length = 3)
    year = models.CharField(max_length=5)
    time = models.CharField(max_length = 100)
    faculty_name = models.ForeignKey(Faculties, on_delete=models.CASCADE, related_name='faculty_name')
    lab_lec = models.BooleanField(default=False)
    subject_name = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='subject_name')
    batch_id = models.CharField(max_length=5)
    college_name = models.CharField(max_length =100, default="BVM")

    # class Meta:
    #     db_table = "timetable"




# class User_info(models.Model):
#     user_id = models.CharField(unique=True,primary_key=True,max_length=20)
#     email_id = models.CharField(max_length = 100)
#     user_type = models.CharField(max_length = 10)
#     password = models.CharField(max_length = 100)
#     dept_id = models.CharField(max_length=100)
#     college_name = models.CharField(max_length =100, default="BVM")

    # class Meta:
    #     db_table = "user_info"

