"""
o.OOOo.   ooOoOOo    Oo    OooOOo.   .oOOOo.  .oOOOo.  ooOoOOo oOoOOoOOo ooOoOOo o      'O    Oo
 O    `o     O      o  O   O     `O .O     o. o     o     O        o        O    O       o   o  O          oO   .oOOo.
 o      O    o     O    o  o      O O       o O.          o        o        o    o       O  O    o          O        O
 O      o    O    oOooOoOo O     .o o       O  `OOoo.     O        O        O    o       o oOooOoOo         o        o
 o      O    o    o      O oOooOO'  O       o       `O    o        o        o    O      O' o      O         O       O'
 O      o    O    O      o o        o       O        o    O        O        O    `o    o   O      o         o      O
 o    .O'    O    o      O O        `o     O' O.    .O    O        O        O     `o  O    o      O         O    .O
 OooOO'   ooOOoOo O.     O o'        `OoooO'   `oooO'  ooOOoOo     o'    ooOOoOo   `o'     O.     O       OooOO oOoOoO
"""


def bussec(V, d):
    i = 1
    while i <= V[0] and d != V[i]:
        i = i + 1
        if i == V[0]:
            return i
    return -1


def busbin(V, d):
    inicio = 1
    fin = V[0]
    while inicio <= fin:
        mitad = (inicio + fin) / 2
        if V[mitad] == d:
            return mitad
        if d < V[mitad]:
            fin = mitad - 1
        else:
            inicio = mitad + 1
    return -1