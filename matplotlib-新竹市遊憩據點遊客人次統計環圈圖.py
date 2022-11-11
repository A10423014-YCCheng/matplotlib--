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

placedatas_108 = df.iloc[0:12,1:].sum() #108各地區遊客加總
total108 = placedatas_108.sum() #108所有地區加總

placedatas_109 = df.iloc[12:24,1:].sum() #109各地區遊客加總
total109 = placedatas_109.sum()#109所有地區加總

placedatas_110 = df.iloc[24:36,1:].sum() #110各地區遊客加總
total110 = placedatas_110.sum()#110所有地區加總

size = 0.3
outerpie =[total108, total109, total110] #外圈的數值
outerlabels = ['108年','109年','110年'] #外圈的標籤
print(type(total108))
innerpie = pd.concat([placedatas_108, placedatas_109, placedatas_110], ignore_index= True) #將每年的各地區遊客串成內圈資料

#選色的方法 https://matplotlib.org/stable/tutorials/colors/colormaps.html
cmap = plt.colormaps["tab20b"]
outer_colors = cmap([3,7,11])
cmap = plt.colormaps["tab20c"]
inner_colors = cmap([n for n in range(0,16,2)])

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d} 人)".format(pct, absolute)
#畫外圈 labeldistance = 資料標籤位置, autopct = 顯示百分比, pctdistance =百分比資料標籤位置 textprops=文字特徵, wedgeprops=圓框特徵
outerwedges, outerlabel,outerautotext= ax.pie(outerpie, labels = outerlabels, radius=1.2, colors=outer_colors,
       autopct=lambda pct: func(pct, outerpie),  textprops=dict(color="k", size = '15'),wedgeprops=dict(width=0.9, edgecolor='w'))
plt.setp(outerautotext, size=15, weight="bold") #額外設定百分比資料標籤的大小

#畫內圈
innerwedges, innerlabel = ax.pie(innerpie, radius = 0.5, colors=inner_colors,
       textprops=dict(color="k", size = '10'),wedgeprops=dict(width=size, edgecolor='k'))

#大小要一致
ax.set(aspect="equal")

#設置圖例
legendlabel = list(df.columns[1:])
ax.legend( outerwedges+innerwedges, outerlabels+legendlabel, facecolor = 'lightyellow', labelcolor = 'k',loc=(1,0.4)) #出現圖例，並設定圖例顏色


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_title('新竹遊憩據點遊客人次統計環圈圖', fontproperties = 梅圓, color = 'w', fontsize = 15)

fig.tight_layout() #盡量擴大版圖

plt.show()
