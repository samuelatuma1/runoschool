from django.contrib import admin
from .models import Photos, WelcImgs, WelcLeaders, News, Welcometab, Welcometab2, admitfiles
from .models import Welcometab3, Welcometab4, newsDetail, about, about2, about3, Steps, Logo

# Register your models here.
admin.site.register(Photos)
admin.site.register(WelcImgs)
admin.site.register(WelcLeaders)
admin.site.register(News)

admin.site.register(Welcometab)
admin.site.register(Welcometab2)
admin.site.register(Welcometab3)
admin.site.register(Welcometab4)
admin.site.register(newsDetail)
admin.site.register(about)
admin.site.register(about2)
admin.site.register(about3)
admin.site.register(Steps)
admin.site.register(admitfiles)
admin.site.register(Logo)
#This point and below is related to pupils and teachers

from .models import Nursery1, Nursery2, Class

# Register your models here.
admin.site.register(Nursery1)
admin.site.register(Nursery2)
admin.site.register(Class)

