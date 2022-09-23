

class TestIframe:
    def test_iframe(self, browser):
        browser.iframeSteps.navigate_to_main_page()
        assert browser.iframeSteps.main_page_is_open()

        browser.iframeSteps.click_alertsFrameWindows_button()
        browser.iframeSteps.click_nested_frames_button()
        assert browser.iframeSteps.nested_frames_form_is_open() \
               and browser.iframeSteps.parent_frame_is_displayed() \
               and browser.iframeSteps.child_iframe_is_displayed()

        browser.iframeSteps.click_frames_button()
        assert browser.iframeSteps.frames_form_is_open() \
               and browser.iframeSteps.upper_frame_message == browser.iframeSteps.lower_frame_message
