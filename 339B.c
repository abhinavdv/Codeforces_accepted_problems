#include <stdio.h>
int main()
{
    long long n,m,counter=0;
    scanf("%I64lld%I64lld", &n, &m);
    long long arr[m];
    for(long long i=0;i<m;i++){
        scanf("%I64lld", &arr[i]);
        if(i==0){
            counter = arr[i]-1;
            continue;
        }
        else if(arr[i]>arr[i-1]){
            counter += arr[i]-arr[i-1];
        }
        else if(arr[i]<arr[i-1]){
            counter+= n-arr[i-1]+arr[i];
        }
        
    }
    printf("%I64lld", counter);
}

