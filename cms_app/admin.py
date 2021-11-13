from django.contrib import admin
# Register your models here.

from cms_app.models import *

admin.site.register(Team)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
