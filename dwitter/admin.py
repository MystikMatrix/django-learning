from django.contrib import admin

# Register your models here.
# dwitter/admin.py

from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile

#admin.site.register(Profile)

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    def get_inlines(self, request, obj=None):
        if obj:
            return [ProfileInline]
        else:
            return []

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group) #this line to unregister the Group model
# Remove: admin.site.register(Profile)
