import asyncio
import traceback

from utilities import download_file, print_emotions
from hume import HumeStreamClient, StreamSocket
from hume.models.config import FaceConfig
import cv2
import os
from dotenv import load_dotenv # for loading api keys


filepath = download_file("https://storage.googleapis.com/hume-test-data/image/obama.png")
async def main():
    try:
        load_dotenv()
        client = HumeStreamClient(os.environ.get("HUMEAI_API_KEY"))
        config = FaceConfig(identify_faces=True)
        async with client.connect([config]) as socket:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                print("Cannot open camera")
                return
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                result = await socket.send_frame(frame)
                print(result)
                if cv2.waitKey(1) == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            #result = await socket.send_file(filepath)
            #print(result)
    except Exception:
        print(traceback.format_exc())

asyncio.run(main())
