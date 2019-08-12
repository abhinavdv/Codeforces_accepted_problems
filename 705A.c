#include<stdio.h>
int main(){
    int n,k=0;
    scanf("%d",&n);
        int m=n;
        while(n>1){
            if(k==0){
                printf("I hate that ");
                n--;
                k=1;
                continue;
            }
            if (k == 1)
            {
                printf("I love that ");
                n--;
                k = 0;
                continue;
            }
        }
        if(m%2==0){
            printf("I love it");
        }
        else{
            printf("I hate it");
        }
}
