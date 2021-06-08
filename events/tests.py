from events.models import Neighborhood
from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.


class NeighborhoodTestClass(TestCase):
    '''Test methods of profile model'''

    def setUp(self):
        self.admin = User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')
        self.neighborhood=Neighborhood(name='Ungwaro',location='Naairobi',admin=self.admin)

    
    def tearDown(self):
        self.neighborhood.delete()
        self.admin.delete()

    def test_create_neighborhood(self):
        self.admin.save()
        self.neighborhood.create_neighborhood()

        neighborhoods = Neighborhood.objects.all()

        self.assertTrue(len(neighborhoods)>0)

    
    def test_delete_neighborhood(self):
        self.admin.save()
        self.neighborhood.create_neighborhood()


        self.obj = Neighborhood.objects.get(pk=self.neighborhood.id)
        
        self.obj.delete_neighborhood()
        neighborhoods = Neighborhood.objects.all()

        self.assertTrue(len(neighborhoods)==0)