from pyautogui import screenshot  # Uncomment this line in your local environment
from PIL import Image, ImageDraw, ImageFont

def take_screenshot():
    """
    Captures a screenshot of the current screen.
    Uncomment the return statement below when using pyautogui in your local environment.
    """
    # return screenshot()
    # For demonstration, returning a placeholder white image
    return Image.new("RGB", (800, 600), "white")

def draw_grid(image, grid_size):
    """
    Draws a grid on the given image.

    Args:
    image: PIL Image object
    grid_size: Size of the grid cells
    """
    draw = ImageDraw.Draw(image)
    width, height = image.size

    # Draw horizontal and vertical lines
    for x in range(0, width, grid_size):
        draw.line(((x, 0), (x, height)), fill=128)
    for y in range(0, height, grid_size):
        draw.line(((0, y), (width, y)), fill=128)

    del draw

def label_vertices(image, grid_size):
    """
    Labels the vertices of the grid on the image.

    Args:
    image: PIL Image object
    grid_size: Size of the grid cells
    """
    draw = ImageDraw.Draw(image)
    width, height = image.size
    font = ImageFont.load_default()

    # Label vertices
    for x in range(0, width, grid_size):
        for y in range(0, height, grid_size):
            label = f"({x},{y})"
            draw.text((x+5, y+5), label, fill="red", font=font)

    del draw

def create_screenshot_with_grid(grid_size):
    """
    Creates a screenshot with a grid and labeled vertices.

    Args:
    grid_size: Size of the grid cells
    """
    image = take_screenshot()
    draw_grid(image, grid_size)
    label_vertices(image, grid_size)
    return image
