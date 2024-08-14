from flask import Flask, render_template, send_file, make_response
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect/<ip>')
def connect(ip):
    rdp_content = f"""
screen mode id:i:2
use multimon:i:0
desktopwidth:i:1920
desktopheight:i:1080
session bpp:i:32
winposstr:s:0,3,0,0,800,600
compression:i:1
keyboardhook:i:2
audiocapturemode:i:0
videoplaybackmode:i:1
connection type:i:2
networkautodetect:i:1
bandwidthautodetect:i:1
displayconnectionbar:i:1
enableworkspacereconnect:i:0
disable wallpaper:i:0
allow font smoothing:i:0
allow desktop composition:i:0
disable full window drag:i:1
disable menu anims:i:1
disable themes:i:0
disable cursor setting:i:0
bitmapcachepersistenable:i:1
full address:s:{ip}
audiomode:i:0
redirectprinters:i:1
redirectcomports:i:0
redirectsmartcards:i:1
redirectclipboard:i:1
redirectposdevices:i:0
autoreconnection enabled:i:1
authentication level:i:2
prompt for credentials:i:0
negotiate security layer:i:1
remoteapplicationmode:i:0
alternate shell:s:
shell working directory:s:
gatewayhostname:s:
gatewayusagemethod:i:4
gatewaycredentialssource:i:4
gatewayprofileusagemethod:i:0
promptcredentialonce:i:1
use redirection server name:i:0
rdgiskdcproxy:i:0
kdcproxyname:s:
"""

    # Create the RDP file in-memory
    rdp_file = io.BytesIO()
    rdp_file.write(rdp_content.encode('utf-8'))
    rdp_file.seek(0)

    # Send the file as an attachment
    response = make_response(rdp_file.read())
    response.headers['Content-Disposition'] = f'attachment; filename=connect_{ip}.rdp'
    response.mimetype = 'application/x-rdp'

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
