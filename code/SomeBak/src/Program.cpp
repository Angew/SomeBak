#include "common.hpp"

#include "Program.hpp"

#include "Archive.hpp"
#include "RuleDatabase.hpp"


namespace SomeBak
{

void Program::compileIntoArchive(const DirectoryRules &dir, Archive &archive)
{

}
//--------------------------------------------------------------------------------------------------
void Program::compileArchive(const RuleDatabase &rules)
{
	Archive archive;
	for (const auto &dir : rules.getDirectories()) {
		compileIntoArchive(dir, archive);
	}
}

}	//namespace SomeBak
