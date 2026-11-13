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

See the [C++ linting guide](cpp-linting.md) for installing the tools, generating compile databases, and running the shared script. The formatter uses LLVM defaults with opening braces attached to the declaration or statement.

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

Generate the database first with the build command in the linting guide. Select clangd as the C++ formatter to use the repository's `.clang-format` when you run **Format Document**. Point clangd at the other package's build directory when changing packages.
