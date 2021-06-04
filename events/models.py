from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
    
    nat_id = models.IntegerField()
    user = models.OneToOneField(
                User,
                on_delete=models.CASCADE,
            )

    # def save_profile(self):
    #     return self.save()


    # @classmethod
    # def update_profile(cls,update_details,id):
    #     return cls.objects.filter(id=int(id)).update(profile_photo=update_details['profile_photo'],
    #                                            bio=update_details['bio'],
    #                                            contact= update_details['contact'],
    #                                            user=update_details['user'])

    # def delete_profile(self):
    #     return self.delete()


    class Meta:
        ordering = ["-pk"]


    def __str__(self):
        return f'{self.user.username}'