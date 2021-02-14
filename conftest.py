import pytest
from selenium import webdriver

url = 'https://www.npmjs.com/package/react-native-toast-message'


@pytest.fixture
def page(request):
    driver = webdriver.Chrome()
    yield request.param(
        driver=driver,
        url=url,
    )
    if request.session.testsfailed:
        driver.get_screenshot_as_file(f'./screenshot/{request.node.name}.png')
    driver.quit()
