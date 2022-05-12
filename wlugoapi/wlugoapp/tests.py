
from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='tester2@user.com',
        password='password', first_name='First Name2', last_name='Last Name2',
        program='Udacity',graduating_year=2067)
        self.assertEqual(user.email, 'tester2@user.com')
        self.assertFalse(user.has_access)
        self.assertFalse(user.is_mod)
        self.assertFalse(user.is_admin)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='',
        password='password', first_name='', last_name='',
        program='',graduating_year=0)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='tester_super@user.com',
        password='password', first_name='First Name', last_name='Last Name',
        program='Udacity',graduating_year=2097)
        self.assertEqual(admin_user.email, 'tester_super@user.com')
        #self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='',
        password='password', first_name='', last_name='',
        program='',graduating_year=0)