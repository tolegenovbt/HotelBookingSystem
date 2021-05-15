import logging
import os
import shutil

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete

from auth_.models import Profile, MainUser


logger = logging.getLogger(__name__)

@receiver(post_delete, sender=Profile)
def delete_avatar_on_profile_delete(sender, instance, *args, **kwargs):
    avatar = instance.avatar
    if avatar:
        user_avatar_path = os.path.abspath(os.path.join(avatar.path, '..'))
        shutil.rmtree(user_avatar_path)
        logger.debug(f'Avatar deleted ID: {instance.avatar}')
        logger.info(f'Avatar deleted ID: {instance.avatar}')
        logger.warning(f'Avatar deleted ID: {instance.avatar}')
        logger.error(f'Avatar deleted ID: {instance.avatar}')
        logger.critical(f'Avatar deleted ID: {instance.avatar}')

@receiver(post_save, sender=MainUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.debug(f'Profile created ID: {instance}')
        logger.info(f'Profile created ID: {instance}')
        logger.warning(f'Profile created ID: {instance}')
        logger.error(f'Profile created ID: {instance}')
        logger.critical(f'Profile created ID: {instance}')