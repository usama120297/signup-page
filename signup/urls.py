from . import views
from django.conf.urls import include, url

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^form/', views.adddata, name='adddata'),
    url(r'^show/', views.showdata, name='showdata'),
    url(r'^success/', views.success, name='success'),
]
