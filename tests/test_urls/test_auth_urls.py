import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_auth_urls(client):
    url = reverse("admin:login")
    response = client.get(url)
    assert response.status_code == 200

    # login url
    url = reverse("app:login")
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url)
    assert response.status_code == 200

    # logout url
    url = reverse("app:logout")
    response = client.get(url, follow=True)
    assert response.status_code == 200

    # sign up url
    url = reverse("app:sign_up")
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url)
    assert response.status_code == 200

    # forgot password url
    url = reverse("app:forgot_password")
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url)
    assert response.status_code == 200
