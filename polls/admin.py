from django.contrib import admin
from .models import Service, User, Order, Profile

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'avatar')

admin.site.register(User)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Profile)