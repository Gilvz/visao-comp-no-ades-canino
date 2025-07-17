from detector import ReconheceObjeto
from video_stream import Camera
from monitor import MonitoramentoSofa
import cv2

def main():
    detector = ReconheceObjeto("[yolov8n.pt](http://yolov8n.pt/)")  # modelo base YOLOv8
    video = Camera(0)

    # sofá manualmente: parte inferior da tela
    sofa_region = (400, 300, 640, 480)

    monitor = MonitoramentoSofa(detector, sofa_region)

    while True:
        frame = video.read()
        if frame is None:
            break

        processed_frame = monitor.process_frame(frame)
        video.show("Dog Near Sofa Monitor", processed_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.close()

if __name__ == "main":
    main()