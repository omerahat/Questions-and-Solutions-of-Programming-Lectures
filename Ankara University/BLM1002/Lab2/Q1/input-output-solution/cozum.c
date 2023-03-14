#include<stdio.h>


int main(){

	float ortalamaSatis, gecenYilMusteri, guncelMusteri, guncelSatis;

	scanf("%f", &ortalamaSatis);
	scanf("%f", &gecenYilMusteri);
	scanf("%f", &guncelMusteri);
	scanf("%f", &guncelSatis);
	
	
	if(guncelSatis > 2*ortalamaSatis && guncelMusteri>=gecenYilMusteri*1.1){
		printf("Kademe 1");
	}
	else if(guncelSatis >= ortalamaSatis){
		if(guncelMusteri>=gecenYilMusteri*1.1){
			printf("Kademe 2");
		}
		else{
			printf("Kademe 3");
		}
	}
	else{
		printf("Kademe 4");
	}

	return 0;
} 
