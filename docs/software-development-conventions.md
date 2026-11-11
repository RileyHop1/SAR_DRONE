# Software Development Conventions

## Development order

Develop each feature in the order below.

1. **Document the interface and expected behavior.** Describe the feature's purpose, inputs, outputs, dependencies, and failure behavior. Define the relevant function or ROS interface before implementing it. Resolve ambiguous expectations with the team.
2. **Write the tests.** Turn the documented behavior into checks for normal operation, relevant edge cases, and failures. Use GoogleTest for C++. Select Python and ROS integration test tools as part of the tooling plan. Confirm that a new test detects the missing or incorrect behavior.
3. **Implement the behavior.** Write the code needed to satisfy the interface and tests. Run the tests, then refactor with the checks passing.

When a requirement changes, update the interface documentation and tests along with the implementation.

## Documentation

- Document classes and functions according to the [C++ conventions](cpp-conventions.md).
- For ROS interfaces, document what each field means, including units, coordinate frames, timestamps, and expected behavior when data is missing or invalid.
- Record relevant setup and usage instructions so another teammate can run and verify the feature.
- Keep interface documentation close to its declaration or definition and link to longer design explanations where needed.

## Local checks and review

- Run applicable tests, lint checks, and formatting checks before requesting review.
- Use the same tool configuration locally, in VS Code, and in CI.
- Provide convenient local commands for testing, linting, and formatting. The command interface is still to be selected.
- Require tests and lint checks before merging into `Development`.
- Recheck tests and lint before merging into production on `main`.
- Review whether the implementation, tests, and documentation describe the same behavior.
- Include reproducible verification steps and outstanding limitations in the pull request.

Follow the team's Git naming and PR conventions. PR descriptions use Changes, Goal, Steps to test, and Pictures.

## Relationship to the roadmap

The [software roadmap](software-roadmap.md) tracks the work needed to establish these practices and deliver the system. These conventions describe how we approach each feature as that tooling becomes available.
