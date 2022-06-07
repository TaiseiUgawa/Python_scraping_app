import requests
import json
from pprint import pprint
import pandas as pd
import time
import sqlite3

app_id = "rakutenID"
app_api = f"https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?applicationId={app_id}"

res = requests.get(app_api)
json_data = json.loads(res.text)
#pprint(json_data)

#to create value of small categoryId columns
#using line 31
parent_dict = {}

df = pd.DataFrame(columns=["category1",      "category2",       "category3",      "categoryId", "categoryName"])
#                (columns=[large categoryId, medium categoryId, small categoryId, categoryId,    categoryName])

#create value of large categoryId columns
for category in json_data["result"]["large"]:
    df = df.append({"category1": category["categoryId"], "category2": "", "category3": "", "categoryId": category["categoryId"],
                    "categoryName": category["categoryName"]}, ignore_index=True)

#create value of medium categoryId columns
for category in json_data["result"]["medium"]:
    df = df.append({"category1": category["parentCategoryId"], "category2": category["categoryId"], "category3": "", "categoryId":str(category['parentCategoryId']) + "-" + str(category['categoryId']),
                     "categoryName": category["categoryName"]}, ignore_index=True)
    parent_dict[str(category["categoryId"])] = category["parentCategoryId"]

#create value of small categoryId columns
for category in json_data["result"]["small"]:
    df = df.append({"category1": parent_dict[category["parentCategoryId"]], "category2": category["parentCategoryId"], "category3":category["categoryId"],
                    "categoryId": parent_dict[category["parentCategoryId"]] + "-" + str(category["parentCategoryId"] + "-" + str(category["categoryId"])),
                     "categoryName": category["categoryName"]}, ignore_index=True)
#print(df)

df_keyword = df.query('categoryName.str.contains("魚")', engine='python')

#check result then specify　categoryId (Test)
categoryId = "32-339"
url = f"https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?applicationId={app_id}&categoryId={categoryId}"
res = requests.get(url)
json_data = json.loads(res.text)
#pprint(json_data)

#Create main DataFrame process
df_recipe = pd.DataFrame(columns=["recipeId", "recipeTitle", "recipeMaterial", "recipeCost", "recipeUrl"])

for index, row in df_keyword.iterrows():
    # consider access interva time
    time.sleep(3)

    url = f"https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?applicationId={app_id}&categoryId="+row['categoryId']
    res = requests.get(url)

    json_data = json.loads(res.text)
    #pprint(json_data)
    recipes = json_data["result"]

    for recipe in recipes:
        df_recipe = df_recipe.append({"recipeId": recipe["recipeId"], "recipeTitle": str(recipe["recipeTitle"]), "recipeMaterial": str(recipe["recipeMaterial"]),
                                     "recipeCost": str(recipe["recipeCost"]), "recipeUrl": str(recipe["recipeUrl"])}, ignore_index=True)


#DataFrame to sqlite process
df_recipe = df_recipe.set_index("recipeId")
#print(df_recipe)

db_name = "recipe.db"
conn = sqlite3.connect(db_name)
df_recipe.to_sql("recipe", conn, if_exists="replace")

#check result
cur = conn.cursor()
query = "SELECT * from recipe"
for row in cur.execute(query):
    print(row)


