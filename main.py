import layoutparser as lp
import pdf2image
from PIL import Image
image = pdf2image.convert_from_path("CM2 CM3 VRAI_compressed.pdf")
model = lp.Detectron2LayoutModel('lp://PrimaLayout/mask_rcnn_R_50_FPN_3x/config')
# image = Image.open("path/to/image")
print(model)
layout = model.detect(image[0])
print(layout)