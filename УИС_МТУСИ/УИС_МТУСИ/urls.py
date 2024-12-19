"""
URL configuration for УИС_МТУСИ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from studentsApp.views import (mentor_list, chat, feedback, event_list, create_event, register_mentor, add_language_skill,language_skill_list, create_mentor, update_mentor)

urlpatterns = [
    path('', mentor_list, name='home'),  # Adiciona a URL raiz
    path('accounts/', include('django.contrib.auth.urls')),  # Inclui as URLs de autenticação
    path('admin/', admin.site.urls),
    path('studentsApp/mentors/', mentor_list, name='mentor_list'),
    path('studentsApp/chat/<int:receiver_id>/', chat, name='chat'),
    path('studentsApp/feedback/', feedback, name='feedback'),
    path('studentsApp/events/', event_list, name='event_list'),
    path('studentsApp/create_event/', create_event, name='create_event'),
    path('studentsApp/register/', register_mentor, name='register_mentor'),
    path('studentsApp/add_language_skill/', add_language_skill, name='add_language_skill'),  # Добавление маршрута
    path('studentsApp/language_skills/', language_skill_list, name='language_skill_list'),  # Добавление маршрута
    path('studentsApp/create_mentor/', create_mentor, name='create_mentor'),  # URL for creating a new mentor
    path('studentsApp/update_mentor/<int:mentor_id>/', update_mentor, name='update_mentor'),  # URL for updating a
]
