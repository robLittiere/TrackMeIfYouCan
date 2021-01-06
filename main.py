import cv2
import numpy as np

img_test = cv2.imread('assets/image_test2.png')
img_ref = cv2.imread('assets/image_ref.png')

# Select ROI
# roi = cv2.selectROI("Image", img_test)

# Crop image
# imageCrop = img_test[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
# cv2.imwrite("assets/cropped_image.png", imageCrop)


# Display crop
#cv2.imshow("image", imageCrop)


dimension = img_test.shape
height = dimension[0]
width = dimension[1]

dimension_ref = img_ref.shape
height_ref = dimension_ref[0]
width_ref = dimension_ref[1]

# for i in range(height - height_ref):
#     for j in range(width - width_ref):
#         r, g, b = img_test[i, j]
#         if r == 36 and g == 28 and b == 237:
#             pass
# print(img_test[14, 182])


for i in range(height - height_ref):
    for j in range(width - width_ref):
        pixel_exist = True
        for k in range(height_ref):
            offset = j
            if not pixel_exist:
                break
            for l in range(width_ref):
                if not pixel_exist:
                    break
                r, g, b = img_test[i, offset]
                comp_r, comp_g, comp_b = img_ref[k, l]
                if r == comp_r and g == comp_g and b == comp_b:
                    pixel_exist = True
                else:
                    pixel_exist = False
                offset += 1
        if pixel_exist:
            print('yes it works')













# for i in range(height - height_ref):
#     for j in range(width - width_ref):
#         # Comparer avec l'image de ref
#         is_same_pixel = True
#         for k in range(height_ref):
#             # Si les pixels ne sont pas les mêmes, on casse et on regarde les prochains
#             if not is_same_pixel:
#                 break
#             offset = j
#             for l in range(width_ref):
#                 if not is_same_pixel:
#                     break
#                 r, g, b = img_test[i, offset]
#                 comp_r, comp_g, comp_b = img_ref[k, l]
#                 # is_same_pixel = r == comp_r and g == comp_g and b == comp_b  version concise du if / else
#                 if r == comp_r and g == comp_g and b == comp_b:
#                     is_same_pixel = True
#                 else :
#                     is_same_pixel = False
#                 offset += 1
#         if is_same_pixel:
#             print(i, j)





#
# # Boucle sur tous les pixels
# for i in range(len(img)):
#
#     # On récupère les composantes rgb de chaque pixel
#     for r, g, b in img[i]:
#         for comp_r, comp_g, comp_b in imageCrop[i]:
#             if r == comp_r and g == comp_g and b == comp_b:
#                 pass
#         # On check si 3 pixels sont égaux aux premiers pixels de notre image ROI
#
#         # Si ils sont égaux
#         if r == comp_r and g == comp_g and b == comp_b:
#
#             # On regarde si les 3 suivants sont eux aussi égaux
#             for comp_r, comp_g, comp_b in imageCrop[i]:
#                 pass
#
#
#
# for x in img:
#     for r, g, b in x:
#         comp_r, comp_g, comp_b = imageCrop[0][0]
#         if r == comp_r and g == comp_g and b == comp_b:
#             pass


# for i in imageCrop:
#     print(i[0, 0])
#
# b, g, r = imageCrop[100, 100]
# print(b)
# print(g)
# print(r)





