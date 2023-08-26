from django.test import TestCase

from users.models import User, Role
from users.tests import UserSetUpTestData
from utils.constants import ADMINISTRATOR


class UserViewTestCase(UserSetUpTestData):

    def test_get_list(self):
        print(User.objects.all().count())
        self.assertEquals(self.role_simple, self.user_manager.role)