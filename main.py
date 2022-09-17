
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4], 'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})

df3=pd.read_html("https://www.fdic.gov/resources/")
print(df3)

import matplotlib.pyplot as plt