from django.contrib import admin
from browser.models import Brand, Gtin


class BrandAdmin(admin.ModelAdmin):
    list_display = ('BSIN', 'BRAND_NM')


admin.site.register(Brand, BrandAdmin)


class GtinAdmin(admin.ModelAdmin):
    list_display = ('GTIN_CD', 'GTIN_NM')
    search_fields = ['GTIN_CD', 'GTIN_NM']


admin.site.register(Gtin, GtinAdmin)
