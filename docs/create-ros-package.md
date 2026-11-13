# Create a ROS 2 Package

Start with [Start ROS 2 Jazzy](environment/ros-jazzy.md) and [Verify Your Environment](environment/verify.md). Run the commands below inside the Jazzy container from `/ros_ws`, the mounted repository root. The repository keeps package sources in `packages/`.

## Choose the name and build type

Use a short, lowercase name with underscores and the `sar_` prefix, such as `sar_status`. Name the package after its responsibility and check whether an existing package already owns that work.

- Use `ament_cmake` for C++ or a package that builds C++ and registers Python tests, like `sar_environment_test`.
- Use `ament_python` for a Python-only package that uses setuptools.

## Generate the package

Choose one command. Both examples use the same package name. Replace the example package and node names with yours.

**C++**

```bash
cd /ros_ws
ros2 pkg create --destination-directory packages --build-type ament_cmake \
  --node-name status_node sar_status --dependencies rclcpp
```

**Python**

```bash
cd /ros_ws
ros2 pkg create --destination-directory packages --build-type ament_python \
  --node-name status_node sar_status --dependencies rclpy
```

- `ros2 pkg create` generates the package skeleton.
- `--destination-directory packages` puts it under the repo's source directory.
- `--build-type` selects the build system.
- `--node-name status_node` adds a starter executable for the validation below. Omit it for a package that only provides a library, interfaces, or tests.
- `sar_status` is the package name. `--dependencies` adds the client library dependency to the generated package.

## Review the generated files

| File | What to review |
| --- | --- |
| `package.xml` | Set the description, maintainer name and email, and project-approved license. Add actual build, runtime, and test dependencies. Keep the exported build type aligned with the package. |
| `CMakeLists.txt` (C++) | Check the executable target, library dependencies, and install destination under `lib/${PROJECT_NAME}` so `ros2 run` can find it. Register tests inside `if(BUILD_TESTING)`. |
| `setup.py` (Python) | Check the package metadata and the `console_scripts` entry that maps the executable name to the module's `main` function. Keep metadata consistent with `package.xml`. |
| `setup.cfg` (Python) | Keep the generated script installation settings so `ros2 run` can find the executable. |
| `src/` (C++) or `sar_status/` (Python) | Put implementation code here. Use `test/` for package tests. |

Follow the [software development conventions](software-development-conventions.md) when defining interfaces and writing tests. Use the [C++ conventions](cpp-conventions.md) or [Python conventions](python-conventions.md) for the implementation.

## Build and verify

Run these commands one at a time from `/ros_ws`. Stop if a command fails.

```bash
colcon list --base-paths packages
colcon build --base-paths packages --packages-up-to sar_status
source install/setup.bash
ros2 pkg prefix sar_status
ros2 run sar_status status_node
```

1. `colcon list` searches `packages/` and should list the new package.
2. `colcon build` builds the package and any workspace dependencies selected by `--packages-up-to`. If a dependency is missing, declare it in `package.xml` and install it in the container before rebuilding.
3. `source install/setup.bash` loads the workspace into the current terminal.
4. `ros2 pkg prefix` prints the package's install location. For a library or test-only package, use this check and run any registered tests.
5. `ros2 run` starts the generated executable. Expect the starter greeting. Stop a node that continues running with **Ctrl+C**.

For a package with registered tests, run the package's checks and inspect the results.

```bash
colcon test --base-paths packages --packages-select sar_status \
  --return-code-on-test-failure
colcon test-result --verbose
```

`--packages-select` runs checks for the named package. `--return-code-on-test-failure` gives the test command a nonzero exit code on failure. `test-result --verbose` prints the recorded results and failure details. Confirm the intended tests ran before reviewing the result.

See the upstream [ROS 2 Jazzy package creation tutorial](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html) for more examples.
