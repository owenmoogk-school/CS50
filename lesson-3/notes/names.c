#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void){
    string names[4] = {"emmsa","david","rodriguo","chris"};
    int found = 0;
    for (int i = 0; i < 4; i++){
        if (strcmp(names[i],"emma") == 0){
            printf("Found\n");
            found = 1;
        }
    }
    if (found == 0){
        printf("not found\n");
    }
}