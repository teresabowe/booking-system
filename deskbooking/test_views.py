from django.test import TestCase, Client
from deskbooking.models import Desk, Booking, User
from . forms import AddForm
from django.urls import reverse


class TestAppModels(TestCase):
    """
    Set up test users, desks and bookings
    """
    @classmethod
    def setUpTestData(self):
        testuser = User.objects.create_user(username="testuser",
                                            password="12345")
        self.testuser = testuser
        testuser2 = User.objects.create_user(username="testuser2",
                                             password="12345")
        self.testuser2 = testuser2
        self.newdesk = Desk.objects.create(desk="9011", floor="9",
                                           description="Window Desk")
        self.newdesk2 = Desk.objects.create(desk="9012", floor="9",
                                            description="Window Desk")
        self.newbooking = Booking.objects\
            .create(desk_booking_date="2022-11-11",
                    desk=self.newdesk, desk_user=self.testuser)
        self.newbooking2 = Booking.objects\
            .create(desk_booking_date="2022-11-12",
                    desk=self.newdesk, desk_user=self.testuser)
        self.newbooking3 = Booking.objects\
            .create(desk_booking_date="2022-11-13",
                    desk=self.newdesk2, desk_user=self.testuser2)
        self.form_data = {
            'desk_booking_date': '2022-11-14',
            'desk': '1',
            'desk_user': 'self.testuser2'
        }

    def test_get_homepage(self):
        """
        Test home page response is 200
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, '<ol class="carousel-indicators">')

    def test_anonymous_cannot_see_page(self):
        """
        Test that anonymous user cannot see page
        """
        response = self.client.get(reverse("view_bookings"))
        self.assertRedirects(response,
                             "/accounts/login/?account_login=/view_bookings/")

    def test_authenticated_user_can_see_booking_listing_page(self):
        """
        Test that authenticated user can see booking listing page
        """
        self.client.force_login(user=self.testuser)
        response = self.client.get(reverse("view_bookings"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Bookings')

    def test_authenticated_user_can_see_add_booking_page(self):
        """
        Test that authenticated user can see add booking page
        """
        self.client.force_login(user=self.testuser)
        response = self.client.get(reverse("add_booking"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add Booking')
