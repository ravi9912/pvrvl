from django.db import models
from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	company_name = models.CharField(max_length=255,null=True,blank=True)
	#address
	#phone
	#mobile


	def __str__(self):
		return self.user.username

@receiver(post_save,sender=User)
def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:

    	userprofile = UserProfile.objects.create(user=instance)
