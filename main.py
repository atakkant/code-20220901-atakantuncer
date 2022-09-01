import pmi
from data import data
from category import category,category_list

if __name__ == '__main__':
    df = pmi.main(data,category,category_list)
    print(df)