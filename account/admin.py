from django.contrib import admin
from .models import Account,Follow

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_filter = ("first_name")
    list_display = ("first_name")


admin.site.register(Account)
admin.site.register(Follow)
