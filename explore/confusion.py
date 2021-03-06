import matplotlib.pyplot as plt

confusion = [0xac, 0xd1, 0x25, 0x94, 0x1f, 0xb3, 0x33, 0x28, 0x7c, 0x2b, 0x17, 0xbc, 0xf6, 0xb0, 0x55, 0x5d,
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
             0xc0, 0xef, 0xd2, 0x16, 0x05, 0xbe, 0x53, 0xf7, 0xc2, 0xc6, 0xa2, 0x24, 0x98, 0x1c, 0xad, 0x04]


def reverseConfOne():
    ret = [[] for i in range(256)]
    for i in range(256):
        ret[confusion[i]].append(i)
    print(ret)


def bitfield(n):
    ret = [int(digit) for digit in bin(n)[2:]][::-1]
    while(len(ret) != 8):
        ret.append(0)
    return ret


def analysis():
    firstHalf = {}
    for i in range(256):
        if(confusion[i] not in firstHalf):
            firstHalf[confusion[i]] = [i]
        else:
            firstHalf[confusion[i]].append(i)
    ret = []
    for i in firstHalf:
        if(len(firstHalf[i]) > 1):
            # print(i, firstHalf[i])
            ret.append(i)

    ret.sort()
    for i in ret:
        print(bitfield(i), " : ", bitfield(
            firstHalf[i][0]), bitfield(firstHalf[i][1]))
    ret = []

    print()
    secondHalf = {}
    for i in range(256, 512):
        if(confusion[i] not in secondHalf):
            secondHalf[confusion[i]] = [i-256]
        else:
            secondHalf[confusion[i]].append(i-256)
    for i in secondHalf:
        if(len(secondHalf[i]) > 1):
            # print(i, secondHalf[i])
            ret.append(i)
    ret.sort()
    for i in ret:
        print(bitfield(i), " : ", bitfield(
            secondHalf[i][0]), bitfield(secondHalf[i][1]))

    # print(firstHalf)


def anyRelations(t):
    for i in range(256):
        print(bitfield(i), " : ", (confusion[i] >> t) & 1)


def invalid():
    firstHalf = [[] for _ in range(256)]
    for i in range(256):
        firstHalf[confusion[i]].append(i)
    for i in range(256):
        if(len(firstHalf[i]) == 2):
            print(hex(firstHalf[i][0]), " ", hex(firstHalf[i][1]))
    holes = []
    for i in range(256):
        if(len(firstHalf[i]) == 0):
            holes.append(i)
    for i in holes:
        print(bitfield(i))


def validity(arr, y):
    t = [2, 3, 6, 7, 8, 9, 12, 13]

    if(len(arr) == 2):
        if(arr[0] & 15 in t):
            i = arr[0]
        else:
            i = arr[1]
    else:
        i = arr[0]
    y[i & 15] += 1
    print(hex(i & 15), end=" ")


firstHalf = {}
for i in range(256):
    if(confusion[i] not in firstHalf):
        firstHalf[confusion[i]] = [i]
    else:
        firstHalf[confusion[i]].append(i)


def onlyValid():
    t = [2, 3, 6, 7, 8, 9, 12, 13]
    remEle = {}
    images = set(())
    for i in t:
        for j in range(16):
            x = firstHalf[16*j + i]
            for k in x:
                if(k & 0xf in t):
                    remEle[16*j + i] = k
                    images.add(k)

    final = {}
    for i in remEle:
        if i in images:
            final[i] = remEle[i]
    print(final)


def preimages():
    arr = [2, 3, 6, 7, 8, 9, 12, 13]
    y = [0]*16
    for i in arr:
        for j in range(16):
            validity(firstHalf[16*j + i], y)
    plt.stem(y)
    plt.show()


# anyRelations(5)
# analysis()
# invalid()
# preimages()
# onlyValid()

finalists = [82, 242, 25, 221, 167, 150, 76,
             125, 236, 54, 99, 40, 7, 195, 136, 185]
