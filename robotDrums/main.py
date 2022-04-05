import mido
import serial
import time


arduino = serial.Serial('COM36', 115200)
print("Настя самый совершенный робот")
#note = [35,37,38,41,44,45,47,48,49] #ноты midi устройства

note = [49,36,38,71,65,81] #ноты midi устройства

mid = mido.MidiFile('robotDrums/4.mid')
for msg in mid.play():
    a = msg.bytes()
    if msg.type == 'note_on':
        print(a[1])
        if a[1] == note[0]:
            arduino.write(b'5') #готово
            print('good1')
        if a[1] == note[1]:
            arduino.write(b'7') #готово
            print('good2')
        if a[1] == note[2]:
            arduino.write(b'4') #готово
            print('good3')
        if a[1] == note[3]:
            arduino.write(b'6') #готово
            print('good4')
        if a[1] == note[4]:
            arduino.write(b'3') #готово
            print('good5')
        if a[1] == note[5]:
            arduino.write(b'1') #готово
            print('good6')
        """
        if a[1] == note[6]:
            arduino.write(b'6')
            print('good7')
        if a[1] == note[7]:
            arduino.write(b'')
            print('good8')
        if a[1] == note[8]:
            arduino.write(b'')
            print('good9')"""
