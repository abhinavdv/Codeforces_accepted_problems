#include <stdio.h>
int main(){
	int k,m=0;
	scanf("%d",&k);
	for(int i=0;i<k;i++){
		int n;
		scanf("%d",&n);
		m+=n;
	}
	if(m==0){
		printf("EASY");
	}
	else{
		printf("HARD");
	}
}