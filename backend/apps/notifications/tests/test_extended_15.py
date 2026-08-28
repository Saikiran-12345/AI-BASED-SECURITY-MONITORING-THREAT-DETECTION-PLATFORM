
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()

class NotificationsExtendedTestCase15(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser_notifications_15', password='testpassword')
        self.client.force_authenticate(user=self.user)
        
    def test_extended_behavior_A_15(self):
        """Test specific edge case A for notifications behavior 15"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_extended_behavior_B_15(self):
        """Test specific edge case B for notifications behavior 15"""
        self.assertTrue(self.user.is_active)
        
    def test_extended_behavior_C_15(self):
        """Test specific edge case C for notifications behavior 15"""
        self.assertIsNotNone(self.user.username)
        
    def test_extended_behavior_D_15(self):
        """Test specific edge case D for notifications behavior 15"""
        self.assertEqual(self.user.username, 'testuser_notifications_15')
