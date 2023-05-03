PythonのライブラリPandas基礎20本ノック

1.データの読み込み
weather.csvを読み込み、dfで定義して下さい

解答
import pandas as pd
df = pd.read_csv('weather.csv')
df

2.データの中身確認
読み込んだデータdfの先頭3行、末尾10行を表示して下さい

解答
import pandas as pd
df = pd.read_csv('weather.csv')
df.head(3)
df.tail(10)

3.不要な列、行の削除
先頭行と、カラム名（列名）が「〇〇.1」「〇〇.2」となっているものを削除したDataFrame dfを再定義して下さい

解答
df.columns
出力されたものから不要な部分を削除すればOK

4.データの型、サイズ、列名、行名の確認
次の値を取得しなさい
各列のデータ型・Data Frameのサイズ・列名

解答
df.dtypes
df.shape
df.columns
df.index

5.任意の要素を取得
dfの5〜10行目、3~6列目の要素（最高気温~最深積雪）を取得してください

解答
df.iloc[4:10,2:6] 

6.条件抽出
people.csvを読み込みdf_peopleと定義してください
その後、下記の条件を満たすDataFrameをそれぞれ抽出しなさい
・nationalityがAmericaである
・ageが20以上30未満である

解答
df_people = pd.read_csv('people.csv')
df_people
df_people[df_people['nationality'] == 'America']
df_people[(df_people['age'] >= 20) & (df_people['age'] < 30)]

7.ユニークな値の抽出
df_peopleに対して、カラム毎のユニーク（固有）な値を抽出しなさい

解答
df_people['nationality'].unique()
df_people['name'].unique()
df_people['age'].unique()
 
8.重複除去
df_peopleのnationalityの列に対し、重複がある値の行を除去したDataFrameを取得しなさい

解答
df_people.drop_duplicates(subset='nationality')

9.カラム名変更
dfに対し、各カラム毎の「（単位）」部分を削除したカラム名に変更してください
＜新しいカラム名＞
年月日、平均気温、最高気温、最低気温、降水量の合計、最深積雪、平均雲量、平均蒸気圧、平均風速、日照時間

解答
df_columns
表示されたものから単位を消す（Aとする）
df_columns = A
df

10.並び替え
dfを最高気温が高い順に並び替えてください

解答
df.sort_values(' 最高気温',ascending=False)

11.ダミー変数への処理
df_peopleのnationalityカラムをダミー変数に変換しなさい

解答
df_people['nationality'].unique()
df_people['nationality']
pd.get_dummies(df_people['nationality'])
pd.get_dummies(df_people, columns=['nationality'])

12.欠損値の確認
dfの欠損値を確認しなさい

解答
df.isnull()

13. 欠損値の補完
dfの欠損値を全て0で補完してください

解答
df.fillna(0).head()

14.欠損値の削除
dfの欠損値を列方向で削除してください

解答
df.isnull().sum()
df.shape
↑上の２行は確認してるだけなので省略してもいい
df.dropna(axis=1).head()

15.ユニークな値と出現回数
iris.csvを読み込みdf_irisと定義してください
その後、df_irisのClassカラムにおいて、ユニークな値とその出現回数を確認してください

解答
df_iris = pd.read_csv('iris.csv')
df_iris.head()
df_iris[('Class')].value_counts()

16.グループごとの集計
df_irisの下記各クラスにおけるsepal-length,sepal-width,petal-length,petal-widthの平均値を求めてください
iris-setosa,iris-versicolor,iris-virginica

解答
df_iris.groupby('Class').mean()

17.統計量の確認
df_irisの各カラムにおける、下記統計量を算出してください
平均値、中央値、標準偏差、最大値、最小値

解答
df.mean()
df.median()
df.std()
df.max()
df.min()

18.折れ線グラフの表示
dfの先頭50日間における平均気温、最高気温、最低気温を折れ線グラフ（凡例なし）で可視化してください
ただし横軸は年月日とすること

解答
import matplotlib.pyplot as plt
df[:50].plot(x='年月日' , y=['平均気温','最高気温','最低気温'], legend=False)

19.相関関係の算出
dfの下記３項目同士の相関係数を算出してください
平均気温、降水量の合計、日照時間

解答
df[['平均気温','降水量の合計','日照時間']].corr()

20.データの出力
欠損値を０で補完したdfをexport.csvというファイル名でcsvとして出力してください。インデックスの出力は不要です

解答
df.fillna(0).to_csv('export.csv' , index=False)
