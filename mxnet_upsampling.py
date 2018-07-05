import mxnet as mx
import numpy as np
import cv2

from collections import namedtuple
Batch = namedtuple('Batch', ['data'])

img_resize_size = 224

class Test:
    def get_image(self, img):
        img = cv2.resize(img, (img_resize_size, img_resize_size), interpolation=cv2.INTER_LINEAR)
        origin_img = img.copy()
        img = img.transpose((2,0,1))
        img = img[np.newaxis,...]
        return img, origin_img

    def test(self):
        ctx = [mx.cpu()]
        data = mx.sym.Variable(name='data')
        upsample = mx.sym.UpSampling(data = data,
                scale = 2, num_filter = 3, sample_type='bilinear')

        self.mod = mx.mod.Module(symbol=upsample, context=ctx, label_names=None)
        self.mod.bind(for_training=False, data_shapes=[('data', (1,3,224,224))],
                label_shapes=self.mod._label_shapes)
        self.mod.init_params(mx.initializer.Uniform(scale=1.0))

        img = np.random.rand(224, 224, 3)
        img = cv2.imread('1.jpg')
        img, origin_img = self.get_image(img)
        self.mod.forward(Batch([mx.nd.array(img)]))
        output = self.mod.get_outputs()[0].asnumpy()

        output = output[0].transpose((1, 2, 0)).astype(np.uint8)
        cv2.imshow('origin_img', origin_img)
        cv2.imshow('output', output)
        cv2.waitKey(0)
        print(origin_img.shape, output.shape)

myTest = Test()
myTest.test()
