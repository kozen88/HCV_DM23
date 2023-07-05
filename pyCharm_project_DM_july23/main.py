# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import openpyxl

sb.set()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # caricamento del dataset per eleborarlo
    df = pd.read_csv('HCV-Egy-Data.csv', delimiter=',')
    # print(df)

    # controlliamo valori null sul dataset
    # is_missing_some_value = df.isnull().any()
    # number_of_null = df.isnull().sum()
    # print(is_missing_some_value)
    # print(number_of_null)

    # trasformiamo il dataset da formato csv a dataframe pandas a formato excel
    # df.to_excel("excel_hcv_data.xlsx")

    df_general_stat = df.describe()
    features_name = list(df.columns)
    print(features_name)

    campioni_per_classe = list(df.groupby('Baselinehistological staging').size())
    classi_per_fibrosi = ['portal_fibrosis', 'periportal_fibrosis', 'bridging_fibrosis', 'cirrhosis']
    map_fibrosi_campioni = {}
    index = 0
    for i in classi_per_fibrosi:
        map_fibrosi_campioni[i] = campioni_per_classe[index]
        index = index + 1

    # mostra se il dizionario appena creato è corretto
    # print(map_fibrosi_campioni)

    # grafico a torta per mostrare la distribuzioni delle classi target e giudicare se il task è bilanciato o meno
    """""
    explode = (0.05, 0.05, 0.05, 0.05)
    plt.pie(map_fibrosi_campioni.values(), explode, map_fibrosi_campioni.keys(),
            colors=['#FFFF40', '#FF7010', '#E00000', '#601070'], shadow=True, )
    plt.title("Distribuzione delle classi corrispondenti ai 4 stati di fibrosi epatica indotta da HCV")
    plt.show()
    """

    # istogramma che mostri la disttribuzione delle classi target
    """""
    plt.bar(map_fibrosi_campioni.keys(), map_fibrosi_campioni.values(), width=0.2,
            color=['#FFFF40', '#FF7010', '#E00000', '#601070'])
    plt.title("Distribuzione dei 4 stati di fibrosi epatica indotta da HCV", color='green')
    plt.ylabel('numero di pazienti', color='green')
    plt.xlabel('stadio fibrosi in oredine di severità', color='green')
    plt.show()
    """

male_cirrhosis = df[((df['Gender'] == 1) & (df['Baselinehistological staging'] == 4))]
female_cirrhosis = df[((df['Gender'] == 2) & (df['Baselinehistological staging'] == 4))]
# print(male_cirrhosis)
# print(female_cirrhosis)
male_bridging_fibrosis = df[((df['Gender'] == 1) & (df['Baselinehistological staging'] == 3))]
female_bridging_fibrosis = df[((df['Gender'] == 2) & (df['Baselinehistological staging'] == 3))]
# print(male_bridging_fibrosis)
# print(female_bridging_fibrosis)
male_periportal_fibrosis = df[((df['Gender'] == 1) & (df['Baselinehistological staging'] == 2))]
female_periportal_fibrosis = df[((df['Gender'] == 2) & (df['Baselinehistological staging'] == 2))]
# print(male_periportal_fibrosis)
# print(female_periportal_fibrosis)
male_portal_fibrosis = df[((df['Gender'] == 1) & (df['Baselinehistological staging'] == 1))]
female_portal_fibrosis = df[((df['Gender'] == 2) & (df['Baselinehistological staging'] == 1))]
# print(male_portal_fibrosis)
# print(female_portal_fibrosis)

# male_cirrhosis.to_excel("exel_male_cirrhosis_hcv_data.xlsx")
# female_cirrhosis.to_excel("excel_female_cirrhosis_hcv_data.xlsx")

# male_bridging_fibrosis.to_excel("excel_male_bridging_fibrosis_hcv_data.xlsx")
# female_bridging_fibrosis.to_excel("excel_female_bridging_fibrosis_hcv_data.xlsx")

# male_periportal_fibrosis.to_excel("excel_male_periportal_fibrosis_hcv_data.xlsx")
# female_periportal_fibrosis.to_excel("excel_female_periportal_fibrosis_hcv_data.xlsx")

# male_portal_fibrosis.to_excel("excel_male_portal_fibrosis_hcv_data.xlsx")
# female_portal_fibrosis.to_excel("excel_female_portal_fibrosis_hcv_data.xlsx")

df.groupby('Gender').size()
df['Gender'].describe()
samples_per_gender = list(df.groupby('Gender').size())
print(samples_per_gender)
gender = ['Male', 'Female']
map_sample_per_gender = {}
j = 0
for i in gender:
    map_sample_per_gender[i] = samples_per_gender[j]
    j = j + 1
print(map_sample_per_gender)
explode = (0.05,0.05)
plt.pie(map_sample_per_gender.values(), explode, map_sample_per_gender.keys(), colors=['#2a60de', '#d8b4d9'], shadow=True, startangle=90)
plt.title("Divisione tra uomini e donne affetti da fibrosi epatica")
plt.show()
