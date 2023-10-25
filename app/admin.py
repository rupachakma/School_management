from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import CourseModel, SessionyearModel, StudentModel, customUser

# Register your models here.
class UserModel(UserAdmin):
    list_display = ['id','username','user_type']

admin.site.register(customUser,UserModel)
admin.site.register(CourseModel)
admin.site.register(SessionyearModel)
admin.site.register(StudentModel)
