from django.db import models

# Create your models here.
class Patient_info(models.Model):
    name    = models.CharField(max_length = 50)
    doctor_name  = models.CharField(max_length = 50)
    choices = [('Male','Male'),('Female','Female'),('others','others')]
    gender  = models.CharField(max_length = 7,choices = choices,default = None,blank = True)
    age     = models.IntegerField()
    contact = models.CharField(max_length=10,default = None,blank = True)
    address = models.TextField(max_length = 100,default = None,blank  = True)
    date    = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name




class imageInput(models.Model):
    eye_image = models.FileField(blank = False,null = False)
    Patient_info = models.ForeignKey('Patient_info', on_delete=models.CASCADE,default = None)
    
    def __str__(self):
        return f"{self.eye_image.name}"