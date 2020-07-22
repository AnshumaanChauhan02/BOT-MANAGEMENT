import csv
import json
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
ip=[]
visit=[]
views=[]
b=0
h=0
bl="ip"
key_bl=""
bl_li=dict()
with open('ibm_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            ip.append(row[9])
            visit.append(row[11])
            views.append(row[13])
            line_count += 1
    for x in range(1048573) :
        if int(views[x])>10:
            b=b+1
            key_bl=bl+str(x)
            bl_li.update({key_bl:ip[x]})
            key_bl=""
        else:
            h=h+1
@app.route('/', methods=['GET'])
def home():
    flag=0
    ip_address=flask.request.remote_addr
    for ipc in ip :
        if ipc==ip_address:
            flag=1
            return '''<h1>BOT</h1>
            <p>Check further whether it is a bad or a good bot</p>'''
        else:
            pass
    if flag==0 :
        return '''<h1>HUMAN USER</h1>
        <p>Allow user the requested resorces</p>'''
    else:
        pass
app.run()
