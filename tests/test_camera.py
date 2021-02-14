from src.camera import Camera


def test_camera():
    camera = Camera()

    assert camera.frame_grabbed
