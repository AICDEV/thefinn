#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int getRandomNumber() {
    return (uint8_t) ((rand() % 25) + 65);
}

int main(int argc, char *argv[]) {

    if(argc != 2) {
        return EXIT_FAILURE;
    }
    

    time_t t;
    srand((unsigned) time(&t));

    printf("Check if license key is valid \n");
    char *license_arg = malloc(sizeof(char) * 4);
    strncpy(license_arg, argv[1], 4);

    char *random_license = malloc(sizeof(char) * 4);

    for(int i = 0; i < 4; i++) {
        char random_char = (char) getRandomNumber();
        strcat(random_license, &random_char);
    }

    int res = strcmp(random_license, license_arg);

    if (res == 0) {
        printf("license accepted \n");
    } else {
        printf("wrong license \n");
    }

    return EXIT_SUCCESS;
}
