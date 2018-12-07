#include<stdio.h>
#include<stdbool.h>
#include <stdlib.h>

int main() {
    bool positive_occurrences[100000] = {false};
    bool negative_occurrences[100000] = {false};

    int flag = 0;
    int sum = 0;
    int inputs[100000] = {0};
    int inputs_length = 0;
    char input_str[10000];


    flag = scanf("%s", input_str);

    while(flag != EOF) {
        inputs[inputs_length] = atoi(input_str);
        inputs_length++;

        flag = scanf("%s", input_str);
    };

    for(int i = 0; ; i = (i+1)%inputs_length) {
        sum += inputs[i];

        if(sum >= 0) {
            if(positive_occurrences[sum]) {
                printf("%d", sum);
                return 0;
            }
            positive_occurrences[sum] = true;
        } else {
            if(negative_occurrences[-1*sum]) {
                printf("%d", sum);
                return 0;
            }
            negative_occurrences[-1*sum] = true;
        }
    }

    return 0;
}
