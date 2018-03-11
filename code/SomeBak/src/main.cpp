#include "common.hpp"

#include "ArchiveDatabase.hpp"
#include "RuleDatabase.hpp"
#include "Program.hpp"


class MockArchiveDatabase : public SomeBak::ArchiveDatabase
{
	bool needsArchiving(const SomeBak::FileArtefact &/*artefact*/) const override
	{
		return true;
	}
};



int main()
{
	SomeBak::Program program;

	MockArchiveDatabase archiveDatabase;
	SomeBak::RuleDatabase ruleDatabase;

	program.compileArchive(ruleDatabase, archiveDatabase);
}
