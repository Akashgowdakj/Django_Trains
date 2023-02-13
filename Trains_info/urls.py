from django.urls import path,re_path
from Trains_info import views

urlpatterns = [
    re_path(r'^$',views.home,name='home'),
    re_path(r'^train_info',views.train_info,name='trains_info'),
    re_path(r'^report',views.report,name='report'),
]
