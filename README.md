# SAR Drone

ROS 2 Jazzy software for an autonomous search-and-rescue drone.

## Architecture

- **Raspberry Pi:** mission management and communication with PX4.
- **Jetson Orin Nano Super:** vision processing using OpenCV and detection models.
- **Pixhawk:** PX4 flight control running on NuttX.
- **Laptop:** development and Gazebo Harmonic simulation.

## Repository Structure

```text
sar-drone/
├── packages/
│   ├── sar_interfaces/    # Shared ROS messages, services, and actions
│   ├── sar_mission/       # Search planning and mission management
│   ├── sar_vision/        # Camera processing and detection
│   ├── sar_px4/           # ROS integration with PX4
│   ├── sar_bringup/       # Launch files and ROS configuration
│   └── sar_simulation/    # Gazebo worlds, models, and simulation setup
├── docker/               # Mission, vision, and simulation Dockerfiles
├── deployment/
│   ├── pi/               # Pi deployment configuration
│   ├── jetson/           # Jetson deployment configuration
│   └── laptop/           # Local simulation configuration
├── firmware/             # PX4 version, parameters, and firmware instructions
├── .github/workflows/    # Automated checks and builds
└── docs/                 # Project documentation
```

## Build and Deployment

GitHub Actions builds and publishes separate mission and vision images from `main`. The Pi and Jetson pull matching releases and activate updates while grounded, disarmed, and outside an active mission.

Laptop simulation reuses the onboard ROS packages with simulated hardware. Pixhawk firmware is built and flashed separately; it is excluded from onboard container images.
