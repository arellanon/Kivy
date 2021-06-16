#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:16:24 2021

@author: nahuel
"""
import numpy as np
import matplotlib.pyplot as plt
import time

plt.style.use("ggplot")
plt.axis([0, 100, 0, 1])
plt.ion()

xs = [0, 0]
ys = [1, 1]

for i in range(100):
    y = np.random.random()
    xs[0] = xs[1]
    ys[0] = ys[1]
    xs[1] = i
    ys[1] = y
    plt.plot(xs, ys)
    time.sleep(0.1)
    plt.pause(0.1)