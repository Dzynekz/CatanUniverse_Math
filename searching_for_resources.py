import cv2
import numpy as np


# Loading imgs
board_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\board.png', cv2.IMREAD_UNCHANGED)
brick_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\brick.png', cv2.IMREAD_UNCHANGED)
sheep_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\sheep.png', cv2.IMREAD_UNCHANGED)
grain_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\grain.png', cv2.IMREAD_UNCHANGED)
ore_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\ore.png', cv2.IMREAD_UNCHANGED)
tree_img = cv2.imread('D:\\Marcin\\projekty\\Catan_AI\\images\\tree.png', cv2.IMREAD_UNCHANGED)

city_imgs = [cv2.imread(f'D:\\Marcin\\projekty\\Catan_AI\\images\\city{i}.png', cv2.IMREAD_UNCHANGED)for i in range(1, 3)]
village_imgs = [cv2.imread(f'D:\\Marcin\\projekty\\Catan_AI\\images\\village{i}.png', cv2.IMREAD_UNCHANGED)for i in range(1, 4)]

road_imgs = [cv2.imread(f'D:\\Marcin\\projekty\\Catan_AI\\images\\road{i}.png', cv2.IMREAD_UNCHANGED) for i in range(1, 4)]

board_img_colored = board_img

# Imgs preprocessing
tree_img = cv2.cvtColor(tree_img, cv2.COLOR_BGR2GRAY)
brick_img = cv2.cvtColor(brick_img, cv2.COLOR_BGR2GRAY)
sheep_img = cv2.cvtColor(sheep_img, cv2.COLOR_BGR2GRAY)
grain_img = cv2.cvtColor(grain_img, cv2.COLOR_BGR2GRAY)
ore_img = cv2.cvtColor(ore_img, cv2.COLOR_BGR2GRAY)

city_imgs = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in city_imgs]
village_imgs = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in village_imgs]
road_imgs_gray = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in road_imgs]

board_img = cv2.cvtColor(board_img, cv2.COLOR_BGR2GRAY)

# Results
result_tree = cv2.matchTemplate(board_img, tree_img, cv2.TM_CCOEFF_NORMED)
result_brick = cv2.matchTemplate(board_img, brick_img, cv2.TM_CCOEFF_NORMED)
result_sheep = cv2.matchTemplate(board_img, sheep_img, cv2.TM_CCOEFF_NORMED)
result_grain = cv2.matchTemplate(board_img, grain_img, cv2.TM_CCOEFF_NORMED)
result_ore = cv2.matchTemplate(board_img, ore_img, cv2.TM_CCOEFF_NORMED)

results_cities = [cv2.matchTemplate(board_img, img, cv2.TM_CCORR_NORMED) for img in city_imgs]
results_villages = [cv2.matchTemplate(board_img, img, cv2.TM_CCORR_NORMED) for img in village_imgs]

results_roads = [cv2.matchTemplate(board_img, img, cv2.TM_CCOEFF_NORMED) for img in road_imgs_gray]

results_list = (
    #(results_cities, city_imgs, 0.95, (0, 0, 0)),
    #(results_villages, village_imgs, 0.92, (255, 255, 255)),
    #(results_roads, road_imgs_gray, 0.9, (100, 165, 0)),
    (result_tree, tree_img, 0.92, (0, 255, 255)),
    (result_grain, grain_img, 0.89, (255, 255, 0)),
    (result_brick, brick_img, 0.88, (255, 0, 0)),
    (result_sheep, sheep_img, 0.92, (128, 0, 128)),
    (result_ore, ore_img, 0.89, (0, 255, 0))
)


# Drawing rectangles on image
for result, img, threshold, color in results_list:
    rectangles = []
    if isinstance(result,list):
        
        for i, result_val in enumerate(result):
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result_val)    

            w = img[i].shape[1]
            h = img[i].shape[0]

            #threshold = 0.91
            yloc, xloc = np.where(result_val >= threshold)
            print(len(xloc))

            for (x,y) in zip(xloc, yloc):
                rectangles.append([int(x),int(y),int(w),int(h)])
                rectangles.append([int(x),int(y),int(w),int(h)])

        rectangles, weights = cv2.groupRectangles(rectangles, 1,0.1)
        #print(len(rectangles))    

        for (x,y,w,h) in rectangles:
            cv2.rectangle(board_img_colored, (x,y), (x+w, y+h),color,2)
    else:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        rectangles = []

        w = img.shape[1]
        h = img.shape[0]

        #threshold = 0.92
        yloc, xloc = np.where(result >= threshold)
        print(len(xloc))

        for (x,y) in zip(xloc, yloc):
            rectangles.append([int(x),int(y),int(w),int(h)])
            rectangles.append([int(x),int(y),int(w),int(h)])

        rectangles, weights = cv2.groupRectangles(rectangles, 1,0.1)
        #print(len(rectangles))

        for (x,y,w,h) in rectangles:
            cv2.rectangle(board_img_colored, (x,y), (x+w, y+h),color,2)      
           
# Show board 
cv2.imshow('Board', board_img_colored)
cv2.waitKey()
cv2.destroyAllWindows()
