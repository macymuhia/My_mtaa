from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to="vibes/",
        max_length=255,
        null=True,
        blank=True,
        default="/static/img/default.png",
    )
    phone = models.CharField(max_length=20, blank=True, default="")
    email_confirmed = models.BooleanField(default=False)
    bio = models.TextField()


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
