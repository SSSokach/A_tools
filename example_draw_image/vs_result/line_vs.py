import matplotlib.pyplot as plt
from matplotlib import font_manager,text
import numpy as np


index=['Acc-1','Acc-2','Acc-3','Acc-4','Acc-5']

blender=np.array([16.95,31.58,45.52,55.39,68.2])/100
misc=np.array([31.668,47.28,59.604,69.364,78.594])/100
transesc=np.array([34.77,52.41,67.27,77.65,85.02])/100



plt.figure(dpi=200)

plt.plot(index,transesc, c='red', label="TransESC")
plt.plot(index,misc, c='green', label="MISC")
plt.plot(index,blender,c='blue',label="BlenderBot-Joint")
# plt.plot(index,misc, c='green', linestyle='--', label="MISC")
# plt.plot(index,blender,c='blue',linestyle='-.', label="Blender-Joint")
plt.scatter(index, transesc, c='red')
plt.scatter(index, misc, c='green')
plt.scatter(index, blender, c='blue')


font_roman = font_manager.FontProperties(size=15,fname='/users10/shilongwang/workplace/A_tools/draw/times_new_roman/timesbd.ttf')
plt.xticks(fontproperties=font_roman)
plt.yticks([0.2,0.4,0.6,0.8], fontproperties=font_roman)
plt.legend(loc='lower right',prop=font_roman)
plt.savefig(f'./out.jpg')
plt.savefig(f'./out.pdf')
plt.savefig(f"./out.svg", dpi=200,format="svg")