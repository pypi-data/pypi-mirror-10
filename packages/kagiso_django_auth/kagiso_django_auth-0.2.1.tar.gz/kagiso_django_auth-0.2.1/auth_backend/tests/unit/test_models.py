from dateutil import parser
from django.test import TestCase
from model_mommy import mommy
import responses

from . import mocks
from ... import models


class KagisoUserTest(TestCase):

    @responses.activate
    def test_create(self):
        # ------------------------
        # -------Arrange----------
        # ------------------------

        email = 'test@email.com'
        first_name = 'Fred'
        last_name = 'Smith'
        is_staff = True
        is_superuser = True
        profile = {
            'age': 22
        }

        url, api_data = mocks.mock_out_post_users(
            1,
            email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            profile=profile
        )
        # ------------------------
        # -------Act--------------
        # ------------------------

        user = mommy.make(
            models.KagisoUser,
            id=None,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            profile=profile,
        )

        # ------------------------
        # -------Assert----------
        # ------------------------

        # Confirmation tokens are saved in memory only.
        assert user.confirmation_token == api_data['confirmation_token']

        result = models.KagisoUser.objects.get(id=user.id)

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == url

        assert result.id == api_data['id']
        assert result.email == api_data['email']
        assert result.first_name == api_data['first_name']
        assert result.last_name == api_data['last_name']
        assert result.is_staff == api_data['is_staff']
        assert result.is_superuser == api_data['is_superuser']
        assert not result.email_confirmed
        assert result.confirmation_token is None
        assert result.profile == api_data['profile']
        assert result.date_joined == parser.parse(api_data['created'])
        assert result.modified == parser.parse(api_data['modified'])

    @responses.activate
    def test_update(self):
        # ------------------------
        # -------Arrange----------
        # ------------------------
        mocks.mock_out_post_users(1, 'test@email.com')

        user = mommy.make(models.KagisoUser, id=None)

        email = 'test@email.com'
        first_name = 'Fred'
        last_name = 'Smith'
        is_staff = True
        is_superuser = True
        profile = {
            'age': 22
        }

        url, api_data = mocks.mock_out_put_users(
            1,
            email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            profile=profile
        )

        # ------------------------
        # -------Act--------------
        # ------------------------

        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.profile = profile
        user.save()

        # ------------------------
        # -------Assert----------
        # ------------------------
        result = models.KagisoUser.objects.get(id=user.id)

        assert len(responses.calls) == 2
        assert responses.calls[1].request.url == url

        assert result.id == api_data['id']
        assert result.email == api_data['email']
        assert result.first_name == api_data['first_name']
        assert result.last_name == api_data['last_name']
        assert result.is_staff == api_data['is_staff']
        assert result.is_superuser == api_data['is_superuser']
        assert result.profile == api_data['profile']
        assert result.modified == parser.parse(api_data['modified'])

    @responses.activate
    def test_delete(self):
        mocks.mock_out_post_users(1, 'test@email.com')
        user = mommy.make(models.KagisoUser, id=None)
        url = mocks.mock_out_delete_users(user.id)

        user.delete()

        user_deleted = not models.KagisoUser.objects.filter(
            id=user.id).exists()

        assert len(responses.calls) == 2
        assert responses.calls[1].request.url == url

        assert user_deleted

    def test_get_full_name_returns_email(self):
        email = 'test@email.com'
        user = models.KagisoUser(email=email)

        assert user.get_full_name() == email

    def test_get_short_name_returns_email(self):
        email = 'test@email.com'
        user = models.KagisoUser(email=email)

        assert user.get_short_name() == email

    def test_set_password(self):
        user = models.KagisoUser()
        password = 'my_password'

        user.set_password(password)

        assert user.raw_password == password

    def test_get_username_returns_email(self):
        email = 'test@email.com'
        user = models.KagisoUser(email=email)

        assert user.username == email

    def test_set_username_sets_username(self):
        username = 'test@username.com'
        user = models.KagisoUser(username=username)

        assert user.email == username

    @responses.activate
    def test_confirm_email(self):
        _, post_data = mocks.mock_out_post_users(1, 'test@email.com')
        user = mommy.make(models.KagisoUser, id=None)
        mocks.mock_out_put_users(
            user.id,
            user.email,
            profile=user.profile
        )
        url = mocks.mock_out_post_confirm_email(user.id)

        user.confirm_email(post_data['confirmation_token'])

        assert len(responses.calls) == 3
        # Create user, confirm user, update user...
        assert responses.calls[1].request.url == url

        result = models.KagisoUser.objects.get(id=user.id)

        assert result.email_confirmed
        assert not result.confirmation_token

    @responses.activate
    def test_record_sign_out(self):
        id = 1
        _, post_data = mocks.mock_out_post_users(id, 'test@email.com')
        user = mommy.make(models.KagisoUser, id=None)
        url = mocks.mock_out_delete_sessions(id)

        did_sign_out = user.record_sign_out()

        assert len(responses.calls) == 2
        assert responses.calls[1].request.url == url

        assert did_sign_out

    @responses.activate
    def test_generate_reset_password_token(self):
        _, post_data = mocks.mock_out_post_users(1, 'test@email.com')
        user = mommy.make(models.KagisoUser, id=None)
        url, data = mocks.mock_out_get_reset_password(user.id)

        reset_password_token = user.generate_reset_password_token()

        assert len(responses.calls) == 2
        assert responses.calls[1].request.url == url

        assert reset_password_token == data['reset_password_token']  # noqa

    @responses.activate
    def test_reset_password(self):
        _, post_data = mocks.mock_out_post_users(1, 'test@email.com')
        user = mommy.make(models.KagisoUser, id=None)
        url = mocks.mock_out_post_reset_password(user.id)

        did_password_reset = user.reset_password('new_password', 'test_token')

        assert len(responses.calls) == 2
        assert responses.calls[1].request.url == url

        assert did_password_reset
