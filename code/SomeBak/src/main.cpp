#include "common.hpp"

#include "RuleDatabase.hpp"
#include "Program.hpp"


class MockRulesDatabase : public SomeBak::RuleDatabase
{
	boost::iterator_range<const SomeBak::DirectoryRules*> getDirectories() const override
	{
		return { nullptr, nullptr };
	}
};



int main()
{
	SomeBak::Program program;

	MockRulesDatabase rulesDatabase;

	program.compileArchive(rulesDatabase);
}
