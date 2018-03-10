#pragma once


#include "Archive.hh"
#include "RuleDatabase.hh"


namespace SomeBak
{

class Program
{
	void compileIntoArchive(const DirectoryRules &dir, Archive &archive);

public:
	void compileArchive(const RuleDatabase &rules);
};

}	// namespace SomeBak
