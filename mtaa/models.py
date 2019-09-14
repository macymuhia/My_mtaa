from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=20)


class NeighbourHood(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    occupants_count = models.IntegerField(default=0)
    Admin = models.ForeignKey(Admin, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    @classmethod
    def all_neighbourhoods(cls):
        return cls.objects.all()


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to="profile/", max_length=255, null=True, blank=True, default=""
    )
    phone = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    email_confirmed = models.BooleanField(default=False)
    bio = models.TextField()
    neighbourhood = models.ForeignKey(
        NeighbourHood, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()


class Business(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(
        upload_to="business/", max_length=255, null=True, blank=True, default=""
    )
    phone = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    email = models.EmailField(max_length=255)
    website = models.URLField(max_length=50, null=True, blank=True, default="")
    owner = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    neighbourhood = models.ForeignKey(
        NeighbourHood, null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name_plural = "Businesses"

    def __str__(self):
        return self.name

    @classmethod
    def all_businesses(cls):
        return cls.objects.all()

    @classmethod
    def fetch_businesses_of_neighbourhood(cls, neighbourhood_id):
        return cls.objects.filter(neighbourhood__id=neighbourhood_id)
