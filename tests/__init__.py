__author__ = "Chris Lucian; Llewellyn Falco; Jim Counts"

from approvaltests import set_default_reporter
from approvaltests.reporters.report_all_to_clipboard import ReporterByCopyMoveCommandForEverythingToClipboard


def configure_approvaltests():
    print("HELLO")
    set_default_reporter(ReporterByCopyMoveCommandForEverythingToClipboard())


configure_approvaltests()
