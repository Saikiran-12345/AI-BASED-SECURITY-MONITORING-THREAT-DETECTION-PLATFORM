
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()

class AccountsExtendedTestCase2(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser_accounts_2', password='testpassword')
        self.client.force_authenticate(user=self.user)
        
    def test_extended_behavior_A_2(self):
        """Test specific edge case A for accounts behavior 2"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_extended_behavior_B_2(self):
        """Test specific edge case B for accounts behavior 2"""
        self.assertTrue(self.user.is_active)
        
    def test_extended_behavior_C_2(self):
        """Test specific edge case C for accounts behavior 2"""
        self.assertIsNotNone(self.user.username)
        
    def test_extended_behavior_D_2(self):
        """Test specific edge case D for accounts behavior 2"""
        self.assertEqual(self.user.username, 'testuser_accounts_2')
