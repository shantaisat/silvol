from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta
from users.models import Availability, UserProfile  # Replace 'users' with your app name if different

class VolunteerAvailabilityTestCase(TestCase):
    def setUp(self):
        # Create a test user (volunteer)
        self.volunteer_user = User.objects.create_user(
            username="volunteer",
            email="volunteer@example.com",
            password="testpassword"
        )

        # Create a UserProfile for the volunteer
        self.volunteer_profile = UserProfile.objects.create(
            user=self.volunteer_user,
            user_type="volunteer",
            skills="Python, Django",
            availability="Weekdays",
            biography="I love helping others with tech.",
            contact_info="volunteer@example.com",
            languages_spoken="English"
        )

        # Log in the volunteer
        self.client.login(username="volunteer", password="testpassword")

        # Test data for availability
        self.availability_data = {
            "start_time": datetime.now() + timedelta(hours=1),
            "end_time": datetime.now() + timedelta(hours=2),
            "description": "Available for tech support."
        }

        # Create an initial availability for testing
        self.availability = Availability.objects.create(
            volunteer=self.volunteer_profile,
            start_time=self.availability_data["start_time"],
            end_time=self.availability_data["end_time"],
            description=self.availability_data["description"]
        )

    def test_create_availability(self):
        # Test creating availability
        response = self.client.post(reverse("availability_create"), {
            "volunteer": self.volunteer_profile.id,
            "start_time": self.availability_data["start_time"],
            "end_time": self.availability_data["end_time"],
            "description": self.availability_data["description"],
        })
        self.assertEqual(response.status_code, 201)  # Assuming 201 for successful creation
        self.assertTrue(Availability.objects.filter(volunteer=self.volunteer_profile).exists())

    def test_edit_availability(self):
        # Test editing availability
        updated_data = {
            "start_time": datetime.now() + timedelta(hours=2),
            "end_time": datetime.now() + timedelta(hours=3),
            "description": "Updated availability."
        }
        response = self.client.post(reverse("availability_edit", args=[self.availability.id]), updated_data)
        self.assertEqual(response.status_code, 200)  # Assuming 200 for successful update
        self.availability.refresh_from_db()
        self.assertEqual(self.availability.start_time, updated_data["start_time"])
        self.assertEqual(self.availability.end_time, updated_data["end_time"])
        self.assertEqual(self.availability.description, updated_data["description"])

    def test_view_availability(self):
        # Test viewing availability
        response = self.client.get(reverse("availability_view", args=[self.availability.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.availability.start_time.strftime('%Y-%m-%d %H:%M:%S'))
        self.assertContains(response, self.availability.end_time.strftime('%Y-%m-%d %H:%M:%S'))
        self.assertContains(response, self.availability.description)

    def test_delete_availability(self):
        # Test deleting availability
        response = self.client.post(reverse("availability_delete", args=[self.availability.id]))
        self.assertEqual(response.status_code, 204)  # Assuming 204 for successful deletion
        self.assertFalse(Availability.objects.filter(id=self.availability.id).exists())