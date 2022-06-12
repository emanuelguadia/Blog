from django.urls import path
from . import views
my_app = 'articles'
urlpatterns = [
    path('', views.article_lists, name='list'),
    path('<slug:slug>/', views.article_detail, name='detail'),
]
