#pragma once

#include "FileArtefact.hxx"

#include <boost/iterator/iterator_categories.hpp>

#include <boost/range/any_range.hpp>

#include <memory>
#include <string>
#include <string_view>
#include <vector>


namespace SomeBak
{

class FileRule
{
public:
	enum class Type
	{
		Including,
		Excluding
	};

private:
	Type mType;

protected:
	FileRule(Type type) : mType{type}
	{}

public:
	static std::unique_ptr<FileRule> createGlobRule(Type type, std::string pattern);

	virtual bool matchesName(std::string_view filename) const = 0;

	virtual bool isIncluding() const
	{ return mType == Type::Including; }
};


class DirectoryRules
{
	std::string mSourcePath;
	std::string mTargetPath;
	std::vector<std::unique_ptr<FileRule>> mFileRules;

public:
	std::string getSourcePath() const
	{ return mSourcePath; }

	template <class T_FilenameRange>
	std::vector<FileArtefact> listFileArtefacts(const T_FilenameRange &filenames) const
	{
		std::vector<FileArtefact> artefacts;
		for (const auto& filename : filenames) {
			if (nameMatchesRules(filename)) {
				artefacts.emplace_back(combinePath(mSourcePath, filename), combinePath(mTargetPath, filename));
			}
		}
		return artefacts;
	}

	bool nameMatchesRules(std::string_view filename) const;
};



class RuleDatabase
{
public:
	std::string getSourcePath() const;
	boost::any_range<const DirectoryRules, boost::forward_traversal_tag> getDirectories() const;
};

}	// namespace SomeBak
