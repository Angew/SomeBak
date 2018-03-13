#pragma once


#include <QByteArray>
#include <QString>
#include <QStringList>

#include <cassert>
#include <limits>
#include <string>
#include <string_view>
#include <type_traits>


namespace SomeBak {

namespace SomeBakImpl {

template <class D, class S>
D size_cast(S arg, std::true_type)
{
	static_assert(std::is_unsigned_v<D>, "size_cast must convert between signed and unsigned");
	assert(arg >=0 );
	return static_cast<D>(arg);
}
//--------------------------------------------------------------------------------------------------
template <class D, class S>
D size_cast(S arg, std::false_type)
{
	static_assert(std::is_signed_v<D>, "size_cast must convert between signed and unsigned");
	assert(arg <= static_cast<S>(std::numeric_limits<D>::max()));
	return static_cast<D>(arg);
}

} //namespace SomeBakImpl



template <class D, class S>
D size_cast(S arg)
{
	return SomeBakImpl::size_cast<D>(arg, typename std::is_signed<S>::type{});
}
//--------------------------------------------------------------------------------------------------
inline bool isFilesystemCaseSensitive()
{
#ifdef WIN32
	return false;
#else
	return true;
#endif
}
//--------------------------------------------------------------------------------------------------
inline QString qStringFromStdString(std::string_view src)
{
	return QString::fromUtf8(src.data(), size_cast<int>(src.size()));
}
//--------------------------------------------------------------------------------------------------
inline QString qStringFromStdString(const std::string &src)
{
	return qStringFromStdString(std::string_view{src.data(), src.size()});
}
//--------------------------------------------------------------------------------------------------
inline std::string stdStringFromQString(const QString &src)
{
	auto data = src.toUtf8();
	return { data.data(), size_cast<size_t>(data.size()) };
}
//--------------------------------------------------------------------------------------------------
template <class... T>
std::string combinePath(const T&... arg)
{
#ifdef CXXSTD_NO_FOLD_EXPRESSIONS
	QStringList list;
	int fold[] = { 0, (list << qStringFromStdString(arg), 0)... };
#else
	auto list = QStringList{} << ... << qStringFromStdString(arg);
#endif
	return stdStringFromQString(list.join("/"));
}

} //namespace SomeBak
