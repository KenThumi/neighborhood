from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Neighborhood(models.Model):
    name = models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name='locations')


    def create_neighborhood(self):
        return self.save()


    def delete_neighborhood(self):
        return self.delete()


    @classmethod
    def find_neigborhood(cls,neigborhood_id):
        return cls.objects.filter(pk=neigborhood_id)

    @classmethod
    def update_neighborhood(cls,update_details,id):
        return cls.objects.filter(id=int(id)).update(name=update_details['name'],
                                               location=update_details['location'])


    @classmethod
    def update_location(cls,update_details,id):
        neiborhood = cls.objects.get(id=int(id))
        return cls.objects.filter(id=int(id)).update(name=update_details['name'],
                                               location=update_details['location'])
    




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

    class Meta:
        ordering = ["-pk"]


    def __str__(self):
        return f'{self.user.username}'


class Business(models.Model):
    name = models.CharField(max_length=60)
    email= models.EmailField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='businesses')
    location = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,related_name='businesses')



    def create_business(self):
        return self.save()


    def delete_business(self):
        return self.delete()


    @classmethod
    def find_business(cls,id):
        return cls.objects.filter(pk=id)

    
    @classmethod
    def update_business(cls,update_details,id):
        return cls.objects.filter(id=int(id)).update(name=update_details['name'],
                                               location=update_details['location'],
                                               email=update_details['email'])
    


    class Meta:
        ordering = ["-pk"]
    
    
    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f'{self.description}'



