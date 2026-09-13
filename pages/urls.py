from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('docs/getting-started/', views.getting_started, name='getting_started'),
    path('docs/blocks/', views.blocks, name='blocks'),
    path('docs/htmx/', views.htmx, name='htmx'),
    path('docs/<str:component>/', views.component, name='component'),
]
