from django.urls import path
from . import views
app_name = 'predictor'

urlpatterns = [
   path('Patient_form',views.accept_details,name = 'Patient_form'),
   path('upload_image',views.upload_image,name = 'upload_image'),
   #path('',views.index,name = 'index')
]