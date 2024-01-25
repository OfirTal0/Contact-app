from django.shortcuts import render,redirect
from .models import User, Contact, Category
from django.db.models import Q
from datetime import datetime

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

def index(request):
    try: 
        user_id = request.session.get("user_id")
        if user_id :
            active_user = User.objects.get(id=user_id)
            contacts = Contact.objects.all()
            date_time = get_date_time()
            return render(request, "dashbord.html", {"user": active_user,"contacts":contacts,"datetime":date_time})
        else:
            return render(request, "login.html")
    except User.DoesNotExist:
        return render(request, "login.html")

def logout(request):
    request.session.clear()
    return render(request, 'login.html')

def add_contact(request):
    user_id = request.session.get("user_id")
    active_user = User.objects.get(id=user_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('dashbord')
        if 'add_contact' in request.POST:
            try:
                name = request.POST.get('name', '').title()
                email = request.POST.get('email', '')
                phone_number = request.POST.get('phone_number', '')
                company = request.POST.get('company', '').title()
                role = request.POST.get('role', '')
                description = request.POST.get('description', '')
                category = request.POST.get('category', '')
                if Contact.objects.filter(email=email).exists():
                    message = "Contact with this email already exists"
                    return render(request, "add_contact.html", {"user": active_user,"categories":categories,"message":message})
                else:
                    contact = Contact(name=name,email=email,phone_number=phone_number,company=company,role=role,description=description,category=Category.objects.get(category=category))
                    contact.save()
                    message = "Contact added successfully"
                    return render(request, "add_contact.html", {"user": active_user,"categories":categories,"message":message})
            except:
                message = "Problem adding the contact, please contact the administrator"
                return render(request, "add_contact.html", {"user": active_user,"categories":categories,"message":message})
    return render(request, "add_contact.html", {"user": active_user,"categories":categories})

def crud(request):
    user_id = request.session.get("user_id")
    active_user = User.objects.get(id=user_id)
    contacts = Contact.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        if 'remove_fav' not in request.POST:
            contact_id = request.POST.get('selected_contact', '')
        else: 
            contact_id = request.POST.get('contact_to_remove', '')
        if contact_id == '' and 'remove_fav' not in request.POST:
            message = "no contact was selected, please select a contact"
            return render(request, "dashbord.html", {"user": active_user,"contacts":contacts,"message":message})
        contact = Contact.objects.get(id=contact_id)
        if 'remove_fav' in request.POST:
            active_user.favorites.remove(contact)
            active_user.save()
            return render(request, "dashbord.html", {"user": active_user,"contacts":contacts})
        elif 'delete' in request.POST:
            contact.delete()
            return redirect('dashbord')
        elif 'update' in request.POST:
            return render(request, "update_contact.html", {"user": active_user,"categories":categories, "contact":contact})
        elif 'add_favorite' in request.POST:
            active_user.favorites.add(contact)
            active_user.save()
            message = "contact added to favorites"
            return render(request, "dashbord.html", {"user": active_user,"contacts":contacts,"message":message})
        

def update(request,contact_id):
    user_id = request.session.get("user_id")
    active_user = User.objects.get(id=user_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        try:
            if 'update' in request.POST:
                name = request.POST.get('name', '').title()
                email = request.POST.get('email', '')
                phone_number = request.POST.get('phone_number', '')
                company = request.POST.get('company', '').title()
                role = request.POST.get('role', '')
                description = request.POST.get('description', '')
                category = request.POST.get('category', '')
                Contact.objects.filter(id=contact_id).update(name=name, email=email,phone_number=phone_number,category=Category.objects.get(category=category),role=role,description=description,company=company)
                message = "Contact updated successfully"
                contact = Contact.objects.get(id=contact_id)
                return render(request, "update_contact.html", {"user": active_user,"categories":categories,"message":message,"contact":contact})
            if 'cancel' in request.POST:
                return redirect('dashbord')
        except:
            message = "Problem adding the contact, please contact the administrator"
            return render(request, "update_contact.html", {"user": active_user,"categories":categories,"contact":contact,"message":message})


def search(request):
    user_id = request.session.get("user_id")
    active_user = User.objects.get(id=user_id)
    text_to_search = request.POST.get('search', '')
    searched_contacts = Contact.objects.filter(
                Q(name__icontains=text_to_search) | 
                Q(email__icontains=text_to_search) | 
                Q(phone_number__icontains=text_to_search) | 
                Q(company__icontains=text_to_search) | 
                Q(category__category__icontains=text_to_search)|
                Q(role__icontains=text_to_search) | 
                Q(description__icontains=text_to_search))
    return render(request, "dashbord.html", {"user": active_user,"contacts":searched_contacts})

def groups(request):
    user_id = request.session.get("user_id")
    active_user = User.objects.get(id=user_id)
    categories = Category.objects.all()
    contacts = Contact.objects.all()
    employees = User.objects.all()
    return render(request, "groups.html", {"user": active_user,"categories":categories,"contacts":contacts,"employees":employees})

def setting(request):
    user_id = request.session.get("user_id")
    active_user = User.objects.get(id=user_id)
    categories = Category.objects.all()
    if request.method == 'GET':
        return render(request, "setting.html", {"user": active_user,"categories":categories})
    if request.method == 'POST':
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

