// http://paste.ubuntu.com/598838/

#include<windows.h>
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#define RAND 1
#define G gotoxy

HANDLE  hConsoleOut = 0;                   /* Handle to the console */
CONSOLE_SCREEN_BUFFER_INFO csbiInfo;   /* Console information */
CHAR attribute;

void initvideo()
{
  hConsoleOut = GetStdHandle(STD_OUTPUT_HANDLE);
  GetConsoleScreenBufferInfo(hConsoleOut, &csbiInfo);
  attribute = 0x07;
}

void gotoxy(int column, int row)
{
  COORD c;

  c.X = column - 1;
  c.Y = row - 1;
  SetConsoleCursorPosition(hConsoleOut, c);
}

void clrscr(void)
{
  COORD c;
  DWORD len, wr;

  if(!hConsoleOut)
    initvideo();

  len = csbiInfo.dwSize.X * csbiInfo.dwSize.Y;
  c.X = c.Y = 0;
  FillConsoleOutputCharacter(hConsoleOut, ' ', len, c, &wr);
  FillConsoleOutputAttribute(hConsoleOut, attribute, len, c, &wr);

  gotoxy(1, 1);
}

void delay(DWORD milliseconds)
{
  Sleep(milliseconds);
}



void grande(int a){
switch(a){
case 65 :
G(60,5); puts(" _______");
G(60,6); puts("|       |");
G(60,7); puts("|_______|");
G(60,8); puts("|       |");
G(60,9); puts("|       |");
G(60,10);puts("|       |");

     break;
case 66 :
G(60,5); puts(" _______");
G(60,6); puts("|       \\");
G(60,7); puts("|_______/");
G(60,8); puts("|       \\");
G(60,9); puts("|        |");
G(60,10);puts("|________/");
     break;
case 67 :
G(60,5); puts(" _________");
G(60,6); puts("|            ");
G(60,7); puts("|            ");
G(60,8); puts("|            ");
G(60,9); puts("|            ");
G(60,10);puts("|_________");
     break;
case 68 :
G(60,5); puts(" _______");
G(60,6); puts("|       \\");
G(60,7); puts("|        \\");
G(60,8); puts("|        |");
G(60,9); puts("|        /");
G(60,10);puts("|_______/");
     break;
case 69 :
G(60,5); puts(" _______");
G(60,6); puts("|");
G(60,7); puts("|");
G(60,8); puts("|-----");
G(60,9); puts("|");
G(60,10);puts("|_______");
     break;
case 70 :
G(60,5); puts(" ________");
G(60,6); puts("|");
G(60,7); puts("|________");
G(60,8); puts("|");
G(60,9); puts("|");
G(60,10);puts("|");
     break;
case 71 :
G(60,5); puts(" ________");
G(60,6); puts("|");
G(60,7); puts("|");
G(60,8); puts("|    ____");
G(60,9); puts("|        |");
G(60,10);puts("|________|");
     break;
case 72 :
G(60,5); puts(" ");
G(60,6); puts("|        |");
G(60,7); puts("|        |");
G(60,8); puts("|--------|");
G(60,9); puts("|        |");
G(60,10);puts("|        |");
     break;
case 73 :
G(60,5); puts("    .    ");
G(60,6); puts("    |    ");
G(60,7); puts("    |    ");
G(60,8); puts("    |    ");
G(60,9); puts("    |    ");
G(60,10);puts("    |    ");
     break;
case 74 :
G(60,5); puts("      .  ");
G(60,6); puts("      |  ");
G(60,7); puts("      |  ");
G(60,8); puts("      |  ");
G(60,9); puts(" |    |  ");
G(60,10);puts(" |____|  ");
     break;
case 75 :
G(60,5); puts("|   / ");
G(60,6); puts("|  /");
G(60,7); puts("| /");
G(60,8); puts("| \\ ");
G(60,9); puts("|  \\");
G(60,10);puts("|   \\  ");
     break;
case 76 :
G(60,5); puts("|        ");
G(60,6); puts("|         ");
G(60,7); puts("|         ");
G(60,8); puts("|         ");
G(60,9); puts("|         ");
G(60,10);puts("|______         ");
     break;
case 77 :
G(60,5); puts("        ");
G(60,6); puts("|\\    /|  ");
G(60,7); puts("| \\  / |   ");
G(60,8); puts("|  \\/  |   ");
G(60,9); puts("|      |");
G(60,10);puts("|      | ");
     break;
case 78 :
G(60,5); puts("        ");
G(60,6); puts("|\\    |  ");
G(60,7); puts("| \\   |   ");
G(60,8); puts("|  \\  |   ");
G(60,9); puts("|   \\ |");
G(60,10);puts("|    \\| ");
     break;
case 79 :
G(60,5); puts(" _______");
G(60,6); puts("|       |");
G(60,7); puts("|       |");
G(60,8); puts("|       |");
G(60,9); puts("|       |");
G(60,10);puts("|_______|");
     break;
case 80 :
G(60,5); puts(" _______");
G(60,6); puts("|       \\");
G(60,7); puts("|        |");
G(60,8); puts("|_______/");
G(60,9); puts("|       ");
G(60,10);puts("|       ");
     break;
case 81 :
G(60,5); puts(" _______");
G(60,6); puts("|       |");
G(60,7); puts("|       |");
G(60,8); puts("|  __   |");
G(60,9); puts("|    \\__|");
G(60,10);puts("|_______|");
    break;
case 82 :
G(60,5); puts(" ______");
G(60,6); puts("|      \\");
G(60,7); puts("|       |");
G(60,8); puts("|______/");
G(60,9); puts("|      \\");
G(60,10);puts("|       \\");
     break;
case 83 :
G(60,5); puts(" _______");
G(60,6); puts("|       ");
G(60,7); puts("|       ");
G(60,8); puts(" -------");
G(60,9); puts("        |");
G(60,10);puts(" _______|");
     break;
case 84 :
G(60,5); puts(" _______");
G(60,6); puts("    |   ");
G(60,7); puts("    |   ");
G(60,8); puts("    |   ");
G(60,9); puts("    |   ");
G(60,10);puts("    |   ");
     break;
case 85 :
G(60,5); puts("        ");
G(60,6); puts("|       |");
G(60,7); puts("|       |");
G(60,8); puts("|       |");
G(60,9); puts("|       |");
G(60,10);puts("|_______|");
     break;
case 86 :
G(60,5); puts("");
G(60,6); puts("\\        / ");
G(60,7); puts(" \\      /  ");
G(60,8); puts("  \\    /   ");
G(60,9); puts("   \\  /    ");
G(60,10);puts("    \\/     ");
     break;
case 87 :
G(60,5); puts("|      |   ");
G(60,6); puts("|      |   ");
G(60,7); puts("|  /\\  |  ");
G(60,8); puts("| /  \\ |  ");
G(60,9); puts("|/    \\|   ");
G(60,10);puts("");
     break;
case 88 :
G(60,5); puts("\\    / ");
G(60,6); puts(" \\  /  ");
G(60,7); puts("  \\/   ");
G(60,8); puts("  /\\   ");
G(60,9); puts(" /  \\  ");
G(60,10);puts("/    \\ ");
     break;
case 89 :
G(60,5); puts("\\    / ");
G(60,6); puts(" \\  /  ");
G(60,7); puts("  \\/   ");
G(60,8); puts("  /     ");
G(60,9); puts(" /      ");
G(60,10);puts("/       ");
     break;
case 90 :
G(60,5); puts(" _______ ");
G(60,6); puts("       / ");
G(60,7); puts("     /     ");
G(60,8); puts("    /      ");
G(60,9); puts("   /       ");
G(60,10);puts(" /______        ");
 break;
default:
G(60,5); puts("         ");
G(60,6); puts("         ");
G(60,7); puts("         ");
G(60,8); puts("         ");
G(60,9); puts("         ");
G(60,10);puts("         ");
break;
      } // fim do switch(a)
     } // fim da fun  o grande

