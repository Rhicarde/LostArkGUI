import PySimpleGUI as sg

# List of my Lost Ark Roster
classes = ['assets/artist.png', 'assets/gunlancer.png', 'assets/gunslinger.png', 'assets/paladin.png', 'assets/reaper.png']

f = open('data.txt', 'w+')
a = f.read()
print(a)

a, b = 0, 1
# Layout used to design selection
layout = [[sg.Button(image_filename='assets/arrows/arrow_left.png', border_width=0,
                       image_size=(50, 50), key='<'),
             sg.Image(classes[a], enable_events=True, background_color='#000000', key='-IMG1-'),
             sg.Image(classes[b], enable_events=True, background_color='#000000', key='-IMG2-'),
             sg.Button(image_filename='assets/arrows/arrow_right.png', border_width=0,
                       image_size=(50, 50), key='>')]]

# for image in classes:
#     first_row.append(sg.Image(image, background_color='#000000', visible=False))


window = sg.Window('', layout, background_color='#000000', button_color='#000000')


while True:
   event, values = window.read()
   print(event, values)
   if event == sg.WIN_CLOSED or event == 'Exit':
      break

   if event == '>':
       print('right')
       a = (a + 2) % len(classes)
       b = (b + 2) % len(classes)

       f.write("%d %d" % (a, b))

       window['-IMG1-'].update(classes[a])
       window['-IMG2-'].update(classes[b])

   elif event == '<':
       print('left')
       a = (a - 2) % len(classes)
       b = (b - 2) % len(classes)

       f.write("%d %d" % (a, b))

       window['-IMG1-'].update(classes[a])
       window['-IMG2-'].update(classes[b])

f.close()
window.close()
