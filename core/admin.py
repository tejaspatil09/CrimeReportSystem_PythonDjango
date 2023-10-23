from django.contrib import admin
from .models import AddComplaint
# Register your models here.

@admin.register(AddComplaint)
class AddcomplaintAdmin(admin.ModelAdmin):
    list_display =['id','username','mobile_no','name','title','city','reported_date','category','description','status']
    search_fields = ('city',)
    list_filter = ['city']
