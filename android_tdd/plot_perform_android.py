#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_tdd1_dnlink = pd.read_csv('raw_tdd1_dnlink.csv')
df_tdd1_uplink = pd.read_csv('raw_tdd1_uplink.csv')
df_tdd2_dnlink = pd.read_csv('raw_tdd2_dnlink.csv')
df_tdd2_uplink = pd.read_csv('raw_tdd2_uplink.csv')

fig = plt.figure(figsize=(16,7))

plt.plot('seconds', 'traffic', data = df_tdd1_dnlink, label = 'TDD1 Downlink')
plt.plot('seconds', 'traffic', data = df_tdd1_uplink, label = 'TDD1 Uplink')
plt.plot('seconds', 'traffic', data = df_tdd2_dnlink, label = 'TDD2 Downlink')
plt.plot('seconds', 'traffic', data = df_tdd2_uplink, label = 'TDD2 Uplink')

plt.xlabel("Time (Seconds)")
plt.ylabel("Throughput (Mbps)")
title = "Template: Throughput (using IPerf3) for Android device under test"
plt.title(title)
plt.xlim(2, 300)
plt.ylim(4, 225)

#major_ticks = np.arange(2, 300, 5)
#plt.set_xticks(major_ticks)
#plt.set_yticks(major_ticks)

plt.legend();

plt.show()

