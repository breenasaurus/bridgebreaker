# GUI for senior design 
# Logic for GUI
# Input ID number> once the proper character
# numbers then light up the start button>
# Have emergncy stop light up >
# Once complete will auto stop and return to 
# the main screen.

from guizero import App, Text, TextBox, PushButton

# Creates the GUI
app = App(title="Start Screen")

# Creates the text instruction
instruction = Text(app, text="Please type in Team ID number and then press Start", size=40, font="Times New Roman")

# Creates TShe text box to enter the ID number
IDbox = TextBox(app, width=5)

# Need to find a library that creates the touchscreen 
# Make the start button bigger
def begintest():


app.display()


