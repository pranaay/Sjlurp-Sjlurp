# HackIT: Navigation Monitor

### How to run?
1. Install the dependencies listed below.
2. Connect the Ultrasonic sensor to the RPi, where the pins:
    * Trig pin on 25
    * Echo pin on 5
3. Run app.py `python app.py`
4. Download the introductory video, and place it in the project directory with the name: `vid.mp4`
5. Visit `localhost` or `127.0.0.1` to see the homepage.

### What happens next?
* When you visit website, you can see the introductory video playing. As soon as you get closer to the ultrasonic sensor, it sends a signal which stops the video and shows the map.
* On the map, one can navigate by selecting the name on the right side window.
* One can also navigate by clicking the room number on the interactive map.
