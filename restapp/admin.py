from django.contrib import admin
from restapp.models import Movie
# Register your models here.
admin.site.register(Movie)
admin.site.site_header = 'REST API'
