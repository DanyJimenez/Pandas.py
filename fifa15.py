import pandas as pd

main_data = pd.read_csv("./players_15.csv")

head = main_data.head()
print(head)
print("\n")

age_name = head[["short_name", "age", "nationality"]]
print(age_name)

print("\n")
mode_age = main_data[["age"]].mode()
print(mode_age)

print("\n")
height_cm_mean = main_data[["height_cm"]].mean()
print(round(height_cm_mean,3))

print("\n")
height_cm_mode = main_data[["height_cm"]].mode()
print(height_cm_mode)

print("\n")
age_mean = head[["age"]].mean()
print(age_mean)

print("\n")
players_over210 = main_data[main_data["height_cm"] > 201]
print(players_over210)

print("\n")
with_name = players_over210[["short_name", "height_cm", "club"]]
print(with_name)

print("\n")
most_weight = main_data[main_data["weight_kg"] > 100 ]
print(most_weight)

print("\n")
most_weight_names = most_weight[["short_name", "height_cm", "weight_kg", "club"]]
print(most_weight_names)

print("\n")
colombians = main_data[main_data["nationality"] == "Colombia"]
print(colombians)

print("\n")
col_names_andTeam = colombians[["club", "short_name", "age"]]
print(col_names_andTeam)

print("\n")
age_colombianMean = colombians[["age"]].mean()
print(round(age_colombianMean,2))

print("\n")
arsenal_team = main_data[main_data["club"]== "Arsenal"]
print(arsenal_team)

print("\n")
arsenal_names = arsenal_team[["short_name", "age", "nationality", "player_positions"]]
print(arsenal_names)

print("\n")
main_arsAge = arsenal_team[["age"]].mean()
print(round(main_arsAge,2))

print("\n")
nation_modeTeam = arsenal_team[["nationality"]].mode()
print(nation_modeTeam)


print("\n")
