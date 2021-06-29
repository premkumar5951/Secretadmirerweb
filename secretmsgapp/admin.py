from django.contrib import admin
from .models import txtmsg,UserProfile,User,feedbackform
# Register your models here.

admin.site.register(txtmsg)
admin.site.register(feedbackform)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display=('id', 'username', "email","first_name","last_name")
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('id', "user")