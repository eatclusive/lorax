# Define the compiler
CXX = g++

# Define compiler flags
CXXFLAGS = -Wall -g

# Define the target executable
TARGET = my_program

# Define the source files
SRCS = gui.cpp

# Define the object files
OBJS = $(SRCS:.cpp=.o)

# The default rule
all: $(TARGET)

# Rule to link the object files to create the executable
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

# Rule to compile source files into object files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean up build files
clean:
	rm -f $(OBJS) $(TARGET)