#pragma once


#include <QByteArray>
#include <QString>

#include <string>


namespace SomeBak {

inline std::string stdStringFromQString(const QString &src)
{
	auto data = src.toUtf8();
	return { data.data(), data.size() };
}

} //namespace SomeBak
