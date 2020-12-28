#include <cs50.h>
#include <stdio.h>

int main(void){
    float price = get_float("what is the price?\n");
    float final = price * 1.13;

    printf("total is %.2f.\n", final);
}
