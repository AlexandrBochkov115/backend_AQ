import pytest
from backend_AQ.pools.models import Pool, PoolImage, PoolDescription

@pytest.fixture
def pool():
    return Pool.objects.create(
        name='Test Pool',
        description_short='Short description',
        slug='test-pool'
    )

def test_pool_str(pool):
    assert str(pool) == 'Test Pool'

def test_pool_image_creation(pool):
    image = PoolImage.objects.create(pool=pool, image='test.jpg')
    assert str(image) == f"Изображение для {pool.name}"

def test_pool_description_creation(pool):
    description = PoolDescription.objects.create(
        pool=pool,
        description='Full description'
    )
    assert str(description) == f"Описание для {pool.name}" 