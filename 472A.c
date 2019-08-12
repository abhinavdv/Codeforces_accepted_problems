#include <stdio.h>
#include <stdbool.h>

bool isprime(int a){
    for(int i=2;i<a^(1/2);i++){
        if(a%i==0){
            return false;
        }
    }
    return true;
}

int main(){
    int n;
    scanf("%d",&n);
    int a=n-4,b=4;
    while(a>=b){
        if(!isprime(a) && !isprime(b)){
            printf("%d %d",a,b);
            return 0;
        }
        a--;
        b++;
    }


}