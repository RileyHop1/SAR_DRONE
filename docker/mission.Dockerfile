#Grabs the base image for ros2, other imporant packages will need to be added later.
FROM ros:jazzy-ros-base-noble


SHELL ["/bin/bash", "-c"]
WORKDIR /ros_ws


COPY packages/ src/

RUN source /opt/ros/jazzy/setup.bash \
    && apt-get update \
    && rosdep update \
    && rosdep install --from-paths src --ignore-src -y \
    && rm -rf /var/lib/apt/lists/*

RUN source /opt/ros/jazzy/setup.bash \
    && colcon build

CMD ["bash"]