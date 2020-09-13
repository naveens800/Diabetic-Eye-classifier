from django.contrib import admin
from .models import Patient_info,imageInput

class Patient_info_mdl_admin(admin.ModelAdmin):
    list_display       = ["name","age","gender"]
    list_editable      = ["name"]
    list_display_links = ["gender"]
    list_filter        = ["date"]
    search_fields      = ["name"]
    
    class Meta:
        model = Patient_info



admin.site.register(Patient_info,Patient_info_mdl_admin)
admin.site.register(imageInput) 