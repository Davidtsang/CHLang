// runtime/ChronoString.cpp

// �������Լ���ͷ�ļ�
#include "ChronoString.h" 

// �ؼ�������������������� ChronoInt.h
// ��Ϊ�����ṩ�� ChronoInt::create() ����������
#include "ChronoInt.h" 

// (���� C++ ��)
#include <string>
#include <algorithm> // for ::toupper

// --- ����ʵ�� ---

ChronoInt* ChronoString::length() const {
    // �������ǿ��԰�ȫ�ص��� ChronoInt::create()
    return ChronoInt::create(static_cast<int32_t>(m_value.length()));
}

ChronoString* ChronoString::toUpper() const {
    std::string upper_s = m_value;
    std::transform(upper_s.begin(), upper_s.end(), upper_s.begin(), ::toupper);
    return ChronoString::create(upper_s);
}