
# Set defaults
EXEEXT := .exe

# Windows-specific settings
ifeq ($(OS), Windows_NT)
	# Directories
	SRCDIR := .\src
	BUILDDIR := .\build
	INCDIR := .\inc
	WILD_OBJ := \*.o

	CXX := x86_64-w64-mingw32-g++
	CXXFLAGS := -I$(INCDIR) -Wall -Wextra -std=c++23 -O1 -Wno-missing-field-initializers -Wno-ignored-qualifiers -DDEBUG
	LDFLAGS := -L$(INCDIR) -luser32 -lkernel32 -loleaut32 -lwbemuuid -lole32
	MKDIR := if not exist "$(BUILDDIR)" mkdir "$(BUILDDIR)"
	RM := del
else
# Cross-compiling from Linux to Windows

	# Directories
	SRCDIR := ./src
	BUILDDIR := ./build
	INCDIR := ./inc
	WILD_OBJ := /*.o

	CXX := x86_64-w64-mingw32-g++
	CXXFLAGS := -I$(INCDIR) -Wall -Wextra -std=c++23 -O1 -static -Wno-missing-field-initializers -Wno-ignored-qualifiers -DDEBUG -s
	LDFLAGS := -L$(INCDIR) -lntdll -luser32 -lkernel32 -loleaut32 -lwbemuuid -lole32 -s
	MKDIR := mkdir -p $(BUILDDIR)
	RM := rm -f
endif

# Target executable
TARGET := $(BUILDDIR)/T-1$(EXEEXT)

# Source files
SRCS := $(wildcard $(SRCDIR)/*.cxx)

# Object files
OBJS := $(SRCS:$(SRCDIR)/%.cxx=$(BUILDDIR)/%.o)

# Rules
all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) $(LDFLAGS) -o $@
	$(RM) $(BUILDDIR)\*.o

$(BUILDDIR)/%.o: $(SRCDIR)/%.cxx
	$(MKDIR)
	$(CXX) $(CXXFLAGS) -c -o $@ $<

clean:
	$(RM) $(BUILDDIR)$(WILD_OBJ)

.PHONY: all clean
