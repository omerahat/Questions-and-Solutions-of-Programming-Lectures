#include <stdio.h>
#include <locale.h>


int main() {
    setlocale(LC_ALL, "Turkish");
    int days_in_month, start_day, i, j, day = 1;
    printf("Aydaki gün sayısını yazınız: ");
    scanf("%d", &days_in_month);
    printf("Ayın başlangıç gününü yazınız (1= Mon, 7=Sun): ");
    scanf("%d", &start_day);
    for (i = 1; i < start_day; i++) {
        printf("   "); // Önceki aya ait günlerin yerine boşluk bırak
    }
    for (j = start_day; j <= 7; j++) {
        printf("%-3d", day); // Günleri yazdır
        day++;
    }
    printf("\n");
    while (day <= days_in_month) {
        for (i = 1; i <= 7 && day <= days_in_month; i++) {
            printf("%-3d", day);
            day++;
        }
        printf("\n");
    }
    return 0;
}
