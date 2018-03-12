#include "common.hpp"

#include "RuleDatabase.hpp"
#include "Utility.hpp"

#include <QRegExp>

#include <boost/range/adaptor/indirected.hpp>



namespace SomeBak {

namespace {

class GlobFileRule : public FileRule
{
	QRegExp mPattern;

public:
	GlobFileRule(Type type, std::string pattern) :
		FileRule{type},
		mPattern{
			qStringFromStdString(pattern),
			isFilesystemCaseSensitive() ? Qt::CaseSensitive : Qt::CaseInsensitive,
			QRegExp::Wildcard
		}
	{}

	bool matchesName(std::string_view filename) const override
	{
		return mPattern.exactMatch(qStringFromStdString(filename));
	}
};

} //namespace



std::unique_ptr<FileRule> FileRule::createGlobRule(Type type, std::string pattern)
{
	return std::make_unique<GlobFileRule>(type, std::move(pattern));
}
//--------------------------------------------------------------------------------------------------
bool DirectoryRules::nameMatchesRules(std::string_view filename) const
{
	bool included = false;
	for (const auto& rule : mFileRules | boost::adaptors::indirected) {
		if (rule.matchesName(filename)) {
			included = rule.isIncluding();
		}
	}
	return included;
}

} //namespace SomeBak
