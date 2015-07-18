import socket
import time

def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    ipaddr = s.getsockname()[0]
    s.close()
    return ipaddr

def write(filename, str):
    f = open(filename, 'w')
    f.write(str)
    f.close()

class LED:
    def __init__(self, num):
        self.name = '/sys/class/leds/led'+str(num)
        self.trigger = self.name + '/trigger'
        self.brightness = self.name + '/brightness'
        self.delay_on = self.name + '/delay_on'
        self.shot = self.name + '/shot'
    def on(self):
        write(self.trigger, 'none')
        write(self.brightness, '1')
    def off(self):
        write(self.trigger, 'none')
        write(self.brightness, '0')
    def heartbeat(self):
        write(self.trigger, 'heartbeat')
    def oneshot(self, second):
        write(self.trigger, 'oneshot')
        write(self.delay_on, str(second))
        write(self.shot, '1')

def num2led(num, led0, led1):
    led1.on()
    for var in range(0, num):
        led0.oneshot(200) #ms
        time.sleep(0.25)
        led0.off()
    led1.off()
    time.sleep(1)

if __name__ == '__main__':
    led0 = LED(0)
    led1 = LED(1)
    ipaddr = get_my_ip()
    ipaddr_last = ipaddr.split(".")[3]
    for num in list(ipaddr_last):
        num2led(int(num), led0, led1)
