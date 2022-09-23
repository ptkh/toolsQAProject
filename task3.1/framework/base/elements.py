from framework.base.baseElement import BaseElement


class Button(BaseElement):
    """Wrapper for button element"""


class Input(BaseElement):
    def enter_text(self, text) -> None:
        self.event_listener.after_change_value_of(self.name, self.driver)
        self.element.send_keys(text)
        self.event_listener.after_change_value_of(self.name, self.driver)


class Text(BaseElement):
    """Wrapper for text element"""
