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



# change fc layer's num classes
import mxnet as mx

def changeFC(num_classes):
  symbol, arg_params, aux_params = mx.model.load_checkpoint('huoshan_money_social_events_resnet-50_rgb', 0)
  all_layers = symbol.get_internals()

  net = all_layers['rgb_dropout_0.50_3_output']
  net = mx.symbol.FullyConnected(data = net, num_hidden = num_classes, name = 'rgb_cnn_fc_cls_new')
  net = mx.symbol.SoftmaxOutput(data = net, name = 'rgb_cnn_softmax')

  new_args = dict({k:arg_params[k] for k in arg_params if 'rgb_cnn_fc_cls' not in k})

  mod = mx.mod.Module(symbol=net, context=mx.cpu(), label_names=None, data_names=['rgb_data'])
  mod.bind(for_training=False, data_shapes=[('rgb_data', (60,5,3,224,224))], label_shapes=mod._label_shapes)
  mod.set_params(new_args, aux_params, allow_missing=True)
  mod.save_checkpoint('huoshan_social_money', 0)

if __name__ == '__main__':
  changeFC(2)

