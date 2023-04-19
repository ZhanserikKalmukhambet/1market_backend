from datetime import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTests(TestCase):

    def setUp(self):
        self.UserModel = get_user_model()

    def test_create_user(self):
        email = 'test@example.com'
        password = 'testpass123'
        username = 'testuser'
        first_name = 'Test'
        last_name = 'User'
        phone_number = '1234567890'
        birth_date = datetime.strptime('2000-01-01', '%Y-%m-%d').date()  # Convert string to date object
        user_type = 'CUSTOMER'

        user = self.UserModel.objects.create_user(
            email=email,
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            birth_date=birth_date,
            user_type=user_type
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.username, username)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.phone_number, phone_number)
        self.assertEqual(user.birth_date.strftime('%Y-%m-%d'), '2000-01-01')  # Use strftime on the date object
        self.assertEqual(user.user_type, user_type)
        self.assertTrue(user.check_password(password))
