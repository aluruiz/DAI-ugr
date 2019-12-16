from django.contrib import admin
from .models import Musico
from .models import Grupo
from .models import Album

# Register your models here.
admin.site.register(Musico)
admin.site.register(Grupo)
admin.site.register(Album)
