import pytest
from framework.utilities.fileUtil import JsonUtil


class TestTables:
    @pytest.mark.parametrize("user", JsonUtil.load_users('./task3.1/toolsQAProject/tests/test_data/testData.json'))
    def test_tables(self, browser, user):
        browser.tablesSteps.navigate_to_main_page()
        assert browser.tablesSteps.main_page_is_open()

        browser.tablesSteps.click_elements_button()
        browser.tablesSteps.click_web_tables_button()
        assert browser.tablesSteps.web_tables_form_is_open()

        browser.tablesSteps.click_add_button()
        assert browser.tablesSteps.registration_form_is_open()

        browser.tablesSteps.enter_user_data(user)
        browser.tablesSteps.click_submit()
        assert browser.tablesSteps.registration_form_is_closed() \
               and browser.tablesSteps.user_in_table(user)

        records_before = browser.tablesSteps.number_of_records
        browser.tablesSteps.delete_user(user)
        records_after = browser.tablesSteps.number_of_records
        assert records_before > records_after \
               and not browser.tablesSteps.user_in_table(user)
