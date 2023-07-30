import yolov7_package as yolo
class Detector(yolo.Yolov7Detector):
    def __init__(self, weights=None, img_size=None, conf_thres=0.25, iou_thres=0.45, augment=False, agnostic_nms=False, device='cuda:0', traced=False, classes='coco'):
        super().__init__(weights, img_size, conf_thres, iou_thres, augment, agnostic_nms, device, traced, classes)
    def detect_image_and_return(self,img):
        classes,boxes,confidence = self.detect(img)
        img = self.draw_on_image(img=img,boxes=boxes[0],scores=confidence[0],class_ids=classes[0])
        return img





