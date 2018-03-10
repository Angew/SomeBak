#pragma once

#include "boost/range/iterator_range.hpp"


namespace SomeBak
{

class DirectoryRules
{
};

class RuleDatabase
{
public:
	virtual boost::iterator_range<const DirectoryRules*> getDirectories() const = 0;
};

}	// namespace SomeBak
