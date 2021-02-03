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
