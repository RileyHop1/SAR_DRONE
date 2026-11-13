# Verify Your Environment

Run the `sar_environment_test` package to check that your Jazzy container can build and run C++ and Python ROS 2 tests. Start with [Start ROS 2 Jazzy](ros-jazzy.md) and use a checkout that contains `packages/sar_environment_test`.

## Build and run the environment checks

Run these commands one at a time inside the container. Stop if a command fails.

```bash
cd /ros_ws
colcon build --base-paths /ros_ws/packages --packages-select sar_environment_test
source install/setup.bash
colcon test --base-paths /ros_ws/packages \
  --packages-select sar_environment_test \
  --return-code-on-test-failure \
  --ctest-args -R '^(test_cpp_ros_setup|python_ros_setup|cpp_python_pubsub)$'
colcon test-result --verbose
```

- `cd /ros_ws` puts you at the workspace root, where colcon writes its build, install, and log directories by default.
- `--base-paths /ros_ws/packages` points colcon at the package sources. `--packages-select sar_environment_test` limits the build and tests to the environment check package.
- `source install/setup.bash` loads the built workspace into the current shell.
- `--return-code-on-test-failure` makes the test command fail if a check fails. `--ctest-args -R` selects the three registered checks by name.
- `colcon test-result --verbose` reports the recorded results and prints details for failures.

## Expected results

| Check | What it verifies |
| --- | --- |
| `test_cpp_ros_setup` | GoogleTest can initialize ROS 2 through `rclcpp` and create a C++ node. |
| `python_ros_setup` | Pytest can initialize ROS 2 through `rclpy` and create a Python node. |
| `cpp_python_pubsub` | A Python subscriber receives the expected message from a C++ publisher. |

Look for all three named checks in the test output. If colcon reports zero packages, run `colcon list --base-paths /ros_ws/packages` to confirm the package is discoverable. If CMake reports a missing dependency, check that you started the Jazzy container and use the dependencies declared in the package's `package.xml`.

Once these checks pass, follow [Create a ROS 2 Package](../create-ros-package.md) to add a package to the workspace.
