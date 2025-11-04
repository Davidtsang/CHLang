// runtime/ChronoString.cpp

#include "ChronoString.h" 
#include "ChronoInt.h"


#include <string>
#include <algorithm> // for ::toupper


ChronoInt* ChronoString::length() const {
    //  ChronoInt::create()
    return ChronoInt::create(static_cast<int32_t>(m_value.length()));
}

ChronoString* ChronoString::toUpper() const {
    std::string upper_s = m_value;
    std::transform(upper_s.begin(), upper_s.end(), upper_s.begin(), ::toupper);
    return ChronoString::create(upper_s);
}