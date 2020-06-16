import pytest

# Connects our tests with our database
pytestmark = pytest.mark.django_db

from ..models import Post

def test___str__():
    post = Post.objects.create(
        name="Stracchino",
        description="Semi-sweet cheese that goes well with starches.",
        type=Post.Type.Social,
    )
    assert post.__str__() == "Stracchino"
    assert str(post) == "Stracchino"
