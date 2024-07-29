## EECS 281 Advanced Makefile

# How to use this Makefile...
###################
###################
##               ##
##  $ make help  ##
##               ##
###################
###################

# IMPORTANT NOTES:
#   1. Set EXECUTABLE to the command name from the project specification.
#   2. To enable automatic creation of unit test rules, your program logic
#      (where main() is) should be in a file named project*.cpp or
#      specified in the PROJECTFILE variable.
#   3. Files you want to include in your final submission cannot match the
#      test*.cpp pattern.

# Change 'executable' to match the command name given in the project spec.
EXECUTABLE  = letter

# The following line looks for a project's main() in files named project*.cpp,
# executable.cpp (substituted from EXECUTABLE above), or main.cpp
PROJECTFILE = $(or $(wildcard project*.cpp $(EXECUTABLE).cpp), main.cpp)
# If main() is in another file delete line above, edit and uncomment below
#PROJECTFILE = mymainfile.cpp

# designate which compiler to use
CXX         = g++

# rule for creating objects
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $*.cpp

# list of test drivers (with main()) for development
TESTSOURCES = $(wildcard test*.cpp)

# list of sources used in project
SOURCES     = $(wildcard *.cpp)
SOURCES     := $(filter-out $(TESTSOURCES), $(SOURCES))
# list of objects used in project
OBJECTS     = $(SOURCES:%.cpp=%.o)

# Default Flags
CXXFLAGS = -std=c++17 -Wconversion -Wall -Werror -Wextra -pedantic

# make debug - will compile sources with $(CXXFLAGS) -g3 and -fsanitize
#              flags also defines DEBUG and _GLIBCXX_DEBUG
debug: CXXFLAGS += -g3 -DDEBUG -fsanitize=address -fsanitize=undefined -D_GLIBCXX_DEBUG
debug:
	$(CXX) $(CXXFLAGS) $(SOURCES) -o $(EXECUTABLE)_debug
.PHONY: debug

# make release - will compile sources with $(CXXFLAGS) and the -O3 flag also
#                defines NDEBUG so that asserts will not check
release: CXXFLAGS += -O3 -DNDEBUG
release: $(EXECUTABLE)
.PHONY: release

# make valgrind - will compile sources with $(CXXFLAGS) -g3 suitable for
#                 CAEN or WSL (DOES NOT WORK ON MACOS).
valgrind: CXXFLAGS += -g3
valgrind:
	$(CXX) $(CXXFLAGS) $(SOURCES) -o $(EXECUTABLE)_valgrind
.PHONY: valgrind

# make profile - will compile "all" with $(CXXFLAGS) and the -g3 and -O3 flags
profile: CXXFLAGS += -g3 -O3
profile:
	$(CXX) $(CXXFLAGS) $(SOURCES) -o $(EXECUTABLE)_profile
.PHONY: profile

# make gprof - will compile "all" with $(CXXFLAGS) and the -pg (for gprof)
gprof: CXXFLAGS += -pg
gprof:
	$(CXX) $(CXXFLAGS) $(SOURCES) -o $(EXECUTABLE)_profile
.PHONY: gprof

# make static - will perform static analysis in the matter currently used
#               on the autograder
static:
	cppcheck --enable=all --suppress=missingIncludeSystem \
      $(SOURCES) *.h *.hpp
.PHONY: static

# Build all executables
all: debug release
all: profile valgrind
.PHONY: all

$(EXECUTABLE): $(OBJECTS)
ifneq ($(EXECUTABLE), executable)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $(EXECUTABLE)
else
	@echo Edit EXECUTABLE variable in Makefile.
	@echo Using default a.out.
	$(CXX) $(CXXFLAGS) $(OBJECTS)
endif

