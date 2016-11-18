import cv2


class MultipleObjectsTracker:
    def __init__(self, min_area=400, min_shift2=5):
        self.object_roi = []
        self.object_box = []

        self.min_cnt_area = min_area
        self.min_shift2 = min_shift2

        # set termination criteria
        self.term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 100, 1)