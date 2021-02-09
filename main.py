import pandas as pd


def main():
    data_df = pd.read_csv("scimagojr_2019.csv", sep=';', )
    categories_data = data_df["Categories"].to_list()
    title_data = data_df["Title"].to_list()
    dict_categories_and_title = dict(zip(title_data, categories_data))
    list_q1, list_q2, list_q3, list_q4, list_q_none = [], [], [], [], []
    for key, item in dict_categories_and_title.items():
        index = [item.find("Q1"), item.find("Q2"), item.find("Q3"), item.find("Q4"), item.find("Q")]
        if index[0] != -1:
            list_q1.append(key)
            continue
        elif index[1] != -1:
            list_q2.append(key)
            continue
        elif index[2] != -1:
            list_q3.append(key)
            continue
        elif index[3] != -1:
            list_q4.append(key)
            continue
        elif index[4] == -1:
            list_q_none.append(key)
            continue
    list_q1 = list(set(list_q1))
    list_q2 = list(set(list_q2))
    list_q3 = list(set(list_q3))
    list_q4 = list(set(list_q4))
    list_q_none = list(set(list_q_none))

    dict_q1 = {"Q1": list_q1}
    dict_q2 = {"Q2": list_q2}
    dict_q3 = {"Q3": list_q3}
    dict_q4 = {"Q4": list_q4}
    dict_q_none = {"Q none": list_q_none}
    result_q1 = pd.DataFrame(dict_q1)
    result_q2 = pd.DataFrame(dict_q2)
    result_q3 = pd.DataFrame(dict_q3)
    result_q4 = pd.DataFrame(dict_q4)
    result_q_none = pd.DataFrame(dict_q_none)
    result_q1.to_excel("result_q1.xlsx")
    result_q2.to_excel("result_q2.xlsx")
    result_q3.to_excel("result_q3.xlsx")
    result_q4.to_excel("result_q4.xlsx")
    result_q_none.to_excel("result_q_none.xlsx")
