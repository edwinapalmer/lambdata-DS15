#from my_mod import enlarge
from pandas import DataFrame

from my_lambdata.my_mod import enlarge

print("HELLO")

print(enlarge(8))


df = DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())