from django.contrib import admin

from .models import Country, FirstName, LastName

# Register your models here.
admin.site.register(Country)


class FirstNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'country')


admin.site.register(FirstName, FirstNameAdmin)


class LastNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'form_is_determined_by_sex')


admin.site.register(LastName, LastNameAdmin)
