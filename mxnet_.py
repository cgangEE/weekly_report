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


# mx.io.DataBatch
for data_batch in DetRecordIter() or mx.io.DataIter():   
    data_batch.data : NDArray list
    data_batch.label : NDArray list
    data_batch.pad : the number of examples padded at the end of a batch
    data_batch.index : the example indices in this batch
    ...

