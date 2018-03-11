#pragma once


#include "FileArtefact.hh"


namespace SomeBak {

class ArchiveDatabase
{
public:
	virtual bool needsArchiving(const FileArtefact &artefact) const = 0;
};

}	//namespace SomeBak
