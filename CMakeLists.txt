cmake_minimum_required(VERSION 3.10)
project(ImGuiExample)

set(CMAKE_CXX_STANDARD 11)

# Add sources
file(GLOB SOURCES
    "imgui/*.cpp"
    "imgui/backends/imgui_impl_glfw.cpp"
    "imgui/backends/imgui_impl_opengl3.cpp"
)

add_executable(ImGuiExample main.cpp ${SOURCES})

# Add include directories
include_directories(imgui imgui/backends)

# Link libraries
find_package(OpenGL REQUIRED)
find_package(glfw3 REQUIRED)
target_link_libraries(ImGuiExample glfw OpenGL::GL)

