from playwright.sync_api import Page, expect

def test_login_page_can_open(page: Page):
    page.goto("https://www.baidu.com/")
    expect(page).to_have_title("百度一下，你就知道")


def test_login_success(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.pause() #停顿一下
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    # 断言登录成功提示出现
    expect(page.get_by_text("You logged into a secure area!")).to_be_visible()


def test_login_wrong_password(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("wrongpassword")
    page.get_by_role("button", name="Login").click()
    # 断言出现密码错误提示
    expect(page.get_by_text("Your password is invalid!")).to_be_visible()
