def test_login(app):
    app.login_as(username="demo", password="demo")
    # TODO: add verification of presence User menu