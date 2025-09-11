#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>

 unsigned int seed;

void anti_debug() {
    FILE* fp = fopen("/proc/self/status", "r");
    if (fp) {
        char line[128];
        while (fgets(line, sizeof(line), fp)) {
            if (strstr(line, "TracerPid:") && line[strlen("TracerPid:")] != '0') {
                printf("Debugger detected!\n");
                exit(1);
            }
        }
        fclose(fp);
    }
}

void build_flag(char* buffer) {


    buffer[0] = (seed >> 24) - 0x91;  
    buffer[1] = (seed >> 16) - 0x68;   
    buffer[2] = (seed >> 8) - 0x7A;  
    buffer[3] = seed - 0x74;         


    buffer[4] = (seed % 100) + 0x21;
    buffer[5] = (seed % 50) + 0x0C;  
    buffer[6] = (seed % 30) + 0x42;  


    buffer[7] = (seed % 70) + 0x5A;  
    buffer[8] = (seed % 60) + 0x2D;  
    buffer[9] = (seed % 40) + 0x09;  
    buffer[10] = buffer[6];          


    buffer[11] = (seed >> 4) - 0x8B; 
    buffer[12] = (seed % 9) + 0x2C;  
    buffer[13] = (seed >> 16) - 0x48;
    buffer[14] = (seed % 7) + 0x31;  


    buffer[15] = (seed >> 16) ^ 0xC3;
    buffer[16] = (seed % 6) + 0x30;  
    buffer[17] = buffer[6];          


    buffer[18] = buffer[8];          
    buffer[19] = buffer[12];         
    buffer[20] = buffer[16];         
    buffer[21] = buffer[6];          


    buffer[22] = buffer[8];          
    buffer[23] = buffer[9];          
    buffer[24] = (seed >> 8) ^ 0xCB; 
    buffer[25] = buffer[16];         


    buffer[26] = buffer[5];          
    buffer[27] = buffer[6];          


    buffer[28] = buffer[5];          
    buffer[29] = (seed % 80) + 0x29; 
    buffer[30] = (seed >> 8) - 0x4E; 
    buffer[31] = buffer[5];          


    buffer[32] = buffer[11];         
    buffer[33] = (seed % 7) + 0x34;  
    buffer[34] = buffer[16];         
    buffer[35] = buffer[6];          


    buffer[36] = (seed >> 20) - 0x74;
    buffer[37] = buffer[12];         
    buffer[38] = buffer[16];         
    buffer[39] = buffer[12];         
    buffer[40] = buffer[33];         
    buffer[41] = buffer[9];          
    buffer[42] = (seed >> 24) ^ 0xAC;
    buffer[43] = buffer[16];         
    buffer[44] = '}';                
    buffer[45] = '\0';               


}

int verify_flag(const char* input) {
    char real_flag[50] = {0};
    build_flag(real_flag);

    return strcmp(input, real_flag) == 0;
}

void check_seed(unsigned int key) {
    printf("key: %x\n", key); 
    if (key != 3735928559) {
    printf("Seed value is valid : %x\n", seed);
        printf("Invalid seed value. Exiting...\n");
        exit(1);
    }

    printf("Seed value is valid. \n");
    seed = key;
}
int main() {
    char *buffer = malloc(50);
    anti_debug();
    unsigned int key;
    printf("Welcome to the advanced seeded flag generator!\n");
    printf("Try to find the flag without debugging... good luck!\n");
    
    char user_input[100];
    printf("[*] Enter the key: ");
    scanf("%u", &key);
    check_seed(key);
    printf("Enter your guess: ");
    scanf("%s]", &user_input);
    user_input[strcspn(user_input, "\n")] = 0;
    
    if (verify_flag(user_input)) {
        printf("Congratulations! You found the flag.\n");
    } else {
        printf("Sorry, that's not the correct flag.\n");
    }
    
    return 0;
}