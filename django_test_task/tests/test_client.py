import datetime
import pytest

from api.models import Client


@pytest.mark.django_db
def test_client_created():
    client = Client.objects.create(
        first_name='Ilya', last_name='Kochinashvili', date_of_birth=datetime.date(1991, 12, 22)
    )

    assert client.zodiac_sing == 'Capricorn'
