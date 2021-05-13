from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from django.db.models.base import Model

from auth_.models import MainUser


# class User(MainUser):
#     gender = models.CharField("Gender", max_length=20, choices=gender)
#     phone_number = models.CharField("Phone Number", max_length=11)
#     alternative_phone_number = models.CharField("Alternative Phone Number", max_length=11)
#
#     class Meta:
#         abstract = True


# class Hotelier(MainUser):
#     gender = models.CharField("Gender", max_length=20, choices=gender)
#     phone_number = models.CharField("Phone Number", max_length=11)
#     alternative_phone_number = models.CharField("Alternative Phone Number", max_length=11)
#
#     def __str__(self):
#         return str(self.first_name)
#
#     class Meta:
#         verbose_name = "Hotelier"
#         verbose_name_plural = "Hoteliers"
from utils.constants import star_numbers, room_type, status_choices


class HotelManager(models.Manager):
    use_in_migrations = True

    def room_details_by_hotel(self, pk, rk):
        return self.get(id=pk).hotel.filter(id=pk)


class Hotel(models.Model):
    name = models.CharField("Name", max_length=20)
    hotelier = models.ForeignKey(MainUser, verbose_name="Hotelier", on_delete=models.CASCADE, null=True)
    number_of_stars = models.IntegerField("Number of stars", choices=star_numbers)
    number_of_ratings = models.IntegerField("Number of ratings", default=0)
    rating = models.FloatField("rating", default=0)
    account_number = models.IntegerField("Account Number", blank=False)
    address = models.CharField("Address", max_length=200, blank=False)
    city = models.CharField("City", max_length=20)
    phone_number = models.CharField("Phone Number", max_length=11)
    yard = models.BooleanField("Yard")
    pool = models.BooleanField("Pool")
    gym = models.BooleanField("Gym")
    wifi = models.BooleanField("Wifi")
    parking = models.BooleanField("Parking")
    restaurant = models.BooleanField("Restaurant")

    objects = HotelManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"


# class RoomsManager(models.Manager):
#     use_in_migrations = True
#
#     def room_details_by_hotel(self, pk, rk):
#         return self.get(id=rk).hotel.filter(id=pk)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, verbose_name="Hotel", on_delete=models.CASCADE, null=True)
    type = models.CharField("Type", choices=room_type, max_length=20)
    cost = models.BigIntegerField("Cost")
    area = models.IntegerField("Area")
    king_bed = models.IntegerField("King Bed")
    queen_bed = models.IntegerField("Queen Bed")
    tv = models.BooleanField("TV")
    wifi = models.BooleanField("Wifi")
    kitchen = models.BooleanField("Kitchen")
    extra_bed = models.BooleanField("Extra Bed")

    def __str__(self):
        return str(self.hotel.name + " " + self.type)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"


class Photos(models.Model):
    photo = models.ImageField()

    class Meta:
        abstract = True


class HotelPhoto(Photos):
    photo = models.ImageField(upload_to='hotel_photos')
    hotel = models.ForeignKey(Hotel, verbose_name="Hotel", on_delete=models.CASCADE, null=True)


class RoomPhoto(Photos):
    photo = models.ImageField(upload_to='room_photos', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    room = models.ForeignKey(Room, verbose_name="Room", on_delete=models.CASCADE, null=True, related_name="room_photos")

# class Customer(MainUser):
#     gender = models.CharField("Gender", max_length=20, choices=gender)
#     phone_number = models.CharField("Phone Number", max_length=11)
#     alternative_phone_number = models.CharField("Alternative Phone Number", max_length=11)
#     room = models.ManyToManyField(Room, verbose_name="Room", through="Reservation")
#
#     def __str__(self):
#         return str(self.first_name)
#
#     class Meta:
#         verbose_name = "Customer"
#         verbose_name_plural = "Customers"


class Reservation(models.Model):
    customer = models.ForeignKey(MainUser, verbose_name="Customer", on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, verbose_name="Room", on_delete=models.CASCADE, null=True,
                             related_name="room_reservations")
    hotel = models.ForeignKey(Hotel, verbose_name="Hotel", on_delete=models.CASCADE, null=True,
                              related_name="hotel_reservations")
    check_in = models.DateField("Check In")
    check_out = models.DateField("Check Out")
    # request_time = models.DateTimeField("Request Time", auto_now=True)
    total_cost = models.BigIntegerField("Total Cost")
    payment_status = models.IntegerField("Payment status", choices=status_choices)

    def __str__(self):
        return self.room.type + ": " + str(self.customer)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"


class Transaction(models.Model):
    reservation = models.OneToOneField(Reservation, verbose_name="Reservation", on_delete=models.CASCADE, null=True)
    reference_number = models.IntegerField("Reference number")

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"


class Comment(models.Model):
    customer = models.ForeignKey(MainUser, verbose_name="Customer", on_delete=models.CASCADE, null=True)
    hotel = models.ForeignKey(Hotel, verbose_name="Hotel", on_delete=models.CASCADE, null=True)
    text = models.TextField("Comment Text")
    number_of_stars = models.IntegerField("Number of stars", choices=star_numbers)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return '%s: %s' % (self.customer.first_name, self.text)

