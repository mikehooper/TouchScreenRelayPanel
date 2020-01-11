from guizero import App, PushButton, Slider, Text
import RPi.GPIO as GPIO

class button:
    def __init__(self,index,image,grid,gpio):
        self.index = index
        self.image = image
        self.grid = grid
        self.gpio = gpio

def general_callback(n):
    print('general_callback()',n)
    if GPIO.input(buttons[n].gpio) == 1:
        pushButtons[n].image = buttons[n].image+'_on.png'
        GPIO.output(buttons[n].gpio,GPIO.LOW)
    else:
        pushButtons[n].image = buttons[n].image+'_off.png'
        GPIO.output(buttons[n].gpio,GPIO.HIGH)
        
GPIO.setwarnings(False)        
GPIO.setmode(GPIO.BOARD)
path = '/home/pi/TouchScreenRelayPanel/'

buttons = []
# index,image,grid,gpio
buttons.append(button(0,'rear_lights' ,[0,0],40))
buttons.append(button(1,'front_lights',[1,0],38))
buttons.append(button(2,'water_pump'  ,[2,0],36))
buttons.append(button(3,'winch'       ,[0,1],37))
buttons.append(button(4,'AirSystem'   ,[1,1],35))
buttons.append(button(5,'AirSystem'   ,[2,1],33))
buttons.append(button(6,'AirSystem'   ,[0,3],32))
buttons.append(button(7,'AirSystem'   ,[1,3],31))

app = App(title="Keypad example", width=480, height=320, layout="grid")
app.bg='black'

pushButtons=[]
for button in buttons:
    GPIO.setup(button.gpio,GPIO.OUT)
    GPIO.output(button.gpio,GPIO.HIGH)
    pushButtons.append(PushButton(app, args=[button.index], command=general_callback, grid=button.grid, align='left', image = path + button.image+'_off.png'))

def main():
    #app.tk.attributes("-fullscreen",True)
    app.tk.config(cursor='none')
    app.display()

if __name__ == '__main__':
    main()
