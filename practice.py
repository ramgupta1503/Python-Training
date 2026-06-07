import pandas as pd

data = {
    "Name" : ["Ram" , "Arnav" , "Shubh" , "Daksh"],
    "Marks" : [85 , 92 , 76 ,88],
    "City" : ["Jhansi" , "Prayagraj" , "Noida" , "Meerut"]
}

# df = pd.DataFrame(data)
# print(df)

print([df["Marks"] < 85])