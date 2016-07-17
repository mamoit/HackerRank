#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct Coord {
    int l;
    int c;
}Coord;

typedef struct Square {
    int l;
    int c;
    int w;
    int l1;
    int c1;
    int n;
}Square;

bool compare_square(Square* s1, Square* s2) {
    if( s1->l != s2->l ||\
        s1->c != s2->c ||\
        s1->w != s2->w) {
        return false;
    }
    return true;
}

int main() {
    int N;
    int S;
    int L;
    Square* square_buff = NULL;
    Square** R = NULL;
    int current_square = -1;

    unsigned long int current_knight = ULONG_MAX;
    Coord knight_coord;

    int buff;

    scanf("%d\n", &N);

    scanf("%d\n", &S);
    R = malloc(S*sizeof(Square*));

    for(int i=0; i<S; i++) {
        square_buff = malloc(sizeof(Square));
        square_buff->n = 0;
        scanf("%d %d %d\n", \
            &(square_buff->l), \
            &(square_buff->c), \
            &(square_buff->w));

        if(current_square <  0) {
            /* There is no square defined yet */
            current_square = 0;
            square_buff->l1 = square_buff->l + square_buff->w;
            square_buff->c1 = square_buff->c + square_buff->w;
            R[current_square] = square_buff;
        } else if (compare_square(square_buff, R[current_square])) {
            /* The current square is equal to the previous one */
            R[current_square]->n++;
            free(square_buff);
        } else {
            /* The current square is a new one */
            R[current_square]->n %= 4;
            current_square++;
            square_buff->l1 = square_buff->l + square_buff->w;
            square_buff->c1 = square_buff->c + square_buff->w;
            R[current_square] = square_buff;
        }
    }
    R[current_square]->n %= 4;

    scanf("%d\n", &L);

    for(int i=0; i<L; i++) {
        scanf("%ld\n", &current_knight);
        knight_coord.l = current_knight / N + 1;
        knight_coord.c = current_knight % N + 1;

        for(int j=0; j<=current_square; j++) {
            if(knight_coord.l < R[j]->l || knight_coord.l > R[j]->l1 || \
               knight_coord.c < R[j]->c || knight_coord.c > R[j]->c1) {
                break;
            } else {
                //rotate(&knight_coord, R[j]);
                switch (R[j]->n) {
                    case 0:
                        buff = knight_coord.l;
                        knight_coord.l = knight_coord.c - R[j]->c + R[j]->l;
                        knight_coord.c = R[j]->w - buff + R[j]->l + R[j]->c;
                        break;
                    case 1:
                        knight_coord.l = R[j]->w - knight_coord.l + 2*R[j]->l;
                        knight_coord.c = R[j]->w - knight_coord.c + 2*R[j]->c;
                        break;
                    case 2:
                        buff = knight_coord.l;
                        knight_coord.l = R[j]->w - knight_coord.c + R[j]->c + R[j]->l;
                        knight_coord.c = buff - R[j]->l + R[j]->c;
                        break;
                }
            }
        }
        printf("%d %d\n", knight_coord.l, knight_coord.c);
    }

    return 0;
}
