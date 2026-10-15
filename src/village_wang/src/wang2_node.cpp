#include"rclcpp/rclcpp.hpp"
#include"std_msgs/msg/string.hpp"
#include <memory>
class SingleNode : public rclcpp::Node{  //这里其实就是继承父类，并且这里public是为作提醒的，把SingleNode当作Node使
    private:
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr cater;  //声明一个成员变量，必须要这么做，不然下面的订阅部分（Line14)会因为作用域而无效
    void topic_callback(const std_msgs::msg::String::SharedPtr msg)   //回调函数,要接受一条这种类型的消息，话题强调订阅者接受消息类型和发布者发出的相同
    {
        RCLCPP_INFO(this->get_logger(), "朕已阅：'%s'", msg->data.c_str());
    };
    public:
    SingleNode(std::string name):Node(name){
        RCLCPP_INFO(this->get_logger(),"大家好,我是wang2");  //不多说，指针基础，其实好像能用另一种类似python的写法写的（？）
        cater = this->create_subscription<std_msgs::msg::String>(
         "sexy_girl", 
         10,
        [this](const std_msgs::msg::String::SharedPtr msg) {
        this->topic_callback(msg);                 //lambda写法，std::bind用的不多了
    });
}
};
int main(int argc, char** argv){
    rclcpp::init(argc,argv);
    rclcpp::spin(std::make_shared<SingleNode>("wang2"));
    rclcpp::shutdown();
}
