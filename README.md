Run dashboard.py & go to IP adress given to access dashboard

##Dependencies:
- numpy
- dash
- dash-bootstrap-components
- pandas
- plotly
- requests
- tinytuya
- websocket-client
- scipy

Create directory & virtual enviornment & install
```
mkdir mir_dash && cd mir_dash
sudo apt install python3.8-venv #install virtual enviornments
python3 -m venv venv
source venv/bin/activate
pip install numpy dash dash-bootstrap-components pandas plotly requests tinytuya websocket-client scipy shapely
```


# Installation:
1. Go to directory `cd mir_dash`
2. Clone repository `git clone https://github.com/leahtyndall/MIR100.git`

3. Run websocket to get ros driver data (signal level)
**NOTE**
- In 'defs.py' replace rosIP with your ROS2 PC IP.
  

- Run dashboard.py & go to IP address given to access dashboard



##Summary of files:
- assets - images, cvs data files, txt logic files ect
- APIs - Connect to Mir/shelly to handle requests
- defs.py - Defines missions from mir
- mirStatus.py - retrieves status info from mir
- missions.py - contains docking/undocking sequences & other buttons on dash
- network.py - to be updated...void?
- networkMap.py - records robot position and signal strength data to be plotted
- rosDiagnostics.py - recieves signal level from mir ros driver
- shellyGateControl.py - runs gate control
- shellyStatsdorMir.py - gets status of gate (combine^?)
- layout2.py - plotly dash layout of dashboard
- dashboard.py - handles all call backs, creates map plot
