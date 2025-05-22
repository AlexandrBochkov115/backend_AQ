import pytest
from django.contrib.admin.sites import AdminSite
from django.core.exceptions import ValidationError
from backend_AQ.pools.admin import PoolAdmin, PoolImageFormSet, PoolDescriptionInline
from backend_AQ.pools.models import Pool, PoolImage, PoolDescription

@pytest.fixture
def admin_site():
    return AdminSite()

@pytest.fixture
def pool_admin(admin_site):
    return PoolAdmin(Pool, admin_site)

@pytest.fixture
def pool():
    return Pool.objects.create(
        name='Test Pool',
        description_short='Short description',
        slug='test-pool'
    )

def test_pool_admin_list_display(pool_admin):
    assert 'name' in pool_admin.list_display
    assert 'slug' in pool_admin.list_display
    assert 'main_image_preview' in pool_admin.list_display
    assert 'short_description_preview' in pool_admin.list_display

def test_pool_image_formset_validation():
    # Создаем форму с валидными данными
    form_data = {
        'form-TOTAL_FORMS': '1',
        'form-INITIAL_FORMS': '0',
        'form-MIN_NUM_FORMS': '0',
        'form-MAX_NUM_FORMS': '6',
        'form-0-image': 'test.jpg'
    }
    formset = PoolImageFormSet(data=form_data)
    assert formset.is_valid()

def test_pool_description_inline(pool):
    inline = PoolDescriptionInline(Pool, AdminSite())
    assert inline.min_num == 1
    assert inline.max_num == 1
    assert inline.validate_min is True

def test_pool_short_description_preview(pool_admin, pool):
    preview = pool_admin.short_description_preview(pool)
    assert preview == 'Short description...' 