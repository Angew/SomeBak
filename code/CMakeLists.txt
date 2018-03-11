cmake_minimum_required(VERSION 3.10)
project(SomeBak)

function(TargetAddHeaders Target)
	foreach(Header IN LISTS ARGN)
		target_sources(${Target} PRIVATE
			${Header}.hh
			${Header}.hpp
			${Header}.hxx
		)
	endforeach()
endfunction()

add_subdirectory(SomeBak)
