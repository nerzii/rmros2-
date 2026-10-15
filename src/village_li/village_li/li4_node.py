#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String  #导入消息类型，只能说这个消息类型是最常用的，其他的消息类型可以在ros2的官方文档中查找
class WriterNode(Node):
    """
    创建一个作家节点，并在初始化时输出一个话
    """
    def __init__(self,name):
        super().__init__(name)  #继承父类super().__init__()，并传入节点名称
        self.get_logger().info("大家好，我是%s,我是一名作家！" % name)#打印日志，除了info还有debug、warn、error、fatal等方法
        self.pub_novel=self.create_publisher(String,"sexy_girl",10)
        self.account = 0
        self.time_period = 5
        self.timer = self.create_timer(self.time_period,self.timer_callback)  #设置一个定时器，每隔5秒调用一次timer_callback函数 create_timer(时间间隔，回调函数)
    #其实上面这段放在c++里面就是编写构造函数
    def timer_callback(self):   #定义一个回调函数
        self.account += 1  #注意点就是这里account是会累加的，而不是每次从0开始（虽然像废话，但我当时的确廷困惑的）
        self.get_logger().info("我写了第%d本小说" % self.account)
        msg = String()
        msg.data = "第%d本小说" % self.account  #此步直接决定了发布的消息内容
        self.pub_novel.publish(msg)  #发布消息
def main(args=None):
    rclpy.init(args=args) # 初始化rclpy
    node = WriterNode("li4")  # 新建一个节点
    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.tryshutdown() # 关闭rclpy
    """
    ros2运行该节点的入口函数
    1. 导入库文件
    2. 初始化客户端库
    3. 新建节点
    4. spin循环节点
    5. 关闭客户端库
    这一段基本上是固定的，除了新建节点的名称可以自定义，其他的都不需要修改（个人见解）
    """
