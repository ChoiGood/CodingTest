#include<stdio.h>
#include<string.h>
int main(){
	int n;
	char s[100];
	scanf("%d", &n);
	int c=n;
	for(int t=0; t<n; t++){
		scanf("%s", s);
		int a[26]={0,};
		for(int i=0; i<strlen(s); i++){
			if(a[s[i]-97]==-1){
				c--;
				break;
			}
			if(s[i]!=s[i+1]) a[s[i]-97]=-1;
		}
	}
	printf("%d", c);
}