import argparse
import json
import subprocess
from pathlib import Path

CPP_SOURCES = {".cpp", ".cc", ".cxx"}
CPP_SUFFIXES = CPP_SOURCES | {".h", ".hpp"}

parser = argparse.ArgumentParser()

parser.add_argument(
    "--format",
    action="store_true",
    help="Apply clang-format to the selected files."
)
parser.add_argument(
    "paths",
    type=Path,
    nargs="+",
    help="Path to a file or directory"
)

args = parser.parse_args()

compile_databases = {}
for database in sorted(Path("build").glob("*/compile_commands.json")):
    for entry in json.loads(database.read_text()):
        source = (Path(entry["directory"]) / entry["file"]).resolve()
        compile_databases.setdefault(source, database.parent)


def lint_file(file: Path) -> None:
    format_flags = ["-i"] if args.format else ["--dry-run", "--Werror"]
    subprocess.run(["clang-format", *format_flags, str(file)], check=True)

    if file.suffix in CPP_SOURCES:
        database_dir = compile_databases.get(file.resolve())
        if database_dir is None:
            parser.error(
                f"No compile database entry for {file}. "
                "Build the workspace with -DCMAKE_EXPORT_COMPILE_COMMANDS=ON."
            )

        subprocess.run(
            ["clang-tidy", "-p", str(database_dir), str(file)],
            check=True,
        )


def lint_dir(directory: Path) -> None:
    for source in sorted(directory.rglob("*")):
        parent_dirs = source.relative_to(directory).parts[:-1]
        if {"build", "install", "log"}.intersection(parent_dirs):
            continue
        if source.is_file() and source.suffix in CPP_SUFFIXES:
            lint_file(source)


for path in args.paths:
    if path.is_dir():
        lint_dir(path)
    elif path.is_file() and path.suffix in CPP_SUFFIXES:
        lint_file(path)
    else:
        parser.error(f"Expected an existing C++ file or directory: {path}")
