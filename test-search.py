from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture()
def size_browser():
    browser.config.window_width = 1600
    browser.config.window_height = 900


def test_positiv_case(size_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene python').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))



def test_negativ_case(size_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('Selene - User-oriented Web UI browser tests in Python'))


