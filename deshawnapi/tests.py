from django.test import TestCase
from rest_framework.test import APIClient
from deshawnapi.models import Walker, Appointment

class AppointmentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a walker to reference in the appointment
        self.walker = Walker.objects.create(...)  # fill in required fields

    def test_create_appointment(self):
        data = {"walkerId": self.walker.id, "appointmentDate": "2022-11-23"}
        response = self.client.post('/appointments', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Appointment.objects.count(), 1)
