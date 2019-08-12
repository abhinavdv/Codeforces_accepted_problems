#include<stdio.h>
#include<stdbool.h>


bool isprime(int a){
    for(int i=2;i<a^(1/2);i++){
        if(a%i==0){
            return false;
        }
    }
    return true;
}