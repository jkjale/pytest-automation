import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will execute last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=["Chrome", "Firefox", "Safari"])
def crossBrowser(request):
    return request.param