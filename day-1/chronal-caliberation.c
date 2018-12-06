#include<stdio.h>

int main() {
    int flag = 0;
    int sum = 0;
    while(flag != EOF) {
        int temp = 0;
        flag = scanf("%d", &temp);

        sum += temp;
    }

    printf("%d\n", sum);
    return 0;
}
