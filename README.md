# intro-cv
Introduction to Image Processing and Computer Vision

To install requirements
```bash
pip install -r requirements.txt
```

Simple image processing example. Your homework is to fill in the 
function with an image processing operation
```bash
python 01_image_input.py /path/to/your/image.jpg
```

Simple implementation of Mask Inference
```bash
git clone https://github.com/matterport/Mask_RCNN.git
```

Then
```bash
cd Mask_RCNN
python setup.py install
```
Just to confirm installation, any of the following,
just to verify the entry `mask-rcnn==2.1`
```bash
pip show mask-rcnn
pip freeze
```

To run the Mask-RCNN example:
```bash
python example.py /path/to/your/image.jpg
```