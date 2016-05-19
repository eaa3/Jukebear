from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.


from .models import Song, Stats, JukeUser, JukeBox

admin.site.register(Song)
admin.site.register(Stats)
admin.site.register(JukeUser)
admin.site.register(JukeBox)