from django import forms

# Create your models here.
class train_details(forms.Form):
    train_ID = forms.IntegerField()
    train_Name = forms.CharField()
    origin_info = forms.CharField()
    destination_info = forms.CharField()
    departure_time = forms.TimeField()
    arrival_time = forms.TimeField()
