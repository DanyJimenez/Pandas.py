#FIFA 2020 analythics

from glob import glob
import pandas as pd
import matplotlib.pyplot as plt

dataSource = pd.read_csv("./players_20.csv")

#Datos de cada columna
col = dataSource.columns.values
print(col)

#primeros 5 registros
print("\n")
head = dataSource.head()
print(head)


print("\n")
shortName = head[["short_name", "club", "overall", "wage_eur"]]
print(shortName)


#Datos de todo el equipo Gunner ===>
print("\n")
arsenalTeam = dataSource[dataSource["club"]== "Arsenal"]
#print(arsenalTeam)


print("\n")
arsenal_wageEur_names = arsenalTeam.sort_values("wage_eur")
print(arsenal_wageEur_names[["short_name", "nationality","age", "wage_eur", "player_positions"]])

print("\n")
meanWage = arsenalTeam[["wage_eur"]].mean()
print(round(meanWage,2))


#Datos de todo el equipo Spurs
print("\n")
tottenham = dataSource[dataSource["club"]== "Tottenham Hotspur"]
#print(tottenham)

print("\n")
spurs_wage_names = tottenham.sort_values("wage_eur")
print(spurs_wage_names[["short_name", "nationality","age", "wage_eur", "player_positions"]])

print("\n")
meanSpursWage = tottenham[["wage_eur"]].mean()
print(round(meanSpursWage,2))




#Datos comparativos entre ambos
#¿Cuál club tiene los mejores jugadores?
print("\n")

#promedio de overall de los Spurs
SpursOverall = tottenham[["overall"]].mean()
print(round(SpursOverall,3))

print("\n")
#promedio de overall de los Gunners
gunnersOverall = arsenalTeam[["overall"]].mean()
print(round(gunnersOverall,3))

#Promedio de valoración en euros de los Spurs
print("\n")
value_spurs = tottenham[["value_eur"]].describe()
print(round(value_spurs,2))


#Promedio de valoración en euros de los Gunners
print("\n")
value_gunners = arsenalTeam[["value_eur"]].describe()
print(round(value_gunners,2))

#Lista de jugadores de los Spurs cuyo valor sea superior a 50 millones
print("\n")
mostValue_spurs = tottenham[tottenham["value_eur"]>50000000]
print(mostValue_spurs[["short_name", "nationality","age", "value_eur"]])

#Lista de jugadores de los Gunners cuyo valor sea superior a 50 millones
print("\n")
mostValue_gunners = arsenalTeam[arsenalTeam["value_eur"]>50000000]
print(mostValue_gunners[["short_name", "nationality","age", "value_eur"]])



#GOALKEEPER ANALYTHICS
print("\n")
global_goalkeepers = dataSource[dataSource["player_positions"]== "GK"]
print(global_goalkeepers[["short_name","club", "nationality","age", "value_eur"]])

#Arqueros más valorizados del mercado
print("\n")
mostValued_GK = global_goalkeepers[global_goalkeepers["value_eur"] > 40000000]
print(mostValued_GK[["short_name","club", "nationality","age", "value_eur"]])