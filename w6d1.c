#include <stdio.h>
#include <ctype.h>

void presentazione(){
    printf("benvenuti ar quiz sulla roma\n");
    
}
char menù_scelta(){
    char scelta;
    printf("menù\n");
    printf("sceglia A per inizare un partita\n");
    printf("scegli B per uscire dal gioco\n");
    printf("scegli ? \n");
    scanf(" %c" , &scelta);
    return scelta;
}
int giocare(){
    int punteggio = 0;
    char risposta;
    char nome[50];

    printf("inserisci il tuo nome\n");
    scanf(" %s", nome );
    printf("\n benvenuo %s", nome);
    printf(" inizamo una nuova partita!\n");
    
    //domanda 1
    printf("quanti scudetti ha vinto la roma ?\n");
    printf("A)1\nB)2\nC)3\n");
    scanf(" %c", & risposta);
    if  (toupper(risposta) == 'C'){
        printf("bravo\n");
        punteggio++;
    }
    else
    printf("Ah laziale, te piacerebbeeee\n");
   //domanda2
    printf("quanti gol ha fatto Dovbyk in serie A?\n");
    printf("A)9\nB)11\nC)15\n");
    scanf(" %c", &risposta);
    if(toupper(risposta) =='B'){
        printf("bravo Bomber di la verità ce l'hai al fanta!!\n");
        punteggio++;
    }
    else{
        printf("seeee datte alla palla a volo\n");
    }
    printf("in quale stagione totti ha vinto la scarpa d'oro ? \n");
    printf("A)2007\nB)2010\nC)2009\n");
    scanf(" %c", &risposta);
    if(toupper(risposta) == 'A') {
        printf("bello pupone\n");
        punteggio++;
    }
    else{
        printf("tranqullo sei solo era difficile per chiunque non fosse della roma\n");
    }

    printf("partita finita hai realizzato %d punti\n" , punteggio);
return punteggio;
}
int main(){
    char scelta;
    presentazione ();
    do {
        scelta =  menù_scelta();
        switch(toupper(scelta)){
        case 'A' : giocare();
            break;
        case 'B' : printf("Arrivederci\n");
            break;
        default : printf("scelta non valida. Riprova\n");
        }
    }
    while (toupper(scelta) != 'B');
    return 0;
}