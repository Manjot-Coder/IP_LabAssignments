import cv2

# Read the grayscale image
img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found!")
    exit()

# CASE 1: Mean Intensity as Threshold
mean_threshold = img.mean()

_, binary_mean = cv2.threshold(
    img, mean_threshold, 255, cv2.THRESH_BINARY
)

print("Case 1: Mean Intensity Threshold =", mean_threshold)

cv2.imshow("Original Grayscale Image", img)
cv2.imshow("Binary Image - Mean Threshold", binary_mean)

cv2.waitKey(0)
cv2.destroyAllWindows()


# CASE 2: User Input Threshold
threshold = int(input("Enter threshold value (0-255): "))

if threshold < 0 or threshold > 255:
    print("Error: Threshold must be between 0 and 255.")
    exit()

_, binary_user = cv2.threshold(
    img, threshold, 255, cv2.THRESH_BINARY
)

cv2.imshow("Binary Image - User Threshold", binary_user)

cv2.waitKey(0)
cv2.destroyAllWindows()
