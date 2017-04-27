
/*
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600.851.475.143 ?
*/

//#include <stdio.h>
#include <math.h>

#define  MAX_N_PRIMES 800000  // 8 m
#define MAX_N_FACTORS 1000

void print_list(unsigned long long *elements, int n_elements){
    printf("Elements: ");
    for (int i=0; i < n_elements; i++){
        printf("%lld, ", elements[i]);
    }
    printf("\n");
}

int add_prime(unsigned long long *primes, unsigned long long to_add, int n_primes){
    primes[n_primes++] = to_add;
    return (n_primes);
}

int is_in_list(unsigned long long *primes, unsigned long long num){
    for(int i=0; i < MAX_N_PRIMES-1; i++){
        if (primes[i] == 0){
           return 0; 
        }
        if (primes[i] == num){
            return 1;
        }
    }
    return 0;
}

int factor(unsigned long long num, unsigned long long *factors){
    int n_factors = 0;
    unsigned long long max_f = sqrt(num) +1;

    for(unsigned long long i=2; i < max_f;){
        if(num % i == 0){
            factors[n_factors++] = i;
            num = num / i;
        }
        else{
            i++;
        }
    } 
    return n_factors;
}


unsigned long long max(unsigned long long *elements, unsigned n_elements){
    unsigned long long biggest = 0;
    for(int i = 0; i<n_elements; i++){
        if(elements[i] > biggest){
            biggest = elements[i];
        }
    }
    return biggest;
}

