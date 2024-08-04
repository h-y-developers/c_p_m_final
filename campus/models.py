from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from datetime import datetime,date
import uuid
import os
from multiselectfield import MultiSelectField
# from rest_framework import fields, serializers
# Create your models here.



class student_data(models.Model):
    clg_id_no = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)




class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    username = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=100)
    
    dept = models.CharField(max_length=100,default="")
    profile_pic = models.FileField(null=True,upload_to='profile_pictures/',default="profile_pictures/H&Y.png")
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    college_name = models.CharField(max_length =100, default="BVM")


    def profile_filename(self):
        return self.profile_pic.name

    


class Marks(models.Model):
    id_no = models.CharField(unique=True,max_length=20,null=True)
    sem_1 = models.CharField(blank=True,max_length=20,default="0.0")
    sem_2 = models.CharField(blank=True,max_length=20,default="0.0")
    sem_3 = models.CharField(blank=True,max_length=20,default="0.0")
    sem_4 = models.CharField(blank=True,max_length=20,default="0.0")
    sem_5 = models.CharField(blank=True,max_length=20,default="0.0")
    sem_6 = models.CharField(blank=True,max_length=20,default="0.0")
    sem_7 = models.CharField(blank=True,max_length=20,default="0.0")
    sem_8 = models.CharField(blank=True,max_length=20,default="0.0")
    first_year = models.CharField(blank=True,max_length=20,default="0.0")
    second_year = models.CharField(blank=True,max_length=20,default="0.0")
    third_year = models.CharField(blank=True,max_length=20,default="0.0")
    fourth_year = models.CharField(blank=True,max_length=20,default="0.0")

    def __str__(self):
        return self.id_no

    





# class Interests(models.Model):
#     boolschoice = (
#         ("wd","Web Development"),("ad","App Development"),("cd","Cloud Computing"),
#         ("excel","Excel"),("wp","Wordpress"),("react","React"),("dj","Django"),
#         ("bc","Block Chain"),("dm","Data Mining"),("py","Python"),("c","C/C++"),
#         ("j","Java")
#     )
#     a_interest = models.CharField(max_length=100,choices=boolschoice,null=True)


# class Skills(models.Model):
#     skill = models.CharField(max_length = 100,default="")

#     def __str__(self):
#         return self.skill


class Student(models.Model):
    
    boolChoice = (
        ("Male","Male"),("Female","Female")
        )
   
    booldchoice  = (
        ("Mechanical","Mechanical"),
        ("EC","EC"),
        ("Civil","Civil"),
        ("IT","IT"),("EL","EL"),("EE","EE"),("Production","Production")
    )

    boolschoice = (
        ("wd","Web_Development"),("ad","App_Development"),("cd","Cloud_Computing"),
        ("excel","Excel"),("wp","Wordpress"),("react","React"),("dj","Django"),
        ("bc","Block_Chain"),("dm","Data_Mining"),("py","Python"),("c","C/C++"),
        ("j","Java")
    )
    boolichoice = (
        ("wd","Web Development"),("ad","App Development"),("cd","Cloud Computing"),
        ("excel","Excel"),("wp","Wordpress"),("react","React"),("dj","Django"),
        ("bc","Block Chain"),("dm","Data Mining"),("py","Python"),("c","C/C++"),
        ("j","Java")
    )
    Id_number = models.CharField(max_length=100,primary_key=True,default="")
    year = models.CharField(max_length=5,default="1")
    slug = models.SlugField(default="")
    fname = models.CharField(max_length=100,blank=True,default="")
    lname = models.CharField(max_length=100,blank=True,default="")
    gender = models.CharField(max_length=6,choices=boolChoice,null=True)
    dob = models.DateField()
    email = models.EmailField(max_length = 254,blank=True,default="")
    mobile = models.CharField(max_length=12,blank=True,default="")
    # role = models.CharField(max_length = 1,choices=boolrchoice,null=True)
    dept = models.CharField(max_length = 10,choices=booldchoice,null=True)
    enrollment = models.CharField(max_length=20,null=True)
    
    permanent_address = models.CharField(max_length=256,null=True)
    state = models.CharField(max_length=100,null=True)
    resident_address = models.CharField(max_length=100,null=True)
    pincode = models.CharField(max_length=6,null=True)
    city= models.CharField(max_length = 100,null=True)
    country = models.CharField(max_length = 100,null=True)
    ssc = models.CharField(max_length = 100,blank=True,default="")
    # ssc_result = models.FileField(blank=True,default="",upload_to='ssc_results/')
    ssc_result = models.CharField(max_length=20,blank=True,default="")
    hsc_result = models.CharField(max_length=20,blank=True,default="")
    hsc = models.CharField(max_length = 100,blank=True,default="")
    profile_pic = models.TextField(null=True,default="H&Y.png")
    # hsc_result = models.FileField(blank=True,default="",upload_to='hsc_results/')
    fb_profile = models.CharField(max_length=255,blank=True,default="")
    insta_profile = models.CharField(max_length=255,blank=True,default="")
    linkedin_profile = models.CharField(max_length=255,blank=True,default="")
    website = models.URLField(max_length=100,blank=True,default="")
    interest = MultiSelectField(choices=boolichoice,blank=True,default="")
    

    def sscfilename(self):
        return os.path.basename(self.ssc_result.name)

    def hscfilename(self):
        return os.path.basename(self.hsc_result.name)



