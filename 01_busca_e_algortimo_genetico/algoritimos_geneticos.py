from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

tp1 = pd.read_csv("./CaixeiroSimples.csv")
tp2 = pd.read_csv("./CaixeiroGrupos.csv")


class Individuo:
    def __init__(self) -> None:
        pass


print(tp1.size)
print(tp2.size)

tp_cidades1 = []
tp_cidades2 = []

for row in tp1.iterrows():
    tp_cidades1.append(row)

for row in tp_cidades1:
    print(row)
