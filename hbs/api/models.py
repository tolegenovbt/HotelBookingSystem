from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.base import Model

from auth_.models import MainUser

gender = (
    ("MALE", "man"),
    ("FEMALE", "female"),
    ("OTHER", "other")
)
star_numbers = (
        (1, "One-Star"),
        (2, "Two-Star"),
        (3, "Three-Star"),
        (4, "Four-Star"),
        (5, "Five-Star")
    )


class User(MainUser):
    gender = models.CharField("Gender", choices=gender)
    phone_number = models.IntegerField("Phone Number", max_length=11)
    alternative_phone_number = models.IntegerField("Alternative Phone Number", max_length=11)

    class Meta:
        abstract = True


class Hotelier(User):
    can_edit_hotel = models.BooleanField(default=False)
    can_edit_room = models.BooleanField(default=False)
    can_delete_hotel = models.BooleanField(default=False)
    can_delete_room = models.BooleanField(default=False)
    can_add_room = models.BooleanField(default=False)
    can_add_hotel = models.BooleanField(default=True)

    def __str__(self):
        return str(self.first_name)

    class Meta:
        verbose_name = "Hotelier"
        verbose_name_plural = "Hoteliers"


class Hotel(models.Model):
    name = models.CharField("Name", max_length=20)
    hotelier = models.ForeignKey(Hotelier, verbose_name="Hotelier", on_delete=models.CASCADE)
    number_of_stars = models.IntegerField("", max_length=1, choices=star_numbers)
    number_of_ratings = models.IntegerField("Number of ratings", default=0)
    rating = models.IntegerField("rating", default=0)
    account_number = models.IntegerField("Account Number", blank=False)
    address = models.TextField("Address", max_length=200, blank=False)
    city = models.CharField("City", max_length=20)
    phone_number = models.BigIntegerField("Phone Number")
    yard = models.BooleanField("Yard")
    pool = models.BooleanField("Pool")
    gym = models.BooleanField("Gym")
    breakfast = models.BooleanField("Breakfast")
    wifi = models.BooleanField("Wifi")
    parking = models.BooleanField("Parking")
    restaurant = models.BooleanField("Restaurant")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"


class HotelPhoto(models.Model):
    photo = models.ImageField("Photo")
    hotel = models.ForeignKey(Hotel, verbose_name="Hotel", on_delete=models.CASCADE)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, verbose_name="Hotel", on_delete=models.CASCADE)
    type = models.CharField("Type", max_length=20)
    cost = models.BigIntegerField("Cost")
    area = models.IntegerField("Area")
    king_bed = models.IntegerField("King Bed")
    queen_bed = models.IntegerField("Queen Bed")
    tv = models.BooleanField("TV")
    wifi = models.BooleanField("Wifi")
    kitchen = models.BooleanField("Kitchen")
    extra_bed = models.BooleanField("Extra Bed")

    def __str__(self):
        return str("Hotel:" + self.hotel.name + "Room: " + self.type)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"


class RoomPhoto(models.Model):
    room = models.ForeignKey(Room, verbose_name="Room", on_delete=models.CASCADE)
    photo = models.ImageField("Photo")


class Customer(User):
    room = models.ManyToManyField(Room, verbose_name="Room", through="Reservation")

    def __str__(self):
        return str(self.first_name)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, verbose_name="Customer", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name="Room", on_delete=models.CASCADE)
    check_in = models.DateField("Check In")
    check_out = models.DateField("Check Out")
    # request_time = models.DateTimeField("Request Time", auto_now=True)
    total_cost = models.BigIntegerField("Total Cost")
    status_choices = (
        (1, "Paid"),
        (0, "Unpaid"),
    )
    payment_status = models.IntegerField("Payment status", default=0, choices=status_choices)

    def __str__(self):
        return self.room.type + ": " + str(self.customer)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"


class Transaction(models.Model):
    reservation = models.OneToOneField(Reservation, verbose_name="Reservation", on_delete=models.CASCADE)
    reference_number = models.IntegerField("Reference", max_length=7)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"


class Comment(models.Model):
    customer = models.ForeignKey(Customer, verbose_name="Customer", on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, verbose_name="Hotel", on_delete=models.CASCADE)
    text = models.TextField("Comment Text")
    star_number = models.IntegerField(choices=star_numbers, max_length=1)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return '%s: %s' % (self.customer.first_name, self.text)

