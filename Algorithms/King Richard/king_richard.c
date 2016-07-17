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
    int n;
}Square;

void rotate(Coord* c, Square* square) {
    int buff;
    switch (square->n) {
        case 0:
            buff = c->l;
            c->l = c->c - square->c + square->l;
            c->c = square->w - buff + square->l + square->c;
            break;
        case 1:
            c->l = square->w - c->l + 2*square->l;
            c->c = square->w - c->c + 2*square->c;
            break;
        case 2:
            buff = c->l;
            c->l = square->w - c->c + square->c + square->l;
            c->c = buff - square->l + square->c;
            break;
        case 3:
            break;
    }
}

bool in_square(Coord* c, Square* square) {
    if((c->l >= square->l && c->l <= square->l + square->w) && \
       (c->c >= square->c && c->c <= square->c + square->w)) {
        return true;
    }
    return false;
}

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
            R[current_square] = square_buff;
        } else if (compare_square(square_buff, R[current_square])) {
            /* The current square is equal to the previous one */
            R[current_square]->n++;
            free(square_buff);
        } else {
            /* The current square is a new one */
            R[current_square]->n %= 4;
            current_square++;
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
            if(!in_square(&knight_coord, R[j])) {
                break;
            }
            rotate(&knight_coord, R[j]);
        }
        printf("%d %d\n", knight_coord.l, knight_coord.c);
    }

    return 0;
}
