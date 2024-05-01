# 05 Bonus: Želva

# Pokud už všechno umíš, nemáš co dělat a nudíš se, vyzkoušej Želvu:
# https://docs.python.org/3/library/turtle.html
# Želva umí kreslit. Pomocí ovládání směru jejího pohybu a dalších parametrů
# můžeš tvořit obrázky a zkoušet si, jak želva reaguje na pokyny.

# Vyzkoušej si pár pokynů podle tutoriálu. Využij radši python skript než Jupyter notebook.
# Po spuštění kódu by se mělo otevřít nové okno, ve kterém bude želva kreslit.

# I když se želva určitě jeví jako zásadní nástroj pro kariéru datového analytika,
# v praxi bude spíš důležitější znát pandas a další témata, která se učíme v DA.

import turtle as t

# Nastavení parametrů
t.shape('turtle')
t.color('blue')
t.speed(5)

# Pohyb a otáčení, vypnutí/zapnutí kreslení (přiložení pera k papíru)
t.forward(100)
t.left(90)

t.penup()
t.forward(100)
t.left(90)

t.pendown()
t.forward(100)

# Hranatá spirála
t.teleport(x=-200, y=50)
num_levels = 5
for i in range(num_levels * 4): 
    t.forward(i * 5)
    t.right(90)