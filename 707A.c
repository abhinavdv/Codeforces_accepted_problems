#include <stdio.h>
int main(){
	int k,m=0;
	scanf("%d",&k);
	scanf("%d",&m);
	for(int i=0;i<k*m;i++){
		char n;
		scanf("%c",&n);
		if(n!='W'|| n!='B'){
			printf("#Color");
			return 0;
		}
	}
printf("#Black&White");
}