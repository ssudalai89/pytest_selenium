import pytest
from pytest_bdd import scenarios, given, when, then
from pages.search_page import SearchPage

# Register scenarios from the feature file
#scenarios('../features/search.feature')

@pytest.fixture
def search_page(browser):
    return SearchPage(browser)

@given('I open the Google homepage')
def open_google_search_page(browser):
    page = SearchPage(browser)
    page.open_page(page.url)
    
@when('I search for "Pytest BDD tutorial"')
def search_for_text(browser):
    page = SearchPage(browser)
    page.search_for("Pytest BDD tutorial")

@then('I should see search results related to "Pytest BDD tutorial"')
def verify_search_results(search_page, browser):
    page = SearchPage(browser)
    page_source = page.get_title()
    assert "Pytest BDD tutorial" in page_source, "Search term not found in page content"

