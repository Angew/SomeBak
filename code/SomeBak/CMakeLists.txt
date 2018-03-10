add_executable(SomeBak
	src/common.hpp
	src/main.cpp
	src/Archive.cpp
	src/Program.cpp
	src/RuleDatabase.cpp
)
TargetAddHeaders(SomeBak
	src/Archive
	src/Program
	src/RuleDatabase
)
target_include_directories(SomeBak PRIVATE ${Boost_INCLUDE_DIRS})