# THIS SET IS CLOSED UNDER ODD XORS (inverse diffusion) AND INVERSE CONFUSION
finalists2 = [175, 210, 64, 61, 197, 87, 49,
              201, 91, 42, 163, 38, 76, 222, 180, 184]
for i in finalists:
    print("{", confusion[i+256], ",", i, "},", end=" ")


# ^ Image under confusion 2 map
"""
possible = [[] for _ in range(256)]
for i in finalists2:
    for j in finalists:
        possible[i ^ j] = [i, j]
print(possible)
ALL 256 charectors are possible
"""

# reverseConfOne()
"""
bits of the outputs that repeat
0010 1100 1101 0011 1001 0111 0110 1000
2 3 6 7 8 9 c d
f 1 0 e 4 a b 5
BOX 1 [:256]
[0, 1, 0, 0, 0, 0, 0, 0]  :  [0, 0, 0, 1, 1, 0, 0, 0] [0, 1, 1, 1, 1, 0, 1, 0]
[0, 0, 1, 1, 1, 0, 0, 0]  :  [1, 1, 0, 0, 1, 0, 1, 0] [1, 0, 0, 0, 1, 1, 1, 0]
[1, 0, 1, 1, 0, 1, 0, 0]  :  [0, 0, 1, 0, 0, 0, 0, 1] [0, 0, 1, 1, 1, 0, 1, 1]
[1, 1, 0, 0, 1, 1, 0, 0]  :  [0, 1, 1, 0, 0, 0, 0, 0] [0, 1, 0, 1, 1, 0, 0, 1]
[1, 0, 0, 1, 0, 0, 1, 0]  :  [1, 0, 1, 1, 0, 0, 1, 0] [1, 0, 0, 0, 1, 0, 1, 1]
[1, 1, 1, 0, 1, 0, 1, 0]  :  [0, 0, 0, 1, 1, 1, 0, 1] [1, 1, 1, 1, 0, 0, 1, 1]
[0, 1, 1, 0, 0, 1, 1, 0]  :  [1, 0, 0, 1, 0, 1, 0, 0] [1, 0, 1, 0, 1, 1, 0, 1]
[0, 0, 0, 1, 1, 1, 1, 0]  :  [1, 0, 1, 0, 1, 0, 0, 0] [1, 1, 1, 0, 1, 0, 0, 1]
<-negation->|-------| common??
[1, 0, 1, 1, 0, 0, 0, 1]  :  [1, 0, 0, 1, 0, 0, 0, 1] [1, 1, 0, 1, 0, 1, 0, 1]
[1, 1, 0, 0, 1, 0, 0, 1]  :  [0, 1, 1, 0, 0, 1, 0, 1] [0, 0, 0, 0, 0, 1, 1, 1]
[0, 1, 0, 0, 0, 1, 0, 1]  :  [0, 1, 0, 1, 1, 1, 0, 0] [1, 1, 0, 0, 1, 1, 1, 1]
[0, 0, 1, 1, 1, 1, 0, 1]  :  [1, 1, 0, 1, 0, 0, 0, 0] [0, 1, 0, 0, 0, 0, 1, 1]
[0, 1, 1, 0, 0, 0, 1, 1]  :  [1, 1, 1, 0, 1, 1, 0, 0] [0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 1, 1, 0, 1, 1]  :  [1, 1, 1, 1, 0, 1, 1, 0] [1, 0, 1, 1, 0, 1, 1, 1]
[1, 0, 0, 1, 0, 1, 1, 1]  :  [0, 0, 1, 0, 0, 1, 0, 0] [0, 0, 1, 1, 1, 1, 1, 0]
[1, 1, 1, 0, 1, 1, 1, 1]  :  [0, 1, 0, 0, 0, 1, 1, 0] [0, 1, 1, 1, 1, 1, 1, 1]

confusion1:
0x0f 0x11 0x20 0x3e 0x44 0x5a 0x6b 0x75 
0x80 0x9e 0xaf 0xb1 0xcb 0xd5 0xe4 0xfa

// not allowed 
f 1 0 e 4 a b 5
2 c d 3 9 7 6 8 
// allowed 
diffusion = [
    0xf26cb481, 0x16a5dc92, 0x3c5ba924, 0x79b65248, 0x2fc64b18, 0x615acd29, 0xc3b59a42, 0x976b2584,
    0x6cf281b4, 0xa51692dc, 0x5b3c24a9, 0xb6794852, 0xc62f184b, 0x5a6129cd, 0xb5c3429a, 0x6b978425,
    0xb481f26c, 0xdc9216a5, 0xa9243c5b, 0x524879b6, 0x4b182fc6, 0xcd29615a, 0x9a42c3b5, 0x2584976b,
    0x81b46cf2, 0x92dca516, 0x24a95b3c, 0x4852b679, 0x184bc62f, 0x29cd5a61, 0x429ab5c3, 0x84256b97]

[1, 1, 1, 1, 0, 0, 0, 0]
[1, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 1, 1, 1, 1, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 1, 0]
[0, 1, 0, 1, 1, 0, 1, 0]
[1, 1, 0, 1, 0, 1, 1, 0]
[1, 0, 1, 0, 1, 1, 1, 0]

[0, 0, 0, 0, 0, 0, 0, 1]
[0, 1, 1, 1, 1, 0, 0, 1]
[1, 1, 1, 1, 0, 1, 0, 1]
[1, 0, 0, 0, 1, 1, 0, 1]
[1, 1, 0, 1, 0, 0, 1, 1]
[1, 0, 1, 0, 1, 0, 1, 1]
[0, 0, 1, 0, 0, 1, 1, 1]
[0, 1, 0, 1, 1, 1, 1, 1]

<----------------->

BOX 2 [256:512]
[0, 0, 1, 0, 0, 1, 0, 0]  :  [0, 0, 1, 0, 0, 0, 0, 1] [1, 1, 0, 1, 1, 1, 1, 1]
[0, 0, 0, 1, 0, 1, 0, 0]  :  [1, 0, 0, 0, 0, 1, 0, 0] [1, 0, 0, 0, 1, 0, 1, 1]
[1, 1, 0, 0, 1, 1, 0, 0]  :  [0, 0, 0, 0, 0, 0, 1, 0] [1, 0, 1, 0, 0, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 0, 0]  :  [0, 1, 1, 1, 0, 0, 0, 0] [1, 1, 1, 1, 0, 1, 1, 0]
[0, 1, 0, 0, 0, 0, 1, 0]  :  [0, 1, 1, 1, 1, 0, 1, 0] [0, 1, 1, 1, 0, 1, 0, 1]
[0, 1, 1, 1, 0, 0, 1, 0]  :  [0, 0, 0, 0, 1, 0, 0, 0] [1, 1, 1, 1, 0, 0, 1, 1]
[1, 0, 1, 0, 1, 0, 1, 0]  :  [0, 1, 0, 1, 0, 1, 1, 0] [0, 1, 0, 1, 1, 0, 0, 1]
[1, 0, 0, 1, 1, 0, 1, 0]  :  [1, 1, 0, 1, 0, 0, 0, 0] [0, 0, 1, 0, 1, 0, 1, 1]
         |----------| common??
[1, 0, 0, 0, 0, 1, 0, 1]  :  [1, 0, 1, 0, 0, 0, 1, 0] [1, 0, 1, 0, 1, 1, 0, 1]
[1, 0, 1, 1, 0, 1, 0, 1]  :  [1, 1, 0, 1, 1, 0, 1, 0] [0, 1, 1, 1, 1, 1, 1, 1]
[0, 1, 1, 0, 1, 1, 0, 1]  :  [1, 0, 0, 0, 1, 1, 1, 0] [1, 0, 0, 0, 0, 0, 0, 1]
[0, 1, 0, 1, 1, 1, 0, 1]  :  [0, 1, 0, 1, 1, 1, 0, 0] [0, 1, 0, 1, 0, 0, 1, 1]
[1, 1, 1, 0, 0, 0, 1, 1]  :  [1, 1, 1, 1, 1, 0, 0, 1] [0, 0, 0, 0, 0, 1, 1, 1]
[1, 1, 0, 1, 0, 0, 1, 1]  :  [0, 0, 1, 0, 0, 1, 0, 0] [0, 0, 0, 0, 1, 1, 0, 1]
[0, 0, 0, 0, 1, 0, 1, 1]  :  [1, 0, 1, 0, 1, 0, 0, 0] [0, 0, 1, 0, 1, 1, 1, 0]
[0, 0, 1, 1, 1, 0, 1, 1]  :  [1, 1, 1, 1, 1, 1, 0, 0] [1, 1, 0, 1, 0, 1, 0, 1]

"""