# names of test executables
TESTS       = $(TESTSOURCES:%.cpp=%)
# Automatically generate any build rules for test*.cpp files
define make_tests
    ifeq ($$(PROJECTFILE),)
	    @echo Edit PROJECTFILE variable to .cpp file with main\(\)
	    @exit 1
    endif
    SRCS = $$(filter-out $$(PROJECTFILE), $$(SOURCES))
    OBJS = $$(SRCS:%.cpp=%.o)
    HDRS = $$(wildcard *.h *.hpp)
    $(1): CXXFLAGS += -g3 -DDEBUG
    $(1): $$(OBJS) $$(HDRS) $(1).cpp
	$$(CXX) $$(CXXFLAGS) $$(OBJS) $(1).cpp -o $(1)
endef
$(foreach test, $(TESTS), $(eval $(call make_tests, $(test))))

alltests: $(TESTS)
.PHONY: alltests

# make clean - remove .o files, executables, tarball
clean:
	rm -Rf *.dSYM
	rm -f $(OBJECTS) $(EXECUTABLE) $(EXECUTABLE)_debug
	rm -f $(EXECUTABLE)_valgrind $(EXECUTABLE)_profile $(TESTS) perf.data* \
      $(PARTIAL_SUBMITFILE) $(FULL_SUBMITFILE) $(UNGRADED_SUBMITFILE)
.PHONY: clean

# Files that should not be included in a tarball
EXCLUDE_FILES = getopt.\?



define MAKEFILE_HELP
EECS281 Advanced Makefile Help
* This Makefile uses advanced techniques, for more information:
    $$ man make

* General usage
    1. Follow directions at each "TODO" in this file.
       a. Set EXECUTABLE equal to the name from the project specification.
       b. Set PROJECTFILE equal to the name of the source file with main()
       c. Add any dependency rules specific to your files.
    2. Build, test, submit... repeat as necessary.

* Preparing submissions
    A) To build 'partialsubmit.tar.gz', a tarball without tests used to
       find buggy solutions in the autograder.

           *** USE THIS ONLY FOR TESTING YOUR SOLUTION! ***

       This is useful for faster autograder runs during development and
       free submissions if the project does not build.
           $$ make partialsubmit
    B) Build 'fullsubmit.tar.gz' a tarball complete with autograder test
       files.

           *** ALWAYS USE THIS FOR FINAL GRADING! ***

       It is also useful when trying to find buggy solutions in the
       autograder.
           $$ make fullsubmit

* Unit testing support
    A) Source files for unit testing should be named test*.cpp.  Examples
       include test_input.cpp or test3.cpp.
    B) Automatic build rules are generated to support the following:
           $$ make test_input
           $$ make test3
           $$ make alltests        (this builds all test drivers)
    C) If test drivers need special dependencies, they must be added
       manually.
    D) IMPORTANT: NO SOURCE FILES WITH NAMES THAT BEGIN WITH test WILL BE
       ADDED TO ANY SUBMISSION TARBALLS.

* Static Analysis support
    A) Matches current autograder style grading tests
    B) Usage:
           $$ make static

* Sync to CAEN support
    A) Requires an .ssh/config file with a login.engin.umich.edu host
       defined, SSH Multiplexing enabled, and an open SSH connection.
    B) Edit the REMOTE_BASEDIR variable if default is not preferred.
    C) Usage:
           $$ make sync2caen
endef
export MAKEFILE_HELP

help:
	@echo "$$MAKEFILE_HELP"
.PHONY: help

#######################
# TODO (begin) #
#######################
# individual dependencies for objects
# Examples:
# "Add a header file dependency"
# project2.o: project2.cpp project2.h
#
# "Add multiple headers and a separate class"
# HEADERS = some.h special.h header.h files.h
# myclass.o: myclass.cpp myclass.h $(HEADERS)
# project5.o: project5.cpp myclass.o $(HEADERS)
#
# SOME EXAMPLES
#
#test_thing: test_thing.cpp class.o functions.o
#class.o: class.cpp class.h
#functions.o: functions.cpp functions.h
#project0.o: project0.cpp class.h functions.h
#
# THE COMPILER CAN GENERATE DEPENDENCIES FROM SOURCE CODE
#
# % g++ -std=c++17 -MM *.cpp
#
# ADD YOUR OWN DEPENDENCIES HERE

######################
# TODO (end) #
######################
