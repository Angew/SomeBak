#pragma once

#include "FileArtefact.hxx"

#include <boost/iterator/iterator_categories.hpp>

#include <boost/range/any_range.hpp>

#include <string>
#include <vector>


namespace SomeBak
{

class DirectoryRules
{
public:
	std::string getSourcePath() const;

  template <class T_FilenameRange>
	std::vector<FileArtefact> listFileArtefacts(const T_FilenameRange &filenames) const;
};



class RuleDatabase
{
public:
	std::string getSourcePath() const;
	boost::any_range<const DirectoryRules, boost::forward_traversal_tag> getDirectories() const;
};

}	// namespace SomeBak