# class Achievement(models.Model):
#     achieve_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     student_name = models.CharField(max_length=100)
#     certificate_name= models.CharField(max_length = 100,blank=True)
#     field_type = models.CharField(max_length=100)
#     issuer_name = models.CharField(max_length = 100,blank=True)
#     certificate_img = models.FileField(upload_to='achievements/')
#     college_name = models.CharField(max_length =100, default="BVM")

    # class Meta:
    #     db_table = "achievements"
class Achievement(models.Model):

    achieve_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    student_name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=100,default="")
    certificate_name= models.CharField(max_length = 100,blank=True)
    issuer_name = models.CharField(max_length = 100,blank=True)
    certificate_img = models.FileField(null=True,upload_to='achievements/')
    college_name = models.CharField(max_length =100, default="BVM")

    # class Meta:
    #     db_table = "achievements"


class Skills(models.Model):
    boolschoice = (
        ("wd","Web Development"),("ad","App Development"),("cd","Cloud Computing"),
        ("excel","Excel"),("wp","Wordpress"),("react","React"),("dj","Django"),
        ("bc","Block Chain"),("dm","Data Mining"),("py","Python"),("c","C/C++"),
        ("j","Java")
        )
    username = models.CharField(unique=True,max_length=100,null=True)
    skills = models.CharField(max_length=400,blank=True)
    # interest = models.CharField(max_length=400,blank=True)

    # skills = MultiSelectField(choices=boolschoice,max_length = 100,default="")
    # interest = MultiSelectField(choices=boolschoice,max_length=100,default="")

    def __str__(self):
        return self.username


class Skill_list(models.Model):
    
    skill_name = models.CharField(unique=True,max_length=255,default="")
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name



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




class Company(models.Model):
    company_id = models.CharField(max_length=255, editable=False)
    company_username = models.CharField(max_length=100,default="")
    company_name = models.CharField(max_length = 100,default="")
    field_name = models.CharField(max_length=100,default="")
    mobile = models.CharField(max_length=10,default="")
    email = models.CharField(max_length = 100)
    description = models.TextField(default="")
    website = models.URLField(max_length=100,blank=True,default="")
    address = models.TextField(default="")
    city = models.CharField(max_length=100,default="")
    state = models.CharField(max_length=100,default="")
    country = models.CharField(max_length=100,default="")
    year_found = models.CharField(max_length=6, default="")
    no_of_employee = models.CharField(max_length=200,default = "")
    fb_profile = models.CharField(max_length=255,default="")
    insta_profile = models.CharField(max_length=255,default="")
    linkedin_profile = models.CharField(max_length=255,default="")
    # type_of_service
    # required_student = models.IntergerField()
    # placed_student = models.IntergerField()
    college_name = models.CharField(max_length =100, default="BVM")

    def __str__(self):
        return self.company_name




class Department(models.Model):
    dept_id = models.AutoField(primary_key=True,unique=True)
    college_name= models.CharField(max_length = 100, default="BVM")
    dept_name = models.CharField(max_length=100)
    dept_hod = models.CharField(max_length = 100)
    no_of_faculty = models.CharField(max_length=10)
    est_year = models.CharField(max_length=5)

    # class Meta:
    #     db_table = "departments"
class Faculties(models.Model):
    boolChoice = (
        ("Male","Male"),("Female","Female")
        )
    
    booldchoice  = (
        ("Mechanical","Mechanical"),
        ("EC","EC"),
        ("Civil","Civil"),
        ("IT","IT"),("EL","EL"),("EE","EE"),("Production","Production")
    )

    # boolschoice = (
    #     ("wd","Web Development"),("ad","App Development"),("cd","Cloud Computing"),
    #     ("excel","Excel"),("wp","Wordpress"),("react","React"),("dj","Django"),
    #     ("bc","Block Chain"),("dm","Data Mining"),("py","Python"),("c","C/C++"),
    #     ("j","Java")
    # )
    Id_number = models.CharField(max_length=100,unique=True,default="")
    slug = models.SlugField(unique=True,default="")
    fname = models.CharField(max_length=100,null=True)
    lname = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=10,choices=boolChoice,null=True)
    dob = models.DateField(default=datetime.now())
    email = models.EmailField(max_length = 254,null=True)
    mobile = models.CharField(max_length=12,null=True)
    # role = models.CharField(max_length = 1,choices=boolrchoice,null=True)
    dept = models.CharField(max_length = 10,choices=booldchoice,null=True)
    
    id_no = models.CharField(max_length=10,null=True)
    desg = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=256,null=True)
    state = models.CharField(max_length=100,null=True)
    resident_address = models.CharField(max_length=100,null=True)
    pincode = models.CharField(max_length=6,null=True)
    city= models.CharField(max_length = 100,null=True)
    country = models.CharField(max_length = 100,null=True)
    B_E_college_name = models.CharField(max_length = 100,null=True)
    B_E_college_result = models.FileField(null=True)
    M_E_college_name = models.CharField(max_length = 100,null=True)
    M_E_college_result = models.FileField(null=True)



