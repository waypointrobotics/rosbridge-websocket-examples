const WebSocket = require('ws');   // sudo npm i ws
const ws = new WebSocket('ws://127.0.0.1:9090'); // replace IP and port if necessary

ws.on('open', function open() {
    console.log('New connection');
    let request_coordinates_msg ={"op":"call_service","service":"/waypoint_db/retrieve_waypoint","args":{"waypointName": "A"}};
    ws.send(JSON.stringify(request_coordinates_msg));
});

ws.on('message', function(msg){
    console.log(msg);
    waypoint_coordinates  = JSON.parse(msg);
    x_coordinate = waypoint_coordinates.values.pose.position.x;
    y_coordinate = waypoint_coordinates.values.pose.position.y;
    z_coordinate = waypoint_coordinates.values.pose.orientation.z;
    w_coordinate = waypoint_coordinates.values.pose.orientation.w;
    let pose_message =  {"op": "publish",
                        "topic": "/move_base_navi_simple/goal",
                        "msg":{ "header": {"frame_id": "map"},
                            "pose": {"position": {"x": x_coordinate, "y": y_coordinate}, "orientation": {"z": z_coordinate, "w": w_coordinate}}}
                        }; 
    ws.send(JSON.stringify(pose_message));
});

ws.on('close', function() {
    console.log('closing connection');
    ws.close();
});
