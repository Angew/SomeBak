#include "common.hpp"

#include "Program.hpp"

#include "Archive.hpp"
#include "ArchiveDatabase.hpp"
#include "RuleDatabase.hpp"
#include "Utility.hpp"

#include <QDir>

#include <boost/range/adaptor/transformed.hpp>


namespace SomeBak
{

void Program::compileIntoArchive(const DirectoryRules &dirRules, const ArchiveDatabase &archiveDatabase, Archive &archive)
{
	QDir dir(QString::fromStdString(dirRules.getSourcePath()));
	const auto entries = dir.entryList(QDir::Files);
	for (const auto& artefact : dirRules.listFileArtefacts(entries | boost::adaptors::transformed(stdStringFromQString))) {
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
