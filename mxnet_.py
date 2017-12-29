# load model
checkpoint = 0
sym, arg_params, aux_params = \
        mx.model.load_checkpoint('model_prefix', checkpoint)

mod = mx.mod.Module(symbol=sym, context=mx.cpu(), label_names=None)
mod.bind(for_training=False, data_shapes=[('data', (1,3,224,224))], 
        label_shapes=mod._label_shapes)
mod.set_params(arg_params, aux_params, allow_missing=True)


# plot model
mx.viz.plot_network()

# get params 
mod = mx.mod.Module(symbol = symbol, context = mx.cpu(), 
        data_names = ['data'], label_names = ['softmax_label'])
arg_params, aux_params = mod.get_params()