int gamedig(){
int letra=0,coluna=0,rodada=0,col[50],tempo=400,lin[20],jafoi[20];
int qtd=0,pontos=0,flag=2,matrizx[50],matrizy[20],erradas=0,cai=0,flag2=0;
int lugar[3];  double pontuacao[3];
char *nomes1[30], *nomes2[30], *nomes3[30];
int dezoito=0,m=4;
double ponto=0;
char caracter[20],digito;
for(int i=0;i<20;i++)jafoi[i]=0;
for(int i=0;i<50;i++)matrizx[i]=0;
for(int j=0;j<20;j++)matrizy[j]=0;
clrscr();
G(1,5);
int n=0;
clrscr();
gotoxy(7,20);printf("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
while(erradas<20){ // inicializa enquanto infinito
//if(rand()%RAND < RAND/3)  { // abre rodada de inatividade

letra=rand()%26 + RAND;
letra=letra%26 + 65;


if(jafoi[rodada]==0){ caracter[rodada]=letra; qtd++; jafoi[rodada]=1;
                      coluna=rand()%50 + RAND;
                      col[rodada]=coluna % 50 + 7; lin[rodada]=1;
}

//jafoi[rodada]=1;
if(qtd%20==0){
if(tempo>39)tempo=tempo-20;
for(int i=0;i<20;i++)jafoi[i]=0;
for(int i=0;i<50;i++)matrizx[i]=0;
for(int j=0;j<20;j++)matrizy[j]=0;
rodada=0;
               }
//rodada=(rodada+1)%20;
for(int i=0;i<20;i++)if(jafoi[rodada]==0){rodada=i;break;}

//for(int i=0;i<rodada;i++){ G(col[i],lin[i]);printf(" ");    }
//for(int i=0;i<qtd;i++){ G(col[i],lin[i]);printf(" ");    }
//if(rodada==0)clrscr();
for(int i=0;i<50;i++)
for(int j=0;j<20;j++){
        if(matrizx[i]==1 && matrizy[j]==1){
        G(matrizx[i],matrizy[j]);printf(" ");
        matrizx[i]=0; matrizy[j]=0;         }        // apagar
                      } // fecha for j

for(int i=0;i<qtd%20;i++){
      if(jafoi[i]==1){
      matrizx[col[i]]=1;       matrizy[lin[i]]=1;
      lin[i]+=1%20;
      if(lin[i]==19){// pontos--;
                     lin[i]=0; jafoi[i]=0;
                     cai=(cai%100)+1;
      gotoxy(col[i],lin[i]-1);printf(" ");
      matrizx[col[i]]=1;       matrizy[lin[i]]=1;
      continue;
      }
// imprime letra ao lado direito
G(60,5); puts("            ");
G(60,6); puts("            ");
G(60,7); puts("            ");
G(60,8); puts("            ");
G(60,9); puts("            ");
G(60,10);puts("            ");
grande(caracter[i]);
// fim imprime letra ao lado direito
delay(15);

      gotoxy(col[i],lin[i]-1);printf(" ");
      gotoxy(col[i],lin[i]);printf("%c",caracter[i]);

      matrizx[col[i]]=1;
      matrizy[lin[i]]=1;
                       }
                        }
if(kbhit()){ // se uma tecla for pressionada
G(2,22);digito=getche();
G(2,22);printf(" ");
if(digito==-32){      G(1,23);getche();           }
if(digito==13){      G(1,23);getche();           }
if(digito==27){clrscr(); break; }
flag=0;
for(int i=0;i<qtd%20;i++){
        if(digito==caracter[i] || digito==caracter[i]+32){
        gotoxy(col[i],lin[i]-1);printf(" ");
        gotoxy(col[i],lin[i]);printf(" ");
        jafoi[i]=0;         pontos++;
        ponto=ponto+0.000001;
        flag=1;
                                              } // SE ACERTOU TECLA PRESSIONADA
                          }
if(digito=='+'){if(tempo>=20)tempo=tempo-10; flag=1;}
            } // fim se uma tecla for pressionada
if(flag==0 && (digito!=13 && digito!=32)){erradas++;}
if(cai%10==0 && flag2==1){
             dezoito=(dezoito%18)+1;
             if(dezoito==18)erradas++;
                            }// a cada 20 perdidas 1 errada
if(cai>0)flag2=1;                       //  flag para que n o comece perdendo
//                            } // fecha rodada de inatividade
//gotoxy(7,1);printf("                                                   ");
gotoxy(10,21);printf("erradas: %d",erradas);
G(25,21);printf("perdidas  :       ");
G(25,21);printf("perdidas: %d",cai);
G(40,23);printf("      velocidade: %d", 10000/tempo);
G(10,23);printf("level: %d", qtd/20+1);
gotoxy(1,22);printf("                                                        ");
G(1,21);printf("R$:%d,00",(int)((1000000*ponto)*(rodada+2)));
G(1,22);printf("\nrodada: %d\tdigito=%c\tqtd:%d\n",rodada,digito,qtd);
printf("digite + para aumentar a velocidade ");
gotoxy(40,21);printf("pontos:                      ");
gotoxy(40,21);printf("pontos: %f",ponto);
if(tempo<10)tempo=10;
while(kbhit()){
//     G(2,22);
     digito=getche();
     if(digito=='+'){if(tempo>=20)tempo=tempo-10; flag=1;}
              }
gotoxy(40,21);printf("pontos: %f              ",ponto);
delay(tempo); // tempo de inatividade
digito=32;
//rodada=(rodada+1)%20;
          } // enquanto infinito
clrscr();

printf("voc%c",136);puts(" Perdeu!!!!");
if(erradas>=20)puts("\nErrou 20 vezes!!!");
delay(2000);getche();
ponto=ponto+0.000001;

pontos=(int)((1000000*ponto)*(rodada+2));
return(pontos);

     } // fim m todo main
/*
void grande(int a){
switch(a){
case 65 :
G(60,5); puts(" _______");
G(60,6); puts("|       |");
G(60,7); puts("|_______|");
G(60,8); puts("|       |");
G(60,9); puts("|       |");
G(60,10);puts("|       |");

     break;
case 66 :
G(60,5); puts(" _______");
G(60,6); puts("|       \\");
G(60,7); puts("|_______/");
G(60,8); puts("|       \\");
G(60,9); puts("|        |");
G(60,10);puts("|________/");
     break;
case 67 :
G(60,5); puts(" _________");
G(60,6); puts("|            ");
G(60,7); puts("|            ");
G(60,8); puts("|            ");
G(60,9); puts("|            ");
G(60,10);puts("|_________");
     break;
case 68 :
G(60,5); puts(" _______");
G(60,6); puts("|       \\");
G(60,7); puts("|        \\");
G(60,8); puts("|        |");
G(60,9); puts("|        /");
G(60,10);puts("|_______/");
     break;
case 69 :
G(60,5); puts(" _______");
G(60,6); puts("|");
G(60,7); puts("|");
G(60,8); puts("|-----");
G(60,9); puts("|");
G(60,10);puts("|_______");
     break;
case 70 :
G(60,5); puts(" ________");
G(60,6); puts("|");
G(60,7); puts("|________");
G(60,8); puts("|");
G(60,9); puts("|");
G(60,10);puts("|");
     break;
case 71 :
G(60,5); puts(" ________");
G(60,6); puts("|");
G(60,7); puts("|");
G(60,8); puts("|    ____");
G(60,9); puts("|        |");
G(60,10);puts("|________|");
     break;
case 72 :
G(60,5); puts(" ");
G(60,6); puts("|        |");
G(60,7); puts("|        |");
G(60,8); puts("|--------|");
G(60,9); puts("|        |");
G(60,10);puts("|        |");
     break;
case 73 :
G(60,5); puts("    .    ");
G(60,6); puts("    |    ");
G(60,7); puts("    |    ");
G(60,8); puts("    |    ");
G(60,9); puts("    |    ");
G(60,10);puts("    |    ");
     break;
case 74 :
G(60,5); puts("      .  ");
G(60,6); puts("      |  ");
G(60,7); puts("      |  ");
G(60,8); puts("      |  ");
G(60,9); puts(" |    |  ");
G(60,10);puts(" |____|  ");
     break;
case 75 :
G(60,5); puts("|   / ");
G(60,6); puts("|  /");
G(60,7); puts("| /");
G(60,8); puts("| \\ ");
G(60,9); puts("|  \\");
G(60,10);puts("|   \\  ");
     break;
case 76 :
G(60,5); puts("|        ");
G(60,6); puts("|         ");
G(60,7); puts("|         ");
G(60,8); puts("|         ");
G(60,9); puts("|         ");
G(60,10);puts("|______         ");
     break;
case 77 :
G(60,5); puts("        ");
G(60,6); puts("|\\    /|  ");
G(60,7); puts("| \\  / |   ");
G(60,8); puts("|  \\/  |   ");
G(60,9); puts("|      |");
G(60,10);puts("|      | ");
     break;
case 78 :
G(60,5); puts("        ");
G(60,6); puts("|\\    |  ");
G(60,7); puts("| \\   |   ");
G(60,8); puts("|  \\  |   ");
G(60,9); puts("|   \\ |");
G(60,10);puts("|    \\| ");
     break;
case 79 :
G(60,5); puts(" _______");
G(60,6); puts("|       |");
G(60,7); puts("|       |");
G(60,8); puts("|       |");
G(60,9); puts("|       |");
G(60,10);puts("|_______|");
     break;
case 80 :
G(60,5); puts(" _______");
G(60,6); puts("|       \\");
G(60,7); puts("|        |");
G(60,8); puts("|_______/");
G(60,9); puts("|       ");
G(60,10);puts("|       ");
     break;
case 81 :
G(60,5); puts(" _______");
G(60,6); puts("|       |");
G(60,7); puts("|       |");
G(60,8); puts("|  __   |");
G(60,9); puts("|    \\__|");
G(60,10);puts("|_______|");
    break;
case 82 :
G(60,5); puts(" ______");
G(60,6); puts("|      \\");
G(60,7); puts("|       |");
G(60,8); puts("|______/");
G(60,9); puts("|      \\");
G(60,10);puts("|       \\");
     break;
case 83 :
G(60,5); puts(" _______");
G(60,6); puts("|       ");
G(60,7); puts("|       ");
G(60,8); puts(" -------");
G(60,9); puts("        |");
G(60,10);puts(" _______|");
     break;
case 84 :
G(60,5); puts(" _______");
G(60,6); puts("    |   ");
G(60,7); puts("    |   ");
G(60,8); puts("    |   ");
G(60,9); puts("    |   ");
G(60,10);puts("    |   ");
     break;
case 85 :
G(60,5); puts("        ");
G(60,6); puts("|       |");
G(60,7); puts("|       |");
G(60,8); puts("|       |");
G(60,9); puts("|       |");
G(60,10);puts("|_______|");
     break;
case 86 :
G(60,5); puts("");
G(60,6); puts("\\        / ");
G(60,7); puts(" \\      /  ");
G(60,8); puts("  \\    /   ");
G(60,9); puts("   \\  /    ");
G(60,10);puts("    \\/     ");
     break;
case 87 :
G(60,5); puts("|      |   ");
G(60,6); puts("|      |   ");
G(60,7); puts("|  /\\  |  ");
G(60,8); puts("| /  \\ |  ");
G(60,9); puts("|/    \\|   ");
G(60,10);puts("");
     break;
case 88 :
G(60,5); puts("\\    / ");
G(60,6); puts(" \\  /  ");
G(60,7); puts("  \\/   ");
G(60,8); puts("  /\\   ");
G(60,9); puts(" /  \\  ");
G(60,10);puts("/    \\ ");
     break;
case 89 :
G(60,5); puts("\\    / ");
G(60,6); puts(" \\  /  ");
G(60,7); puts("  \\/   ");
G(60,8); puts("  /     ");
G(60,9); puts(" /      ");
G(60,10);puts("/       ");
     break;
case 90 :
G(60,5); puts(" _______ ");
G(60,6); puts("       / ");
G(60,7); puts("     /     ");
G(60,8); puts("    /      ");
G(60,9); puts("   /       ");
G(60,10);puts(" /______        ");
 break;
default:
G(60,5); puts("         ");
G(60,6); puts("         ");
G(60,7); puts("         ");
G(60,8); puts("         ");
G(60,9); puts("         ");
G(60,10);puts("         ");
break;
      } // fim do switch(a)



     } // fim da fun  o grande
*/
void snake(int){
int vetor[2000],vetorx[2000];
int limpa[2000],limpax[2000],limpatam=-1;
int tam=0,v=0,x1=0,y1=0,perdeu=0,y3=0;

       int w=0,time=100,d=0,velo=0,anted=0,random=0,r1=30,r2=15,anterandom=0;
       int comparede=0,level=1,rapido=1,saiu=0;
       //float tempo;
       int n1,n2,n3,n4,n32, nt,nn3;
       n1=n2=n3=nt=n4=0; n32=1;
       char c='f';
//       char ops[25];
//       for(int i=0;i<25;i++)ops[i]='a';
       clrscr();
//       int vetor[20];
       int x=10,y=10,qtd=0,pausa=0;
       //tempo=clock();

       while (1){

       clrscr();

       G(20,y3+5);puts("\x1");
       G(25,5);puts("SEM PAREDE");
       G(25,10);puts("COM PAREDE");
       G(25,15);puts("SAIR");
       c=getche();
       if(c=='e' || c==72)y3=y3-5;
       if(c=='d' || c==80)y3=y3+5;
       if(y3>10)y3=0;
       if(y3<0 )y3=10;
       if(c==13){
       G(20,y3+5);puts("            ");
       G(25,5);puts("               ");
       G(25,10);puts("              ");
       G(25,15);puts("              ");
                 if(y3==10)exit(2);
                 if(y3==0)break;
                 if(y3==5){comparede=1;break;}
                 }
             }
       c='f';
       while (1){
    //   clrscr();
      if(tam==0){
                 G(vetorx[0],vetor[0]);puts(" ");
                 }
      for(int i=0;i<limpatam;i++){
      G(vetorx[i],vetor[i]);puts(" ");
                                  }
       if(random>anterandom){
        anterandom=random;
        for(int i=0;i<qtd%20;i++)r1=rand()%67;
        r1+=3;
        for(int i=0;i<qtd%20;i++)r2=rand()%19;
        r2+=3;
                             }

       anted=d;
       if(c==-32)c=getche();
       rapido=0;
       if(c==77 && d!=2)d=0;
       if(c==72 && d!=3)d=1;
       if(c==75 && d!=0)d=2;
       if(c==80 && d!=1)d=3;
       if(c==13)d=4;
       if(w==1)if(c==32)rapido=1;
       else  if(c==27){saiu=1;break;}
       else  if(c=='p')pausa=1;
     //  else  if(c=='q')time=1000;
       if(tam>0){
       v=v%tam;
       vetorx[v]=x;
       vetor[v]=y;
       v++;}
       switch(d){
       case 0:x++;break;
       case 1:y--;break;
       case 2:x--;break;
       case 3:y++;break;
       case 4:y++;x--;break;
                 }
       for(int i=2;i<25;i++){
       G(2,i); puts("\xBA");
       G(73,i);puts("\xBA");
               }
       for(int i=3;i<73;i++){
       G(i,2); puts("\xCD");
       G(i,25);puts("\xCD");
               }
       G(73,2);puts("\xBB");
       G(2,25);puts("\xC8");
       G(2,2); puts("\xC9");
      G(73,25);puts("\xBC");
      G(75,3);printf("LEVEL:");
      G(75,4);printf("%d",level);
      G(75,5);printf("PONTOS");
      G(75,6);printf(":%d",tam);
      G(75,7); printf("___");
      G(75,8); printf("WIL");
      G(75,9); printf(" & ");
      G(75,10);printf("VIT");
      G(75,11);printf("\xEE\xEE\xEE");
      printf("%c",c);
      //G(75,6);  puts("TEMPO:");
      //G(75,7);printf("%d:%d:%d",hora,min,nt);
      //G(2,30);printf("tempo: %f",tempo);

       if(comparede==1){if(x>71 || y>24 || x<3 || y<3)perdeu=1;}
       //if(rede==1)exit(2);
       if(x>71)x=3;
       if(y>24)y=3;
       if(x<3)x=71;
       if(y<3)y=24;


//       G(x,y);puts("\xDB");
       G(x,y);puts("\xFA");
       if(tam==0){
         vetorx[0]=x;
         vetor[0]=y;
                  }
       for(int i=0;i<tam;i++){
//       G(vetorx[i],vetor[i]);puts("\xDB");
G(vetorx[i],vetor[i]);puts("\xFE");
limpax[i]=vetorx[i];
limpa[i]=vetor[i];
limpatam=tam;
if(vetorx[i]==x&&vetor[i]==y)perdeu=1;
                            }
       w=kbhit();
       if(w==1){
       qtd++;
       G(70,24); c=getch();
       G(70,24);puts(" ");
       /*case 's':break;
       case 'f':break;
       case 'e':break;
       case 'd':break;*/
                }

       if(x==r1 && y==r2){random++;tam++;}
       G(r1,r2);
       //printf("%d-%d",random,d);
       //tempo=clock();
       if(pausa==1){getch();pausa=0;c='a'; }
      if(rapido==0)delay(time/level);
      if(rapido!=0)delay((time/(level+1)));
       if(random%10==0 && anterandom!=random)level++;
       qtd++;
       qtd=qtd%60;
//       time=100;
       if(perdeu==1)break;
       }
       clrscr();
       G(1,1);
if(saiu==0){
puts("            ______     _______   _______");
puts("\\        / |      |   |         |       ");
puts(" \\      /  |      |   |         |       ");
puts("  \\    /   |      |   |         |----   ");
puts("   \\  /    |      |   |         |       ");
puts("    \\/     |______|   |_______  |_______");
puts("\n");
puts(" _______    ______   ______     _____   ______  ___   ___  ||| ");
puts("|       )  |        |      )   |     \\ |        ---   ---  |||");
puts("|------    |___     |------\\   |      ||___     ---   ---  |||");
puts("|          |        |       \\  |      ||         --   --   |||");
puts("|          |______  |        | |_____/ |______    -___-     0 ");
getch();
        }
}
/*
void smacia(int x, int y){
int sx=35, sy=15;
G(10,10);puts("\x1:");
G(10,11);puts("a");W;puts(" ");W;puts("S");W;puts("u");W;puts("p");W;puts("r");
W;puts("e");W;puts("m");W;puts("a");W;puts("c");W;puts("i");W;puts("a");W;
puts("!");W;puts("!");W;puts("!");W;
clrscr();
//tela 13 vila
while(sy>9){
G(18,19);puts(" ____ ");
G(18,20);puts("|    |");
G(18,21);puts("|   c|");
G(18,22);puts("|    |");
G(32,19);puts("==================");
G(33,20);puts("||\\_/| |   |   |");
G(33,21);puts("|||_|| |  c|   |");
G(33,22);puts("||/ \\| |   |   |");
G(51,19);puts("| 71 |");
G(51,20);puts("|    |");
G(51,21);puts("|   c|");
G(51,22);puts("|    |");
G(7,20);printf("\xDC\xB0\xB0\xDC");
G(7,21);printf("\xB0\xB0\xB8\xB0");
G(7,22);printf("\xDB\xB0\xB0\xDB");
G(1,23);
puts("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW");
G(x+1,y);puts("\x1");
G(x,y+1);puts("/#\\");
G(x,y+2);puts("/ \\");
G(sx,sy);puts("\xCF");
delay(500);
sy--;
           }

} */
void copper(void){
     clrscr();
int y=0;
char string1[100]={"Depois de um momento voc\x88 vai entrar em um mundo de magia"};
char string2[100]={"Voc\x88 testemunhar\xA0 o incr\xA1vel!"};
char string3[100]={"Voc\x88 \x82 parte de uma ilus\xC6o... "};
char string4[100]={"Ilus\xC6o de Copperfield"};
char string5[100]={"Neste programa simples voc\x88 ver\xA0, "};
char string6[100]={"Que eu posso dizer o que voc\x88 pensa, por seu computador..."};
char string7[100]={"Voc\x88 pode ver 6 cartas."};
char string8[100]={"Pense num deles"};
char string9[100]={"Somente pense."};
char string10[100]={"N\xC6o clique isto."};
char string11[100]={"Pense agora"};
char string12[100]={"Examine meus olhos.  Somente pense sobre sua carta."};
char string13[100]={"\t\tEu n\xC6o fa\x87o saiba voc\x88. \n\t\tEu n\xC6o posso ver voc\x88...\n\t\tMas eu sei o que voc\x88 pensa."};
char string14[100]={"\t\tOlhe,\n\t\t Eu levei\n\t\t sua carta !!! "};
char string15[100]={"Eu sabia\n\t\t da escolha que voc\x88\n\t\t estaria fazendo!"};
//G(10,10);printf("Depois de um momento
for(int i=0;i<strlen(string1);i++){
G(10+i,10);printf("%c",string1[i]);delay(70);
                                   }
delay(1000);
G(10,10);puts("                                                          ");
for(int i=0;i<strlen(string2);i++){
G(10+i,10);printf("%c",string2[i]);delay(70);
                                    }
delay(1000);
G(10,10);puts("                                                          ");

for(int i=0;i<strlen(string3);i++){
G(10+i,10);printf("%c",string3[i]);delay(70);
                                    }
delay(1000);
G(10,10);puts("                                                          ");

G(60,4);printf(" !!!!!!!!!!!");
G(60,5);printf(" |          | ");
G(60,6);printf("(  0    0    )");
G(60,7);printf(" |   <      |");
G(60,8);printf(" | ______   |");
G(60,9);printf(" |__________|");
for(int i=0;i<strlen(string4);i++){
G(10+i,10);printf("%c",string4[i]);delay(70);
                                    }
delay(3000);
G(10,10);puts("                                                          ");

for(int i=0;i<strlen(string5);i++){
G(10+i,10);printf("%c",string5[i]);delay(70);
                                    }
delay(1000);
G(10,10);puts("                                                          ");

for(int i=0;i<strlen(string6);i++){
G(10+i,11);printf("%c",string6[i]);delay(70);
                                    }
delay(1000);
G(10,11);puts("                                                          ");


G(9,17);printf(" ____  ___  ___  ___  ___  ___");
G(9,18);printf("|K   ||J  ||K  ||Q  ||Q  ||J  |");
G(9,19);printf("|  %C || %C || %C || %C || %C || %C |",3,6,6,4,5,4);
G(9,20);printf("|___K||__J||__K||__Q||__Q||__J|");
//G(9,15);printf("");
//G(9,15);printf("");

for(int i=0;i<strlen(string7);i++){
G(10+i,10);printf("%c",string7[i]);delay(70);
                                    }
delay(1000);
//G(10,10);puts("                                                          ");

for(int i=0;i<strlen(string8);i++){
G(10+i,11);printf("%c",string8[i]);delay(70);
                                    }
delay(1000);
//G(10,10);puts("                                                          ");

for(int i=0;i<strlen(string9);i++){
G(10+i,12);printf("%c",string9[i]);delay(70);
                                    }
delay(1000);
//G(10,1);puts("                                                          ");

for(int i=0;i<strlen(string10);i++){
G(10+i,13);printf("%c",string10[i]);delay(70);
                                    }
delay(1000);
//G(10,10);puts("                                                          ");

for(int i=0;i<strlen(string11);i++){
G(10+i,14);printf("%c",string11[i]);delay(70);
                                    }
delay(1000);
//G(10,10);puts("                                                          ");
G(10,15);
printf("Pressione o barra espa%co ...",135);getch();

for(int i=10;i<21;i++){
G(9,i);
printf("                                                                       ");
        }
for(int i=0;i<strlen(string12);i++){
G(10+i,10);printf("%c",string12[i]);delay(70);
                                    }
delay(1000);
G(10,10);puts("                                                          ");
G(1,10);
for(int i=0;i<strlen(string13);i++){
//G(10+i,10);
printf("%c",string13[i]);delay(70);
if(string13[i]=='\n'){delay(1000);printf("\n");}
                                    }
delay(1000);
G(1,10);puts("                                                                                ");
G(1,11);puts("                                                                                ");
G(1,12);puts("                                                                                ");
G(1,13);puts("                                                                                ");
G(1,14);puts("                                                                                ");
G(1,15);puts("                                                                                ");

G(1,10);
for(int i=0;i<strlen(string14);i++){
//G(10+i,10+y);
printf("%c",string14[i]);delay(70);
if(string14[i]=='\n'){delay(1000);y++;printf("\n");}
                                    }
delay(1000);
G(10,10);puts("                                                          ");
G(10,11);puts("                                                          ");
G(10,12);puts("                                                          ");
G(10,13);puts("                                                          ");
G(10,14);puts("                                                          ");
G(10,15);puts("                                                          ");

G(9,17);printf(" ____  ___  ___  ___  ___ ");
G(9,18);printf("|Q   ||K  ||J  ||Q  ||K  |");
G(9,19);printf("|  %C || %C || %C || %C || %C |",3,5,3,6,4);
G(9,20);printf("|___Q||__K||__J||__Q||__K|");

delay(4000);

for(int i=0;i<strlen(string15);i++){
G(10+i,10);printf("%c",string15[i]);delay(70);
if(string15[i]=='\n')delay(1000);
                                    }
delay(1000);
G(10,10);puts("                                                          ");
     }
 int main(){
//int valor=gamedig();
 //copper();
 snake(1);

clrscr();
printf("Bastaria as pessoas serem mais sinceras, honestas e humildes,\n");
printf(" que ver amos comportamentos maravilhosamente diversificados, \n");
printf("personalidades espontaneamente interessantes, decis es amplamente\n");
printf("mais libertas, preconceitos instantanemente eliminados e atitudes \n");
printf("surpeendentemente menos ego stas.\n");
printf("                                                     ( NeoqJav )\n");

getch();
}



