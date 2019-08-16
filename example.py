# example of mask inference with a pre-trained model (COCO)
import sys
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from mrcnn.config import Config
from mrcnn.model import MaskRCNN
from mrcnn.visualize import display_instances
from tools import load_config

# load config params - labels
cfg_dict = load_config('config.yaml')
class_names = cfg_dict['class_names']


# config settings for model inference
class ConfigParams(Config):
    NAME = "test"
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    NUM_CLASSES = 1 + 80


# replicate the model for pure inference
rcnn_model = MaskRCNN(mode='inference', model_dir='models/', config=ConfigParams())
# model weights input
path_weights_file = 'models/mask_rcnn_coco.h5'
rcnn_model.load_weights(path_weights_file, by_name=True)

# single image input
path_to_image = sys.argv[1]
img = load_img(path_to_image)

# transition to array
img = img_to_array(img)
print('Image shape:', img.shape)
# make inference
results = rcnn_model.detect([img], verbose=0)
# the output is a list of dictionaries, where each dict has a single object detection
# {'rois': array([[ 30,  54, 360, 586]], dtype=int32),
#  'class_ids': array([21], dtype=int32),
#  'scores': array([0.9999379], dtype=float32),
#  'masks': huge_boolean_array_here ...
result_params = results[0]
# show photo with bounding boxes, masks, class labels and scores
display_instances(img,
                  result_params['rois'],
                  result_params['masks'],
                  result_params['class_ids'],
                  class_names,
                  result_params['scores'])
