 
import rospy
from std_msgs.msg import String

rospy.init_node('exercicio')
matricula = String()

def subCallBack(msg):
    global matricula
    matricula = msg

def timerCallBack(event):
    soma = 0
    for i in range(len(matricula.data)):
        soma=soma+int(matricula.data[i])
    print('Soma dos numeros: ('+matricula.data + ')')
    
    soma_msg = String()
    soma_msg.data = str(soma)
    pub.publish(soma_msg)

sub = rospy.Subscriber('/exercicio/matricula', String, subCallBack)
pub = rospy.Publisher('auxiliar/resposta', String, queue_size=1)

timer = rospy.Timer(rospy.Duration(1), timerCallBack)

rospy.spin()