from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', Car.review_count)

    list_filter = ('brand', 'model')
    search_fields = ('brand', 'model', 'review__title')

    ordering = ['id']

class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
