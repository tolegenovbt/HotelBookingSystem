import logging
import os
import shutil

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete

from auth_.models import Profile, MainUser


@receiver(post_delete, sender=Profile)
def delete_avatar_on_profile_delete(sender, instance, *args, **kwargs):
    avatar = instance.avatar
    if avatar:
        user_avatar_path = os.path.abspath(os.path.join(avatar.path, '../'))
        shutil.rmtree(user_avatar_path)


@receiver(post_save, sender=MainUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
