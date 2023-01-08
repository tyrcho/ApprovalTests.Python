from pathlib import Path


def test_init_present():
    assert_directories_have_inits(Path("../approvaltests"))
    assert_directories_have_inits(Path("../approval_utilities"))


def is_generated_code(directory_name: str):
    return "__" in directory_name


def assert_directories_have_inits(directory: Path):
    if not is_generated_code(f"{directory}"):
        if not (directory / "__init__.py").exists():
            assert False, f"__init__.py is missing from {directory}"
        for subdirectory in directory.iterdir():
            if subdirectory.is_dir():
                assert_directories_have_inits(subdirectory)
