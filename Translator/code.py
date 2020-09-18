# To Install required moduled, run below on terminal/cmd
# !pip install pandas
# !pip install googletrans


# import require modules
import pandas as pd
from googletrans import Translator

translator = Translator()

# read the input file
# df = pd.read_excel('input_file.xlsx', header=None)
df = pd.read_csv('input_file.csv', header=None)

# assign columns name 
no_of_cols = len(df.columns)
columns = ['col_'+str(i) for i in range(no_of_cols)]
df.columns = columns

# Fill any empty field with some dummy text
df.fillna('Empty_Field', inplace=True)

# convert the columns text into english
def convert_text(x):
    trans = translator.translate(x,dest="en")
    return trans.text

for col in df.columns:
    df[col+'_eng'] = df[col].apply(convert_text)

# re-arrange columns
for i in range(no_of_cols):
    col = df['col_'+str(i)+'_eng']
    df.drop(labels=['col_'+str(i)+'_eng'], axis=1,inplace = True)
    idx = df.columns.get_loc("col_"+str(i))
    df.insert(idx+1, 'col_'+str(i)+'_eng', col)

# Save the output
df.to_csv("output_file.csv")
# df.to_excel("output_file.xlsx")