#include <stdio.h>

int main() {
    double ortalama_satis, gecen_yil_musteri, su_an_musteri, guncel_satis;

    scanf("%lf", &ortalama_satis);

    scanf("%lf", &gecen_yil_musteri);

    scanf("%lf", &su_an_musteri);

    scanf("%lf", &guncel_satis);

    double musteri_artisi = (su_an_musteri - gecen_yil_musteri) / gecen_yil_musteri * 100; // yuzde cinsinden musteri artisi
    float satis_orani = guncel_satis / ortalama_satis; // satışın ortalama satışa oranı

    if (satis_orani > 2 && musteri_artisi >= 10) {
        printf("Kademe 1");
    } else if (satis_orani >= 1 && musteri_artisi >= 10) {
        printf("Kademe 2");
    } else if (satis_orani >= 1) {
        printf("Kademe 3");
    } else {
        printf("Kademe 4");
    }
    return 0;
}
