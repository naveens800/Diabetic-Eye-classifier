from django.urls import path
from . import views
app_name = 'webapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('AI_in_Healthcare',views.AiHC,name='AiHC'),
    path('Diagnosis',views.diagnosis,name = 'diagnosis'),
    path('DiabeticRetinopathy',views.DbR,name = 'DbR'),
    path('Deeplearning',views.deeplearning,name = 'deeplearning'),
    path('SignsAndSymptoms',views.Signs,name = 'Signs'),
]