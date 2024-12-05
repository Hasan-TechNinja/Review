from django.contrib import admin
from . models import Brand, Product, Profile, Rating, Review

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'logo'
    )
admin.site.register(Brand, BrandAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'brand',
        'image'
    )
admin.site.register(Product, ProductAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'image'
    )
admin.site.register(Profile, ProfileAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'review_text',
        'rating',
        'vote'
    )
admin.site.register(Review, ReviewAdmin)


class RatingAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'value'
    )
admin.site.register(Rating, RatingAdmin)