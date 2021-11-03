#include <string.h>
#include <unordered_map>
#include <iostream>

typedef unsigned char u8;
typedef unsigned int u32;

u8 confusion[512] = {
    0xac, 0xd1, 0x25, 0x94, 0x1f, 0xb3, 0x33, 0x28, 0x7c, 0x2b, 0x17, 0xbc, 0xf6, 0xb0, 0x55, 0x5d,
    0x8f, 0xd2, 0x48, 0xd4, 0xd3, 0x78, 0x62, 0x1a, 0x02, 0xf2, 0x01, 0xc9, 0xaa, 0xf0, 0x83, 0x71,
    0x72, 0x4b, 0x6a, 0xe8, 0xe9, 0x42, 0xc0, 0x53, 0x63, 0x66, 0x13, 0x4a, 0xc1, 0x85, 0xcf, 0x0c,
    0x24, 0x76, 0xa5, 0x6e, 0xd7, 0xa1, 0xec, 0xc6, 0x04, 0xc2, 0xa2, 0x5c, 0x81, 0x92, 0x6c, 0xda,
    0xc6, 0x86, 0xba, 0x4d, 0x39, 0xa0, 0x0e, 0x8c, 0x8a, 0xd0, 0xfe, 0x59, 0x96, 0x49, 0xe6, 0xea,
    0x69, 0x30, 0x52, 0x1c, 0xe0, 0xb2, 0x05, 0x9b, 0x10, 0x03, 0xa8, 0x64, 0x51, 0x97, 0x02, 0x09,
    0x8e, 0xad, 0xf7, 0x36, 0x47, 0xab, 0xce, 0x7f, 0x56, 0xca, 0x00, 0xe3, 0xed, 0xf1, 0x38, 0xd8,
    0x26, 0x1c, 0xdc, 0x35, 0x91, 0x43, 0x2c, 0x74, 0xb4, 0x61, 0x9d, 0x5e, 0xe9, 0x4c, 0xbf, 0x77,
    0x16, 0x1e, 0x21, 0x1d, 0x2d, 0xa9, 0x95, 0xb8, 0xc3, 0x8d, 0xf8, 0xdb, 0x34, 0xe1, 0x84, 0xd6,
    0x0b, 0x23, 0x4e, 0xff, 0x3c, 0x54, 0xa7, 0x78, 0xa4, 0x89, 0x33, 0x6d, 0xfb, 0x79, 0x27, 0xc4,
    0xf9, 0x40, 0x41, 0xdf, 0xc5, 0x82, 0x93, 0xdd, 0xa6, 0xef, 0xcd, 0x8d, 0xa3, 0xae, 0x7a, 0xb6,
    0x2f, 0xfd, 0xbd, 0xe5, 0x98, 0x66, 0xf3, 0x4f, 0x57, 0x88, 0x90, 0x9c, 0x0a, 0x50, 0xe7, 0x15,
    0x7b, 0x58, 0xbc, 0x07, 0x68, 0x3a, 0x5f, 0xee, 0x32, 0x9f, 0xeb, 0xcc, 0x18, 0x8b, 0xe2, 0x57,
    0xb7, 0x49, 0x37, 0xde, 0xf5, 0x99, 0x67, 0x5b, 0x3b, 0xbb, 0x3d, 0xb5, 0x2d, 0x19, 0x2e, 0x0d,
    0x93, 0xfc, 0x7e, 0x06, 0x08, 0xbe, 0x3f, 0xd9, 0x2a, 0x70, 0x9a, 0xc8, 0x7d, 0xd8, 0x46, 0x65,
    0x22, 0xf4, 0xb9, 0xa2, 0x6f, 0x12, 0x1b, 0x14, 0x45, 0xc7, 0x87, 0x31, 0x60, 0x29, 0xf7, 0x73,
    0x2c, 0x97, 0x72, 0xcd, 0x89, 0xa6, 0x88, 0x4c, 0xe8, 0x83, 0xeb, 0x59, 0xca, 0x50, 0x3f, 0x27,
    0x4e, 0xae, 0x43, 0xd5, 0x6e, 0xd0, 0x99, 0x7b, 0x7c, 0x40, 0x0c, 0x52, 0x86, 0xc1, 0x46, 0x12,
    0x5a, 0x28, 0xa8, 0xbb, 0xcb, 0xf0, 0x11, 0x95, 0x26, 0x0d, 0x34, 0x66, 0x22, 0x18, 0x6f, 0x51,
    0x9b, 0x3b, 0xda, 0xec, 0x5e, 0x00, 0x2a, 0xf5, 0x8f, 0x61, 0xba, 0x96, 0xb3, 0xd1, 0x30, 0xdc,
    0x33, 0x75, 0xe9, 0x6d, 0xc8, 0xa1, 0x3a, 0x3e, 0x5f, 0x9d, 0xfd, 0xa9, 0x31, 0x9f, 0xaa, 0x85,
    0x2f, 0x92, 0xaf, 0x67, 0x78, 0xa5, 0xab, 0x03, 0x21, 0x4f, 0xb9, 0xad, 0xfe, 0xf3, 0x42, 0xfc,
    0x17, 0xd7, 0xee, 0xa3, 0xd8, 0x80, 0x14, 0x2e, 0xa0, 0x47, 0x55, 0xc4, 0xff, 0xe5, 0x13, 0x3f,
    0x81, 0xb6, 0x7a, 0x94, 0xd0, 0xb5, 0x54, 0xbf, 0x91, 0xa7, 0x37, 0xf1, 0x6b, 0xc9, 0x1b, 0xb1,
    0x3c, 0xb6, 0xd9, 0x32, 0x24, 0x8d, 0xf2, 0x82, 0xb4, 0xf9, 0xdb, 0x7d, 0x44, 0xfb, 0x1e, 0xd4,
    0xea, 0x5d, 0x35, 0x69, 0x23, 0x71, 0x57, 0x01, 0x06, 0xe4, 0x55, 0x9a, 0xa4, 0x58, 0x56, 0xc7,
    0x4a, 0x8c, 0x8a, 0xd6, 0x6a, 0x49, 0x70, 0xc5, 0x8e, 0x0a, 0x62, 0xdc, 0x29, 0x4b, 0x42, 0x41,
    0xcb, 0x2b, 0xb7, 0xce, 0x08, 0xa1, 0x76, 0x1d, 0x1a, 0xb8, 0xe3, 0xcc, 0x7e, 0x48, 0x20, 0xe6,
    0xf8, 0x45, 0x93, 0xde, 0xc3, 0x63, 0x0f, 0xb0, 0xac, 0x5c, 0xba, 0xdf, 0x07, 0x77, 0xe7, 0x4e,
    0x1f, 0x28, 0x10, 0x6c, 0x59, 0xd3, 0xdd, 0x2d, 0x65, 0x39, 0xb2, 0x74, 0x84, 0x3d, 0xf4, 0xbd,
    0xc7, 0x79, 0x60, 0x0b, 0x4d, 0x33, 0x36, 0x25, 0xbc, 0xe0, 0x09, 0xcf, 0x5b, 0xe2, 0x38, 0x9e,
    0xc0, 0xef, 0xd2, 0x16, 0x05, 0xbe, 0x53, 0xf7, 0xc2, 0xc6, 0xa2, 0x24, 0x98, 0x1c, 0xad, 0x04};

