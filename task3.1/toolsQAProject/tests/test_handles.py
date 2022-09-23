

class TestHandles:
    def test_handles(self, browser):
        browser.handlesSteps.navigate_to_main_page()
        assert browser.handlesSteps.main_page_is_open()

        browser.handlesSteps.click_alertsFrameWindows_button()
        browser.handlesSteps.click_browser_windows_button()
        assert browser.handlesSteps.windows_form_is_open()

        browser.handlesSteps.click_new_tab_button()
        assert browser.handlesSteps.number_of_windows is 2 \
               and browser.handlesSteps.sample_page_is_open()

        browser.handlesSteps.close_current_tab()
        assert browser.handlesSteps.windows_form_is_open()

        browser.handlesSteps.click_elements_button()
        browser.handlesSteps.click_links_button()
        assert browser.handlesSteps.links_form_is_open()

        browser.handlesSteps.click_home_link_and_switch_to_new_tab()
        assert browser.handlesSteps.number_of_windows is 2 \
               and browser.handlesSteps.main_page_is_open()

        browser.handlesSteps.resume_to_previous_tab()
        assert browser.handlesSteps.links_form_is_open()
