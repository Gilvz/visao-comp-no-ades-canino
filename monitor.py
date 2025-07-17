import cv2

class MonitoramentoSofa:
    def __init__(self, detector, sofa_region):
            self.detector = detector
            self.sofa_region = sofa_region  # (x1,y1,x2,y2)

    def is_near_sofa(self, dog_box):
        dx1, dy1, dx2, dy2 = dog_box
        sx1, sy1, sx2, sy2 = self.sofa_region
    
        overlap_x1 = max(dx1, sx1)
        overlap_y1 = max(dy1, sy1)
        overlap_x2 = min(dx2, sx2)
        overlap_y2 = min(dy2, sy2)
    
        overlap_area = max(0, overlap_x2 - overlap_x1) * max(0, overlap_y2 - overlap_y1)
        dog_area = (dx2 - dx1) * (dy2 - dy1)
        if dog_area == 0:
            return False
        overlap_ratio = overlap_area / dog_area
        return overlap_ratio > 0.2

    def process_frame(self, frame):
        results = self.detector.detect(frame)
    
        # área do sofá (azul)
        sx1, sy1, sx2, sy2 = self.sofa_region
        cv2.rectangle(frame, (sx1, sy1), (sx2, sy2), (255,0,0), 2)
        cv2.putText(frame, "sofa area", (sx1, sy1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

        for box in results.xyxy[0]:
            x1, y1, x2, y2, conf, cls = box
            cls_name = self.detector.model.names[int(cls)]
    
            if cls_name != "dog":
                continue
    
            dog_box = (int(x1), int(y1), int(x2), int(y2))
            is_close = self.is_near_sofa(dog_box)
    
            color = (0,0,255) if is_close else (0,255,0)
    
            cv2.rectangle(frame, (dog_box[0], dog_box[1]), (dog_box[2], dog_box[3]), color, 2)
            cv2.putText(frame, f"dog {conf:.2f}", (dog_box[0], dog_box[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            return frame