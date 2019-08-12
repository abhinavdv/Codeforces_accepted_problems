#include <stdio.h>
int main(){
	int total;
	scanf("%d",&total);
	int k =total;
	int h=0,l=0;

	for(int i=0;i<total;i++){
		int m;
		scanf("%d",&m);
		if(m==-1){
			if(h==0)
				l++;
			else{
				h--;
			}
			}
		if(m!=-1){
			h+=m;
		}
		
	}
	printf("%d",l);
}