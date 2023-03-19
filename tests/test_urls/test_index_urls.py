from django.urls import reverse


def test_urls(client):
    url = reverse("app:index")
    response = client.get(url)
    assert response.status_code == 200
