from django.test import TestCase, Client
from .models import Hotel
from django.urls import reverse


# Create your tests here.
class HotelTestcase(TestCase):
    def setUp(self):
        self.hotel=Hotel('')

# Testing if new hotels can be made
class HotelModelTest(TestCase):
    def test_create_hotel(self):
        hotel = Hotel.objects.create(
            hotel_id=1,
            hotel_name='UK Stays Norwich',
            hotel_location='Norfolk',
            hotel_rating=4,
            price_per_night=99.99
        )

        # Check each field individually
        self.assertEqual(hotel.hotel_id, 1)
        self.assertEqual(hotel.hotel_name, 'UK Stays Norwich')
        self.assertEqual(hotel.hotel_location, 'Norfolk')
        self.assertEqual(hotel.hotel_rating, 4)
        self.assertEqual(hotel.price_per_night, 99.99)


# Testing to see if the Navigation links work
class NavbarTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_navbar_links_exist(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="' + reverse('index') + '"')
        self.assertContains(response, 'href="' + reverse('hotel_view') + '"')
        self.assertContains(response, 'href="' + reverse('booking') + '"')
        self.assertContains(response, 'href="' + reverse('create_login') + '"')
        self.assertContains(response, 'href="' + reverse('enter_login') + '"')


