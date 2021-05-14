
import os
import shutil

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete

from api.models import RoomPhoto, HotelPhoto


@receiver(post_delete, sender=RoomPhoto)
def delete_photo_on_room_photo_delete(sender, instance, *args, **kwargs):
    photo = instance.photo
    if photo:
        room_photo_photo_path = os.path.abspath(os.path.join(photo.path, '../..'))
        shutil.rmtree(room_photo_photo_path)


@receiver(post_delete, sender=HotelPhoto)
def delete_photo_on_hotel_photo_delete(sender, instance, *args, **kwargs):
    photo = instance.photo
    if photo:
        # hotel_photo_photo_path = os.path.abspath(photo.path))
        shutil.rmtree(photo.path)
