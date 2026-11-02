import pytest
from playwright.sync_api import expect
from pages.sauce_page import SaucePage


@pytest.fixture
def sauce(page):
    app = SaucePage(page)
    app.open()
    return app


@pytest.mark.smoke
def test_valid_login(sauce):
    sauce.login("standard_user", "secret_sauce")

    expect(sauce.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


@pytest.mark.regression
def test_add_product_to_cart(sauce):
    sauce.login("standard_user", "secret_sauce")
    sauce.add_backpack()

    expect(
        sauce.page.locator(".shopping_cart_badge")
    ).to_have_text("1")


@pytest.mark.regression
def test_remove_product(sauce):
    sauce.login("standard_user", "secret_sauce")
    sauce.add_backpack()
    sauce.remove_backpack()

    expect(
        sauce.page.locator(".shopping_cart_badge")
    ).to_have_count(0)


@pytest.mark.smoke
def test_complete_checkout(sauce):
    sauce.login("standard_user", "secret_sauce")
    sauce.add_backpack()
    sauce.open_cart()

    expect(
        sauce.page.locator(".cart_item")
    ).to_have_count(1)

    sauce.checkout("Test", "User", "60601")

    expect(
        sauce.page.locator(".complete-header")
    ).to_have_text("Thank you for your order!")


@pytest.mark.regression
def test_invalid_login(sauce):
    sauce.login("invalid_user", "wrong_password")

    expect(
        sauce.page.locator("[data-test='error']")
    ).to_contain_text(
        "Username and password do not match"
    )
