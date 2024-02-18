from django.contrib import admin
from users.models import User, Payments


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('email', 'is_active')


@admin.register(Payments)
class UserAdmin(admin.ModelAdmin):
    fields = ('date_payment', 'payment_amount', 'payment_method', 'user', 'paid_course', 'paid_lesson',)
