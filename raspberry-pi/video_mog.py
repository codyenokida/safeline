from firebase import firebase
from picamera import PiCamera
from picamera.array import PiRGBArray
from sendgrid.helpers.mail import Email, Content, Mail, Attachment
from threading import Thread
import base64
import cv2
import cv2.bgsegm
import imutils
import imutils.object_detection
import numpy as np
import os
import sendgrid
import time

# Overview: This algorithm for fall detection is very rudimentary. At each frame
# of the video stream, it simply finds the largest moving shape and draws a
# rectangle around it. If that rectangle has large enough area, the algorithm
# checks if the rectangle is wider than it is large, by some scale. If this is
# true, the algorithm adds 1 to a count called "fallen". If fallen crosses a
# certain threshold, a fall is registered, and the script sends an email and
# updates the database. After this, it sets a "sent" variable to the SEND_DELAY
# value. Once this sent variable has reached 0, the script is allowed to detect
# falling again (this delay prevents the script from repeatedly detecting the
# same fall).

# delay between checks in milliseconds
DELAY = 20

# how many frames does the person have to be fallen to consider a fall?
FALL_THRESHOLD = 10

# how much wider than longer does someone have to be to be "falling"?
SCALE = 1.1

# how big does the box have to be in order to be considered a person?
AREA_THRESHOLD = 1500

# how many intervals to wait before we can send the msg
# again? - currently this comes out to 1 min - 1000 * DELAY
SEND_DELAY = 200

# Firebase
firebaseclient = firebase.FirebaseApplication(
    'https://safelineuci.firebaseio.com/', None)


def send_to_firebase(encoded):
    t = time.asctime()
    result = firebaseclient.post('/data', {"Time": t, "Img": encoded})
    print(result)


# Sendgrid
sgclient = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("btjanaka@uci.edu")
subject = "ALERT! A LOVED ONE HAS FALLEN!"
content = Content("text/plain",
                  "PLEASE TAKE ACTION IMMEDIATELY BY CALLING 911!")
to_emails = [Email("bryon.tjanaka@gmail.com")]


def encode_image(img):
    cv2.imwrite("./.tmp-img.jpeg", img)
    with open("./.tmp-img.jpeg", "rb") as f:
        return base64.b64encode(f.read()).decode()


def send_emails_via_sendgrid(encoded_img: "base 64 string"):
    attachment = Attachment()
    attachment.content = encoded_img
    attachment.type = "image/jpeg"
    attachment.filename = "fallen.jpeg"
    attachment.disposition = "inline"
    attachment.content_id = "fallen-picture"

    for to_email in to_emails:
        email_data = Mail(from_email, subject, to_email, content)
        email_data.add_attachment(attachment)
        response = sgclient.client.mail.send.post(request_body=email_data.get())
        print("email status: {}".format(response.status_code))


def send_datas(img):
    encoded = encode_image(img)
    send_to_firebase(encoded)
    send_emails_via_sendgrid(encoded)


# Multi-threaded video stream
class VideoStream:

    def __init__(self, resolution=(640, 480), framerate=32):
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.camera.rotation = 270
        self.rawCapture = PiRGBArray(self.camera, size=resolution)
        self.stream = self.camera.capture_continuous(
            self.rawCapture, format="bgr", use_video_port=True)

        self.frame = None
        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        for f in self.stream:
            self.frame = f
            self.rawCapture.truncate(0)

            if self.stopped:
                self.stream.close()
                self.rawCapture.close()
                self.camera.close()
                return

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True


def main():
    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
    fallen = 0
    sent = 0

    video = VideoStream()
    video.start()
    time.sleep(1)  # warmup time for camera

    try:
        while True:
            frame = video.read()
            img = frame.array
            fgmask = fgbg.apply(img)
            _, contours, _ = cv2.findContours(fgmask.copy(), cv2.RETR_TREE,
                                              cv2.CHAIN_APPROX_SIMPLE)

            if len(contours) != 0:
                # Find max contour
                mxi = max((i for i in range(len(contours))),
                          key=lambda i: cv2.contourArea(contours[i]))

                x, y, w, h = cv2.boundingRect(contours[mxi])

                # Detect fallen
                if w > SCALE * h and cv2.contourArea(
                        contours[mxi]) >= AREA_THRESHOLD:
                    fallen = min(FALL_THRESHOLD * 2, fallen + 1)
                else:
                    fallen = max(0, fallen - 1)

                # Draw shapes
                text = str(fallen)
                color = (0, 255, 0)  # green
                if fallen > FALL_THRESHOLD:
                    text += " - WARNING"
                    color = (0, 0, 255)  # red

                cv2.putText(img, text, (x, y - 3), cv2.FONT_HERSHEY_PLAIN, 2.0,
                            color)
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)

                # Send msgs
                if fallen > FALL_THRESHOLD:
                    # Only send the msg again after at most SEND_DELAY intervals
                    if sent == 0:
                        sent = SEND_DELAY
                        # Do the sending in another thread to avoid freezing
                        Thread(target=send_datas, args=(img,)).start()

            sent = max(sent - 1, 0)

            # Display images
            cv2.imshow('binary', fgmask)
            cv2.imshow('original', img)

            # Check for quitting
            if cv2.waitKey(DELAY) & 0xFF == ord('q'):
                break
    finally:
        video.stop()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
