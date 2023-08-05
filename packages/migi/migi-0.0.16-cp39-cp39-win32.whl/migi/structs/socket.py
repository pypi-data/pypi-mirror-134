from ctypes import c_uint16, c_char, POINTER, Structure, Union, c_uint32, c_uint8


class SockAddr(Structure):
    _fields_ = [
            ('sa_family', c_uint16),
            ('sa_data', c_char * 14),
    ]


class SUnionB(Structure):
    _fields_ = [
        ('s_b1', c_uint8),
        ('s_b2', c_uint8),
        ('s_b3', c_uint8),
        ('s_b4', c_uint8)
    ]


class SUnionW(Structure):
    _fields_ = [
        ('s_w1', c_uint16),
        ('s_w2', c_uint16)
    ]


class InAddr(Union):
    _fields_ = [
        ('S_addr', c_uint32),
        ('S_un_w', SUnionW),
        ('S_un_b', SUnionB)
    ]


class In6Addr(Union):
    _fields_ = [
        ('Byte', c_uint8 * 16),
        ('Word', c_uint16 * 8)
    ]


class SockAddrIn(Structure):

    _fields_ = [
        ('sin_family', c_uint16),
        ('sin_port', c_uint16),
        ('sin_addr', InAddr),
        ('sin_zero', c_char * 8)
    ]


class SockAddrIn6(Structure):
    _fields_ = [
        ('sin6_family', c_uint16),
        ('sin6_port', c_uint16),
        ('sin6_flowinfo', c_uint32),
        ('sin6_addr', In6Addr)
    ]


sockaddr = SockAddr
sockaddr_p = POINTER(sockaddr)

in_addr = InAddr
in_addr_p = POINTER(in_addr)

sockaddr_in = SockAddrIn
sockaddr_in_p = POINTER(SockAddrIn)

sockaddr_in6 = SockAddrIn6
sockaddr_in6_p = POINTER(sockaddr_in6)

AF_INET = 2
AF_INET6 = 23
