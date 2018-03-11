#include "common.hpp"

#include "Program.hpp"

#include "Archive.hpp"
#include "ArchiveDatabase.hpp"
#include "RuleDatabase.hpp"


namespace SomeBak
{

void Program::compileIntoArchive(const DirectoryRules &dir, const ArchiveDatabase &archiveDatabase, Archive &archive)
{
	for (const auto& artefact : dir.listFileArtefacts()) {
		if (archiveDatabase.needsArchiving(artefact)) {
			archive.add(artefact);
		}
	}
}
//--------------------------------------------------------------------------------------------------
void Program::compileArchive(const RuleDatabase &rules, const ArchiveDatabase &archiveDatabase)
{
	Archive archive;
	for (const auto &dir : rules.getDirectories()) {
		compileIntoArchive(dir, archiveDatabase, archive);
	}
}

}	//namespace SomeBak
