
def test_create_status(app, logged_user):
    input_text = 'Welcome to l'
    # Locate existest text statuses
    old_status_list = app.status_text_elements()
    app.create_new_text_status(input_text)
    # new_status_element = app.wait_new_status_appear(old_status_list)
    # Verification
    # assert new_status_element.text == input_text
    print(app.user_of_new_status_elements()[0].text)
    print(logged_user.real_name)
    assert app.user_of_new_status_elements()[0].text == logged_user.real_name
    # assert app.user_of_new_status_elements()[0].text() == 'fff'


# def create_new_status_text(driver, input_text, wait):
#     # Enter new status text
#     status_input_field = wait.until(EC.presence_of_all_elements_located(By.NAME), 'status')
#     status_input_field.send_keys(input_text)
#     # Submit new status
#     driver.find_element_by_class_name('save').click()
