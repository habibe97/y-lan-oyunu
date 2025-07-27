
import turtle
import random

# Sabit değerler
genislik = 900
yukseklik = 500
gecikme = 100
yem_boyutu = 12
renkler = ['red', 'yellow', 'cyan', 'green', 'purple', 'pink', 'blue']
sekiller = ['circle', 'square', 'triangle']

yonler = {
    'yukarı': (0, 20),
    'aşağı': (0, -20),
    'sağ': (20, 0),
    'sol': (-20, 0),
}


def yon_tuslari():
    ekran.onkey(lambda: yilan_yon_belirle('yukarı'), "Up")
    ekran.onkey(lambda: yilan_yon_belirle('sağ'), "Right")
    ekran.onkey(lambda: yilan_yon_belirle('aşağı'), "Down")
    ekran.onkey(lambda: yilan_yon_belirle('sol'), "Left")
    ekran.onkey(lambda: yilan_yon_belirle('yukarı'), "w")
    ekran.onkey(lambda: yilan_yon_belirle('sağ'), "d")
    ekran.onkey(lambda: yilan_yon_belirle('aşağı'), "s")
    ekran.onkey(lambda: yilan_yon_belirle('sol'), "a")


def yilan_yon_belirle(yon):
    global yilan_yon
    if yon == "yukarı" and yilan_yon != "aşağı":
        yilan_yon = "yukarı"
    elif yon == "aşağı" and yilan_yon != "yukarı":
        yilan_yon = "aşağı"
    elif yon == "sol" and yilan_yon != "sağ":
        yilan_yon = "sol"
    elif yon == "sağ" and yilan_yon != "sol":
        yilan_yon = "sağ"


def hareket_yilan():
    bas.clearstamps()
    yeni_bas = yilan[-1].copy()
    yeni_bas[0] += yonler[yilan_yon][0]
    yeni_bas[1] += yonler[yilan_yon][1]

    if yeni_bas in yilan or yeni_bas[0] < -genislik / 2 or yeni_bas[0] > genislik / 2 or yeni_bas[1] < -yukseklik / 2 or yeni_bas[1] > yukseklik / 2:
        reset()
    else:
        yilan.append(yeni_bas)

        if not yem_etkilesim():
            if len(yilan) > 1:
                yilan.pop(0)

        for parca in yilan:
            bas.goto(parca[0], parca[1])
            bas.stamp()

        ekran.title(f' - Klasik Yılan Oyunu - Skor: {skor}')
        ekran.update()
        turtle.ontimer(hareket_yilan, gecikme)


def yem_etkilesim():
    global yem_pozisyon, zehir_pozisyon, skor

    if uzaklık_bul(yilan[-1], yem_pozisyon) < 20:
        skor += 1
        yem_pozisyon = rastgele_yem()
        yem.goto(yem_pozisyon)
        zehir_pozisyon = rastgele_yem()
        zehir.goto(zehir_pozisyon)
        return True
    elif uzaklık_bul(yilan[-1], zehir_pozisyon) < 20:
        skor -= 1
        zehir_pozisyon = rastgele_yem()
        zehir.goto(zehir_pozisyon)
        if len(yilan) > 1:
            yilan.pop(0)
    return False


def rastgele_yem():
    x = random.randint(-genislik // 2 + yem_boyutu, genislik // 2 - yem_boyutu)
    y = random.randint(-yukseklik // 2 + yem_boyutu,
                       yukseklik // 2 - yem_boyutu)
    yem.color(random.choice(renkler))
    return (x, y)


def uzaklık_bul(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((y2 - y1)**2 + (x2 - x1)**2) ** 0.5


def reset():
    global skor, yilan, yilan_yon, yem_pozisyon, zehir_pozisyon
    skor = 0
    yilan = [[0, 0], [20, 0], [40, 0], [60, 0]]
    yilan_yon = 'sağ'
    yem_pozisyon = rastgele_yem()
    yem.goto(yem_pozisyon)
    zehir_pozisyon = rastgele_yem()
    zehir.goto(zehir_pozisyon)
    hareket_yilan()


# Ekran ayarları
ekran = turtle.Screen()
ekran.setup(genislik, yukseklik)
ekran.title('Klasik Yılan Oyunu')
ekran.bgcolor('Black')
ekran.tracer(0)
ekran.listen()
yon_tuslari()

# Yılan başı
bas = turtle.Turtle()
bas.shape("circle")
bas.color("cyan")
bas.penup()

# Yem
yem = turtle.Turtle()
yem.shapesize(yem_boyutu / 20)
yem.penup()
yem.shape('circle')

# Zehirli yem
zehir = turtle.Turtle()
zehir.shapesize(yem_boyutu / 20)
zehir.penup()
zehir.shape('triangle')
zehir.color("orange")

reset()
turtle.done()
