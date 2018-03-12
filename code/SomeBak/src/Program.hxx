#pragma once


#include "Archive.hh"
#include "ArchiveDatabase.hh"
#include "RuleDatabase.hh"


namespace SomeBak
{

class Program
{
	void compileIntoArchive(const DirectoryRules &directoryRules, const ArchiveDatabase &archiveDatabase, Archive &archive);

public:
	void compileArchive(const RuleDatabase &rules, const ArchiveDatabase &archiveDatabase);
};

}	// namespace SomeBak
