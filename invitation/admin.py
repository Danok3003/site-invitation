from django.contrib import admin
from .models import Guest, Timer

class GuestAdmin(admin.ModelAdmin):
    list_display = [
        "name_first_guest", "name_second_guest", "name_slug",
        "first_seconds_names", "drinks", "presence_on_wedding",
                    ]
    fields = [
        "name_first_guest", "name_second_guest", "one_plus",
        "name_slug", "first_seconds_names", "drinks",
        "presence_on_wedding",
    ]
    list_filter = [
        "presence_on_wedding",
        "drinks"
    ]
    prepopulated_fields = {"name_slug": ["name_first_guest", "name_second_guest"]}

admin.site.register(Guest, GuestAdmin)

class TimerAdmin(admin.ModelAdmin):
    list_display = [
        "date",
    ]
    fields = [
        "date",
    ]
    list_filter = [
        "date",
    ]

admin.site.register(Timer, TimerAdmin)