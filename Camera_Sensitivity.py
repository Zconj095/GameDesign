class GameCamera:
    def __init__(self, sensitivity=1.0):
        self.sensitivity = sensitivity
        self.position = [0, 0, 0]  # X, Y, Z coordinates

    def adjust_sensitivity(self, new_sensitivity):
        self.sensitivity = new_sensitivity

    def move_camera(self, input_vector):
        """
        Moves the camera based on input vector adjusted by the camera's sensitivity.

        :param input_vector: A tuple or list representing input direction (x, y, z)
        """
        movement = [i * self.sensitivity for i in input_vector]
        self.position = [self.position[i] + movement[i] for i in range(3)]
        print(f"Camera moved to {self.position}")

# Example Usage
camera = GameCamera(sensitivity=1.5)
camera.move_camera([1, 0, 0])  # Move camera along the X-axis