from events.models import Business, Neighborhood, Profile
from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.


class NeighborhoodTestClass(TestCase):
    '''Test methods of Neighborhood model'''

    def setUp(self):
        self.admin = User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')
        self.neighborhood=Neighborhood(name='Ungwaro',location='Naairobi',admin=self.admin)
        self.occupant = Profile(nat_id=2556879,user=self.admin,location=self.neighborhood)

    
    def tearDown(self):
        self.occupant.delete()
        self.neighborhood.delete()
        self.admin.delete()

    def test_create_neighborhood(self):
        self.admin.save()
        self.neighborhood.create_neighborhood()
        self.occupant.save()

        neighborhoods = Neighborhood.objects.all()

        self.assertTrue(len(neighborhoods)>0)

    
    def test_delete_neighborhood(self):
        self.admin.save()
        self.neighborhood.create_neighborhood()
        self.occupant.save()


        self.obj = Neighborhood.objects.get(pk=self.neighborhood.id)
        
        self.obj.delete_neighborhood()
        neighborhoods = Neighborhood.objects.all()

        self.assertTrue(len(neighborhoods)==0)



    def test_find_neigborhood(self):
        self.admin.save()
        self.neighborhood.create_neighborhood()
        self.occupant.save()

        results = Neighborhood.find_neigborhood(self.neighborhood.id)

        self.assertTrue(len(results)>0)



    def test_update_neighborhood(self):
        self.admin.save()
        self.neighborhood.create_neighborhood()
        self.occupant.save()

        update_details = {'name':'new name','location':'new location'}

        Neighborhood.update_neighborhood(update_details,self.neighborhood.id)

        self.obj = Neighborhood.objects.get(pk=self.neighborhood.id)

        self.assertEqual(self.obj.name,'new name')


    def test_update_occupant(self):
        self.admin.save()
        self.neighborhood.create_neighborhood()
        self.occupant.save()

        update_details = {'name':'new name','location':'new location'}

        Neighborhood.update_neighborhood(update_details,self.neighborhood.id)

        self.obj = Neighborhood.objects.get(pk=self.neighborhood.id)

        self.assertEqual(self.obj.name,'new name')




class BusinessTestClass(TestCase):
    '''Test methods of Neighborhood model'''

    def setUp(self):
        self.user = User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')
        self.neighborhood=Neighborhood(name='Ungwaro',location='Naairobi',admin=self.user)
        self.business = Business(name='Shop',user=self.user,location=self.neighborhood, email='shop@email.com')

    
    def tearDown(self):
        self.business.delete()
        self.neighborhood.delete()
        self.user.delete()


    def test_create_business(self):
        self.user.save()
        self.neighborhood.save()
        self.business.create_business()

        businesses = Business.objects.all()

        self.assertTrue(len(businesses)>0)

    
    def test_delete_business(self):
        self.user.save()
        self.neighborhood.save()
        self.business.create_business()


        self.obj = Business.objects.get(pk=self.business.id)
        
        self.obj.delete_business()
        businesses = Business.objects.all()

        self.assertTrue(len(businesses)==0)



    def test_find_business(self):
        self.user.save()
        self.neighborhood.save()
        self.business.create_business()

        results = Business.find_business(self.business.id)

        self.assertTrue(len(results)>0)



    def test_update_business(self):
        self.user.save()
        self.neighborhood.save()
        self.business.create_business()

        update_details = {'name':'new name','location':self.neighborhood, 'email':'newemail@gm.com'}

        Business.update_business(update_details,self.business.id)

        self.obj = Business.objects.get(pk=self.business.id)

        self.assertEqual(self.obj.email,'newemail@gm.com')


    # def test_update_occupant(self):
    #     self.admin.save()
    #     self.neighborhood.create_neighborhood()
    #     self.occupant.save()

    #     update_details = {'name':'new name','location':'new location'}

    #     Neighborhood.update_neighborhood(update_details,self.neighborhood.id)

    #     self.obj = Neighborhood.objects.get(pk=self.neighborhood.id)

    #     self.assertEqual(self.obj.name,'new name')


