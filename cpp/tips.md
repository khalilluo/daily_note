dynamic_cast是使用typeid获取对象真正类型来转换，基类需包含虚函数



如果整数类型具有固定宽度需要从，利用类型<cstdint>报头，但请注意，它可选的实施方式中的标准品牌支持精确宽类型int8_t，int16_t，int32_t，int64_t，intptr_t，uint8_t，uint16_t，uint32_t，uint64_t和uintptr_t。



queue拿出front时使用右值，如果马上pop的话内容可能错乱