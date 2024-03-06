import pandas as pd
from imc_menu import main

df = pd.read_csv("data_info.csv")
df.sample(20)
