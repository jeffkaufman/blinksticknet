import time
import socket
from blinkstick import blinkstick

UDP_IP = "127.0.0.1"
UDP_PORT = 23512

def set_light(index, r, g, b, bstick=[None]):
  try:
    if not bstick[0]:
      bstick[0] = blinkstick.find_first();
      if not bstick[0]:
        print ("No blinkstick available")
    bstick[0].set_color(index=index, red=r, green=g, blue=b)
  except Exception:
    pass
  time.sleep(0.1)

def start():
  sock = socket.socket(socket.AF_INET, # Internet
                       socket.SOCK_DGRAM) # UDP
  sock.bind((UDP_IP, UDP_PORT))

  while True:
    data, addr = sock.recvfrom(1024)
    print("got %s bytes" % (len(data)))
    if len(data) != 4:
      continue

    index, r, g, b = data
    print("c=%s r=%s g=%s b=%s" % (index, r, g, b))
    if index > 7:
      continue # light out of range

    set_light(index, r, g, b)

if __name__ == "__main__":
  start()