u32 diffusion[32] = {
    0xf26cb481, 0x16a5dc92, 0x3c5ba924, 0x79b65248, 0x2fc64b18, 0x615acd29, 0xc3b59a42, 0x976b2584,
    0x6cf281b4, 0xa51692dc, 0x5b3c24a9, 0xb6794852, 0xc62f184b, 0x5a6129cd, 0xb5c3429a, 0x6b978425,
    0xb481f26c, 0xdc9216a5, 0xa9243c5b, 0x524879b6, 0x4b182fc6, 0xcd29615a, 0x9a42c3b5, 0x2584976b,
    0x81b46cf2, 0x92dca516, 0x24a95b3c, 0x4852b679, 0x184bc62f, 0x29cd5a61, 0x429ab5c3, 0x84256b97};

u8 input[32] = {0};

static u32 diffusioninv[32] = {
    4067210369, 379968658, 1012640036, 2041991752, 801524504, 1633340713, 3283458626, 2540381572,
    1827832244, 2769720028, 1530668201, 3061401682, 3324975179, 1516317133, 3049472666, 1805091877,
    3028415084, 3700561573, 2837724251, 1380481462, 1259876294, 3442041178, 2588066741, 629446507,
    2176085234, 2463933718, 615078716, 1213380217, 407619119, 701323873, 1117435331, 2217044887};

