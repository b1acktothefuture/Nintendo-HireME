# Nintendo HireME challenge

The solutions to this challenge belong to different levels :

- Level 1 : an iterative algorithm which typically takes more than a second to
find a solution (for any given output). 

Most people stop here, which is fine, but if you want to go further, there is :

- Level 2 : a non-iterative algorithm which typically takes less than a
millisecond to find a solution (for any given output).

Few people have reached this level. But if you want to beat it completely,
there's yet another castle...

- Level 3 : an algorithm which can provide any of the 2^128 solutions (for any
given output).

Even fewer people have reached this final level. Congratulations to them!

## Primitive Solution (Level 1)

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
            d[j] = s[c[j]]; // confusion
            c[j] = 0;
        }

        for (u8 j = 0; j < 32; j++)
            for (u8 k = 0; k < 32; k++)
                c[j] ^= d[k] * ((p[j] >> k) & 1); // diffusion
    }
    for (u8 i = 0; i < 16; i++)
        d[i] = s[c[i * 2]] ^ s[c[i * 2 + 1] + 256]; //scramble
}
```

<br>

### Few Observations 
- This function has collisions, meaning two different inputs can have same output.
- Similarly, by peigeon hole priniple, there is a 256-bit string that is not an output of any 256-bit input string.
- The diffusion transform is linear and invertible :
    ```c[j] ^= d[k] * ((p[j] >> k) & 1);```

<br>

## Solution
There are two main parts to the solution:
- part A: Inverting the Substitution Permutation loop

```bool ConfuseAndDiffuse(u8 input[32], u32 iterNum);```
- part B: Unscrambling the final result.

```bool scramble(u8 input[16], u8 find[32], u32 level);```

### Compile and Run
```console
foo@bar:~$ g++ -o "HireMe"  HireMe.cpp 
foo@bar:~$ ./HireMe
```
#### Output (Hex)

```
5d c5 da 80 81 ad e e6 da 88 d9 67 43 63 1c 87 8b 72 60 24 4d bc d9 a7 fa 86 19 26 1e 69 3 6
```
Correctness:
for proof of correctness, run
```console
foo@bar:~$ echo $?
0
```
It prints '0' if there is an exact match

## Faster Solution (Level 2)
I have implemented a faster solution (<b>HireMeFast.cpp</b>) that runs in milliseconds, it finds <b>A</b> solution to the problem <b>not</b> all the possible solutions, it is based on finding as subset of [0,255] which is closed under both confusion and diffusion map, although I have not written down the solution/proof of work formally, some of my useful observations can be found in ```explore``` directory.

### Compile and Run
```console
foo@bar:~$ g++ -o "HireMeFast"  HireMeFast.cpp 
foo@bar:~$ ./HireMeFast
```
#### Output (Hex)

```
Hire me!!!!!!!!
```
Correctness:
for proof of correctness, run 
```console
foo@bar:~$ echo $?
0
```
It prints '0' if there is an exact match

## Level 3??
The Level two solution is very loose, in the sense are lot of the potential inputs are discarded, there is a great room for improvement especially with observed symmetries in diffusion map pointed out in <b>invert diffuse.py</b>. If anyone wishes to continue on this work, or improve upon current solution, you are welcome.





