#include <stdio.h>
#include <threads.h>

//from threading import Thread, Lock
const int lenX = 14;
const int lenY = 20;

char labirinto[lenX][lenY] = {
        {"PPPPPPPPPPPPPPPPPPPP"},
        {"P                  P"},
        {"P         PPPPPP   P"},
        {"P   PPPP       P   P"},
        {"P   P        PPPP  P"},
        {"P PPP  PPPP        P"},
        {"P   P     P P      P"},
        {"P   P     P   PPP PP"},
        {"P   PPP PPP   P P  P"},
        {"P     P   P   P P  P"},
        {"PPP   P   PPPPP P  P"},
        {"P P      PP        P"},
        {"P P   PPPP   PPP   P"},
        {"P     P    S   P   P"},
        {"PPPPPPPPPPPPPPPPPPPP"},
    };

int Jogador(){

    int x = 1;
    int y = 1;

    if (labirinto[x][y] == ' '){
        labirinto[x][y] = 'O';
    }else{
        for (int i = 0; i < lenX; i++){
            for (int j = 0; j < lenY; j++){
                if (labirinto[i][j] == ' '){
                    labirinto[i][j] = 'O';
                }
            }
            
        }
    }


    // def move(self, dx, dy):
        
    //     # Move each axis separately. Note that this checks for collisions both times.
    //     if dx != 0:
    //         self.move_single_axis(dx, 0)
    //     if dy != 0:
    //         self.move_single_axis(0, dy)
    
    // def move_single_axis(self, dx, dy):
        
    //     # Move the rect
    //     self.rect.x += dx
    //     self.rect.y += dy

    //     # If you collide with a wall, move out based on velocity
    //     # for wall in walls:
    //     #     if self.rect.colliderect(wall.rect):
    //     #         if dx > 0: # Moving right; Hit the left side of the wall
    //     #             self.rect.right = wall.rect.left
    //     #         if dx < 0: # Moving left; Hit the right side of the wall
    //     #             self.rect.left = wall.rect.right
    //     #         if dy > 0: # Moving down; Hit the top side of the wall
    //     #             self.rect.bottom = wall.rect.top
    //     #         if dy < 0: # Moving up; Hit the bottom side of the wall
    //     #             self.rect.top = wall.rect.bottom
    return 0;
};

int desenharLabirinto(){
    for (int i = 0; i < lenX; i++){
        for (int j = 0; j < lenY; j++){
            printf("%c", labirinto[i][j]);
        }
        printf("\n");
    }
    return 0;
}

int main(){
    //P = Parede
    //S = Saída

    desenharLabirinto();
    //while(1):
    Jogador();
    printf("\n\nJogador Adicionado\n\n");
    desenharLabirinto();

    return 0;
};