static std::unordered_map<u8, u8> reverseConfuse = {{82, 82}, {185, 242}, {242, 25}, {25, 221}, {221, 167}, {167, 150}, {150, 76}, {76, 125}, {125, 236}, {236, 54}, {54, 99}, {99, 40}, {40, 7}, {7, 195}, {195, 136}, {136, 185}};

static std::unordered_map<u8, u8> reverseConfuse2 = {{175, 82}, {210, 242}, {64, 25}, {61, 221}, {197, 167}, {87, 150}, {49, 76}, {201, 125}, {91, 236}, {42, 54}, {163, 99}, {38, 40}, {76, 7}, {222, 195}, {180, 136}, {184, 185}};

static u8 reverseText[256][2] = {{76, 76}, {184, 185}, {42, 40}, {222, 221}, {163, 167}, {87, 82}, {197, 195}, {49, 54}, {175, 167}, {91, 82}, {201, 195}, {61, 54}, {64, 76}, {180, 185}, {38, 40}, {210, 221}, {38, 54}, {210, 195}, {64, 82}, {180, 167}, {201, 221}, {61, 40}, {175, 185}, {91, 76}, {197, 221}, {49, 40}, {163, 185}, {87, 76}, {42, 54}, {222, 195}, {76, 82}, {184, 167}, {210, 242}, {38, 7}, {180, 150}, {64, 99}, {61, 25}, {201, 236}, {91, 125}, {175, 136}, {49, 25}, {197, 236}, {87, 125}, {163, 136}, {222, 242}, {42, 7}, {184, 150}, {76, 99}, {184, 136}, {76, 125}, {222, 236}, {42, 25}, {87, 99}, {163, 150}, {49, 7}, {197, 242}, {91, 99}, {175, 150}, {61, 7}, {201, 242}, {180, 136}, {64, 125}, {210, 236}, {38, 25}, {61, 125}, {201, 136}, {91, 25}, {175, 236}, {210, 150}, {38, 99}, {180, 242}, {64, 7}, {222, 150}, {42, 99}, {184, 242}, {76, 7}, {49, 125}, {197, 136}, {87, 25}, {163, 236}, {87, 7}, {163, 242}, {49, 99}, {197, 150}, {184, 236}, {76, 25}, {222, 136}, {42, 125}, {180, 236}, {64, 25}, {210, 136}, {38, 125}, {91, 7}, {175, 242}, {61, 99}, {201, 150}, {163, 195}, {87, 54}, {197, 167}, {49, 82}, {76, 40}, {184, 221}, {42, 76}, {222, 185}, {64, 40}, {180, 221}, {38, 76}, {210, 185}, {175, 195}, {91, 54}, {201, 167}, {61, 82}, {201, 185}, {61, 76}, {175, 221}, {91, 40}, {38, 82}, {210, 167}, {64, 54}, {180, 195}, {42, 82}, {222, 167}, {76, 54}, {184, 195}, {197, 185}, {49, 76}, {163, 221}, {87, 40}, {210, 82}, {38, 167}, {180, 54}, {64, 195}, {61, 185}, {201, 76}, {91, 221}, {175, 40}, {49, 185}, {197, 76}, {87, 221}, {163, 40}, {222, 82}, {42, 167}, {184, 54}, {76, 195}, {184, 40}, {76, 221}, {222, 76}, {42, 185}, {87, 195}, {163, 54}, {49, 167}, {197, 82}, {91, 195}, {175, 54}, {61, 167}, {201, 82}, {180, 40}, {64, 221}, {210, 76}, {38, 185}, {76, 236}, {184, 25}, {42, 136}, {222, 125}, {163, 7}, {87, 242}, {197, 99}, {49, 150}, {175, 7}, {91, 242}, {201, 99}, {61, 150}, {64, 236}, {180, 25}, {38, 136}, {210, 125}, {38, 150}, {210, 99}, {64, 242}, {180, 7}, {201, 125}, {61, 136}, {175, 25}, {91, 236}, {197, 125}, {49, 136}, {163, 25}, {87, 236}, {42, 150}, {222, 99}, {76, 242}, {184, 7}, {163, 99}, {87, 150}, {197, 7}, {49, 242}, {76, 136}, {184, 125}, {42, 236}, {222, 25}, {64, 136}, {180, 125}, {38, 236}, {210, 25}, {175, 99}, {91, 150}, {201, 7}, {61, 242}, {201, 25}, {61, 236}, {175, 125}, {91, 136}, {38, 242}, {210, 7}, {64, 150}, {180, 99}, {42, 242}, {222, 7}, {76, 150}, {184, 99}, {197, 25}, {49, 236}, {163, 125}, {87, 136}, {61, 221}, {201, 40}, {91, 185}, {175, 76}, {210, 54}, {38, 195}, {180, 82}, {64, 167}, {222, 54}, {42, 195}, {184, 82}, {76, 167}, {49, 221}, {197, 40}, {87, 185}, {163, 76}, {87, 167}, {163, 82}, {49, 195}, {197, 54}, {184, 76}, {76, 185}, {222, 40}, {42, 221}, {180, 76}, {64, 185}, {210, 40}, {38, 221}, {91, 167}, {175, 82}, {61, 195}, {201, 54}};

