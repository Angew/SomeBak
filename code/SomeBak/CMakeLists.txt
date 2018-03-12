find_package(Boost REQUIRED)
find_package(Qt4 REQUIRED QtCore)

add_executable(SomeBak
	src/common.hpp
	src/main.cpp
	src/Archive.cpp
	src/ArchiveDatabase.cpp
	src/FileArtefact.cpp
	src/Program.cpp
	src/RuleDatabase.cpp
	src/Utility.cpp
)
TargetAddHeaders(SomeBak
	src/Archive
	src/ArchiveDatabase
	src/FileArtefact
	src/Program
	src/RuleDatabase
	src/Utility
)
target_include_directories(SomeBak PRIVATE ${Boost_INCLUDE_DIRS})
target_link_libraries(SomeBak PRIVATE Qt4::QtCore)
target_compile_features(SomeBak PRIVATE cxx_std_17)
