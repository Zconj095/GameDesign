import time

def display_text_at_speed(text, cps):
    """
    Display text at a specified characters per second (cps) rate.

    :param text: The text to display
    :param cps: Speed of text display in characters per second
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(1 / cps)
    print()  # Move to the next line after text is displayed

# Example Usage
text = "Welcome to the world of Python gaming!"
cps = 10  # Characters per second
display_text_at_speed(text, cps)