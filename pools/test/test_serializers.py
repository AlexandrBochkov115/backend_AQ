import pytest
from backend_AQ.pools.serializers import PoolListSerializer, PoolDetailSerializer, PoolImageSerializer
from backend_AQ.pools.models import Pool, PoolImage, PoolDescription

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

def test_pool_list_serializer(pool):
    serializer = PoolListSerializer(pool)
    data = serializer.data
    assert data['name'] == 'Test Pool'
    assert data['description_short'] == 'Short description'
    assert data['slug'] == 'test-pool'

def test_pool_detail_serializer(pool_with_description):
    serializer = PoolDetailSerializer(pool_with_description)
    data = serializer.data
    assert data['name'] == 'Test Pool'
    assert data['description'] == 'Full description'
    assert data['slug'] == 'test-pool'

def test_serializer_example():
    assert True 