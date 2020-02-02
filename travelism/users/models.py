from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)
    is_agent = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class AgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='agent_profile')
    joined_trips = models.IntegerField(default=0)


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='customer_profile')
    number_of_trips = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_agent:
        AgentProfile.objects.get_or_create(user=instance)
    else:
        CustomerProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_agent:
        instance.agent_profile.save()
    else:
        CustomerProfile.objects.get_or_create(user=instance)
