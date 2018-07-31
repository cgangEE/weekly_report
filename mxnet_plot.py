#!/usr/bin/env python

import mxnet as mx
import argparse
import os

def plot(filename, data, data_shape):
    sym = mx.sym.load(filename)
    node_attrs = {"hide_weights":"true", "fixedsize":"false", "shape":"oval"}
    viz = mx.viz.plot_network(sym, shape={data:data_shape}, node_attrs = node_attrs)
    filename += '_plot'
    viz.render(filename)
    os.remove(filename)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('symbol', help='mxnet json symbol file')
    p.add_argument('--data', default='data', help='input node name')
    p.add_argument('--shape', default=(1, 3, 224, 224), help='input node shape', nargs="+", type=int)
    args = p.parse_args()
    args.shape = tuple(args.shape)

    plot(args.symbol, args.data, args.shape)

