import pytest
from selene.support.shared import browser


# все общие фикстуры мы пишем в файле conftest.py, они будут видны всем тестовым классам по умолчанию

@pytest.fixture(scope="function")
def browser_start():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()