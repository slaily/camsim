from time import sleep

from .frames import generate_color_frame


class Camera:
    def __init__(self):
        self.frame_grabbed, self.frame = self.generate_frame()
        self.stopped = False

    def generate_frame(self):
        sleep(0.1)

        try:
            frame = generate_color_frame(256, 256)

            return True, frame
        except Exception as exc:
            print(str(exc))

            return False, None

    def read(self):
        while not self.stopped:
            if not self.frame_grabbed:
                self.stop()
                break

            self.frame_grabbed, self.frame = self.generate_frame()

        return None

    def stop(self):
        self.stopped = True

        return None
