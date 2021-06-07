from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Neighborhood(models.Model):
    name = models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name='locations')


    class Meta:
        ordering = ["-pk"]


    def __str__(self):
        return f'{self.name} , {self.location}'


class Profile(models.Model):
    
    nat_id = models.IntegerField()
    user = models.OneToOneField(
                User,
                on_delete=models.CASCADE,
            )
    location = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,related_name='profile',null=True)
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


class Business(models.Model):
    name = models.CharField(max_length=60)
    email= models.EmailField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='businesses')
    location = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,related_name='businesses')
    
    
    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')

    def __str__(self):
        return f'{self.description}'



