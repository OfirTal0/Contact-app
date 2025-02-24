import os
from django.core.wsgi import get_wsgi_application
from django.middleware.security import SecurityMiddleware
from django.contrib.sessions.middleware import SessionMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contacts.settings')

application = get_wsgi_application()  # תקרא לפונקציה זו פעם אחת בלבד
application = SessionMiddleware(application)  # הוסף את המידלוורק של session אחרי זה
