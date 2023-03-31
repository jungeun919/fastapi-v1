# 23.03.29 16:00
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, StreamingResponse
import cv2
import json
import base64
import time
import uvicorn
import gzip

app = FastAPI()

@app.get("/webcam_stream")
async def webcam_feed():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    if not cap.isOpened():
        return Response(content=json.dumps({"message": "Unable to open webcam."}), media_type="application/json")

    def video_stream():
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            _, jpeg = cv2.imencode(".jpg", frame)
            frame_bytes = jpeg.tobytes()
            # frame_bytes = gzip.compress(frame_bytes)
            frame_str = base64.b64encode(frame_bytes).decode('ascii')
            data = {"frame": frame_str}

            yield json.dumps(data)
            time.sleep(5)

        cap.release()

    return StreamingResponse(video_stream(), media_type="application/json")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, access_log=False)
