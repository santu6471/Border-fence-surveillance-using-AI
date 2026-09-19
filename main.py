
from modules.detection import Detector
from modules.tracking import Tracker
from modules.analyzer import Analyzer
from modules.alert_service import AlertService
from utils.config import CONFIG

def main():
    det = Detector()
    tracker = Tracker() 
    analyzer = Analyzer()
    alert_svc = AlertService()

    for frame_id, frame, detections in det.stream_frames(imgsz=1280):
        tracked = tracker.update_tracks(frame_id, detections, frame)
        
        alerts = analyzer.check(tracked)
        for a in alerts:
            alert_svc.handle_alert(a, frame)

if __name__ == "__main__":
    main()
