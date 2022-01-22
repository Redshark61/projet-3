from django.contrib import admin
from login_signup.models import Diseases, RPPS, Job, Location, User

# Register your models here.
admin.site.register(Diseases)
admin.site.register(RPPS)
admin.site.register(Job)
admin.site.register(Location)
admin.site.register(User)
