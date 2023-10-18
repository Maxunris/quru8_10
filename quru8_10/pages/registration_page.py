from quru8_10 import resourse

from selene import browser, have, be, by


class RegistrationPage:
    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def fill_email(self, value):
        browser.element("#userEmail").type(value)

    def choose_a_gender(self, gender):
        gender = f'//label[@for="gender-radio-1" and text()="{gender}"]'
        browser.element(gender).click()

    def fill_number_pelephone(self, value):
        browser.element("#userNumber").type(value)

    def coose_data_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element('.react-datepicker__month-select').should(be.visible).click()
        browser.element(f'.react-datepicker__month-select > option:nth-child({month})').should(be.visible).click()
        browser.element('.react-datepicker__year-select').should(be.visible).click()
        browser.element(f'.react-datepicker__year-select > option:nth-child({year})').should(be.visible).click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--{day}').should(be.visible).click()

    def choose_subject(self, value):
        browser.element('#subjectsInput').type('Engl').press_enter()

    def choose_hobby_1(self, hobby):
        hobby = f'//label[@for="hobbies-checkbox-1" and text()="{hobby}"]'
        browser.element(hobby).should(be.clickable).click()

    def choose_hobby_2(self, hobby):
        hobby = f'//label[@for="hobbies-checkbox-2" and text()="{hobby}"]'
        browser.element(hobby).should(be.clickable).click()

    def donwload_page(self, value):
        browser.element('#uploadPicture').type(resourse.path(value))

    def current_adress(self, value):
        browser.element('#currentAddress').type(value)

    def choose_state(self, value):
        browser.element('#react-select-3-input').should(be.visible).type(value).press_enter()

    def choose_city(self, value):
        browser.element('#react-select-4-input').should(be.visible).type(value).press_enter()

    def submit_form(self):
        browser.element('#submit').execute_script('element.click()')

    def should_regustration_user(self, full_name, email, gender, phone_number, date_of_birth, subject, hobby, picture,
                                 state, city):
        browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
            full_name,
            email,
            gender,
            phone_number,
            date_of_birth,
            subject,
            hobby,
            picture,
            state,
            city
        ))
        browser.element("#closeLargeModal").should(be.visible).click()
