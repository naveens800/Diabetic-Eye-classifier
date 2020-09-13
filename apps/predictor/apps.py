from django.apps import AppConfig
from django.conf import settings
import os
import joblib
class PredictorConfig(AppConfig):
    #create path to models
    path = os.path.join(settings.MODELS,'JOBmodel.sav')

    #load models into separate variables
    MLmodel = joblib.load(path)