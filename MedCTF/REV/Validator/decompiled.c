
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <unistd.h>
void check_the_flag(char* arg1) __noreturn
{
    int64_t var_b8;
    __builtin_memcpy(&var_b8, 
        "\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44", 
        0xa0);
    
    if (getenv("LD_PRELOAD"))
    {
        puts("Debugging detected! Aborting.");
        exit(1);
        /* no return */
    }
    
    int64_t var_158;
    __builtin_memcpy(&var_158, 
        "\x59\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x09\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x09\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x09\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x95\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff\x00\x11\x22\x33\x44", 
        0xa0);
    
    for (int32_t i = 0; i <= 3; i += 1)
    {
        arg1[i] ^= 0xaa;
        arg1[i] = (arg1[i] * 2) | arg1[i] >> 7;
        arg1[i] = (arg1[i] & 0xf0) | ((arg1[i] & 0xf) ^ 0x55);
        arg1[i] = (arg1[i] & 0xf) | ((arg1[i] & 0xf0) ^ 0xaa);
        arg1[i] s>>= 1;
        arg1[i] = (arg1[i] & 0xf0) | ((arg1[i] & 0xf) ^ 0x56);
        arg1[i] = (arg1[i] & 0xf) | ((arg1[i] & 0xf0) ^ 0xaa);
        arg1[i] s>>= 1;
        arg1[i] = (arg1[i] & 0xf0) | ((arg1[i] & 0xf) ^ 0x57);
        arg1[i] = (arg1[i] & 0xf) | ((arg1[i] & 0xf0) ^ 0xaa);
        arg1[i] s>>= 1;
        arg1[i] = (arg1[i] & 0xf0) | ((arg1[i] & 0xf) ^ 0x58);
        arg1[i] = (arg1[i] & 0xf) | ((arg1[i] & 0xf0) ^ 0xaa);
        arg1[i] s>>= 1;
        arg1[i] = (arg1[i] & 0xf0) | ((arg1[i] & 0xf) ^ 0x59);
        arg1[i] = (arg1[i] & 0xf) | ((arg1[i] & 0xf0) ^ 0xaa);
        arg1[i] s>>= 1;
        arg1[i] = (arg1[i] & 0xf0) | ((arg1[i] & 0xf) ^ 0x5a);
        arg1[i] = (arg1[i] & 0xf) | ((arg1[i] & 0xf0) ^ 0xaa);
        arg1[i] s>>= 1;
        arg1[i] = (arg1[i] & 0xf0) | ((arg1[i] & 0xf) ^ 0x5b);
        arg1[i] = (arg1[i] & 0xf) | ((arg1[i] & 0xf0) ^ 0xaa);
        arg1[i] s>>= 1;
        arg1[i] = (arg1[i] & 0xf0) | ((arg1[i] & 0xf) ^ 0x5c);
        arg1[i] = (arg1[i] & 0xf) | ((arg1[i] & 0xf0) ^ 0xaa);
        arg1[i] s>>= 1;
        arg1[i] = (arg1[i] & 0xf0) | ((arg1[i] & 0xf) ^ 0x5d);
        arg1[i] = (arg1[i] & 0xf) | ((arg1[i] & 0xf0) ^ 0xaa);
        arg1[i] s>>= 1;
        arg1[i] = (arg1[i] & 0xf0) | ((arg1[i] & 0xf) ^ 0x5e);
        arg1[i] = (arg1[i] & 0xf) | ((arg1[i] & 0xf0) ^ 0xaa);
        arg1[i] s>>= 1;
        arg1[i] = (arg1[i] & 0xf0) | ((arg1[i] & 0xf) ^ 0x5f);
        arg1[i] = (arg1[i] & 0xf) | ((arg1[i] & 0xf0) ^ 0xaa);
        arg1[i] s>>= 1;
        arg1[i] = (arg1[i] & 0xf0) | ((arg1[i] & 0xf) ^ 0x60);
        arg1[i] = (arg1[i] & 0xf) | ((arg1[i] & 0xf0) ^ 0xaa);
        arg1[i] s>>= 1;
        arg1[i] = (arg1[i] & 0xf0) | ((arg1[i] & 0xf) ^ 0x61);
    }
    
    arg1[strlen(arg1)] = 0;
    
    for (int32_t i_1 = 0; i_1 <= 3; i_1 += 1)
    {
        if (i_1 & 1)
            arg1[i_1] = (arg1[i_1] & 0xf) | ((arg1[i_1] & 0xf0) ^ 0xaa);
        else
            arg1[i_1] = (arg1[i_1] & 0xf0) | ((arg1[i_1] & 0xf) ^ 0x62);
        
        arg1[i_1] s>>= 1;
    }
    
    printf("choose number betwen 0 and 9 : ");
    int32_t var_15c;
    __isoc99_scanf("%d", &var_15c);
    
    if (rand() % 0xa != var_15c)
    {
        exit(0);
        /* no return */
    }
    
    puts("are you lucky ?");
    
    if (cmp_key(arg1, &var_b8))
    {
        puts("Yawdi yawdi al9raya hhhhhhhh");
        exit(1);
        /* no return */
    }
    
    if (cmp_key(arg1, &var_158) == 1)
    {
        exit(0);
        /* no return */
    }
    
    printf("Bibaaaaaah_Ahssan_wahid_d_taxiya…");
    exit(0);
    /* no return */
}

void sub_401f82(char* arg1) __noreturn
{
    int64_t var_38;
    __builtin_strncpy(&var_38, ", r-(*\")", 8);
    int64_t var_30 = 0x1e2d75357523751e;
    int64_t var_28 = 0x35701e2570251e34;
    int32_t rax_3 = strlen(arg1);
    char var_78[0x40];
    
    for (int32_t i = 0; i < rax_3; i += 1)
        var_78[i] = arg1[i] ^ 0x41;
    
    var_78[rax_3] = 0;
    
    if (!strcmp(&var_78, &var_38))
    {
        puts(arg1);
        exit(0);
        /* no return */
    }
    
    if (rand() % 5)
    {
        puts("Ak i3awn rbi ");
        exit(1);
        /* no return */
    }
    
    puts("iwa ach ghadi dir akhaoya khalih…");
    exit(0x539);
    /* no return */
}

int32_t main(int32_t argc, char** argv, char** envp)
{
    srand(0xdeadbeef);
    srand(time(nullptr));
    
    if (argc == 2)
    {
        check_the_flag(argv[1]);
        /* no return */
    }
    
    printf("Usage: %s <key>\n", *argv);
    printf("Example: %s D4ark0ps\n", *argv);
    return 1;
}
