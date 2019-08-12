int main(){
    int n,j=0;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int maxindex = 0, minindex = 0;
    for (int i = 1; i < n; i++)
    {
        if(arr[i]>arr[maxindex]){
            maxindex=i;
        }
        if(arr[i]<=arr[minindex]){
            minindex = i;
        }
    }
    if(minindex>maxindex){
        printf("%d",maxindex+n-minindex -1);
    }
    if(minindex<maxindex){
        printf("%d", maxindex + n - minindex - 2);
    }
}