import PySimpleGUI as sg

# List of my Lost Ark Roster
classes = ['assets/artist.png', 'assets/gunlancer.png', 'assets/gunslinger.png', 'assets/paladin.png', 'assets/reaper.png']

a, b = 0, 1

with open('data.txt', 'r') as f:
    a, b = [int(x) for x in next(f).split()]

# Layout used to design selection
layout_main = [[sg.Button(image_filename='assets/arrows/arrow_left.png', border_width=0,
                       image_size=(50, 50), key='<'),
             sg.Image(classes[a], enable_events=True, background_color='#000000', key='-IMG1-'),
             sg.Image(classes[b], enable_events=True, background_color='#000000', key='-IMG2-'),
             sg.Button(image_filename='assets/arrows/arrow_right.png', border_width=0,
                       image_size=(50, 50), key='>')]]

window = sg.Window('', layout_main, background_color='#000000', button_color='#000000', grab_anywhere=True, location=(100, 100), no_titlebar=True)


while True:
   event, values = window.read()

   f = open('data.txt', 'w')
   f.write("%d %d" % (a, b))
   f.close()

   if event == sg.WIN_CLOSED or event == 'Exit':
      break

   if event == '>':
       #print('right')
       a = (a + 2) % len(classes)
       b = (b + 2) % len(classes)

       #print("%d %d" % (a, b))
       f = open('data.txt', 'w')
       f.write("%d %d" % (a, b))
       f.close()

       window['-IMG1-'].update(classes[a])
       window['-IMG2-'].update(classes[b])

   elif event == '<':
       #print('left')
       a = (a - 2) % len(classes)
       b = (b - 2) % len(classes)

       f = open('data.txt', 'w')
       f.write("%d %d" % (a, b))
       f.close()

       window['-IMG1-'].update(classes[a])
       window['-IMG2-'].update(classes[b])

f.close()
window.close()
