1. python -m django startproject blog
2. cd blog
3. code .
4. ctrl + `
5. cmd
6. python manage.py migrate
7. python manage.py startapp app
8. settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app', <= ဒီမှာ
]
9. settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  <= ဒီမှာ
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

10. terminal => mkdir templates
11. templates => index.html file ဆောက် => ! enter (Hello World)
12. views.py
def index(request):
    return render(request,'index.html')

13. urls.py
from django.contrib import admin
from django.urls import path
from app import views <= ဒီမှာတစ်ကြောင်း

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),  <= ဒီမှာတစ်ကြောင်း
]

14. terminal
python manage.py runserver