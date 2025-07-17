from ultralytics import YOLO

class ReconheceObjeto: # Detecta o objeto
    def __init__(self, model_path: str):
        # Carrega o modelo YOLO (ex: "yolov8n.pt")
        self.model = YOLO(model_path)
    
    def detect(self, frame): # Retorna os resultados da detecção no frame

        return self.model(frame)