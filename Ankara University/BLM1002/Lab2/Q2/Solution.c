#include <stdio.h>

int main() {
    int num, bir=0 ,iki=0,uc=0;
    while(1){
        scanf("%d",&num);
        if (num==-1){
            break;
        }
        else if(num<10){
            bir++;
        }
        else if(num<100){
            iki++;
        }
        else{
            uc++;
        }
    }
    printf("%d tane 1 basamakli\n",bir);
    printf("%d tane 2 basamakli\n",iki);
    printf("%d tane 3 basamakli\n",uc);

    return 0;
}
