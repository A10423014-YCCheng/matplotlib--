import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

#Step1. 設定整體參數，可以print(mpl.rcParams.keys())看目前設定
mpl.rcParams['font.family'] = 'MingLiU' #設定整體字型，電腦必須要有，包括座標軸標題字型
mpl.rcParams['font.size'] = 10 #設定整體字型大小，包括座標軸標題字型
mpl.rcParams['text.color'] = 'w' #設定標題顏色
mpl.rcParams['xtick.color'] = 'b' #設定x坐標軸刻度線顏色
mpl.rcParams['xtick.labelcolor'] = 'w' #設定x坐標軸顏色
mpl.rcParams['ytick.color'] = 'y' #設定y坐標軸刻度線顏色，預設會連坐標軸一起修改，如果要分開需再去設定labelcolor
mpl.rcParams['ytick.labelcolor'] = 'w' #設定y坐標軸刻度線顏色
mpl.rcParams['axes.facecolor'] = '0.3'

#設定字體，並用變數儲存，以便後面使用
微軟正黑 = mpl.font_manager.FontProperties(fname=r'C:\Windows\Fonts\msjh.ttf',size = 10)
粉圓 = mpl.font_manager.FontProperties(fname=r'C:\Windows\Fonts\Kingnam-Maiyuan-2.otf',size = 10)
梅圓 = mpl.font_manager.FontProperties(fname=r'C:\Windows\Fonts\jf-openhuninn-1.1.ttf',size = 10)

#Step2. 產生圖紙及小圖案，然後做圖紙的設定
fig, ax = plt.subplots()
fig.set_facecolor("gray")
fig.set_size_inches(16, 9,forward = True)

#新竹遊憩據點遊客人數統計
str1 = r'D:\Python\Program\2022-08-19\新竹市重要遊憩據點遊客人次統計.xlsx'
df = pd.read_excel(str1)

x = list(df.iloc[0:12,0])
y = df.iloc[0:12,1:]
y = y.T

means1 = list(y.loc['十八尖山'])
means2 = list(y.loc['青青草原'])
means3 = list(y.loc['城隍廟'])
means4 = list(y.loc['新竹漁港'])
means5 = list(y.loc['賞蟹步道'])
means6 = list(y.loc['青草湖'])
means7 = list(y.loc['十七公里腳踏車道'])
means8 = list(y.loc['新竹公園'])

width = 0.05  # the width of the bars

ax.plot(x,means1,label=y.index[0])
ax.plot(x,means2,label=y.index[1])
ax.plot(x,means3,label=y.index[2])
ax.plot(x,means4,label=y.index[3])
ax.plot(x,means5,label=y.index[4])
ax.plot(x,means6,label=y.index[5])
ax.plot(x,means7,label=y.index[6])
ax.plot(x,means8,label=y.index[7])


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.legend(facecolor = 'lightblue', labelcolor = 'k') #出現圖例，並設定圖例顏色

ax.set_ylabel('人數', fontproperties = 梅圓, color = 'w', fontsize = 15)
ax.set_xlabel('日期', fontproperties = 梅圓, color = 'w', fontsize = 15)
ax.set_title('新竹遊憩據點遊客人次統計折線圖', fontproperties = 梅圓, color = 'w', fontsize = 15)

fig.tight_layout() #盡量擴大版圖

plt.show()

ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')
ax.bar_label(p3, label_type='center')
ax.bar_label(p4, label_type='center')
ax.bar_label(p5, label_type='center')
ax.bar_label(p6, label_type='center')
ax.bar_label(p7, label_type='center')
ax.bar_label(p8, label_type='center')