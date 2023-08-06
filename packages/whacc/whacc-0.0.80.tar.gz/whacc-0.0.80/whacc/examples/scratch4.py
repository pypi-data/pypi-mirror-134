
from whacc import image_tools
from datetime import datetime

h5 = ['/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/model_testing/all_data/test_data/small_h5s/3lag/small_test_3lag.h5']
h5 = ['/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/model_testing/all_data/all_models/regular_80_border/data/regular/train_regular.h5']

h5 = ['/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/model_testing/all_data/all_models/regular_80_border_aug_0_to_9/data/3lag/train_3lag.h5']

lstm_len = 5
batch_size = 100
h5_file_list = h5
G = image_tools.ImageBatchGenerator_LSTM(lstm_len, batch_size, h5_file_list, label_key = 'labels', IMG_SIZE = 96)
start = datetime.now()
for k in range(G.__len__()):
      x, y = G.__getitem__(k)
print(datetime.now() - start)

lstm_len = 5
batch_size = 400
h5_file_list = h5
G = image_tools.ImageBatchGenerator_LSTM(lstm_len, batch_size, h5_file_list, label_key = 'labels', IMG_SIZE = 96)
start = datetime.now()
for k in range(G.__len__()):
      x, y = G.__getitem__(k)
print(datetime.now() - start)

lstm_len = 5
batch_size = 800
h5_file_list = h5
G = image_tools.ImageBatchGenerator_LSTM(lstm_len, batch_size, h5_file_list, label_key = 'labels', IMG_SIZE = 96)
start = datetime.now()
for k in range(G.__len__()):
      x, y = G.__getitem__(k)
print(datetime.now() - start)

lstm_len = 5
batch_size = 1200
h5_file_list = h5
G = image_tools.ImageBatchGenerator_LSTM(lstm_len, batch_size, h5_file_list, label_key = 'labels', IMG_SIZE = 96)
start = datetime.now()
for k in range(G.__len__()):
      x, y = G.__getitem__(k)
print(datetime.now() - start)


import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

multiplier_1 = ((8.33+3.59)/8.33)
multiplier_1*8*200/60



from whacc import utils, image_tools
from datetime import datetime
h5_file_list = ["/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/model_testing/all_data/all_models/small_h5s/data/3lag/small_train_3lag.h5"]
lstm_len = 5
batch_size = 100
G = image_tools.ImageBatchGenerator_LSTM(lstm_len, batch_size, h5_file_list, label_key = 'labels', IMG_SIZE = 96)
start = datetime.now()
h5creator = image_tools.h5_iterative_creator('/Users/phil/Desktop/LSTM_small_train.h5')
for k in range(G.__len__()):
      x, y = G.__getitem__(k)
      h5creator.add_to_h5(x, y)
print(datetime.now() - start)


h5 = '/Users/phil/Desktop/LSTM_small_train.h5'
import h5py
with h5py.File(h5, 'r') as h:
      print(h['images'].shape)



from whacc import image_tools

h5_file_list = ['/Users/phil/Dropbox/HIRES_LAB/GitHub/Phillip_AC/model_testing/all_data/all_models/small_h5s/data/3lag/small_train_3lag.h5']
lstm_len = 5
batch_size = 100 # 1, 5, 10 and 50 work  ....... # 2, 22, 20, 100, 240 dont work
G = image_tools.ImageBatchGenerator_LSTM(lstm_len, batch_size, h5_file_list, label_key = 'labels', IMG_SIZE = 96)
for k in range(G.__len__()):
  x, y = G.__getitem__(k)
  print(x.shape, y.shape)
