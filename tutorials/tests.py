from django.test import TestCase
from tutorials.models import Tutorial

# Create your tests here.
from django.urls import reverse
import pytest

def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.mark.django_db
def test_create_tutorial():
    @pytest.fixture
    def new_tutorial(db):
        tutorial = Tutorial.objects.create(
            title='Pytest',
            tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
            description='Tutorial on how to apply pytest to a Django application',
            published=True
        )
        return tutorial
    
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    assert tutorial.title == "Pytest"