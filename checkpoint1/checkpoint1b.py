import pandas as pd
"""
Checkpoint 1b

*First complete the steps in checkpoint1a.pdf

Here you will create a script to preprocess the data given in starbucks.csv. You may want to use
a jupyter notebook or python terminal to develop your code and test each function as you go... 
you can import this file and its functions directly:

    - jupyter notebook: include the lines `%autoreload 2` and `import preprocess`
                        then just call preprocess.remove_percents(df) to test
                        
    - python terminal: run `from importlib import reload` and `import preprocess`
                       each time you modify this file, run `reload(preprocess)`

Once you are finished with this program, you should run `python preprocess.py` from the terminal.
This should load the data, perform preprocessing, and save the output to the data folder.

"""

def remove_percents(df, col):
    percentList = []
    for char in df[col]:
        char = str(char)
        if len(char) > 0:
            if char[0] != "n":
                char = int(float(char[:len(char)-1]))
        percentList.append(char)
    df[col] = percentList
    return df

def fill_zero_iron(df):
    iron = []
    col = df["Iron (% DV)"]
    for char in col:
        if type(char) is str:
            iron.append('0')
        else:
            iron.append(char)
    df['Iron (% DV)'] = iron
    return df
    
def fix_caffeine(df):
    caffeine = []
    for char in df['Caffeine (mg)']:
        if type(char) is float:
            caffeine.append(0)
        elif char[len(char)-1] == "s":
            caffeine.append(0)
        else:
            caffeine.append(char)
    df['Caffeine (mg)'] = caffeine
    return df

def standardize_names(df):
    columns = []
    for col in df:
        col = col.lower()
        if col[len(col)-1] == ")":
            openindex = col.index("(")
            col = col[0:openindex:1]
        columns.append(col)
    df.columns = columns
    return df

def fix_strings(df, col):
    strings = []
    for char in df[col]:
        char = char.encode("ascii", "ignore")
        char = char.lower()
        char = str(char)
        strings.append(char[2:len(char)-1])
    df[col] = strings
    return df


def main():
    
    # first, read in the raw data
    df = pd.read_csv('../data/starbucks.csv')
    
    # the columns below represent percent daily value and are stored as strings with a percent sign, e.g. '0%'
    # complete the remove_percents function to remove the percent symbol and convert the columns to a numeric type
    pct_DV = ['Vitamin A (% DV)', 'Vitamin C (% DV)', 'Calcium (% DV)', 'Iron (% DV)']
    for col in pct_DV:
        df = remove_percents(df, col)
    
    # the column 'Iron (% DV)' has missing values when the drink has no iron
    # complete the fill_zero_iron function to fix this
    df = fill_zero_iron(df)

    # the column 'Caffeine (mg)' has some missing values and some 'varies' values
    # complete the fix_caffeine function to deal with these values
    # note: you may choose to fill in the values with the mean/median, or drop those values, etc.
    df = fix_caffeine(df)
    
    # the columns below are string columns... starbucks being starbucks there are some fancy characters and symbols in their names
    # complete the fix_strings function to convert these strings to lowercase and remove non-alphabet characters
    names = ['Beverage_category', 'Beverage']
    for col in names:
        df = fix_strings(df, col)
    
    # the column names in this data are clear but inconsistent
    # complete the standardize_names function to convert all column names to lower case and remove the units (in parentheses)
    df = standardize_names(df)
    
    # now that the data is all clean, save your output to the `data` folder as 'starbucks_clean.csv'
    # you will use this file in checkpoint 2
    df.to_csv('../data/starbucks_clean.csv')
    

if __name__ == "__main__":
    main()
