import os
from gps import *
from time import *
from time import sleep
import threading
from ISStreamer.Streamer import Streamer
from geopy.distance import vincenty
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
import plotly.graph_objs as go
from time import sleep
stream_ids = tls.get_credentials_file()['stream_ids']
print (stream_ids)

#streamer = Streamer(bucket_name="Jazz2.0", bucket_key="874c7a07-fac5-4311-af6b-3e996f091950", access_key="THlgdECGquJlQK1v5EX5BZc5ZVJK5vMD")# bucket_key="bucket_key",
destination = 33.534228, -102.002558

gpsd = None #seting the global variable

os.system('clear') #clear the terminal (optional)

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer










def scatter1(type, text, id, max):
    trace1 = Scatter(
        x=[],
        y=[],
        mode=type,
        name=text,
        stream=Stream(
            token=stream_ids[id],
            maxpoints=max
        )
    )

def data(scatter):
    data = Data(sactter)

def layout(tit):
    layout = Layout(title = tit)

def figure(data, layout):
    fig = Figure(data=data, layout=layout)

def unique(figure, name):
    unique_url = py.plot(figure, filename='name')


scatter1 = scatter1(line, GPS, 0, 20)
data = data(scatter1)
layout = layout(GPS-Speed)


figure = figure(data, layout)
unique_url = unique(figure, GPS-Line)
s1 = py.Stream(stream_ids[0])
s1.open()








if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:

      #It may take a second or two to get good data
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc

      os.system('clear')

      print (gpsd.fix.time)
      print (gpsd.fix.latitude, gpsd.fix.longitude)
      lalo = gpsd.fix.latitude, gpsd.fix.longitude
      now = gpsd.fix.time
      speed = gpsd.fix.speed
      print(vincenty(destination, lalo).feet)
      print (speed)
      x = speed
      y = now

      s1.write(dict(x=x, y=y))
      #streamer.log('Time', time)
      #streamer.log('Data', lalo)

      sleep(0.1)
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print ("\nKilling Thread...")
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print ("Done.\nExiting.")
  s1.close()
