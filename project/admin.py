from django.contrib import admin

# Register your models here.
from .models import UserProfile, Food, Entry, DailyReport

admin.site.register(UserProfile)
admin.site.register(Food)
admin.site.register(Entry)
admin.site.register(DailyReport)