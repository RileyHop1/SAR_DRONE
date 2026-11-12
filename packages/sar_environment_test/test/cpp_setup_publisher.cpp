#include <chrono>
#include <memory>

#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>


int main(int argc, char ** argv) {
    rclcpp::init(argc, argv);

    auto node = std::make_shared<rclcpp::Node>("sar_setup_publisher");
    auto publisher = node->create_publisher<std_msgs::msg::String>("sar_setup_check", 10);

    auto timer = node->create_wall_timer(
        std::chrono::milliseconds(100), [&publisher](){
            std_msgs::msg::String message;
            message.data = "hello from C++";
            publisher->publish(message);
        }
    );

    rclcpp::spin(node);
    rclcpp::shutdown();

    return 0;
}