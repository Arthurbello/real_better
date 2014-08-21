from django.contrib import admin
from better_forecast.models import BetterUser, RainFavourite, SunFavourite, SnowFavourite

admin.site.register(BetterUser)
admin.site.register(RainFavourite)
admin.site.register(SunFavourite)
admin.site.register(SnowFavourite)
