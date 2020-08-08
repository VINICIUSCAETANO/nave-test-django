from django.db import models
from django.utils import timezone

# Create your models here.


#modelo Usuário

class User(models.Model):
    email = models.EmailField(name="email do Usuário", unique=True, blank=False, null=False)
    password = models.CharField(name="senha", max_length=20, blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


#modelo Naver

JOBS_ROLES = [
    ('DEV', 'Desenvolvedor'),
    ('DES', 'Designer'),
    ('UXD', 'Designer de UX')
]

class Naver(models.Model):
    name = models.CharField(name="Nome do Naver", max_length=50)
    birthdate = models.DateField(name="Data de Nascimento")
    admission_date = models.DateField(name="Data de Admissão na Empresa")
    job_role = models.CharField("Cargo do naver", choices=JOBS_ROLES, max_length=10)
    projects = models.ManyToManyField(User, through='Project')
    created_date = models.DateTimeField(default=timezone.now)
    # added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

#modelo Project

class Project(models.Model):
    name = models.CharField(name="descrição do Projeto", max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    naver = models.ForeignKey(Naver, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name