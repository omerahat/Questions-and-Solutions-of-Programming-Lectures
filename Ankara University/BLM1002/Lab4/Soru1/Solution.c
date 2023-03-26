#include <stdio.h>

int is_prime(int n) {
    if (n <= 1) {
        return 0;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

void print_prime(int n) {
    printf("%d sayisi asaldir\n", n);
}

void print_not_prime(int n) {
    printf("%d sayisi asal degildir\n", n);
}

int main() {
    int sayi, prime_count = 0, not_prime_count = 0;
    
    do {
        scanf("%d", &sayi);
        
        if (sayi == -1) {
            break;
        }
        
        if (is_prime(sayi)) {
            print_prime(sayi);
            prime_count++;
        } else {
            print_not_prime(sayi);
            not_prime_count++;
        }
    } while (1);
    
    printf("Toplam %d sayi asal, %d sayi asal degildir", prime_count, not_prime_count);
    
    return 0;
}
