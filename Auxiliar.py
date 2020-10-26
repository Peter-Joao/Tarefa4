import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32

rospy.init_node('Auxiliar')
resp = String()

def subCallBack(msg):
    global resp
    resp = msg

def timerCallBack(event):
    msg = String()
    msg.data = '2016018028'
    pub.publish(msg)
    
    print('resultado: '+resp.data)
    

sub = rospy.Subscriber('/auxiliar/resposta', String, subCallBack)
pub = rospy.Publisher('exercicio/matricula', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(1), timerCallBack)

rospy.spin()