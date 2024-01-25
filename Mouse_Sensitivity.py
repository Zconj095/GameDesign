class GameCamera:
    def __init__(self, mouse_sensitivity=1.0):
        self.mouse_sensitivity = mouse_sensitivity
        self.camera_angle = [0, 0]  # Horizontal and Vertical angles

    def adjust_mouse_sensitivity(self, new_sensitivity):
        self.mouse_sensitivity = new_sensitivity

    def rotate_camera(self, mouse_movement):
        """
        Rotate the camera based on mouse movement adjusted by mouse sensitivity.

        :param mouse_movement: A tuple (dx, dy) representing mouse movement
        """
        dx, dy = mouse_movement
        self.camera_angle[0] += dx * self.mouse_sensitivity
        self.camera_angle[1] += dy * self.mouse_sensitivity
        print(f"Camera angle is now {self.camera_angle}")

# Example Usage
camera = GameCamera(mouse_sensitivity=0.5)
camera.rotate_camera((20, 10))  # Simulating mouse movement