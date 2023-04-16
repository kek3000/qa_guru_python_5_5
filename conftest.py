import pytest
from selene import be
from selene.support.shared import browser


# все общие фикстуры мы пишем в файле conftest.py, они будут видны всем тестовым классам по умолчанию

@pytest.fixture(scope="function")
def browser_start():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.quit()