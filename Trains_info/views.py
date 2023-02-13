from django.shortcuts import render
from django.http import HttpResponse
from Trains_info.models import train_details
from Trains_info import forms

# Create your views here.

def home(Request):
    return render(Request,"Train_INFO/home.html")

def train_info(Request):
    form = forms.train_details()
    return render(Request,"Train_INFO/Trains_info.html",context=dict({'form_dict':form}))


def report(Request):
    train_model_details = train_details.objects.order_by('train_ID')
    train_details_dict ={"insert_train_details":train_model_details}
   # return HttpResponse("Collect Report info")
    return render(Request,"Train_INFO/report_info.html",context=train_details_dict)
