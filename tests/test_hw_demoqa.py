from quru8_10.pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # wwhen

    registration_page.fill_first_name('Max')
    registration_page.fill_last_name('Cheshire')
    registration_page.fill_email('MaxCheshire@gmail.com')
    registration_page.choose_a_gender('Male')
    registration_page.fill_number_pelephone('7999123123')
    registration_page.coose_data_of_birth(month='2', year='99', day='026')
    registration_page.choose_subject('English')
    registration_page.choose_hobby_1('Sports')
    registration_page.choose_hobby_2('Reading')
    registration_page.donwload_page('fier.webp')
    registration_page.current_adress('Pyshkina-kolotushkina, Moscow, Russia')
    registration_page.choose_state('Uttar')
    registration_page.choose_city('ag')
    registration_page.submit_form()

    registration_page.should_regustration_user(
        "Max Cheshire",
        "MaxCheshire@gmail.com",
        "Male",
        "7999123123",
        "26 February,1998",
        "English",
        "Sports, Reading",
        "fier.webp",
        "Pyshkina-kolotushkina, Moscow, Russia",
        "Uttar Pradesh Agra"
    )
