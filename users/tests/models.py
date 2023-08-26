from django.test import TestCase

from users.models import User, Role
from utils.constants import ADMINISTRATOR


class CustomUserManagerTestCase(TestCase):

    def test_super_user(self):
        superuser = User.objects.create_superuser(
            'test_super@gmail.com',
            'test_super_1234'
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_super_user_exceptions(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(None, 'test_super_1234')
        with self.assertRaises(ValueError):
            User.objects.create_superuser('test_super@gmail.com', 'test_super_1234', is_staff=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser('test_super@gmail.com', 'test_super_1234', is_superuser=False)

    def test_user(self):
        user = User.objects.create_user(
            'test@gmail.com',
            'test_1234'
        )
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


class UserSetUpTestData(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.role_administrator = Role.objects.create(
            name=ADMINISTRATOR,
            description="Allowed to manage users"
        )
        cls.role_simple = Role.objects.create(
            name="Manager",
            description="Simple user, allowed just own data"
        )

        cls.superuser = User.objects.create_superuser(
            "test_super@gmail.com",
            "test_super_1234"
        )
        cls.user_administrator = User.objects.create_user(
            "test_admin@gmail.com",
            "test_admin_1234",
            first_name="Admin name",
            last_name="Admin surname",
            role=cls.role_administrator,
        )
        cls.user_manager = User.objects.create_user(
            'test@gmail.com',
            'test_1234',
            first_name = "Name",
            last_name = "Surname",
            role = cls.role_simple,
        )
