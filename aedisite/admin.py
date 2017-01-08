from django.contrib import admin
from  .models import TaigaAccount
# Register your models here.


class TaigaAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'date')

admin.site.register(TaigaAccount, TaigaAccountAdmin)
