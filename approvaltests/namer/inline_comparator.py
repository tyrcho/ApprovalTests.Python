import tempfile
from inspect import FrameInfo
from pathlib import Path
from typing import Optional, Callable, Any

from approval_utilities.utilities.multiline_string_utils import remove_indentation_from
from approvaltests import Namer, StackFrameNamer
from approvaltests.namer.inline_python_reporter import InlinePythonReporter


class InlineComparator(Namer):
    def get_approved_filename(self, base: Optional[str] = None) -> str:
        file = tempfile.NamedTemporaryFile(suffix=".approved.txt", delete=False).name
        docs = self.get_test_method_doc_string()
        Path(file).write_text(docs)
        return file

    def get_received_filename(self, base: Optional[str] = None) -> str:
        return tempfile.NamedTemporaryFile(suffix=".received.txt", delete=False).name

    def get_test_method_doc_string(self):
        test_stack_frame: FrameInfo = StackFrameNamer.get_test_frame()
        method: Callable[..., Any] = self.get_caller_method(test_stack_frame)
        return remove_indentation_from(method.__doc__)

    def get_caller_method(self, caller_frame) -> Callable:
        caller_function_name: str = caller_frame[3]
        caller_function_object = caller_frame.frame.f_globals.get(
            caller_function_name, None
        )
        return caller_function_object

    def register(self, options: "Options", show_code: bool):
        options2 = options.with_namer(self)
        if show_code:
            options2 = options2.with_reporter(InlinePythonReporter(options.reporter))
        return options2
