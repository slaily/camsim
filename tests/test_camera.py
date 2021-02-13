from src.camera import Camera


def test_camera():
    camera = Camera()

    assert camera.grabbed
