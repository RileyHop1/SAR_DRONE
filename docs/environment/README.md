# Start Here

Use this section to set up a development environment for the SAR drone project. The guides cover macOS, Windows, and Ubuntu. Start on your development computer, where you edit the code and run local checks.

## How the tools fit together

| Tool | What it does |
| --- | --- |
| Git | Gets a local copy of the project and tracks your changes. |
| Docker | Runs the project's Linux environment on your computer. The image supplies the ROS 2 Jazzy base environment. |
| ROS 2 Jazzy | Provides the tools and libraries we use to build and test the project's ROS packages. |
| GitHub Actions | Runs checks on GitHub so teammates can review results before merging. |

Edit the repository with your usual editor. The container guide shows how to mount that checkout so commands inside Linux can use the same files. The verification guide walks through the C++ and Python node checks and a cross-language communication check.

## Setup order

1. [Install and verify Docker](docker.md) to prepare your machine, clone the repository, and check that Docker can start a Linux container.
2. [Start ROS 2 Jazzy](ros-jazzy.md) to open a ROS shell with the project mounted.
3. [Verify your environment](verify.md) to build the environment test package and run the environment checks.
