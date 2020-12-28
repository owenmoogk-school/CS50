#include <stdio.h>

int main(void)
{
    int counter;
    counter = 1;
    counter = counter + 1;
    counter += 1;
    counter += 3;

    if (counter < 5){
        printf("counter is less than 5\n");
    }
    else{
        printf("counter is more than 5\n");
    }

    printf("%i\n",counter);
}
