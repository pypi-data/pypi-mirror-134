import copy
import os
import cv2
import numpy as np
from Openpose.src import util
from Openpose.src.body import Body
from Openpose.src.hand import Hand
import glob

os.environ["CUDA_VISIBLE_DEVICES"] = "0"


class Openpose:
    def __init__(self, body_pose_model, hand_pose_model):
        self.body_estimation = Body(body_pose_model)
        self.hand_estimation = Hand(hand_pose_model)

    def train(self, images_root_path, results_root_path):
        images = glob.glob(os.path.join(images_root_path, '*.png')) + \
                 glob.glob(os.path.join(images_root_path, '*.jpg')) + \
                 glob.glob(os.path.join(images_root_path, '*.bmp')) + \
                 glob.glob(os.path.join(images_root_path, '*.jpeg')) + \
                 glob.glob(os.path.join(images_root_path, '*.JPG'))

        for test_image in images:
            oriImg = cv2.imread(test_image)  # B,G,R order
            candidate, subset = self.body_estimation(oriImg)
            canvas = copy.deepcopy(oriImg)
            canvas = util.draw_bodypose(canvas, candidate, subset)
            # detect hand
            hands_list = util.handDetect(candidate, subset, oriImg)

            all_hand_peaks = []
            for x, y, w, is_left in hands_list:
                models = self.hand_estimation(oriImg[y:y + w, x:x + w, :])
                models[:, 0] = np.where(models[:, 0] == 0, models[:, 0], models[:, 0] + x)
                models[:, 1] = np.where(models[:, 1] == 0, models[:, 1], models[:, 1] + y)
                all_hand_peaks.append(models)

            canvas = util.draw_handpose(canvas, all_hand_peaks)

            cv2.imwrite(results_root_path + '/' + test_image.split('/')[-1], canvas[:, :, [2, 1, 0]])
