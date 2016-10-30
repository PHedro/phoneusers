from django.contrib.auth.hashers import make_password, check_password
from django.test import TestCase

from phones.models import Phone
from user.models import ConcreteUser
from user.serializers import ConcreteUserSerializer


class TestConcreteUserSerializerTestCase(TestCase):
    def setUp(self):
        self.data = {
            'name': 'joão da silva',
            'email': 'joao@a.com',
            'password': 'testejoao',
            'phones': [
                {'ddd': '021', 'number': '987654321'},
                {'ddd': '021', 'number': '987654320'},
            ]
        }

    def test_create_cria_user_corretamente(self):
        serializer = ConcreteUserSerializer(data=self.data)

        self.assertTrue(serializer.is_valid())
        _user = serializer.save()
        self.assertIsInstance(_user, ConcreteUser)
        self.assertEqual(_user.first_name, 'joão')
        self.assertEqual(_user.last_name, 'da silva')
        self.assertEqual(_user.name, 'joão da silva')
        self.assertEqual(_user.email, 'joao@a.com')

    def test_create_cria_telefones_corretamente(self):
        initial_count = ConcreteUser.objects.count()
        initial_phone_count = Phone.objects.count()

        serializer = ConcreteUserSerializer(data=self.data)

        self.assertTrue(serializer.is_valid())
        _user = serializer.save()
        _phone1_ok = Phone.objects.filter(
            ddd='021', number='987654321', user=_user
        )
        _phone2_ok = Phone.objects.filter(
            ddd='021', number='987654320', user=_user
        )
        self.assertIsInstance(_user, ConcreteUser)
        self.assertEqual(initial_count + 1, ConcreteUser.objects.count())
        self.assertEqual(initial_phone_count + 2, Phone.objects.count())
        self.assertTrue(_phone1_ok)
        self.assertTrue(_phone2_ok)


    def test_create_verifica_se_password_nao_e_plain_text(self):
        serializer = ConcreteUserSerializer(data=self.data)
        serializer.is_valid()
        _user = serializer.save()
        _check = check_password('testejoao', _user.password)

        self.assertNotEquals('testejoao', _user.password)
        self.assertTrue(_check)
