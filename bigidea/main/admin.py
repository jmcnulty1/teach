from django.contrib import admin

from main.models import Contact

class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact, ContactAdmin)
