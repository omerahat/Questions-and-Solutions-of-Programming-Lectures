#include<stdio.h>

int main(){

	int birBasamak=0, ikiBasamak=0, ucBasamak=0;
	int sayi;
	int count=0;
	
	scanf("%d", &sayi);
	
	do{
		if(sayi==0)
		birBasamak++;
		while(sayi!=0){
			count++;
			sayi=sayi/10;
		}
		if(count==1){
			birBasamak++;
		}else if(count==2){
			ikiBasamak++;
		}else if(count==3){
			ucBasamak++;
		}
		
		count=0;
		scanf("%d", &sayi);
	}while(sayi!=-1);
	
	
	printf("%d tane 1 basamakli\n", birBasamak);
	printf("%d tane 2 basamakli\n", ikiBasamak);
	printf("%d tane 3 basamakli\n", ucBasamak);
	
}
