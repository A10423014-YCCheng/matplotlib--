import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

#Step1. 設定整體參數，可以print(mpl.rcParams.keys())看目前設定
# 將字體換成Microsoft JhengHei
mpl.rcParams['font.family'] = ['Microsoft JhengHei']
mpl.rcParams['text.color'] ='w'
# 修復負號顯示問題
mpl.rcParams['axes.unicode_minus'] = False
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


means1 = y['十八尖山']
means2 = y['青青草原']
means3 = y['城隍廟']
means4 = y['新竹漁港']
means5 = y['賞蟹步道']
means6 = y['青草湖']
means7 = y['十七公里腳踏車道']
means8 = y['新竹公園']

width = 0.35       # the width of the bars: can also be len(x) sequence
base = np.zeros(12)
cmap = plt.colormaps["Paired"]
colors = cmap([i for i in range(9)])

#累加基底，每一次的基底都要加上前面的人
#迴圈寫法
for n,item in enumerate(y):
    ax.bar(x,y[item],width, bottom = base, label = item, color = colors[n])
    base += y[item]
#笨方法
#ax.bar(x, y['十八尖山'],                width,                                  label='十八尖山')
#ax.bar(x, y['青青草原'],                width,  bottom=y['十八尖山'],  label='青青草原')
#ax.bar(x, y['城隍廟'],                   width,  bottom=y['十八尖山']+y['青青草原'], label='城隍廟')
#ax.bar(x, y['新竹漁港'],                width,  bottom=y['十八尖山']+y['青青草原']+y['城隍廟'], label='新竹漁港')
#ax.bar(x, y['賞蟹步道'],                width,  bottom=y['十八尖山']+y['青青草原']+y['城隍廟']+y['新竹漁港'], label='賞蟹步道')
#ax.bar(x, y['青草湖'],                   width,  bottom=y['十八尖山']+y['青青草原']+y['城隍廟']+y['新竹漁港']+y['賞蟹步道'], label='青草湖')
#ax.bar(x, y['十七公里腳踏車道'],    width,  bottom=y['十八尖山']+y['青青草原']+y['城隍廟']+y['新竹漁港']+y['賞蟹步道']+y['青草湖'], label='十七公里腳踏車道')
#ax.bar(x, y['新竹公園'],                width,  bottom=y['十八尖山']+y['青青草原']+y['城隍廟']+y['新竹漁港']+y['賞蟹步道']+y['青草湖']+y['十七公里腳踏車道'], label='新竹公園')

ax.axhline(0, color='grey', linewidth=0.8)
ax.set_xticks(x, labels=x)


# Label with label_type 'center' instead of the default 'edge'




# Add some text for labels, title and custom x-axis tick labels, etc.
ax.legend(facecolor = 'lightyellow', labelcolor = 'k') #出現圖例，並設定圖例顏色

ax.set_ylabel('人數', fontproperties = 梅圓, color = 'w', fontsize = 15)
ax.set_xlabel('日期', fontproperties = 梅圓, color = 'w', fontsize = 15)
ax.set_title('新竹遊憩據點遊客人次統計折線圖', fontproperties = 梅圓, color = 'w', fontsize = 15)

fig.tight_layout() #盡量擴大版圖

plt.show()