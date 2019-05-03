from flask import Flask ,render_template, jsonify
import RPi.GPIO as GPIO
import time 
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=["POST", "GET"])
def hello_world():
	return jsonify(getState())


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