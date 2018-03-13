#pragma once

#include <string>


namespace SomeBak {

class FileArtefact
{
	std::string mSourcePath;
	std::string mTargetPath;

public:
	FileArtefact(std::string sourcePath, std::string targetPath) :
		mSourcePath{std::move(sourcePath)},
		mTargetPath{std::move(targetPath)}
	{}
};

}	//namespace SomeBak
