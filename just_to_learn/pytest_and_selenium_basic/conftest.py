import pytest


@pytest.fixture(scope="function") #if don't put scope="..." here, default is function. Additionally, scope="class" will work same as beforeClass and afterClass in testNG
def setup_and_teardown():
    print("Hello guys, welcome to pytest!")
    yield
    print("Goodbye, see you later")

@pytest.fixture()
def data_load():
    print("This is data returned from data_load fixture")
    return ["Foden Duong", "vinhdtvt1999@gmail.com"]

@pytest.fixture(params=["Chrome", "Firefox", "IE"])
def cross_browser(request):
    return request.param