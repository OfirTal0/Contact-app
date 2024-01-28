from django.contrib import admin

from .models import User, Category, Contact, Task

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Task)

