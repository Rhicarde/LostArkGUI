import PySimpleGUI as psg

# List of my Lost Ark Roster
classes = ['assets/artist.png', 'assets/gunlancer.png', 'assets/gunslinger.png', 'assets/paladin.png', 'assets/reaper.png']
a, b = 0, 1

layout = [
   [psg.Image(classes[a], enable_events=True, key='-TEXT-')],

   [psg.Slider(range=(0, 4), default_value=0,
   expand_x=True, enable_events=True,
   orientation='horizontal', key='-SL-')]
]
window = psg.Window('Hello', layout, size=(715, 150))
while True:
   event, values = window.read()
   print(event, values)
   if event == psg.WIN_CLOSED or event == 'Exit':
      break
   if event == '-SL-':
      window['-TEXT-'].update(classes[int(values['-SL-'])])
window.close()