import cv2

# 01. 일반이미지
# img = cv2.imread('./Day07/image.jpeg')
# cv2.imshow('Original',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 02. 그레이이미지
# img = cv2.imread('./Day07/image.jpeg', cv2.IMREAD_GRAYSCALE) # 회색

# cv2.imshow('Original',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 03. 이미지 사이즈 축소
# img = cv2.imread('./Day07/image.jpeg', cv2.IMREAD_GRAYSCALE) # 회색

# img_small = cv2.resize(img,(200,120))
# cv2.imshow('Small',img_small)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 04. 원본을 그대로 두고 흑백을 추가
# img = cv2.imread('./Day07/image.jpeg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Original', img)
# cv2.imshow('Gray', gray)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 05. 이미지 자르기
# img = cv2.imread('./Day07/image.jpeg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# height, width, channel = img.shape
# print(height, width, channel)

# img_crop = img[:, :int(width /2)]
# gray_crop = gray[:, :int(width /2)]
# cv2.imshow('Original', img_crop)
# cv2.imshow('Gray', gray_crop)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 06. 이미지 블러
img = cv2.imread('./Day07/image.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, width, channel = img.shape
print(height, width, channel)

img_crop = img[:, :int(width /2)]
gray_crop = gray[:, :int(width /2)]

img_blur = cv2.blur(img_crop, (30,30)) # 숫자가 클수록 더 많이 블러

cv2.imshow('Original', img_blur)
cv2.imshow('Gray', gray_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()