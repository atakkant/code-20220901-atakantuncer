import json
import sys

import pmi
from category import category, category_list


def run_test(test_cases):
    all_tests_passed = True
    df_testing = pmi.main(test_cases,category,category_list)
    tests = pmi.construct_df(test_cases)

    for ind,test in tests.iterrows():
        HeightCm = test['HeightCm']
        WeightKg = test['WeightKg']
        df = df_testing.query(f'(HeightCm == {HeightCm}) & (WeightKg == {WeightKg})')

        if not df.empty and not test.empty:
            if df.at[ind,'category'] == test.at['category']:
                 print(f"category is true")
            else:
                print(f"category is false",df.at[ind,'category'], test.at['category'])
                all_tests_passed = False

            if df.at[ind,'risk'] == test.at['risk']:
                 print(f"risk is true")
            else:
                print(f"risk is false", df.at[ind,'risk'], test.at['risk'])
                all_tests_passed = False

            if round(df.at[ind,'pmi'],2) == round(test.at['pmi'],2):
                print(f"pmi is true")
            else:
                print(f"pmi is false", df.at[ind,'pmi'], test.at['pmi'])
                all_tests_passed = False
        
    if all_tests_passed:
        return True
    else:
        return False

if __name__ == '__main__':
    args = sys.argv
    f = open(args[1],'r')
    test_cases = json.loads(f.read())

    result = run_test(test_cases)
    if result:
        print("all tests passed!")
    else:
        print("some tests failed. Please check")