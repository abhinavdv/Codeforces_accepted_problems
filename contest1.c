#include<stdio.h>
int main(){
    int n,t=1;
    scanf("%d",&n);
    char arr[n];
    int arr1[10];
    scanf("%s",arr);
    for(int i=0; i<10 ;i++){
        arr1[i]=0;
    }
    for(int i=0;i<n;i++){
        if(arr[i]=='L'){
            for(int j=0;j<10;j++){
                if(arr1[j]==0){
                    arr1[j]=1;
                    break;
                }
            }
        }
        if (arr[i] == 'R')
        {
            for (int j = 9; j >=0; j--)
            {
                if (arr1[j] == 0)
                {
                    arr1[j] = 1;
                    break;
                }
            }
        }
        else{
            int k = arr[i] - '0';
            arr1[k] = 0;
        
        }

    }
    for(int i=0;i<10;i++){
        printf("%d",arr1[i]);
    }
}