void Forward(u8 c[32], u8 d[32], u8 s[512], u32 p[32])
{
    for (u32 i = 0; i < 256; i++)
    {
        for (u8 j = 0; j < 32; j++)
        {
            d[j] = s[c[j]];
            c[j] = 0;
        }

        for (u8 j = 0; j < 32; j++)
            for (u8 k = 0; k < 32; k++)
                c[j] ^= d[k] * ((p[j] >> k) & 1);
    }
    for (u8 i = 0; i < 16; i++)
        d[i] = s[c[i * 2]] ^ s[c[i * 2 + 1] + 256];
}

void Reverse(u8 ip[16])
{
    u8 d[32];
    for (u8 i = 0; i < 16; i++)
    {
        input[2 * i] = reverseConfuse[reverseText[ip[i]][1]];
        input[2 * i + 1] = reverseConfuse2[reverseText[ip[i]][0]];
    }
    for (u32 i = 0; i < 256; i++)
    {
        for (u8 j = 0; j < 32; j++)
        {
            d[j] = 0;
            for (u8 k = 0; k < 32; k++)
                d[j] ^= input[k] * ((diffusioninv[j] >> k) & 1);
        }
        for (u8 j = 0; j < 32; j++)
            input[j] = reverseConfuse[d[j]];
    }
}

int main(int argc, char *argv[])
{
    u8 target[16] = "Hire me!!!!!!!!";
    u8 output[32];
    Reverse(target);
    Forward(input, output, confusion, diffusion);
    std::cout << output << "\n";
    return memcmp(output, target, 16); // => contact jobs(at)nerd.nintendo.com
}