#!/usr/bin/env python

import argparse
import re, os
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def get_metric(filename):

    f = open(filename, 'r')
    lines = f.readlines()

    epoch = []
    cross_entropy = []
    mae = []
    cross_entropy_classify = []


    val_epoch = []
    val_cross_entropy = []
    val_mae = []
    val_cross_entropy_classify = []

    for line in lines:
        line = line.strip()
        pattern = re.compile('INFO:root:Epoch\[\d+\] Batch \[\d+\]\s*Speed: \d+\.\d* samples/sec\s*cross-entropy=\d+\.\d*\s*mae=\d+\.\d*')
        match = pattern.match(line)
        if match is not None:
            digit = re.compile('\d+\.?\d*')
            res = digit.findall(line)
            epoch.append(int(res[0]))
            cross_entropy.append(float(res[3]))
            mae.append(float(res[4]))
            if len(res) == 6:
                cross_entropy_classify.append(float(res[5]))


        pattern = re.compile('INFO:root:Epoch\[\d+\] Validation-cross-entropy=\d+\.\d*')
        match = pattern.match(line)
        if match is not None:
            digit = re.compile('\d+\.?\d*')
            res = digit.findall(line)
            val_epoch.append(int(res[0]))
            val_cross_entropy.append(float(res[1]))


        pattern = re.compile('INFO:root:Epoch\[\d+\] Validation-mae=\d+\.\d*')
        match = pattern.match(line)
        if match is not None:
            digit = re.compile('\d+\.?\d*')
            res = digit.findall(line)
            val_mae.append(float(res[1]))


        pattern = re.compile('INFO:root:Epoch\[\d+\] Validation-classify cross-entropy=\d+\.\d*')
        match = pattern.match(line)
        if match is not None:
            digit = re.compile('\d+\.?\d*')
            res = digit.findall(line)
            val_cross_entropy_classify.append(float(res[1]))

    return [[epoch, cross_entropy], [epoch, mae], 
            [val_epoch, val_cross_entropy], [val_epoch, val_mae],
            [epoch, cross_entropy_classify], [val_epoch, val_cross_entropy_classify]]


global c 
color = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'] * 10

def fliter_by_scale(epoch, metric):
    global scale
    epoch_list = []
    metric_list = []

    res_epoch = []
    res_metric = []

    for e, m in zip(epoch, metric):
        epoch_list.append(e)
        metric_list.append(m)
        if len(epoch_list) == int(scale):
            res_epoch.append(np.mean(epoch_list))
            res_metric.append(np.mean(metric_list))

            epoch_list = []
            metric_list = []

    return res_epoch, res_metric


def refresh():
    global file_list 
    global val_list 
    global canvas


    global metrics 
    global metrics_val

    import matplotlib.backends.tkagg as tkagg
    from matplotlib.backends.backend_agg import FigureCanvasAgg

    global color

    figure = plt.figure()
    for i, filename in enumerate(file_list):
        if val_list[i].get() == 1:
            epoch, metric = get_metric(filename)[metrics_val.get()]
            if len(metric) == 0:
                epoch = []
            epoch, metric = fliter_by_scale(epoch, metric)
            plt.plot(epoch, metric, color=color[i])
            
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()    
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)

    plt.close()

    global photo
    photo = tk.PhotoImage(master=canvas)
    canvas.create_image(figure_w/2, figure_h/2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
            
def set_scale(s):
    global scale
    scale = s
    refresh()


if __name__ == '__main__':
    import Tkinter as tk
    w = tk.Tk()
    w.title('my window')
    w.geometry('1200x900')

    global file_list 
    global val_list 

    file_list = []
    val_list = []
    

    for parent, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            if 'stderr' in filename:
                file_list.append(filename)
                val = tk.IntVar()
                c = tk.Checkbutton(w, text=filename, variable=val, onvalue=1, offvalue=0,
                        command=refresh).place(x = 35, y = len(file_list) * 25, anchor='nw')
                val_list.append(val)

                l = tk.Label(w, text='==', fg=color[len(file_list) - 1])
                l.place(x = 10, y = len(file_list) * 25, anchor='nw')

    s = tk.Scale(w, label='scale', from_=1, to=20, orient=tk.HORIZONTAL,
                         length=200, showvalue=1, tickinterval=19, resolution=1, command=set_scale)
    s.place(x = 20, y = (len(file_list) + 1.5) * 25, anchor='nw')

    global metrics 
    global metrics_val

    metrics = ['CE', 'MAE', 'val-CE', 'val-MAE', 'CE-classify', 'val-CE-classify'] 
    metrics_val = tk.IntVar()

    for i, metric in enumerate(metrics):
        c = tk.Radiobutton(w, text=metric, value=i, variable=metrics_val,
                command=refresh).place(x = 20, y = (len(file_list) + 5) * 25 + i * 25, anchor='nw')

    
    global canvas
    canvas = tk.Canvas(w, bg='white', height=800, width=800)
    canvas.pack(side='right')

    w.mainloop()

