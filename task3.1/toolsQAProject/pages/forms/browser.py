
from toolsQAProject.steps.alertsSteps import AlertsSteps
from toolsQAProject.steps.handlesSteps import HandlesSteps
from toolsQAProject.steps.iframeSteps import IframeSteps
from toolsQAProject.steps.tablesSteps import TablesSteps
from framework.utilities.driverUtil import DriverUtil


class Browser:
    """"""
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    @property
    def alertsSteps(self):
        return AlertsSteps()

    @property
    def iframeSteps(self):
        return IframeSteps()

    @property
    def tablesSteps(self):
        return TablesSteps()

    @property
    def handlesSteps(self):
        return HandlesSteps()