# Check C++ Formatting and Naming

Run `scripts/lint.py` before opening a PR. It uses `.clang-format` for layout and `.clang-tidy` for the project's C++ naming rules. See [C++ conventions](cpp-conventions.md) for examples and VS Code setup.

## Set up the tools

From `/ros_ws` inside the [Jazzy container](environment/ros-jazzy.md), run the following commands in order. Stop if a command fails. These installation commands assume the container's default root shell.

```bash
apt-get update
apt-get install -y clang-format clang-tidy
rosdep update --rosdistro jazzy
rosdep install --from-paths packages --ignore-src --rosdistro jazzy -y
colcon build --base-paths packages \
  --cmake-args -DBUILD_TESTING=ON -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
source install/setup.bash
```

- `apt-get update` refreshes the package index, and `apt-get install -y` installs both Clang tools.
- `rosdep update` refreshes dependency definitions. `rosdep install` uses package manifests under `packages/` to install external dependencies. `--ignore-src` skips dependencies already present as workspace packages.
- `colcon build` builds the discovered packages. `--cmake-args` passes settings to CMake. `BUILD_TESTING=ON` includes test targets and `CMAKE_EXPORT_COMPILE_COMMANDS=ON` records the compiler commands for each CMake package.
- `source install/setup.bash` loads the built workspace into the current shell.

## Run the checks

```bash
# Check the whole workspace, as CI does.
python3 scripts/lint.py packages

# Check a single package's test directory.
python3 scripts/lint.py packages/sar_environment_test/test

# Apply formatting to that directory, then check naming.
python3 scripts/lint.py --format packages/sar_environment_test/test
```

Review the diff after using `--format`. The script writes formatting changes directly and reports naming issues for you to fix. By default, formatting differences and naming violations fail the command.

## Script reference

Usage is `python3 scripts/lint.py [--format] PATH [PATH ...]`. Supply one or more existing C++ files or directories. Run it from the repository root so it can find `build/`. Run `python3 scripts/lint.py --help` for the CLI options.

1. **Find source files.** The script recursively searches directory arguments for `.cpp`, `.cc`, `.cxx`, `.h`, and `.hpp` files. Directory scans skip files under nested `build/`, `install/`, and `log/` directories.
2. **Load compiler commands.** The script reads `build/*/compile_commands.json` once at startup. Each entry records the source path, the compiler's working directory, and the compiler arguments. The script resolves the source path and remembers which database lists it. If multiple databases list a source, it uses the first in sorted order.
3. **Check formatting.** For sources and headers, the script runs `clang-format --dry-run --Werror`. With `--format` it uses `clang-format -i` to apply formatting.
4. **Check C++ naming.** For source files, the script passes the matching database directory to `clang-tidy -p`. That gives clang-tidy the compiler flags and include paths for that file. It can also check declarations in project headers included by those sources.
5. **Report failures.** The script stops at the first tool failure and exits unsuccessfully. The ROS 2 PR workflow uses that exit status to fail the check.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| `FileNotFoundError` for `clang-format` or `clang-tidy` | Install the tools inside the current container. The dotfiles supply their configuration. |
| `No compile database entry` | Run the build above from `/ros_ws`. Confirm the source belongs to an enabled CMake target and appears in its package's database. |
| Formatting differences | Run with `--format` on the affected paths and review the diff. |
| Naming violation | Update the identifier according to the C++ conventions, then rerun check mode. |
