import layoutparser as lp
import pdf2image
from PIL import Image
image = Image.open("test.jpg")
model = lp.Detectron2LayoutModel('lp://PrimaLayout/mask_rcnn_R_50_FPN_3x/config')
# image = Image.open("path/to/image")
print(model)
layout = model.detect(image)
lp.draw_box(image, layout, box_width=3)