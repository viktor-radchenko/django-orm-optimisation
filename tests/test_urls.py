import pytest

from django.urls import reverse


def test_urls(client):
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200

    url = reverse("admin:index")
    response = client.get(url, follow=True)
    assert response.status_code == 200

    url = reverse("admin:login")
    response = client.get(url)
    assert response.status_code == 200
