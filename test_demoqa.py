from selene.support.shared import browser
from selene import have
import os


def test_form(browser_start):
    # Открываем url https://demoqa.com/automation-practice-form
    browser.open('/automation-practice-form')

    # Заполняем Name
    browser.element('#firstName').type('Nikita')
    browser.element('#lastName').type('Alekseev')

    # Заполняем Email
    browser.element('#userEmail').type('test@test.ru')

    # Заполняем Gender
    browser.element('#gender-radio-1').double_click()

    # Заполняем Mobile(10 Digits)
    browser.element('#userNumber').type('79999999999')

    # Заполняем Date of Birth
    browser.element('#dateOfBirthInput').press()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="6"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1991"]').click()
    browser.element('div[aria-label="Choose Thursday, July 18th, 1991"]').click()

    # Заполняем Subjects
    browser.element('#subjectsInput').type('Computer Science').press_enter()

    # Заполняем Hobbies
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()

    # Заполняем Picture
    browser.element('#uploadPicture').send_keys(os.getcwd() + "/image.jpg")

    # Заполняем Current Address
    browser.element('#currentAddress').type('Russia, Reutov')

    # Заполняем State and City
    browser.element('#state').click()
    browser.element('#react-select-3-input').set_value('Haryana').press_tab()
    browser.element('#city').click()
    browser.element('#react-select-4-input').set_value('Panipat').press_tab()

    # Жмём кнопку Submit
    browser.element('#submit').press_enter()

    # Проверка всех введёных значений
    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Nikita Alekseev', 'Student Email test@test.ru', 'Gender Male', 'Mobile 7999999999',
        'Date of Birth 18 July,1991', 'Subjects Computer Science', 'Hobbies Sports, Music',
        'Picture image.jpg', 'Address Russia, Reutov', 'State and City Haryana Panipat'))

    print('\nФорма полностью заполнена, отправлена и проверена. Тест пройден успешно.')
