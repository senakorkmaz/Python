#include<graphics.h>
int main()
{
    int x=0, y=0;
    char say1[5], say2[5];
    initwindow(800,600);
    rectangle(20,20,40,40); // hiç bir amacı yok çok sade kalmasın diye çizdim. 

    while(!ismouseclick(WM_LBUTTONDOWN)) {
        outtextxy(50,50,"tıkla");
    }

    while(ismouseclick(WM_LBUTTONDOWN)){
        getmouseclick(WM_LBUTTONDOWN,x,y);
        sprintf(say1,"x:%d",x);
        sprintf(say2,"y:%d",y);
        outtextxy(100,50,say1);
        outtextxy(150,50,say2);
     }

    getch();
    closegraph();
    return 0;
}