# class Project(models.Model):
#     project_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     # subject_id = models.CharField(max_length=100)
#     student_name = models.CharField(max_length = 100)
#     project_name= models.CharField(max_length = 100,blank=True)
#     description = models.CharField(max_length = 500,blank=True)
#     url = models.URLField(max_length=100,blank=True)
#     rating_star = models.CharField(max_length =3,default="0")
#     college_name = models.CharField(max_length =100, default="BVM")
# class Project(models.Model):
#     project_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     # subject_id = models.CharField(max_length=100)
#     student_id = models.CharField(max_length = 100)
#     project_name= models.CharField(max_length = 100,blank=True)
#     description = models.CharField(max_length = 500,blank=True)
#     url = models.URLField(max_length=100,blank=True)
#     rating_star = models.CharField(max_length =3)
#     college_name = models.CharField(max_length =100, default="BVM")

    # class Meta:
    #     db_table = "projects"






class Subject(models.Model):
    subject_id = models.CharField(max_length=100,  primary_key=True, unique=True)
    subject_name = models.CharField(max_length = 100)
    semester = models.CharField(max_length=3)
    teach_year = models.CharField(max_length = 5)
    faculty_id = models.CharField(max_length=100)
    dept_id = models.CharField(max_length=100)
    college_name = models.CharField(max_length =100, default="")

    # class Meta:
    #     db_table = "subjects"





class Timetable(models.Model):
    time_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    semester = models.CharField(max_length = 3)
    year = models.CharField(max_length=5)
    time = models.CharField(max_length = 100)
    faculty_name = models.CharField(max_length = 100)
    lab_lec = models.CharField(max_length=1)
    subject_name = models.CharField(max_length = 20)
    batch_id = models.CharField(max_length=5)
    college_name = models.CharField(max_length =100, default="BVM")

class Events(models.Model):
    # event_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # faculty_name = models.CharField(max_length=200)
    event_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    instructions = models.CharField(max_length=1000,blank=True,default="")
    url = models.URLField(max_length=100,blank=True)
    file = models.FileField(upload_to='events/' ,null=True)
    # depart_name = models.CharField(max_length=200)
    # college_name = models.CharField(max_length =100, default="BVM")
    event_date = models.DateField(default=datetime.now())

    def __str__(self):
        return self.event_name

    def event_poster_name(self):
        return os.path.basename(self.file.name)    

    def is_past_due(self):
        return date.today() > self.date



class Exams(models.Model):
    exam_choice=(
        ("Mid","Mid"),
        ("External","External")
    )
    exam_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    subject_id = models.CharField(max_length=200)
    stud_name = models.CharField(max_length=200)
    exam_type = models.CharField(max_length=10,choices=exam_choice)
    obtain_marks = models.CharField(max_length=10)
    total_marks = models.CharField(max_length=10)




class Requirements(models.Model):
    company_name = models.CharField(default="",max_length=200)
    job_description = models.CharField(max_length=200,default="")
    no_of_vacancies = models.IntegerField()
    url = models.URLField(blank=True)
    file = models.FileField(null=True,upload_to="requirements/")


    def __str__(self):
        return self.company_name





class Project(models.Model):
    project_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    student_name = models.CharField(max_length = 100)
    project_name= models.CharField(max_length = 100,blank=True)
    description = models.CharField(max_length = 500,blank=True)
    url = models.URLField(max_length=100,blank=True)
    
    likes = models.ManyToManyField(User,default=None,blank=True)


    def __str__(self):
        return self.project_name

    def num_likes(self):
        return self.likes.all.count()



like_choices = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    value = models.CharField(choices=like_choices,default='Like',max_length=10)

    # def user_like_post(sender,instance, *args, **kwargs):
    #     like = instance
    #     project = like.project
    #     sender = like.user
    #     notify = Notification(project=project,sender=sender,user=User,notification_type=1)
    #     notify.save()

    def _str_(self):
        return str(self.project)




