#include <memory>
#include <gtest/gtest.h>
#include <rclcpp/rclcpp.hpp>

TEST(CppRosSetup, CreatesNode) {
    auto context = std::make_shared<rclcpp::Context>();
    context->init(0, nullptr);

    rclcpp::NodeOptions options;
    options.context(context);

    {
        auto node = std::make_shared<rclcpp::Node>("sar_cpp_setup_test", options);
        EXPECT_STREQ(node->get_name(), "sar_cpp_setup_test");
    }

    context->shutdown("C++ setup test complete");

}