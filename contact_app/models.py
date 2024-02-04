from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    permissions = models.CharField(max_length=200)
    image = models.ImageField(upload_to='contact_app/static/contact_app/images/users', default="contact_app/static/contact_app/images/basicuser.png")
    favorites_tasks = models.ManyToManyField('Task', related_name='favorited_tasks', blank=True)
    company = models.CharField(max_length=200,default='N3Cure')
    role = models.CharField(max_length=200, default='employee')
    address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True) 
    note = models.CharField(max_length=200, default='none')
    birth_day = models.DateField(default='1970-01-01')

    def __str__(self) -> str:
        return f'{self.name}'

class Category(models.Model):
    category = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f'{self.category}'
        
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, default='none')
    phone_number = models.CharField(max_length=20, blank=True, null=True, default='none') 
    company = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    role=  models.CharField(max_length=200,default='none')
    description = models.CharField(max_length=200,default='none')

    def __str__(self) -> str:
        return f'{self.name}'


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks', null=True, blank=True)
    related_employees = models.ManyToManyField('User', related_name='related_employees')
    related_contacts = models.ManyToManyField('Contact', related_name='related_contacts')

    def __str__(self):
        return self.title
