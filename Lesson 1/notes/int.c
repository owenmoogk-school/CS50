#include <cs50.h>
#include <stdio.h>

int main(void){
    int age = get_int("whats your age\n");
    int days = age*365;

    printf("you are at least %i days old. \n", days);
}
