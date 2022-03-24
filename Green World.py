import cv2
import numpy as np
import matplotlib.pyplot as plt

path = input("Enter file path: ")

CE = int(input("Enter the amount of carbon emission of the region per year in kg "))

image = cv2.imread(path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# plt.imshow(gray, cmap='gray')

blur = cv2.GaussianBlur(gray, (11, 11), 0)
# plt.imshow(blur, cmap='gray')

canny = cv2.Canny(blur, 30, 150, 3)
#plt.imshow(canny,cmap="gray")

dilated = cv2.dilate(canny, (1, 1), iterations=0)
# plt.imshow(dilated, cmap='gray')

(cnt, hierarchy) = cv2.findContours(
    dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
# plt.imshow(rgb)

n = len(cnt)

print("Number of trees in the image is:", n)
o = n*0.7
c = n*0.068
print("Amount of oxygen emitted by the trees in the area ", round(o, 3), "kg per day")
AP = o*365
print("Amount of oxygen emitted by the trees in the area per year ", round(AP, 3), 'kg')

print("Amount of carbon dioxide absorbed by the trees in the area per year ", round(c, 3), "kg per day")
AB = c*365
print("Amount of carbon absorbed by the trees in the area per year ", round(AB, 3), "kg")
w = CE-AB
print()
if w<0:
  print("Please recheck the carbon emissions submitted")
else:
  if w <= 2000:
    print("The health of the region is perfect")

  else:
    if n < 90:
      print("plant ", 90-n, "trees")
      print("Pine, Oak, Aspen, Douglas-fir, Spruce, True fir, Beech, and Maple are suitable for the condition ")
      t = round(90-n/9)
      print("plant", t, "trees of different species ")
    else:
      print("Carbon levels are high and emissions must be controlled")

  print()
  print(" /// COMPOSITION OF OXYGEN AND CARBON DIOXIDE \\\ ")
  y = np.array([AP, w])
  mylabels = ["Oxygen", "Carbon dioxide"]

  myexplode = [0.05, 0]

  plt.pie(y, labels = mylabels, explode = myexplode)

  plt.show() 
