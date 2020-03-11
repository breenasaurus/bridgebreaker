
from guizero import App, Text, TextBox, PushButton

# Creates the GUI
app = App(title="Start Screen")

# Creates the text instruction
instruction = Text(app, text="Please type in Team ID number and then press Start", size=28, font="Times New Roman")

# Creates TShe text box to enter the ID number
IDbox = TextBox(app, width=5)

# Creates the start button
def start_button():
  IDbox.value = teamID.value
  update_ID = PushButton(app, command = start_button, text="Start bridge test!")

# Need to find a library that creates the touchscreen 
# Make the start button bigger
def begintest():
    app.display()