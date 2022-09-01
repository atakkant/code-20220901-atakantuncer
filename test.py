import pmi
from data import data
from category import category, category_list

from test_cases import test_cases


if __name__ == '__main__':
    all_tests_passed = True

    for ind,row in enumerate(test_cases):
        df = pmi.main([row],category,category_list)
        test = pmi.construct_df([row])
        
        if not df.empty and not test.empty:
            print(df)
            print(test)
            if df.at[ind,'category'] == test.at[ind,'category']:
                 print(f"category is true")
            else:
                print(f"category is false",df.at[ind,'category'], test.at[ind,'category'])
                all_tests_passed = False

            if df.at[ind,'risk'] == test.at[ind,'risk']:
                 print(f"risk is true")
            else:
                print(f"risk is false", df.at[ind,'risk'], test.at[ind,'risk'])
                all_tests_passed = False

            if df.at[ind,'pmi'] == test.at[ind,'pmi']:
                print(f"pmi is true")
            else:
                print(f"pmi is false", df.at[ind,'pmi'], test.at[ind,'pmi'])
                all_tests_passed = False
        
    if all_tests_passed:
        print("all tests passed!")
    else:
        print("some tests failed. Please check")