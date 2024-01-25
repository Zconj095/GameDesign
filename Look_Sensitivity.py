class PlayerCamera:
    def __init__(self, look_sensitivity=1.0):
        self.look_sensitivity = look_sensitivity
        self.camera_angle = [0, 0]  # Horizontal and Vertical angles

    def adjust_look_sensitivity(self, new_sensitivity):
        self.look_sensitivity = new_sensitivity

    def update_camera_angle(self, input_change):
        """
        Update the camera angle based on input change and look sensitivity.

        :param input_change: A tuple (dx, dy) representing change in input (mouse/controller)
        """
        dx, dy = input_change
        self.camera_angle[0] += dx * self.look_sensitivity
        self.camera_angle[1] += dy * self.look_sensitivity
        print(f"Updated camera angle: {self.camera_angle}")

# Example Usage
player_camera = PlayerCamera(look_sensitivity=2.0)
player_camera.update_camera_angle((0.5, 0.2))  # Simulating input change