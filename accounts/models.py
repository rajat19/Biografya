from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_created = models.IntegerField(blank=True, default=0)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('accounts:profile', kwargs={'pk': self.pk})

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()
