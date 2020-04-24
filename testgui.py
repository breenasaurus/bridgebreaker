
from guizero import App, Text, TextBox, PushButton, info, Window

# Creates the GUI
app = App(title="Start Screen")

# Creates the text instruction
instruction = Text(app, text="Please type in Team ID number,\n and then press Start", size=28, font="Times New Roman")

# Creates TShe text box to enter the ID number
IDbox = TextBox(app, width=5)

# Sets team ID to 0 before ID number placed
teamID = 00000

# Sets initial weight to 0, time to 1 second and command to fetch weight
weight = 0
time = 1000
def fetchweight():

# Creates the start button
def start_button():
  IDbox = int(teamID)
  info("Testing", "Testing the Bridge")
  actual_test = Window(app, title = "Emergency Stop")
  text = Text(actual_test, text="In case of emergency please press the emergency stop.")
  weightdisplay = (actual_test, text = weight,repeat(time,command = fetchweight, args=None)
  emergency = PushButton(actual_test,command = actual_test.hide, text="EMERGENCY STOP!")
  
update_ID = PushButton(app, command = start_button, text="Start bridge test!")


    app.display()
