# Nintendo HireME challenge

This is a simple backtracking based solution to the [HireMe](https://www.nerd.nintendo.com/files/HireMe.html) challenge published by Nintendo.

<br>

The Encoding Algorithm:
```
void Forward(u8 c[32], u8 d[32], u8 s[512], u32 p[32])
{
    for (u32 i = 0; i < 256; i++) // Substitution Permutation
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
```
<br>

### Few Observations 
- This function has collisions, meaning two different inputs can have same output.
- Similarly, by peigeon hole priniple, there is a 256-bit string that is not an output of any 256-bit input string.
- The diffusion transform is linear and invertible :
    ```c[j] ^= d[k] * ((p[j] >> k) & 1);```

<br> 
Other relevent observations I have made are in the explore directory.

<br>

## Solution
There are two main parts to the solution:
- part A: Inverting the Substitution Permutation loop

```bool ConfuseAndDiffuse(u8 input[32], u32 iterNum);```
- part B: Unscrambling the final result.

```bool scramble(u8 input[16], u8 find[32], u32 level);```

### Compile and Run
```
g++ -o "HireMe"  Hire\ me\!\!\!\!\!\!\!\!.cpp 
./HireMe
```
#### Output (Hex)

```
5d c5 da 80 81 ad e e6 da 88 d9 67 43 63 1c 87 8b 72 60 24 4d bc d9 a7 fa 86 19 26 1e 69 3 6
```
Correctness:
for proof oc correntness, run
```
echo $?
```
It will print '0' if there is an exact match


