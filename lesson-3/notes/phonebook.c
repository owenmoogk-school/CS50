#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct{
    string name;
    string number;
}
person;

int main(void){

    person people[2];

    people[0].name = "Emma";
    people[0].name = "154-151-1515";
    people[1].name = "Rodrigo";
    people[1].name = "151-151-1868";

    int found = 0;

    for (int i = 0; i < 2; i++){
        if (strcmp(people[i].name,"Rodrigo") == 0){
            printf("%s\n", people[i].number);
            found = 1;
        }
    }
    if (found == 0){
        printf("not found\n");
    }
}