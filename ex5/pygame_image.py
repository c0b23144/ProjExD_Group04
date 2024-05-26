import os
import sys
import pygame as pg
import time

WIDTH, HEIGHT = 1600, 900
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Time():
    """
    時間の表示
    """
    def __init__(self):
        self.font = pg.font.Font(None, 50)
        self.tmr = 10
        self.txt = self.font.render(str(self.tmr), True, (255, 255, 255))
    
    def update(self, screen: pg.Surface):
        self.txt = self.font.render(str(self.tmr), True, (255, 255, 255))
        screen.blit(self.txt, [800, 0])




def GameOver():
    """
    ゲームオーバー画面の表示
    ブラックアウト画面の設定→文字表示の設定→こうかとん表示の設定
    スクリーン表示とディスプレイ更新
    """
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    #ゲームオーバー画面
    gm_img = pg.Surface((WIDTH,HEIGHT))  #ブラックアウト
    pg.draw.rect(gm_img,(0),(0,0,WIDTH,HEIGHT))
    gm_img.set_alpha(150) #半透明
    gm_rct = gm_img.get_rect()
    gm_rct.center = WIDTH/2, HEIGHT/2
    fonto = pg.font.Font(None,100) 
    txt = fonto.render("Game Over",True,(0))
    #ゲームオーバー画面のこうかとん
    gm_kk_img = pg.transform.rotozoom(pg.image.load("fig/2.png"), 0, 2.0)
    gm_kk_img2 = pg.transform.flip(gm_kk_img,True,False) #画像反転
    screen.blit(gm_img,gm_rct)
    screen.blit(txt,[WIDTH/2 - 170, HEIGHT/2 - 40])
    screen.blit(gm_kk_img, (500,370))
    screen.blit(gm_kk_img2, (1050,370))
    pg.display.update()
 



def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_img = pg.transform.rotozoom(kk_img,10,1.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    tim = Time()
    
    x=0
    y=0
    #ゲームオーバー画面
    """
    gm_img = pg.Surface((WIDTH,HEIGHT))  #ブラックアウト
    pg.draw.rect(gm_img,(0),(0,0,WIDTH,HEIGHT))
    gm_img.set_alpha(150) #半透明
    gm_rct = gm_img.get_rect()
    gm_rct.center = WIDTH/2, HEIGHT/2
    fonto = pg.font.Font(None,100) 
    txt = fonto.render("Game Over",True,(0))
    #ゲームオーバー画面のこうかとん
    gm_kk_img = pg.transform.rotozoom(pg.image.load("fig/2.png"), 0, 2.0)
    gm_kk_img2 = pg.transform.flip(gm_kk_img,True,False) #画像反転
    """
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img,kk_rct)       
        clock.tick(200)
        tim.update(screen)
        clock.tick(1)
        tim.tmr -= 1
        if tim.tmr < 0:
            #ブラックアウトと文字、こうかとんの表示
            GameOver()
            """
            screen.blit(gm_img,gm_rct)
            screen.blit(txt,[WIDTH/2 - 170, HEIGHT/2 - 40])
            screen.blit(gm_kk_img, (500,370))
            screen.blit(gm_kk_img2, (1050,370))
            """
            pg.display.update()
            pg.time.wait(5000)  #5秒間止める
            return
        screen.blit(bg_img, [0, 0])
        pg.display.update() 

        """
        if time.tmr == 5:
            screen.blit(bg_img, [0, 0])
            GameClear()
            pg.display.update()
            time.sleep(1)
        """





if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()