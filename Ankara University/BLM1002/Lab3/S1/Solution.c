#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <locale.h>


int main() {
    setlocale(LC_ALL, "Turkish");
    int hour, minute;
    int departureHour, departureMinute, arrivalHour, arrivalMinute;
    int closestDepartureHour, closestDepartureMinute, closestArrivalHour, closestArrivalMinute;
    int timeDiff, minTimeDiff = 1440; // 24 saat x 60 dakika

    scanf("%d", &hour);
    scanf("%d", &minute);

    // en yakın saat bulmak için tüm kalkışları test ediyoruz
    for (int i = 1; i <= 8; i++) {
        // tablodan kalkış ve varış saatlerini çıkaralım
        switch (i) {
            case 1: departureHour = 8; departureMinute = 10; arrivalHour = 10; arrivalMinute = 16; break;
            case 2: departureHour = 9; departureMinute = 43; arrivalHour = 11; arrivalMinute = 52; break;
            case 3: departureHour = 11; departureMinute = 19; arrivalHour = 13; arrivalMinute = 31; break;
            case 4: departureHour = 12; departureMinute = 47; arrivalHour = 15; arrivalMinute = 10; break;
            case 5: departureHour = 14; departureMinute = 10; arrivalHour = 14; arrivalMinute = 17; break;
            case 6: departureHour = 15; departureMinute = 45; arrivalHour = 17; arrivalMinute = 55; break;
            case 7: departureHour = 19; departureMinute = 1; arrivalHour = 21; arrivalMinute = 20; break;
            case 8: departureHour = 21; departureMinute = 45; arrivalHour = 23; arrivalMinute = 58; break;
        }

        // giriş zamanı ile mevcut kalkış zamanı arasındaki zaman farkını hesaplayalım
        timeDiff = abs((hour * 60 + minute) - (departureHour * 60 + departureMinute));
        
        // eğer mevcut olan daha yakınsa en yakın kalkış ve varış zamanını güncelleyelim
        if (timeDiff < minTimeDiff) {
            minTimeDiff = timeDiff;
            closestDepartureHour = departureHour;
            closestDepartureMinute = departureMinute;
            closestArrivalHour = arrivalHour;
            closestArrivalMinute = arrivalMinute;
        }
    }

    printf("En yakın kalkış %d:%02d varış %d:%02d\n", closestDepartureHour, closestDepartureMinute, closestArrivalHour, closestArrivalMinute);

    return 0;
}
