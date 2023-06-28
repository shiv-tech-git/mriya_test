FROM ros:noetic

SHELL [ "/bin/bash" , "-c" ]

RUN apt-get update && apt-get install python3-pip -y
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN source /opt/ros/noetic/setup.bash \
    && mkdir -p /catkin_ws/src \
    && cd /catkin_ws/src \
    && catkin_init_workspace 

COPY http_endpoint /catkin_ws/src/http_endpoint
COPY logger /catkin_ws/src/logger
COPY startup /catkin_ws/src/startup
COPY start.sh /catkin_ws/

RUN source /opt/ros/noetic/setup.bash \
 && cd catkin_ws \
 && catkin_make

RUN mkdir catkin_ws/log

WORKDIR /catkin_ws
RUN mkdir -p /catkin_ws/log

EXPOSE 8080

CMD ["/bin/bash", "start.sh"]
