from flask import Flask ,render_template
import RPi.GPIO as GPIO
import time 
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("index.html",state = getState())


def getState():
	GPIO.setmode(GPIO.BOARD)

	trig = 26

	echo =5
	GPIO.setup(trig,GPIO.OUT)
	GPIO.output(trig,0)

	GPIO.setup(echo,GPIO.IN)

	time.sleep(0.1)


	GPIO.output(trig,1)
	time.sleep(0.00001)
	GPIO.output(trig,0)
	while GPIO.input(echo) == 0:
		pass
	start = time.time()
	while GPIO.input(echo) == 1:
		pass
	stop = time.time()
	if (stop - start)*17000 < 35:
		
		print("true")
		return "true"
	else:
		print("false")
		return "false"
	GPIO.cleanup()

if __name__ == '__main__':
      app.run(debug=True,host='0.0.0.0')