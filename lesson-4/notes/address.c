#include <stdio.h>

int main(void){
    int n = 50;
    int *p = &n;
    // go to the address
    printf("%p\n",p);
}