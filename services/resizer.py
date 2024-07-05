import trimesh
from json import loads

def resize_model(input_file_path, output_file_path, new_sizes):
    """
    Resize a 3D model and print its original dimensions in centimeters.

    Parameters:
    - input_file_path: Path to the input model file.
    - output_file_path: Path where the resized model will be saved.
    - scale_factor: A scalar or a tuple of three values to scale the model. 
                    Use a scalar for uniform scaling or (scale_x, scale_y, scale_z) for non-uniform scaling.
    """
    # Load the model
    mesh = trimesh.load(input_file_path)

    # Calculate and print the size of the model in centimeters
    size_x, size_y, size_z = mesh.bounds[1] - mesh.bounds[0]  # Size in model's units (often meters)
    size_x_cm, size_y_cm, size_z_cm = int(size_x * 100), int(size_y * 100), int(size_z * 100) # Convert to centimeters
    new_scale = 1
    new_sizes = loads(new_sizes)
    if new_sizes.get("x", 0) not in [0, '', None]:
        new_scale = int(new_sizes["x"]) / size_x_cm
    elif new_sizes.get("y", 0) not in [0, '', None]:
        new_scale = int(new_sizes["y"]) / size_y_cm
    elif new_sizes.get("z", 0) not in [0, '', None]:
        new_scale = int(new_sizes["z"]) / size_z_cm

    # Scale the model
    mesh.apply_scale(new_scale)

    # Save the resized model
    mesh.export(output_file_path)