from django.contrib import admin
from .models import Profile, Skills, Experience, Projects, Contact

# Register your models here.

admin.site.register(Profile)
admin.site.register(Skills)
admin.site.register(Experience)
admin.site.register(Projects)
admin.site.register(Contact)

# admin styling 
admin.site.site_header = "Portfolio"
admin.site.site_title = "Portfolio Admin Panel"
admin.site.index_title = "Welcome to Portfolio Dashboard"
