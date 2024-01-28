from django.shortcuts import render,redirect
from .models import User, Contact, Category, Task
from django.db.models import Q
from datetime import datetime
from django.utils import timezone


def get_date_time():
    current_time = datetime.now().time()
    if current_time < datetime.strptime("12:00:00", "%H:%M:%S").time():
        return "Morning"
    elif current_time < datetime.strptime("17:00:00", "%H:%M:%S").time():
        return "Afternoon"
    else:
        return "Evening"
    
def login(request):
    users = User.objects.all()
    message = ""
    if request.method == 'GET':
        if 'user_id' in request.session:
            return redirect('dashbord')
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        for user in users:
            if username == user.name and password == user.password:
                request.session["user_id"] = user.id
                return redirect('dashbord')
        message = "Login is not approved, please contact the administrator"
    return render(request, "login.html", {"message": message})

def index(request,message="", tasks=None):
    try: 
        user_id = request.session.get("user_id")
        if user_id :
            active_user = User.objects.get(id=user_id)
            contacts = Contact.objects.all()
            my_tasks = Task.objects.filter(Q(related_employees = active_user) & Q(completed = False))
            date_time = get_date_time()
            if tasks is None:
                tasks = Task.objects.all()
            return render(request, "dashbord.html", {"user": active_user,"contacts":contacts,"tasks": tasks, "my_tasks": my_tasks, "datetime":date_time, "message":message})
        else:
            return render(request, "login.html")
    except User.DoesNotExist:
        return render(request, "login.html")

def logout(request):
    request.session.clear()
    return render(request, 'login.html')

def add_task(request):
    user_id = request.session.get("user_id")
    active_user = User.objects.get(id=user_id)
    categories = Category.objects.all()
    users = User.objects.all()
    contacts = Contact.objects.all()
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('dashboard')
        if 'add_task' in request.POST:
            try:
                title = request.POST.get('title', '').title()
                description = request.POST.get('description', '')
                responsible_name = request.POST.get('responsible', '')
                due_date = request.POST.get('due_date', '').title()
                category_name = request.POST.get('category', '')
                responsible = User.objects.get(name=responsible_name)
                related_employees_ids = request.POST.getlist('related_employees', [])
                related_contacts_ids = request.POST.getlist('related_contacts', [])
                related_employees_ids = [int(id) for id in related_employees_ids]
                related_contacts_ids = [int(id) for id in related_contacts_ids]
                task = Task(
                    created_at=timezone.now(),
                    created_by=active_user,
                    title=title,
                    description=description,
                    responsible=responsible,
                    due_date=due_date,
                    category=Category.objects.get(category=category_name),
                )
                task.save()

                task.related_employees.set(User.objects.filter(id__in=related_employees_ids))
                task.related_contacts.set(Contact.objects.filter(id__in=related_contacts_ids))

                message = "Task added successfully"
                return render(request, "add_task.html", {"user": active_user, "categories": categories, "message": message, "users": users, "contacts": contacts})
            except: 
                message = "Problem adding the task, please contact the administrator"
                return render(request, "add_task.html", {"user": active_user, "categories": categories, "message": message, "users": users, "contacts": contacts})

    return render(request, "add_task.html", {"user": active_user, "categories": categories, "users": users, "contacts": contacts})

