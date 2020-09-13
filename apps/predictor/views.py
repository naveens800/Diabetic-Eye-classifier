import cv2
import numpy as np
import matplotlib as plt
import os
from keras.preprocessing import image
import plotly.express as px
from plotly.offline import plot
import urllib
import base64
import pandas as pd
import io
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)





from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Patient_info,imageInput
from .forms import PatientForm,imageInputForm
from django.shortcuts import render
from .apps import PredictorConfig
IMG_SIZE = 224
global graph

#initializing the graph
graph = tf.get_default_graph()

# Create your views here.
def accept_details(request):

    # If form is submitted
    if request.method =='POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('predictor:upload_image'))

    # If form is requested
    form = PatientForm()
    context = {'form':form}
    return render(request,'predictor/accept_details.html',context)


def upload_image(request):
    # If image is uploaded & recieved by server
    if request.method=='POST':
        form = imageInputForm(request.POST,request.FILES)
        if form.is_valid():
            fileObj = request.FILES['eye_image']
            fs = FileSystemStorage()
            filePathName=fs.save(fileObj.name,fileObj)
            filePathName = fs.url(filePathName)
            testimage = '.'+filePathName
            img = image.load_img(testimage, target_size=(IMG_SIZE, IMG_SIZE))
            img =preprocess_image(testimage)
            img = np.expand_dims(img, axis=0)
            with graph.as_default():
                probs=PredictorConfig.MLmodel.predict_proba(img)
            fiveProbs = []
            labels = ['No DR','Mild','Moderate','Severe','Proliferative DR']
            for i in range(5):
                fiveProbs.append(probs[0,i])
            label = fiveProbs.index(max(fiveProbs))
            print(label)
            data = pd.DataFrame(zip(fiveProbs,labels),columns=['fiveProbs','labels'])
            fig = px.funnel(data, x='fiveProbs', y='labels')
            plt_div = plot(fig, output_type='div',include_plotlyjs=False)



        context={
            'filePathName':filePathName,
            'filename':fileObj.name,
            'plt_div':plt_div,
            'label':label,
        }
        return render(request,'predictor/pred.html',context)
    # If Image Upload Page Requested
    else:
        form    = imageInputForm()
        context = {'form':form}
        return render(request,'predictor/upload_image.html',context)
    











def preprocess_image(image_path, desired_size=IMG_SIZE):
    im = load_ben_color(image_path,sigmaX = 30)
    return im

def load_ben_color(path, sigmaX=10):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = crop_image_from_gray(image)
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    image=cv2.addWeighted ( image,4, cv2.GaussianBlur( image , (0,0) , sigmaX) ,-4 ,128)
        
    return image

def crop_image_from_gray(img,tol=7):
    if img.ndim ==2:
        mask = img>tol
        return img[np.ix_(mask.any(1),mask.any(0))]
    elif img.ndim==3:
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        mask = gray_img>tol
        
        check_shape = img[:,:,0][np.ix_(mask.any(1),mask.any(0))].shape[0]
        if (check_shape == 0): # image is too dark so that we crop out everything,
            return img # return original image
        else:
            img1=img[:,:,0][np.ix_(mask.any(1),mask.any(0))]
            img2=img[:,:,1][np.ix_(mask.any(1),mask.any(0))]
            img3=img[:,:,2][np.ix_(mask.any(1),mask.any(0))]
    #         print(img1.shape,img2.shape,img3.shape)
            img = np.stack([img1,img2,img3],axis=-1)
    #         print(img.shape)
        return img