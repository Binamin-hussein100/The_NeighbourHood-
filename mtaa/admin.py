from django.contrib import admin
from .models import User,NeigbourHood,Business,Profile,Post

# Register your models here.
admin.site.register(User),
admin.site.register(NeigbourHood),
admin.site.register(Business),
admin.site.register(Profile),
admin.site.register(Post)