#include <stdio.h>

int main() {
    int ay, gun, yil;
    int en_erken_ay = 0, en_erken_gun = 0, en_erken_yil = 0;

    while (1) {
        scanf("%d", &ay);
        scanf("%d",&gun);
        scanf("%d",&yil);

        if (ay == 0 && gun == 0 && yil == 0) {
            break;
        }

        if (en_erken_yil == 0) {
            en_erken_yil = yil;
            en_erken_ay = ay;
            en_erken_gun = gun;
        }
        else if (yil < en_erken_yil || 
                (yil == en_erken_yil && ay < en_erken_ay) || 
                (yil == en_erken_yil && ay == en_erken_ay && gun < en_erken_gun)) {
            en_erken_yil = yil;
            en_erken_ay = ay;
            en_erken_gun = gun;
        }
    }

    printf("%d %d %d en erken tarih\n", en_erken_ay, en_erken_gun, en_erken_yil);

    return 0;
}
