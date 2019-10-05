import cv2
from umano.manosola.utils import rescale_frame

CAMERA_INDEX = 1


def main():
    capture = cv2.VideoCapture(CAMERA_INDEX)

    while capture.isOpened():
        pressed_key = cv2.waitKey(1)
        _, frame = capture.read()

        cv2.imshow("Live Feed", rescale_frame(frame))

        if pressed_key == 27:
            break

    cv2.destroyAllWindows()
    capture.release()


if __name__ == '__main__':
    main()
