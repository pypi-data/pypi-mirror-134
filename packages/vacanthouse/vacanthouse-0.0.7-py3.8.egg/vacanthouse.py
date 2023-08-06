import pandas as pd
import matplotlib.pyplot as plt
import subprocess as sp


sp.call("wget https://raw.githubusercontent.com/Lifengtong1/vacancy_rate_and_population_in_JP_and_USA/main/data/vacancy_rate.csv",shell=True)
vacant = pd.read_csv("vacancy_rate.csv")

sp.call("wget https://raw.githubusercontent.com/Lifengtong1/vacancy_rate_and_population_in_JP_and_USA/main/data/population.csv",shell=True)
population = pd.read_csv("population.csv")

def main():
  fig = plt.figure(figsize=(12, 5))
  ax1 = fig.add_subplot(1, 2, 1) #1つ目のsubplot 1行2列の1つ目
  ax2 = fig.add_subplot(1, 2, 2) #2つ目のsubplot 1行2列の2つ目

  #1つ目の表示するデータを用意
  x11 = vacant['year'].values
  y11 = vacant['japan'].values

  x12 = vacant['year'].values
  y12 = vacant['USA'].values

  #1つ目のグラフラベル付け
  ax1.set_xlabel("year")
  ax1.set_ylabel("vacancy rate")
  ax1.set_xticks(x11)
  ax1.set_title("Vacancy Rate")

  #1つ目のデータをプロット
  ax1.plot(x11, y11, label='Japan')
  ax1.plot(x12, y12, label='USA')

  # 凡例
  ax1.legend()

  #2つ目の表示するデータを用意
  x21 = population['year'].values
  y21 = population['Japan'].values

  x22 = population['year'].values
  y22 = population['USA'].values

  #2つ目のグラフラベル付け
  ax2.set_xlabel("year")
  ax2.set_ylabel("population (10 million)")
  ax2.set_xticks(x21)
  ax2.set_title("Population")

  #2つ目のデータをプロット
  width = 1.5
  ax2.bar(x11 - width / 2, y21, width=width, label='Japan')
  ax2.bar(x11 + width / 2, y22, width=width, label='USA')

  # 凡例
  ax2.legend()

  #レイアウトの設定
  plt.tight_layout()

  #グラフの表示
  plt.show()

if __name__ == "__main__":
 main()