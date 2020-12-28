#include <stdio.h>

int main(void)
{
    // while (1){
    //     printf("hello, world\n");
    // }

    int i = 0;
    while (i < 50){
        printf("hello world");
        i += 1;
    }
    printf("done 1\n");

    for (int p = 0; p<50; p++){
        printf("hello, world");
    }
}
