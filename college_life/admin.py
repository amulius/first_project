from django.contrib import admin

# Register your models here.
from college_life.models import Skill, Major, Character, Zone, Mob, Monster


admin.site.register(Skill)
admin.site.register(Major)
admin.site.register(Character)
admin.site.register(Zone)
admin.site.register(Mob)
admin.site.register(Monster)
