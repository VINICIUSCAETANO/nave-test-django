from django.db import models
from django.utils import timezone

# Create your models here.


#modelo Usuário

class User(models.Model):
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.email

 
#modelo Project

class Project(models.Model):
    name = models.CharField(max_length=30)
    #navers = models.ManyToManyField(Naver)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

#modelo Naver

JOBS_ROLES = [
    ('DEV', 'Desenvolvedor'),
    ('DES', 'Designer'),
    ('UXD', 'Designer de UX')
]

class Naver(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField()
    admission_date = models.DateField()
    job_role = models.CharField(choices=JOBS_ROLES, max_length=10)
    projects = models.ManyToManyField(Project, default=None, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name