import os

from approvaltests import verify

from approvaltests.reporters.python_native_reporter import *


def test_files_identical(tmpdir):
    file1 = os.path.join(tmpdir, "a.received.txt")
    file2 = os.path.join(tmpdir, "b.approved.txt")
    identical_contents = "abc"
    with open(file1, "w") as f1:
        f1.write(identical_contents)
    with open(file2, "w") as f2:
        f2.write(identical_contents)
    assert calculate_diff(file1, file2) == "Files are identical"


def test_files_differ(tmpdir):
    file1 = os.path.join(tmpdir, "a.received.txt")
    file2 = os.path.join(tmpdir, "b.approved.txt")
    with open(file1, "w") as f1:
        f1.write("abc")
    with open(file2, "w") as f2:
        f2.write("def")
    diff = calculate_diff(file1, file2)
    diff = diff.replace(str(tmpdir), "tmpdir")
    verify(diff)

