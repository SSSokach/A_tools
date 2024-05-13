import matplotlib.pyplot as plt
import numpy as np


index={
  "neutral": 0,
  "joy": 1,
  "disgust": 2,
  "optimism": 3,
  "pessimism": 4,
  "trust": 5,
  "surprise": 6,
  "fear": 7,
  "anticipation": 8,
  "anger": 9,
  "love": 10,
  "sadness": 11
}
x=list(index.keys())

nums=[3262, 1022, 687, 880, 178, 1118, 199, 453, 832, 226, 187, 486]


plt.figure(dpi=300)

bar=plt.bar(x,nums)

plt.bar_label(bar,padding=5)
plt.xticks(list(index.values()),list(index.keys()), rotation=35)
plt.yticks([0,1000,2000,3000,4000])

# plt.legend(loc='lower right')
plt.subplots_adjust(bottom=0.15)
plt.savefig(f'out.jpg')