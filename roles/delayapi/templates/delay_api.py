#coding:utf-8
import sys
try:
    from flask import Flask, jsonify
except:
    sys.exit("Please exec: pip install flask")

from flask import request as req
import subprocess

app = Flask(__name__)

@app.route('/delay', methods=['POST'])
def CheckDelay():
    ip = req.form.get("ip", None)
    if not ip:
        return jsonify({"success":False,"msg":""})
    try:
        map(int, ip.split("."))
    except:
        return jsonify({"success":False,"msg":""})

    rc, output = shell_exec(*['ping', '-c', '2', '-W', '2', ip])
    try:
        delay = output.strip().split('\n')[-1].split('/')[-3]
        delay = float(delay)
    except Exception, e:
        return jsonify({"success":False,"msg":""})
    return jsonify({"success":True,"msg":delay})


def shell_exec(*cmd):
    cmd = map(str, cmd)
    PIPE = subprocess.PIPE
    obj = subprocess.Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE, close_fds=True)
    output = obj.communicate()
    print output[0]
    obj.stdin.close()
    return obj.returncode, output[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=999)
