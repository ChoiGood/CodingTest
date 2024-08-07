#include<stdio.h>

int main(){
  char ch[105];
  int len=0;
  scanf(" %s",ch);
  for(int pt=0;ch[pt];pt++){
    if(ch[pt]=='='&&ch[pt-1]=='z'&&ch[pt-2]=='d') len--;
    else if(ch[pt]=='='||ch[pt]=='-'||(ch[pt]=='j'&&(ch[pt-1]=='l'||ch[pt-1]=='n')));
    else len++;
  }
  printf("%d",len);
}
