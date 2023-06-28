sudo docker build -t ros_mriya .
sudo docker run -it -p 8080:8080 -v "$(pwd)":/catkin_ws/log/ ros_mriya