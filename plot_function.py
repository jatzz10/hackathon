# import pandas as pd
# import numpy as np
# import json

# def city():
#   try:
#       df = pd.read_csv("hackathon_data.csv")
#   except Exception as e:
#       print("error in reading dataframe",e)
#   print("success in reading dataframe")

#   lis = []
#   dic = dict()
#   # print(df["city_id"].value_counts().index)
#   dic["x"] = json.dumps(list(df["city_id"].value_counts().index))
#   dic["y"] =  json.dumps(df["city_id"].value_counts().values.tolist())
#   dic["text"] = json.dumps("City having highest transaction")
#   # print(dic)

#   with open('data.json', 'w') as f:  # writing JSON object
#     json.dump(dic, f)

#   # di = dict()
#   # dic["x"] = df["city_id"].to_json()
#   # dic["y"] = df["total_cost"].to_json()
#   # dic["text"] = json.dumps("total revenue generated by that city")

#   # lis.append(dic)

#   # return json.dumps(lis)

# city()