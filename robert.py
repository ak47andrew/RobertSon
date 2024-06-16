# Import necessary modules and functions
import modes
import speech_recognition as sr
from helper import record_sample, change_mode

# Initialize the recognizer
r = sr.Recognizer()
# Set initial mode and mode arguments
mode = "normal"
mode_args = ""

def main():
    # Declare global variables to be used across functions
    global mode, mode_args
    # Welcome message
    print("Добро пожаловать. Всё настроено и готово")
    # Main loop for continuous speech recognition
    while True:
        # Print recording message
        print("Recording...")
        try:
            # Record audio sample and convert it to text
            text = record_sample(r)
        except sr.UnknownValueError:
            # If no audio is provided, print an error message and continue the loop
            print("No audio provided")
            continue

        # Print the recognized text
        print(text)

        # Store the old mode for comparison later
        old_mode = mode
        # Change the mode based on the recognized text
        mode = change_mode(mode, text)

        # Check if the mode has changed
        if mode[0] == old_mode:
            # If the mode remains the same, set mode to the first element of the tuple
            mode = mode[0]
            # Call the corresponding mode function with the recognized text and mode arguments
            getattr(modes, mode)(text, mode_args)
        else:
            # If the mode has changed, update the mode arguments and set the new mode
            mode_args = mode[1]
            mode = mode[0]
            # Print the new mode
            print(f"Mode has been set to {mode}")

# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()
