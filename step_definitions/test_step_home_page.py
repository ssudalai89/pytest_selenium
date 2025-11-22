import pytest
from pytest_bdd import scenarios, given, when, then
from pages.search_page import SearchPage
from pages.home_page import HomePage

# Register scenarios from the feature file
scenarios('../features/para_home_page.feature')

@given('I open the Para Bank homepage')
def open_parabank_home_page(browser):
    pass

@then('I should see the title as "ParaBank | Welcome | Online Banking"')
def verify_parabank_home_page_title(browser):
    page = HomePage(browser)
    page.title_validation("ParaBank | Welcome | Online Banking")

