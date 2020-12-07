import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# data to plot
n_groups = 11


bld_old = (9.03, 6.61, 6.56, 14.21,	6.95,	11.08,	4.31,	2.83,	9.11,	7.64, 21.01)
bld_new = (9.31, 6.53, 6.69, 14.48, 5.91, 10.18, 4.29, 2.01, 10.98, 6.94, 21.85)

#plt.figure(1)
#plt.figure(figsize=(10,5))

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8

rects1 = plt.bar(index, bld_new, bar_width, alpha=opacity, color='teal', label='Bld 2')

rects2 = plt.bar(index + bar_width, bld_old, bar_width, alpha=opacity, color='chocolate', label='Bld 1')

#plt.xlabel('some build (26) vs. some build (81)')
plt.ylabel('Time (Seconds)')
#plt.title('Some Performance test with Load')
plt.xticks(rotation=75)
#plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'))
plt.legend()

plt.tight_layout()

rows = ["Build2", "Build1"]
columns = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K')
color = ('teal', 'chocolate')

#plt.figure(figsize=(10,5))

#the_table = plt.table(cellText=[[1,2,3,4,5,6,7,8,9,10,11], [3,4,5,6,7,8,9,8,7,6,5]],
the_table = plt.table(cellText=[bld_new, bld_old],
                      rowLabels=rows,
                      rowColours=color,
                      colLabels=columns,
                      loc='bottom')

the_table.auto_set_font_size(False)
the_table.set_fontsize(9)

#### plt.figure(figsize=(10,5))

#plt.subplots(figsize=(10,5))

plt.subplots_adjust(left=0.1, bottom=0.2, top=0.9)

plt.ylabel("KPI (in seconds)")
#plt.yticks(new_build, old_build)
plt.xticks([])

plt.figtext(0.5, 0.05,"01(2) vs. old build 1", wrap=True, horizontalalignment='center', fontsize=9)

plt.title('Template: KPI Performance: with Load (seconds or bandwidth')

#### plt.figure(figsize=(10,5))

#matplotlib.rc('figure', figsize=[10,5])

plt.show()

