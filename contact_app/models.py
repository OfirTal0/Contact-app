from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    permissions = models.CharField(max_length=200)
    image = models.ImageField(upload_to='contact_app/static/contact_app/images/users')
    favorites = models.ManyToManyField('Contact', related_name='favorited_by')
    company = models.CharField(max_length=200,default='N3Cure')
    role = models.CharField(max_length=200, default='employee')
    address = models.CharField(max_length=200, default='none')
    phone_number = models.CharField(max_length=20, blank=True, null=True, default='none') 
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
