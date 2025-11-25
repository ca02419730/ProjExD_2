import os
import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1100, 650
DELTA = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}




# def gameover(screen: pg.Surface) -> None
"""
1行目：画面を生成する
2行目：色を黒に変える
3行目：透明度の調整
"""
#     bb_img = pg.Surface((WIDTH, HEIGHT))
#     bb_img.set_colorkey((0, 0, 0))
#     bb_img.Surface.set_alpha(0)

# def init_bb_imgs() -> tuple[list[pg.Surface], list[int]]:
"""
1行目：10段階の変化
2行目：爆弾サイズの変化
3行目：爆弾の生成
4行目：リストにbb_imgを格納
5行目：1～10のまでの数字のリストをを作る

"""
#     for r in range(1, 11):
#         bb_img = pg.Surface((20*r, 20*r))
#         pg.draw.circle(bb_img, (255, 0, 0), (10*r, 10*r), 10*r) 
#         bb_imgs.append(bb_img)
#         bb_accs = [a for a in range(1, 11)]
#         return bb_img, bb_accs

# def get_kk_imgs() -> dict[tuple[int, int], pg.Surface]
"""
画像の回転を行う関数
"""
#     kk_dict = {
#         ( 0, 0): rotozoom(kk_img,) # キー押下がない場合
#         (+5, 0): rotozoom(???) # 右
#         (+5,-5): rotozoom() # 右上
#         ( 0,-5): rotozoom(pg.K_UP) # 上... 
#   }

#def calc_orientation(org: pg.Rect, dst: pg.Rect, current_xy: tuple[float, float])-> tuple[float, float]
    #org dict
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_bound(rct: pg.Rect) ->tuple[bool, bool]:
    """
    引数：こうかとんRectかばくだんRect
    戻り値：タプル（横方向判定結果，縦方向判定結果）
    画面内ならTrue，画面外ならFalse
    """
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:  # 横のはみだし
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:  # 縦のはみだし
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    bb_img = pg.Surface((20, 20))  # 空のSerface
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 半径10の赤い円
    bb_img.set_colorkey((0, 0, 0))  # 黒色を透過
    bb_rct = bb_img.get_rect()  # 爆弾rect
    bb_rct.centerx = random.randint(0, WIDTH)  # 爆弾横
    bb_rct.centery = random.randint(0, HEIGHT) # 爆弾縦
    vx, vy = +5, +5  # 爆弾の横速度，縦速度
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
            if kk_rct.colliderect(bb_rct):  # こうかとんと爆弾が衝突したら
                print("ゲームオーバー")
                return
        screen.blit(bg_img, [0, 0])

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        # if key_lst[pg.K_UP]:
        #     sum_mv[1] -= 5
        # if key_lst[pg.K_DOWN]:
        #     sum_mv[1] += 5
        # if key_lst[pg.K_LEFT]:
        #     sum_mv[0] -= 5
        # if key_lst[pg.K_RIGHT]:
        #     sum_mv[0] += 5
        for key , mv in DELTA.items():
            if key_lst[key]:
                sum_mv[0] += mv[0]  # 横移動
                sum_mv[1] += mv[1]  # 縦移動
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):  # 画面外なら
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])  # 移動をなかったことにする
        screen.blit(kk_img, kk_rct)
        yoko, tate = check_bound(bb_rct)
        if not yoko:  # 横にはみ出たら
            vx *= -1
        if not tate:  # 縦にはみ出たら
            vy *= -1   
        bb_rct.move_ip(vx, vy)
        screen.blit(bb_img, bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