"""
inverse confusion : {{106}, {26}, {24, 94}, {89}, {56}, {86}, {227}, {195}, {228}, {95}, {188}, {144}, {47}, {223}, {70}, {}, {88}, {}, {245}, {42}, {247}, {191}, {128}, {10}, {204}, {221}, {23}, {246}, {83, 113}, {131}, {129}, {4}, {}, {130}, {240}, {145}, {48}, {2}, {112}, {158}, {7}, {253}, {232}, {9}, {118}, {132, 220}, {222}, {176}, {81}, {251}, {200}, {6, 154}, {140}, {115}, {99}, {210}, {110}, {68}, {197}, {216}, {148}, {218}, {}, {230}, {161}, {162}, {37}, {117}, {}, {248}, {238}, {100}, {18}, {77, 209}, {43}, {33}, {125}, {67}, {146}, {183}, {189}, {92}, {82}, {39}, {149}, {14}, {104}, {184, 207}, {193}, {75}, {}, {215}, {59}, {15}, {123}, {198}, {252}, {121}, {22}, {40}, {91}, {239}, {41, 181}, {214}, {196}, {80}, {34}, {}, {62}, {155}, {51}, {244}, {233}, {31}, {32}, {255}, {119}, {}, {49}, {127}, {21, 151}, {157}, {174}, {192}, {8}, {236}, {226}, {103}, {}, {60}, {165}, {30}, {142}, {45}, {65}, {250}, {185}, {153}, {72}, {205}, {71}, {137, 171}, {96}, {16}, {186}, {116}, {61}, {166, 224}, {3}, {134}, {76}, {93}, {180}, {213}, {234}, {87}, {187}, {122}, {}, {201}, {69}, {53}, {58, 243}, {172}, {152}, {50}, {168}, {150}, {90}, {133}, {28}, {101}, {0}, {97}, {173}, {}, {13}, {}, {85}, {5}, {120}, {219}, {175}, {208}, {135}, {242}, {66}, {217}, {11, 194}, {178}, {229}, {126}, {38}, {44}, {57}, {136}, {159}, {164}, {55, 64}, {249}, {235}, {27}, {105}, {}, {203}, {170}, {102}, {46}, {73}, {1}, {17}, {20}, {19}, {}, {143}, {52}, {111, 237}, {231}, {63}, {139}, {114}, {167}, {211}, {163}, {84}, {141}, {206}, {107}, {}, {179}, {78}, {190}, {35}, {36, 124}, {79}, {202}, {54}, {108}, {199}, {169}, {29}, {109}, {25}, {182}, {241}, {212}, {12}, {98, 254}, {138}, {160}, {}, {156}, {225}, {177}, {74}, {147}}
finalists = [82, 242, 25, 221, 167 ,150 ,76 ,125, 236 ,54 ,99 ,40, 7 ,195 ,136, 185]
^ analysis suggests the above are closed under inverse confusion map
"""
