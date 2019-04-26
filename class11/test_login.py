from modules.user import User

def test_login(app):
    user = User(username='demo', password='demo', real_name='Demo')
    # app.login_as(username='demo',password ='demo')
    app.login_as(user)
    assert app.is_user_menu_present()
    # TODO: add verifficatin of presence User Name