"""Check that a Python ROS node can receive a C++ node's message."""

import os
import subprocess
from uuid import uuid4

import rclpy
from rclpy.task import Future
from std_msgs.msg import String


def test_receives_cpp_message():
    """Receive the expected message from the C++ publisher."""
    topic = f"/sar_setup_check_{uuid4().hex}"
    received = Future()

    rclpy.init()
    try:
        node = rclpy.create_node("sar_setup_subscriber")
        node.create_subscription(
            String, topic, lambda msg: received.set_result(msg.data), 10
        )

        with subprocess.Popen(
            [
                os.environ["SAR_TEST_PUBLISHER"],
                "--ros-args",
                "-r",
                f"sar_setup_check:={topic}",
            ]
        ) as publisher:
            try:
                rclpy.spin_until_future_complete(node, received, timeout_sec=5.0)
                assert received.done(), "No message received from C++ within 5 seconds"
                assert received.result() == "hello from C++"
            finally:
                publisher.kill()
    finally:
        rclpy.shutdown()