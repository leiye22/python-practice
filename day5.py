#coding=utf-8
import pandas as pd
df = pd.read_excel(r"D:\pycharm\PyCharm Community Edition 2021.3\一周小任务\student.xlsx")
result = df[df["年龄"]>20]
result.to_excel("result.xlsx",index=False)
