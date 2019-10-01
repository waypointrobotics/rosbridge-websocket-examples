const WebSocket = require('ws');   // sudo npm i ws
const ws = new WebSocket('ws://127.0.0.1:9090');  // replace IP and port if necessary


ws.on('open', function open() {
    console.log('New connection');
    let pose_message = '{"op": "publish", "topic": "/move_base_navi_simple/goal","msg":{ "header": {"frame_id": "map"},"pose": {"position": {"x": 0, "y": 0}, "orientation": {"z": 0, "w": 1}}}}'; 
    ws.send(pose_message);
});

ws.on('message', function(msg){
    console.log(msg);
});

ws.on('close', function() {
    console.log('closing connection');
    ws.close();
});


