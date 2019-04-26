def test_create_status(app, session):
    input_text = 'dddd'
    # Locate existed text statuses
    old_status_list = app.status_text_elements()
    app.create_new_text_status(input_text)
    new_status_element = app.wait_new_status_appear(old_status_list)
    # Verification
    assert new_status_element.text == input_text




