<h5><strong>IMPORTANT</strong> Working directory is \u-mano\umano\tools\camera_stream</h5>

<pre>
(umano) ~u-mano\umano\tools\camera_stream>python app.py -h
usage: app.py [-h] [-p PORT] [-t TITLE] [-c CAMERA] [--processor PROCESSOR]

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  port to listen to (default 5000)
  -t TITLE, --title TITLE
                        default title for web page (default Camera)
  -c CAMERA, --camera CAMERA
                        local camera index to stream from (default 0) or
                        camera stream url
  --processor PROCESSOR
                        image processing to apply to frame ['BaseProcessing',
                        'BackgroundSubtraction']
</pre>

For a running example with laptop webcam open two terminal.

<pre>

# terminal 1
(umano) ~\u-mano\umano\tools\camera_stream>python app.py

# terminal 2
 (umano) ~\u-mano\umano\tools\camera_stream>python app.py -p 5001 --camera="http://localhost:5000/video_feed" --processor="BackgroundSubtraction"

</pre>

Then open two browser window at http://localhost:5000 and http://localhost:5001 to have som fun :)