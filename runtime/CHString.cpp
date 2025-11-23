// runtime/CHString.cpp

#include "CHString.h"
#include "CHInt.h"


#include <string>
#include <algorithm> // for ::toupper


CHInt* CHString::length() const {
    //  CHInt::create()
    return CHInt::create(static_cast<int32_t>(m_value.length()));
}

CHString* CHString::toUpper() const {
    std::string upper_s = m_value;
    std::transform(upper_s.begin(), upper_s.end(), upper_s.begin(), ::toupper);
    return CHString::create(upper_s);
}