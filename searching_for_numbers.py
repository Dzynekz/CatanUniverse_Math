import cv2
import numpy as np
import pandas as pd


# Loading imgs
board_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\board.png', cv2.IMREAD_UNCHANGED)
two_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\2.png', cv2.IMREAD_UNCHANGED)
three_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\3.png', cv2.IMREAD_UNCHANGED)
four_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\4.png', cv2.IMREAD_UNCHANGED)
five_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\5.png', cv2.IMREAD_UNCHANGED)
six_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\6.png', cv2.IMREAD_UNCHANGED)
eight_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\8.png', cv2.IMREAD_UNCHANGED)
nine_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\9.png', cv2.IMREAD_UNCHANGED)
ten_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\10.png', cv2.IMREAD_UNCHANGED)
eleven_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\11.png', cv2.IMREAD_UNCHANGED)
twelve_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\12.png', cv2.IMREAD_UNCHANGED)
desert_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\desert.png', cv2.IMREAD_UNCHANGED)

board_img_colored = board_img

# Imgs preprocessing
two_img = cv2.cvtColor(two_img, cv2.COLOR_BGR2GRAY)
three_img = cv2.cvtColor(three_img, cv2.COLOR_BGR2GRAY)
four_img = cv2.cvtColor(four_img, cv2.COLOR_BGR2GRAY)
five_img = cv2.cvtColor(five_img, cv2.COLOR_BGR2GRAY)
six_img = cv2.cvtColor(six_img, cv2.COLOR_BGR2GRAY)
eight_img = cv2.cvtColor(eight_img, cv2.COLOR_BGR2GRAY)
nine_img = cv2.cvtColor(nine_img, cv2.COLOR_BGR2GRAY)
ten_img = cv2.cvtColor(ten_img, cv2.COLOR_BGR2GRAY)
eleven_img = cv2.cvtColor(eleven_img, cv2.COLOR_BGR2GRAY)
twelve_img = cv2.cvtColor(twelve_img, cv2.COLOR_BGR2GRAY)
desert_img = cv2.cvtColor(desert_img, cv2.COLOR_BGR2GRAY)

board_img = cv2.cvtColor(board_img, cv2.COLOR_BGR2GRAY)

# Results *-
result_two= cv2.matchTemplate(board_img, two_img, cv2.TM_CCOEFF_NORMED)
result_three = cv2.matchTemplate(board_img, three_img, cv2.TM_CCOEFF_NORMED)
result_four = cv2.matchTemplate(board_img, four_img, cv2.TM_CCOEFF_NORMED)
result_five = cv2.matchTemplate(board_img, five_img, cv2.TM_CCOEFF_NORMED)
result_six = cv2.matchTemplate(board_img, six_img, cv2.TM_CCOEFF_NORMED)
result_eight = cv2.matchTemplate(board_img, eight_img, cv2.TM_CCOEFF_NORMED)
result_nine = cv2.matchTemplate(board_img, nine_img, cv2.TM_CCOEFF_NORMED)
result_ten = cv2.matchTemplate(board_img, ten_img, cv2.TM_CCOEFF_NORMED)
result_eleven = cv2.matchTemplate(board_img, eleven_img, cv2.TM_CCOEFF_NORMED)
result_twelve = cv2.matchTemplate(board_img, twelve_img, cv2.TM_CCOEFF_NORMED)
result_desert = cv2.matchTemplate(board_img, desert_img, cv2.TM_CCOEFF_NORMED)

results_list = (

    (result_two, two_img, 0.95, (0, 255, 255), '2'),
    (result_three, three_img, 0.95, (255, 0, 255), '3'),
    (result_four, four_img, 0.95, (255, 0, 255), '4'),
    (result_five, five_img, 0.95, (255, 0, 255), '5'),
    (result_six, six_img, 0.95, (255, 0, 255), '6'),
    (result_eight, eight_img, 0.95, (255, 0, 255), '8'),
    (result_nine, nine_img, 0.95, (255, 0, 255), '9'),
    (result_ten, ten_img, 0.95, (255, 255, 0), '10'),
    (result_eleven, eleven_img, 0.95, (128, 44, 55), '11'),
    (result_twelve, twelve_img, 0.95, (212, 100, 30), '12'),
    (result_desert, desert_img, 0.95, (255, 0, 255), '0')
)

detected_rectangles = []

# Drawing rectangles on image
for result, img, threshold, color, number in results_list:
    rectangles = []
    if isinstance(result, list):
        for i, result_val in enumerate(result):
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result_val)
            w = img[i].shape[1]
            h = img[i].shape[0]
            yloc, xloc = np.where(result_val >= threshold)
            for (x, y) in zip(xloc, yloc):
                rectangles.append([int(x), int(y), int(w), int(h)])
                rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.1)
        for (x, y, w, h) in rectangles:
            detected_rectangles.append((x, y, w, h, number))
            cv2.rectangle(board_img_colored, (x, y), (x + w, y + h), color, 2)
    else:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = img.shape[1]
        h = img.shape[0]
        yloc, xloc = np.where(result >= threshold)
        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), int(w), int(h)])
            rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.1)
        for (x, y, w, h) in rectangles:
            detected_rectangles.append((x, y, w, h, number))
            cv2.rectangle(board_img_colored, (x, y), (x + w, y + h), color, 2)  


print('a')
df = pd.DataFrame(detected_rectangles, columns=['x', 'y', 'width', 'height', 'number'])
df = df.sort_values(by=['y'],).reset_index(drop=True)

reference_y = df.loc[0, 'y']

for i in range(1, len(df)):
    if df.loc[i, 'y'] - reference_y < 20:
        df.loc[i, 'y'] = reference_y
    else:
        reference_y = df.loc[i, 'y']

board_numbers = df.sort_values(by=['y', 'x'],).reset_index(drop=True)
print(board_numbers)
      
# Show board 
#cv2.imshow('Board', board_img_colored)
#cv2.waitKey()
#cv2.destroyAllWindows()