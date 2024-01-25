import random
import numpy as np

def is_occluded(point, scene_objects):
    """
    Determine if a point is occluded by other objects in the scene.

    :param point: The point to check
    :param scene_objects: A list of objects in the scene
    :return: Boolean indicating if the point is occluded
    """
    for obj in scene_objects:
        if obj.blocks_light_to(point):
            return True
    return False

def calculate_ambient_occlusion(scene_objects, num_samples=100):
    """
    Calculate ambient occlusion for each point in the scene.

    :param scene_objects: A list of objects in the scene
    :param num_samples: Number of samples to take for occlusion calculation
    :return: A numpy array representing the occlusion values
    """
    occlusion_map = np.zeros((len(scene_objects), len(scene_objects)))

    for i, point in enumerate(scene_objects):
        occluded_count = sum(is_occluded(point, scene_objects) for _ in range(num_samples))
        occlusion_map[i] = occluded_count / num_samples

    return occlusion_map