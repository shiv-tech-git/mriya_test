import rospy
from std_msgs.msg import String
from flask import Flask, request

PORT = "8080"

app = Flask(__name__)
pub = rospy.Publisher('received_data', String, queue_size=10)
rospy.init_node('talker', anonymous=True, disable_signals = True)

@app.route('/api/log', methods = ['POST'])
def hello_world():
    if request.content_type != "application/json":
        return ("Invalid content type", 404)
    if request.json == "":
        return ("Empty body", 404)
    if "data" not in request.json:
        return ("Invalid json", 404)
    
    data = request.json["data"]
    rospy.loginfo(data)
    pub.publish(data)
    return ('', 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)

