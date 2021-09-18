import pytest


@pytest.fixture(scope="class")
def setup():
    print("\nI will be executed first\n")
    yield
    print("\nI will be executed last\n")


@pytest.fixture()
def data_load():
    print("\nUser profile data is being created\n")
    return ["firstname", "lastname", "vedge.id"]


@pytest.fixture(params=[("Chrome", "firstname", "lastname"), ("Firefox", "jen"), ("IE", "SS")])
def cross_browser(request):
    return request.param

