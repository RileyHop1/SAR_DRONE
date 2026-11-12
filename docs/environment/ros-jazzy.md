# Start ROS 2 Jazzy

Use the same ROS 2 Jazzy base image as the project's Pi mission Dockerfile to open a development shell. Docker runs the Linux environment, and a bind mount makes your local checkout available inside it.

## Before you start

Complete [Install and Verify Docker](docker.md), then open a terminal at the root of your SAR_DRONE checkout. On macOS, use Terminal and keep Docker Desktop running. On Windows, use the Ubuntu WSL terminal with Docker Desktop integration enabled. On Ubuntu, use your normal terminal and start Docker Engine if needed.

## Start the container

Run this from the repository root on your computer:

```bash
docker run --rm -it \
  --mount "type=bind,source=$PWD,target=/ros_ws" \
  --workdir /ros_ws \
  ros:jazzy-ros-base-noble bash
```

Docker pulls the image on the first run if it is missing locally. The bind mount lets you edit files on your computer and use those same files at `/ros_ws` in the container. If your Ubuntu Docker setup requires administrator access, run the command with `sudo`.

## Check the ROS shell

Run these commands **inside the container**:

```bash
echo "$ROS_DISTRO"
ros2 --help
pwd
```

Expect `jazzy`, the ROS 2 command help, and `/ros_ws`. Type `exit` to return to your computer's shell. Docker removes the container on exit, and changes in the mounted repository persist on your computer.

The ROS package tests will be covered in [Verify Your Environment](verify.md).
