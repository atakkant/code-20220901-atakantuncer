import pandas as pd
from test_cases import test_cases


def construct_df(data,columns=None):
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

def main(data,category,category_list):
    category_df = construct_df(category_list,columns=category)
    df = construct_df(data,columns=None)
    df = categorize_df(df,category_df)

    overweight = len(df.query('category == "Overweight"').index)
    print(f"number of overweight people: {overweight}")

    very_severely_obese = len(df.query('category == "Very severely obese"').index)
    severely_obese = len(df.query('category == "Severely obese"').index)
    #print(f"number of very_severely_obese people: {very_severely_obese}")
    #print(f"number of severely_obese people: {severely_obese}")

    #print(df)
    cat_nums = df.groupby('category')['category'].count()

    print(cat_nums)

    return df

