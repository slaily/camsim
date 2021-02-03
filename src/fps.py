import datetime


class FPS:
    def __init__(self):
        # Store the start time, end time, and total number of frames
        # that were examined between the start and end intervals
        self._start_time = None
        self._end_time = None
        self._total_frames = 0

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def total_frames(self):
        return self._total_frames

    def start(self):
        # Start the timer
        self._start_time = datetime.datetime.now()

        return self

    def stop(self):
        # Stop the timer
        self._end_time = datetime.datetime.now()

    def update(self):
        # Increment the total number of frames examined during the
        # start and end intervals
        self._total_frames += 1

    def elapsed(self):
        # Return the total number of seconds between the start and
        # end interval
        return (self._end_time - self._start_time).total_seconds()

    def fps(self):
        # Compute the approximate frames per second
        return self._total_frames / self.elapsed()
