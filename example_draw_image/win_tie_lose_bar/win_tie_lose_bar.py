import matplotlib.pyplot as plt
from matplotlib import font_manager

name_list=[
    'Chinese Alpaca w/o H.R',
    'Bloomz-7b1-mt w/o H.R',
    'Chinese LLaMA w/o H.R',
    'Bloom-7b1 w/o H.R',
    'Chinese LLaMA',
    'zero-shot Chinese Alpaca',
    'BART',
    'ChatGPT',
]
all_result_count=[
    [57, 3, 40], 
    [53, 2, 45], 
    [60, 0, 40], 
    [54, 0, 46], 
    [55, 4, 41],
    [66, 1, 33], 
    [65, 2, 33], 
    [54, 1, 45]
]


colors = ['#ffa289', '#6a92cc', '#706fab']
labels = ['Win', 'Tie', 'Lose']

fig, ax = plt.subplots(1, dpi=400,figsize=(7,5))
font_roman_legend = font_manager.FontProperties(size=15,fname='/users10/shilongwang/workplace/A_tools/draw/times_new_roman/timesbd.ttf')
font_roman_xticks = font_manager.FontProperties(size=12,fname='/users10/shilongwang/workplace/A_tools/draw/times_new_roman/timesbd.ttf')
font_roman_yticks = font_manager.FontProperties(size=11,fname='/users10/shilongwang/workplace/A_tools/draw/times_new_roman/timesbd.ttf')
# 绘图
left = len(all_result_count) * [0]
x=[i+1 for i in range(len(all_result_count))]
for idx in range(len(labels)):
    value=[i[idx] for i in all_result_count]
    bar=plt.barh(name_list, value, left = left, color=colors[idx])
    plt.bar_label(bar, label_type='center', fontproperties=font_roman_yticks)
    left = [a+b for a,b in zip(left,value)]


# 标题、图例、标签
plt.legend(labels, bbox_to_anchor=(0.5,0.98),loc='lower center', ncol=4, frameon=False, prop=font_roman_legend)
plt.yticks(name_list,rotation=30, fontproperties=font_roman_yticks)
plt.xticks(fontproperties=font_roman_xticks)
plt.subplots_adjust(left=0.25,bottom=0.2)
# 去除spines
ax.spines['right'].set_visible(False)
# ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# 调整界限并绘制网格线
# plt.ylim(-0.5, ax.get_yticks()[-1] + 0.5)
ax.set_axisbelow(True)
ax.xaxis.grid(color='gray', linestyle='dashed')

plt.savefig('./visualization.jpg')
# plt.savefig('./visualization.pdf')