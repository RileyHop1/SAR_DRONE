"""Verify that Python can create a node."""

import rclpy
from rclpy.context import Context


def test_creates_node():
    context = Context();
    rclpy.init(context=context)

    try:
        node = rclpy.create_node("sar_python_setup_test", context=context)
        try:
            assert node.get_name() == "sar_python_setup_test"
        finally:
            node.destroy_node()

    finally:
        rclpy.shutdown(context=context)