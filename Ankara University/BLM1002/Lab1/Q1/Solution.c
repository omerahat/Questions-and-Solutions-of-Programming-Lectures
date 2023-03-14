#include <stdio.h>
#include <math.h>
int main(){
//Uygulamanın sabit değerleri:
	int taksit = 10,m2_34 = 5000,m2_06 = 4500, m2_35 = 4000, m2_01 = 3500, m2_55 = 3000;

	int sehirKodu, evinMetreKaresi, aylikOdenebilecekTaksit,pesinat,m2bedeli;
	float yillikFaiz;
	scanf("%d %d %d %d %f",&sehirKodu,&evinMetreKaresi,&aylikOdenebilecekTaksit,&pesinat,&yillikFaiz);
	if(sehirKodu==34){
		m2bedeli=5000;
		}
	else if(sehirKodu==6){
		m2bedeli=4500;
		}
	else if(sehirKodu==35){
		m2bedeli=4000;
		}
	else if(sehirKodu==1){
		m2bedeli=3500;
		}
	else if(sehirKodu==55){
		m2bedeli=3000;
		}
	
	int evin_fiyati = m2bedeli*evinMetreKaresi;
	printf("%d\n",evin_fiyati);
	
	float aylikFaiz = yillikFaiz/12/100;
	printf("%.4f\n", aylikFaiz);
	
	int kredi_tutari= evin_fiyati-pesinat;
	
	float aylikTaksit = kredi_tutari* aylikFaiz* pow((1+aylikFaiz),taksit) / (pow((1+aylikFaiz),taksit)-1);
	printf("%.2f\n", aylikTaksit);
	
	if(aylikTaksit <= aylikOdenebilecekTaksit){
		printf("true\n");
		}
	else{
		printf("false\n");
		}
	
	//Taksit1
	
	float kalanBorc = evin_fiyati-pesinat;
	float odenecekFaizMiktari = kalanBorc *aylikFaiz;
	float odenecekAnaparaMiktari = aylikTaksit - odenecekFaizMiktari;
	
	printf("%.2f\n", kalanBorc);
	printf("%.2f\n", odenecekFaizMiktari);
	printf("%.2f\n", odenecekAnaparaMiktari);
	
	//taksit2
	
	kalanBorc = kalanBorc -odenecekAnaparaMiktari ;
	odenecekFaizMiktari = kalanBorc * aylikFaiz;
	odenecekAnaparaMiktari = aylikTaksit - odenecekFaizMiktari;
	printf("%.2f\n", kalanBorc);
	printf("%.2f\n", odenecekFaizMiktari);
	printf("%.2f\n", odenecekAnaparaMiktari);
	
	//taksit3
	kalanBorc = kalanBorc - odenecekAnaparaMiktari;
	odenecekFaizMiktari = kalanBorc * aylikFaiz;
	odenecekAnaparaMiktari = aylikTaksit - odenecekFaizMiktari;
	printf("%.2f\n", kalanBorc);
	printf("%.2f\n", odenecekFaizMiktari);
	printf("%.2f\n", odenecekAnaparaMiktari);
	
	
	
}
