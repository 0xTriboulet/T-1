# Directories
SRCDIR := ./src
BUILDDIR := ./build
INCDIR := ./inc

# Compiler and flags
CXX := x86_64-w64-mingw32-g++
CXXFLAGS := -I$(INCDIR) -Wall -Wextra -std=c++23 -O1 -Wno-missing-field-initializers -Wno-ignored-qualifiers -DDEBUG
LDFLAGS := -L$(INCDIR) -lntdll -luser32 -lkernel32

# Target executable
TARGET := $(BUILDDIR)/T-70.exe

# Source files
SRCS := $(wildcard $(SRCDIR)/*.cxx)

# Object files
OBJS := $(SRCS:$(SRCDIR)/%.cxx=$(BUILDDIR)/%.o)

# Rules
all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) $(LDFLAGS) -o $@
	rm -f $(BUILDDIR)/*.o

$(BUILDDIR)/%.o: $(SRCDIR)/%.cxx
	@mkdir -p $(BUILDDIR)
	$(CXX) $(CXXFLAGS) -c -o $@ $<

clean:
	rm -rf $(BUILDDIR)

.PHONY: all clean
