from django.test import TestCase
from deskbooking.models import Desk, Booking, User


class TestAppModels(TestCase):
    """
    Set up test desk and test booking
    """
    @classmethod
    def setUpTestData(self):
        self.newdesk = Desk.objects.create(desk="9011", floor="9",
                                           description="Window Desk")
        self.newbooking = Booking.objects\
            .create(desk_booking_date="2022-11-08",
                    desk=self.newdesk)

    def test_newdesk_desk_str(self):
        """
        Test that database contains desk data
        """
        self.assertEqual(str(self.newdesk), "9011")

    def test_newdesk_floor_str(self):
        """
        Test that database contains floor data
        """
        self.assertEqual(str(self.newdesk.floor), "9")

    def test_newdesk_description_str(self):
        """
        Test that database contains description data
        """
        self.assertEqual(str(self.newdesk.description), "Window Desk")

    def test_newbooking_desk_booking_date_str(self):
        """
        Test that database contains booking date data
        """
        self.assertEqual(str(self.newbooking.desk_booking_date), "2022-11-08")

    def test_newbooking_desk_str(self):
        """
        Test that database contains booking desk data
        """
        self.assertEqual(str(self.newbooking), "9011")
