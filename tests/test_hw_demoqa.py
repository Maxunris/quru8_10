
from quru8_10.pages.registration_page import RegistrationPage
from quru8_10.data.users import User
from selene import browser

registration_page = RegistrationPage()


def test_student_registration_form():
    user = User(first_name='Max',
                last_name='Cheshire',
                email='MaxCheshire@gmail.com',
                gender='Male',
                phone_number='7999123123',
                month_of_birth='February',
                year_of_birth='1998',
                day_of_birth='26',
                subject='English',
                hobby='Sports, Reading',
                picture='fier.webp',
                current_address='Pyshkina-kolotushkina, Moscow, Russia',
                state='Uttar Pradesh',
                city='Agra')
    registration_page.open()


    # WHEN
    registration_page.register(user)

    # THEN
    registration_page.user_should_registered(user)






