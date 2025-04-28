import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class TestFodenUseFixture:
    def test_method1(self):
        print("Method 1")

    def test_method2(self):
        print("Method 1")

    def test_method3(self):
        print("Method 1")
    def test_method4_use_data_load(self, data_load):
        print(data_load)
    # Output from fixture setup_and_teardown first, when a test function uses multiple fixtures,
    # fixtures are executed in the order they are specified as function arguments.
    # setup_and_teardown has cope="function", so it will implicitly passed as arguments of each test method.
    # Then the test_method4_use_data_load seems like
    # def test_method4_use_data_load(self, setup_and_teardown, data_load):
        # print(data_load)
    # => That the reason you will see the output as below:
    # Hello guys, welcome to pytest!
    # This is data returned from data_load fixture
    # ['Foden Duong', 'vinhdtvt1999@gmail.com']
    # Goodbye, see you later

    #Specially, if use 2 fixtures just to print something for example, the order will be the order that they are listed in the pytest.mark.usefixtures()

    def test_data_provider(self, cross_browser):
        print(cross_browser) # Will run three times, each time will print out Chrome, Firefox, IE respectively