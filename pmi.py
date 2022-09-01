import pandas as pd

def construct_df(data,columns=None):
    if isinstance(data,dict):
        return pd.DataFrame(data,index=[0])

    if columns: 
        return pd.DataFrame(data,columns=columns)
    else:
        return pd.DataFrame(data)

def categorize_df(df,category_df):
    df['pmi'] = df['WeightKg'] / ((df['HeightCm']/100)**2)

    for ind,row in df.iterrows():
        pmi = row['pmi']
        category = ""
        risk = ""

        for i,r in category_df.iterrows():
            if r["Min_PMI"] <= pmi <= r["Max_PMI"]:
                df.loc[ind,"category"] = r["Category"]
                df.loc[ind,'risk'] = r["Health_risk"]
                break
    
    return df

def observations(df):
    print("total number of people: ", len(df.index))

    overweight = len(df.query('category == "Overweight"').index)
    print(f"number of overweight people: {overweight}")

    cat_nums = df.groupby('category')['category'].count()
    print("number of people based on category")
    print(cat_nums)

    men_women = df.groupby('Gender')['Gender'].count()
    print("number of men and women:")
    print(men_women)

    check_height_null = 0 in df['HeightCm'].values
    if check_height_null:
        ind = df.query('HeightCm == 0').index
        print(f"There is '0' value in data set. Index: {ind}")
        
    else:
        print("no zero values")

def main(data,category,category_list):
    category_df = construct_df(category_list,columns=category)
    df = construct_df(data,columns=None)
    df = categorize_df(df,category_df)


    observations(df)

    return df

