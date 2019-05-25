# from models.user import User
# from pages.pages import MainPage, SignInPage, DashboardPage


def test_login(app, user):                     # TODO: post-condition - logout
    # user = User(username='admin', password='pass', real_name="Admin")
    # main_page = MainPage(driver)
    app.main_page.sign_in_click()
    # sing_in_page = SignInPage(driver)
    assert app.sign_in_page.is_this_page()
    app.sign_in_page.input_username(user)
    app.sign_in_page.input_password(user)
    app.sign_in_page.sign_in_click()  # !!!! Добавила явное ожидание в этот метод, что затемнение исчезло, чтоб пофиксить багу
    # dashboard_page = DashboardPage(driver)
    assert app.dashboard_page.active_menu.text == "DASHBOARD"
    # dashboard_page = main_page.login_as(user)
    assert app.dashboard_page.user_menu_present()
    assert app.dashboard_page.user_menu_present().text == user.real_name

    # TODO verify message!