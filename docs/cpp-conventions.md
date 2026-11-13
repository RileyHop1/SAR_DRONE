# C++ Conventions

| Item | Agreed convention | Example |
| --- | --- | --- |
| Classes | PascalCase | `MissionManager` |
| Functions and methods | camelCase | `startSearch()` |
| Variables | snake_case | `search_area` |
| Data members | snake_case with a trailing underscore | `search_area_` |
| Opening braces | Same line as the declaration or control statement | `void startSearch() {` |

Parameters should be distinguishable from data members. Their exact naming convention is still open. Constants, namespaces, indentation, and line length also need a decision.

The preference against "trailing initialization" needs a short code example before becoming an enforceable rule. Confirm which syntax this refers to, such as constructor initializer lists, brace initialization, or trailing return types.

## Documentation expectations

- Document each class and its responsibility.
- Document functions in their header declarations.
- Add a short file-level description explaining the file's purpose and role in the project.

Proposed format is Doxygen-style comments. Agree on required details such as parameters, return values, units, coordinate frames, and error behavior. Define an equivalent rule for implementation-only functions and decide which documentation checks can be automated and which need review.

## Run the C++ checks

The repository root contains `.clang-format` for layout and `.clang-tidy` for naming. Both tools look for their configuration in parent directories of the source file. The formatter uses LLVM defaults for settings still open to discussion, with opening braces attached to the declaration or statement.

Run these commands from `/ros_ws` inside the [Jazzy container](environment/ros-jazzy.md). Install the tools inside the container if needed. The commands below assume the default root shell.

```bash
apt-get update
apt-get install -y clang-format clang-tidy
```

`apt-get update` refreshes the package index. `apt-get install -y` installs the tools and accepts the package manager's confirmation prompt.

Check formatting on a source file:

```bash
clang-format --dry-run --Werror packages/sar_environment_test/test/test_cpp_ros_setup.cpp
```

`--dry-run` checks the file and `--Werror` makes a formatting difference fail the command. To apply the formatting, run `clang-format -i` with the same file path.

Build the package to generate the compiler settings used by clang-tidy:

```bash
colcon build --base-paths packages --packages-up-to sar_environment_test \
  --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
clang-tidy -p build/sar_environment_test \
  packages/sar_environment_test/test/test_cpp_ros_setup.cpp
```

`--packages-up-to` builds the selected package and its workspace dependencies. The CMake flag generates `compile_commands.json` in the package's build directory. `clang-tidy -p` reads that database so the check sees the same ROS headers and compiler flags as the build. For another package, use its own build directory and source path.

## VS Code

For editor diagnostics, open the workspace in the Jazzy container using VS Code Dev Containers, then install the clangd extension in that container. In your local workspace settings, set the following clangd arguments for the package you are editing:

```json
{
  "clangd.arguments": [
    "--clang-tidy",
    "--compile-commands-dir=/ros_ws/build/sar_environment_test"
  ]
}
```

Generate the database first with the build command above. Select clangd as the C++ formatter to use the repository's `.clang-format` when you run **Format Document**. Point clangd at the other package's build directory when changing packages.
