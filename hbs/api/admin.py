from django.contrib import admin
from .models import Hotel, Room, Reservation, RoomPhoto, Transaction, MainUser, AbstractUser,\
    HotelPhoto, Comment

# Register your models here.

admin.site.register(Hotel)
admin.site.register(HotelPhoto)
admin.site.register(Room)
admin.site.register(RoomPhoto)
admin.site.register(Reservation)
admin.site.register(Transaction)
# admin.site.register(MainUser)
admin.site.register(Comment)

# @admin.register()
# class Admin(admin.ModelAdmin):
#     list_display = []
#     ordering = []
#     search_fields = []
#     list_filter = []
#     list_editable = []
#
#
# @admin.register(Hotel)
# class HotelAdmin(admin.ModelAdmin):
#     list_display = []
#     ordering = []
#     search_fields = []
#     list_filter = []
#     list_editable = []
#
#
# @admin.register(Room)
# class RoomAdmin(admin.ModelAdmin):
#     list_display = []
#     ordering = []
#     search_fields = []
#     list_filter = []
#     list_editable = []
#
#
# @admin.register(Reservation)
# class ReservationAdmin(admin.ModelAdmin):
#     list_display = []
#     ordering = []
#     search_fields = []
#     list_filter = []
#     list_editable = []
