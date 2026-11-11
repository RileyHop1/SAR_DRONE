# Software Roadmap

Working draft for JDR-39. Updated November 11, 2026.

Our baseline goal is to execute a planned search, detect a possible person, and report their estimated ground location. Adaptive search planning is a stretch goal.

The six goals discussed by the team are grouped into three sections below. We will expand their expectations, dependencies, verification, owners, and dates as we work through the plan.

Follow the [software development conventions](software-development-conventions.md) and [C++ conventions](cpp-conventions.md).

## 1. Development foundation and ROS setup

Establish a repeatable way for the team to develop, check, build, and run the software.

### Already established

- Created the repository and documented the intended package and deployment layout.
- Created the Pi mission Dockerfile using ROS 2 Jazzy on Ubuntu 24.04, including package copying, dependency installation, and colcon build steps.
- Wrote the GitHub Actions workflow to build an ARM64 Pi image on pushes to `main`, check the ROS CLI, and publish a commit-tagged image to GitHub Container Registry (GHCR).
- Documented the initial onboard architecture in JDR-32 and recorded C++ style conventions.

Successful image building and publishing still need verified run evidence. The ROS CLI check establishes that the CLI starts.

### Work to plan

- Configure tests and lint checks as merge requirements for `Development`, and recheck them before merging into `main`.
- Set up GoogleTest for C++ and agree on Python testing.
- Agree on linting and formatting tools, versions, rules, and generated-code exceptions.
- Provide simple local check, format, and test commands, plus shared VS Code configuration.
- Configure Pi, Jetson, and laptop development environments and dependencies.
- Establish package structure, launch configuration, and basic ROS publisher/subscriber communication.
- Document teammate setup and how to reproduce CI checks locally.

### Proposals and open decisions

- Proposed tools are clang-tidy, clang-format, ament_cmake_gtest, pytest, and Ruff.
- Candidate local commands are `make lint`, `make format`, and `make test`.
- Define package ownership, platform compatibility, and how dependencies are pinned.

The initial completion expectation is that a teammate can build the project, run its checks, and demonstrate basic ROS communication using the documented steps.

## 2. Simulation and SAR interfaces

Establish simulation before depending on it to validate mission behavior. Interface design can proceed alongside simulation setup.

### Work to plan

- Bring up Gazebo and PX4 SITL on the development laptop and connect ROS 2.
- Demonstrate basic simulated flight commands and telemetry first.
- Add simulated cameras and target detection in a later increment.
- Define interfaces for search requests, progress, detections, flight requests, and results.
- Choose topics, services, or actions according to each interaction's requirements.
- Agree on message fields, units, coordinate frames, timestamps, synchronization, and error behavior.
- Create initial nodes with synthetic inputs and repeatable launch commands.
- Add ROS integration tests and reusable simulation scenarios.

### Open decisions

- Which basic flight scenario proves the simulation connection works?
- Which interfaces are needed for that first scenario?
- How will simulated and recorded inputs exercise the same interfaces as hardware?

The initial completion expectation is a reproducible simulated flight with ROS commands and telemetry, followed by tested initial SAR interfaces. Hardware communication and camera-access checks can proceed early to expose integration problems.

## 3. Baseline SAR mission and onboard integration

Build and verify the search mission, then demonstrate the complete flow on the aircraft.

### Work to plan

- Implement search-area input, mission states, search execution, interruption, progress, and completion.
- Integrate RGB and thermal perception and candidate detections.
- Decide ownership of ground-location estimation and define its required calibration, pose, camera pointing, and ground reference.
- Define the operator report and evaluate detection performance and location error.
- Run packages on the Pi and Jetson and integrate the physical cameras and Pixhawk.
- Confirm Ethernet switch ports and video routing, and establish the Pi–Pixhawk UART link through TELEM2.
- Define logs, recordings, fault reporting, storage limits, and software version identification.
- Develop the Pi's systemd-based image update process and agree on the Jetson deployment process.
- Test startup, communication loss, recovery, and progression from bench testing to controlled flight.
- Keep adding unit, integration, simulation, and hardware tests as behavior is implemented.

### Deployment decisions

- How does the Pi discover an approved GHCR tag or digest, and what triggers an update check?
- How are Pi and Jetson releases kept compatible?
- How are registry access and downloads configured?
- How do we confirm the aircraft is grounded, disarmed, and outside an active mission before activation?
- What health checks confirm success, and what triggers rollback?
- How do updates recover from interrupted downloads, unavailable networking, power loss, or application failure?

### Open acceptance decisions

- Agree on the demo deadline and team capacity.
- Define acceptable detection performance and target-location error.
- Select the operator reporting interface.
- Define the evidence required before progressing from simulation to bench testing and flight.

The completion expectation is a demonstrated baseline SAR mission against agreed acceptance criteria. Adaptive replanning can follow once the baseline is verified.

For each section, agree on its detailed expectations and dependencies before assigning milestones and creating implementation tickets.
