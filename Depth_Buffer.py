def apply_depth_based_blur(scene, depth_buffer, focus_depth, blur_strength):
    """
    Apply blur to a scene based on depth information.

    :param scene: The 3D scene or image
    :param depth_buffer: Depth information for each pixel
    :param focus_depth: The depth at which objects are in focus
    :param blur_strength: The strength of the blur effect
    :return: Scene with depth-based blur applied
    """
    blurred_scene = scene.copy()
    for x in range(scene.width):
        for y in range(scene.height):
            pixel_depth = depth_buffer.get_depth(x, y)
            if abs(pixel_depth - focus_depth) > threshold:
                blurred_scene.apply_blur(x, y, blur_strength)

    return blurred_scene


