from framework.utilities.randomUtil import RandomUtil


class TestAlerts:

    def test_alerts(self, browser):
        browser.alertsSteps.navigate_to_main_page()
        assert browser.alertsSteps.main_page_is_open()

        browser.alertsSteps.click_alertsFrameWindows_button()
        browser.alertsSteps.click_alerts_button()
        assert browser.alertsSteps.alerts_form_is_open()

        browser.alertsSteps.click_see_alerts_button()
        assert browser.alertsSteps.alert_is_open("You clicked a button")

        browser.alertsSteps.click_OK_on_alert()
        assert browser.alertsSteps.alert_is_closed()

        browser.alertsSteps.click_confirm_box_will_appear_button()
        assert browser.alertsSteps.alert_is_open("Do you confirm action?")

        browser.alertsSteps.click_OK_on_alert()
        assert browser.alertsSteps.alert_is_closed() \
               and browser.alertsSteps.confirm_text_is_displayed("You selected Ok")

        browser.alertsSteps.click_prompt_box_will_appear_button()
        assert browser.alertsSteps.alert_is_open("Please enter your name")

        random_string = RandomUtil.get_random_string(length_range=(6, 10))
        browser.alertsSteps.enter_text_in_alert(random_string)
        browser.alertsSteps.click_OK_on_alert()
        assert browser.alertsSteps.prompt_text_is_displayed(random_string)
