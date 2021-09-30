from django.test import TestCase
from .models import NeigbourHood,Profile,Business,User
# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='', password='Access')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()
        

class NeighborhoodTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='king_bin')
        self.neighbor = NeigbourHood.objects.create(id=1, name='Moringa business', description='Moringa is the best place',image='https://cloudinary url',created_at='2021,6,24',updated_at='2021,6,26', neighbor=self.neighbor,user=self.user,email='roney.juma@student.moringaschool.com')

    def test_create_neighbor(self):
        self.neighbor.create_neighbor()
        neighbor = NeigbourHood.objects.all()
        self.assertTrue(len(neighbor) > 0)

    def test_get_neighbor(self, id):
        self.neighbor.save()
        neighbor = NeigbourHood.get_neighbor(neighbor_id=id)
        self.assertTrue(len(neighbor) == 1)