import json
import sys

import pmi
from category import category,category_list


if __name__ == '__main__':
    args = sys.argv
    f = open(args[1],'r')
    data = json.loads(f.read())
    df = pmi.main(data,category,category_list)
    print(df)
