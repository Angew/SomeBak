#pragma once

#include "FileArtefact.hxx"

#include "boost/iterator/iterator_categories.hpp"

#include "boost/range/any_range.hpp"

#include <vector>


namespace SomeBak
{

class DirectoryRules
{
public:
	std::vector<FileArtefact> listFileArtefacts() const;
};



class RuleDatabase
{
public:
	boost::any_range<const DirectoryRules, boost::forward_traversal_tag> getDirectories() const;
};

}	// namespace SomeBak
