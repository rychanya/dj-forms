from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'review_count')
    list_filter = ('model', )
    search_fields = ('model', 'brand')
    ordering = ('-id', )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'car')
    list_filter = ('title', 'car')
    form = ReviewAdminForm
    search_fields = ('title', 'text')
    ordering = ('-id', )



admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
