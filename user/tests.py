from django.contrib.auth.hashers import make_password, check_password
from django.test import TestCase

from phones.models import Phone
from user.models import ConcreteUser
from user.serializers import ConcreteUserSerializer


class TestConcreteUserSerializerTestCase(TestCase):
    def test_create_cria_telefones_corretamente(self):
        initial_count = ConcreteUser.objects.count()
        initial_phone_count = Phone.objects.count()
        data = {
            'first_name': 'joão',
            'email': 'joao@a.com',
            'password': 'testejoao',
            'phones': [
                {'ddd': '021', 'number': '987654321'},
                {'ddd': '021', 'number': '987654320'},
            ]
        }

        serializer = ConcreteUserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        _user = serializer.save()
        self.assertIsInstance(_user, ConcreteUser)
        self.assertEqual(initial_count + 1, ConcreteUser.objects.count())
        self.assertEqual(initial_phone_count + 2, Phone.objects.count())
        self.assertEqual(_user.first_name, 'joão')
        self.assertEqual(_user.email, 'joao@a.com')

    def test_create_verifica_se_password_nao_e_plain_text(self):
        data = {
            'first_name': 'joão',
            'email': 'joao@a.com',
            'password': 'testejoao',
            'phones': [
                {'ddd': '021', 'number': '987654321'},
                {'ddd': '021', 'number': '987654320'},
            ]
        }

        serializer = ConcreteUserSerializer(data=data)
        serializer.is_valid()
        _user = serializer.save()
        _check = check_password('testejoao', _user.password)

        self.assertNotEquals('testejoao', _user.password)
        self.assertTrue(_check)
