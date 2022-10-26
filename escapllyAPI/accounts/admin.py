from pyexpat import model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from .models import MyUser, UserProfile


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('email',)

# Register your models here.

class AccountAdmin(UserAdmin):
    add_form = CustomUserCreationForm

admin.site.register(MyUser, AccountAdmin)
# admin.site.register([MyUser, UserProfile])
admin.site.register(UserProfile)
