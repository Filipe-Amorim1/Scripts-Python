# Mostrar contagem regressiva para estouro de fogos
# indo de 0 até 10
# pausa de 1 segundo

import time
import emoji

for c in range (1,11):
    time.sleep(1)
    print(c)
print(emoji.emojize('\033[1;33mBUuuuuuuuuMMMMM:punch:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',use_aliases=(True)))