import pytest
from test_data.login_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD
)

@pytest.mark.smoke
def test_valid_login(login_page):
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    assert "/secure" in login_page.page.url
    assert "You logged into a secure area!" in login_page.get_message()

@pytest.mark.regression
def test_invalid_username(login_page):
    login_page.login(INVALID_USERNAME, VALID_PASSWORD)
    assert "Your username is invalid!" in login_page.get_message()

@pytest.mark.regression
def test_invalid_password(login_page):
    login_page.login(VALID_USERNAME, INVALID_PASSWORD)
    assert "Your password is invalid!" in login_page.get_message()

@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password",
    [
        ("", ""),
        ("tomsmith", ""),
        ("", "SuperSecretPassword!")
    ]
)
def test_missing_credentials(login_page, username, password):
    login_page.login(username, password)
    assert "invalid!" in login_page.get_message()
