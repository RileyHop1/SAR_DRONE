# Install and Verify Docker

## Prerequisites

- Use a supported macOS, Windows, or Ubuntu release. Check the platform guide below for requirements and choose an installer that matches your processor.
- Have internet access to download Docker and pull container images. Use a machine where you can install software and enable virtualization if needed.
- Install Git and confirm it works with `git --version`. On Windows, run that check in your Ubuntu WSL terminal once WSL is installed. [Git installation](https://git-scm.com/install/)
- Make sure you can access the SAR_DRONE repository with your GitHub account. A code editor is useful for working on the checkout.

Docker will supply the Linux environment for ROS 2 Jazzy. The checks on this page verify Docker itself. The project container and ROS checks have their own guides.

## macOS

1. Open **Apple menu → About This Mac** and check whether your Mac has an Apple chip or an Intel processor.
2. Download the matching Docker Desktop installer, open the disk image, and drag Docker into **Applications**.
3. Open **Docker** from Applications and finish first-run setup. Wait for Docker Desktop to show that the engine is running.
4. Open Terminal and continue to [Verify Docker](#verify-docker).

[Docker Desktop for Mac](https://docs.docker.com/desktop/setup/install/mac-install/)

## Windows

Use Docker Desktop with its WSL 2 backend. Check Docker's Windows requirements, including hardware virtualization. If WSL and Ubuntu are missing, open PowerShell as administrator and run the command below. Restart if prompted, then open Ubuntu once to finish its initial setup.

```powershell
wsl --install -d Ubuntu
```

1. Install Docker Desktop for Windows and open it from the Start menu.
2. In Docker Desktop settings, enable the WSL 2 engine and enable integration for Ubuntu under **Resources → WSL Integration**. Apply the settings and wait for Docker Desktop to start. Use Linux containers for this project.
3. Open your **Ubuntu WSL terminal** and continue below. Keep your checkout in the Ubuntu home directory so your Git and Docker commands use the same environment.

[Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/) · [Docker Desktop WSL integration](https://docs.docker.com/desktop/features/wsl/) · [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

## Ubuntu

1. Install Docker Engine from Docker's official Ubuntu package repository using the linked guide.
2. Confirm the service is active. If it is stopped, start it and check again.

```bash
sudo systemctl status docker --no-pager
sudo systemctl start docker
```

3. Continue in your Ubuntu terminal. If your Engine installation requires administrator access, run the Docker verification commands below with `sudo`. Follow Docker's post-install guide if your team chooses to set up non-root access.

[Docker Engine for Ubuntu](https://docs.docker.com/engine/install/ubuntu/) · [Linux post-install steps](https://docs.docker.com/engine/install/linux-postinstall/)

## Verify Docker

Run these commands in Terminal on macOS, your Ubuntu WSL terminal on Windows, or your terminal on Ubuntu.

```bash
docker --version
docker info
docker run --rm hello-world
```

- `docker --version` confirms the client command is installed.
- `docker info` should show **Server** information. This confirms the client can reach the running engine.
- `hello-world` should print **Hello from Docker!**. Docker downloads the test image if needed and runs it in a container.

## Get the project checkout

If you already cloned the project, open your existing checkout. Otherwise run these commands from the directory where you keep your projects.

```bash
git clone https://github.com/RileyHop1/SAR_DRONE.git
cd SAR_DRONE
git status --short --branch
```

Git should show the checked-out branch. This directory will be the starting point for the [Jazzy container setup](ros-jazzy.md).

## Troubleshooting

| What you see | What to check |
| --- | --- |
| `docker: command not found` | Finish installation and reopen your terminal. On Windows, confirm integration is enabled for the WSL distribution you are using. |
| Cannot connect to the Docker daemon | Open Docker Desktop on macOS or Windows and wait for the engine to start. On Ubuntu, check `systemctl status docker`. |
| Permission denied on the Docker socket | On Ubuntu Engine, retry with `sudo` or follow the official non-root setup guide above. |
| Image pull times out | Check internet access and whether your network requires a proxy. |
