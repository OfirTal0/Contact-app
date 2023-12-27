from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    permissions = models.CharField(max_length=200)
    image = models.ImageField(upload_to='contact_app/static/contact_app/images')
    favorites = models.ManyToManyField('Contact', related_name='favorited_by')
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
