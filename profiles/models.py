from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify

from django_countries.fields import CountryField


# Create your models here.
class UserProfile(models.Model):
    """User profile section"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    default_slug = models.SlugField(unique=True, null=True)
    default_updated = models.DateTimeField(auto_now=True)
    default_profile_created = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username}-{self.default_profile_created}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(UserProfile, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
