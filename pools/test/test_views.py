import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from backend_AQ.pools.models import Pool, PoolDescription

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def pool():
    return Pool.objects.create(
        name='Test Pool',
        description_short='Short description',
        slug='test-pool'
    )

@pytest.fixture
def pool_with_description(pool):
    PoolDescription.objects.create(
        pool=pool,
        description='Full description'
    )
    return pool

@pytest.mark.django_db
def test_pool_list_view(api_client, pool):
    url = reverse('pool-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Test Pool'

@pytest.mark.django_db
def test_pool_detail_view(api_client, pool_with_description):
    url = reverse('pool-detail', kwargs={'slug': pool_with_description.slug})
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['name'] == 'Test Pool'
    assert response.data['description'] == 'Full description'

def test_view_example():
    assert True 