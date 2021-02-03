from datetime import datetime

from src.fps import FPS


class TestFPS:
    @classmethod
    def setup_class(cls):
        cls.fps = FPS()

    @classmethod
    def teardown_class(cls):
        del cls.fps

    def test_start(self):
        self.fps.start()

        assert isinstance(self.fps.start_time, datetime)

    def test_stop(self):
        self.fps.stop()

        assert isinstance(self.fps.end_time, datetime)

    def test_update(self):
        self.fps.update()

        assert self.fps.total_frames == 1

    def test_elapsed(self):
        elapsed = self.fps.elapsed()

        assert elapsed > 0

    def test_fps(self):
        fps = self.fps.fps()

        assert isinstance(fps, float)
