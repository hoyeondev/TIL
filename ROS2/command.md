

### .bashrc

```bash
# sublime text로 .bashrc 열기
subl ~/.bashrc

# .bashrc에서 alias 설정
echo "ROS2 humble is activated!"
source /opt/ros/humble/setup.bash

alias humble="source /opt/ros/humble/setup.bash; echo \"ROS2 Humble is activated!!!!\""
alias sb="source ~/.bashrc; echo \"bashrc is reload\""
alias ros_domain="export ROS_DOMAIN_ID=<ID>"
```
