import glymur
import tifffile as tiff
import numpy as np
def imread16bit(path):

    img_16bit = tiff.imread(path)
    img_16bit = img_16bit.astype(np.float16)
    img_16bit = img_16bit[:, :, 0:3]
    return img_16bit

'''compress'''
# path = r"C:\Users\Administrator\Desktop\meiyong\Y_cropped_row0_col0.tif"
# img_array = imread16bit(path)
# img_array = img_array.astype(np.uint16)
#
# output_jp2 = r"C:\Users\Administrator\Desktop\meiyong\output_lossless.jp2"
# glymur.Jp2k(
#     output_jp2,
#     img_array,
#     irreversible=False,
#     colorspace='RGB',
#     shape=(512,512,3)
# )


'''decode'''

input_jp2 = r"C:\Users\Administrator\Desktop\meiyong\output_lossless.jp2"
jp2 = glymur.Jp2k(input_jp2)

decoded_array = jp2[:]

tiff.imwrite(r'C:\Users\Administrator\Desktop\meiyong\decoded_image.tif',decoded_array, photometric='rgb')
