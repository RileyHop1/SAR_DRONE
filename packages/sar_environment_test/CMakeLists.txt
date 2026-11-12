cmake_minimum_required(VERSION 3.8)
project(sar_environment_test)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)

  find_package(ament_lint_auto REQUIRED)
  find_package(ament_cmake_gtest REQUIRED) 
  find_package(ament_cmake_pytest REQUIRED)
  find_package(rclcpp REQUIRED)

  ament_add_gtest(test_cpp_ros_setup test/test_cpp_ros_setup.cpp)
  ament_add_pytest_test(python_ros_setup test/test_python_ros_setup.py)
  ament_target_dependencies(test_cpp_ros_setup rclcpp)

  find_package(std_msgs REQUIRED)
  add_executable(cpp_setup_publisher test/cpp_setup_publisher.cpp)
  ament_target_dependencies(cpp_setup_publisher rclcpp std_msgs)
  ament_add_pytest_test(cpp_python_pubsub test/test_cpp_python_pubsub.py
    ENV "SAR_TEST_PUBLISHER=$<TARGET_FILE:cpp_setup_publisher>"
    TIMEOUT 20
  )

  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