def crud(request):
    user_id = request.session.get("user_id")
    active_user = User.objects.get(id=user_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        if 'remove_fav' not in request.POST:
            task_id = request.POST.get('selected_task', '')
        else: 
            task_id = request.POST.get('task_to_remove', '')
        if task_id == '' and 'remove_fav' not in request.POST:
            message = "no task was selected, please select a task"
            return index(request, message=message)
        task = Task.objects.get(id=task_id)
        if 'remove_fav' in request.POST:
            active_user.favorites_tasks.remove(task)
            active_user.save()
            message = "Task remove favorites"
            return index(request, message=message)
        elif 'delete' in request.POST:
            task.delete()
            return index(request, message="")
        elif 'open' in request.POST:
            return render(request, "card.html", {"user":active_user,"type":"task","task":task})
        elif 'update' in request.POST:
            users = User.objects.all()
            contacts = Contact.objects.all()
            return render(request, "update_task.html", {"user": active_user,"categories":categories, "task":task,"users":users, "contacts":contacts})
        elif 'add_favorite' in request.POST:
            check_addition = active_user.favorites_tasks.filter(id=task.id).exists()
            if check_addition:
                message = "Task is already in your favorites"
            else:
                active_user.favorites_tasks.add(task)
                active_user.save()
                message = "Task added to favorites"
            return index(request, message=message)
        

def update(request,task_id):
    if request.method == 'POST':
        try:
            if 'update' in request.POST:
                title = request.POST.get('title', '').title()
                description = request.POST.get('description', '')
                responsible_name = request.POST.get('responsible', '')
                due_date = request.POST.get('due_date', '').title()
                category_name = request.POST.get('category', '')
                responsible = User.objects.get(name=responsible_name)
                related_employees_ids = request.POST.getlist('related_employees', [])
                related_contacts_ids = request.POST.getlist('related_contacts', [])
                completed = request.POST.get('completed', False)  
                related_employees_ids = [int(id) for id in related_employees_ids]
                related_contacts_ids = [int(id) for id in related_contacts_ids]
                task = Task.objects.get(id=task_id)

                task.updated_at = timezone.now()
                task.title = title
                task.description = description
                task.responsible = responsible
                task.category = Category.objects.get(category=category_name)
                task.due_date = due_date
                if completed != False:
                    task.completed = True 
                task.related_employees.set(User.objects.filter(id__in=related_employees_ids))
                task.related_contacts.set(Contact.objects.filter(id__in=related_contacts_ids))
                task.save()
                message = "Task updated successfully"
                return index(request, message=message)
            if 'cancel' in request.POST:
                return redirect('dashbord')
        except:
            message = "Problem updating the task, please contact the administrator"
            return index(request, message=message)


def search(request):
    text_to_search = request.POST.get('search', '')
    searched_tasks = Task.objects.filter(
                Q(title__icontains=text_to_search) | 
                Q(description__icontains=text_to_search) | 
                Q(due_date__icontains=text_to_search))
    return index(request, message="", tasks= searched_tasks)

def contacts(request):
    user_id = request.session.get("user_id")
    active_user = User.objects.get(id=user_id)
    categories = Category.objects.all()
    contacts = Contact.objects.all()
    employees = User.objects.all()
    return render(request, "contacts.html", {"user": active_user,"categories":categories,"contacts":contacts,"employees":employees})

def setting(request):
    user_id = request.session.get("user_id")
    active_user = User.objects.get(id=user_id)
    categories = Category.objects.all()
    if request.method == 'GET':
        return render(request, "setting.html", {"user": active_user,"categories":categories})
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return index(request, message="")
        try:
            name = request.POST.get('name', '').title()
            address = request.POST.get('address', '')
            phone_number = request.POST.get('phone_number', '')
            role = request.POST.get('role', '')
            birth_day = request.POST.get('birthday', '')
            note = request.POST.get('note', '')
            if birth_day == '':
                birth_day = '1970-01-01'
            User.objects.filter(id=user_id).update(name=name, address=address,phone_number=phone_number,birth_day=birth_day,role=role,note=note)
            message = "Details updated successfully"
            active_user = User.objects.get(id=user_id)
            return render(request, "setting.html", {"user": active_user,"categories":categories, "message":message})
        except:
            message = "Problem adding the contact, please contact the administrator"
            return render(request, "setting.html", {"user": active_user,"categories":categories, "message":message})

def card(request,contact_id,type):
    user_id = request.session.get("user_id")
    active_user = User.objects.get(id=user_id)
    if type == "contact":
        contact = Contact.objects.get(id=contact_id)
    if type == "user":
        contact = User.objects.get(id=contact_id)
    return render(request, "card.html", {"user": active_user,"type":type,"contact": contact})
