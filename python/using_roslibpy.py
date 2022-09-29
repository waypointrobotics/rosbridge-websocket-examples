"""
In this example, we use roslibpy to request the execution of a 
program created in Dispatcher (the robot's GUI) and saved with
under the name 'helloworld'.

Modify this exaple to request the execution of your own programs.

"""

import roslibpy

client = roslibpy.Ros(host='10.66.171.2', port=9090)
client.run()

print('Is ROS connected?', client.is_connected)

service = roslibpy.Service(client, 'mission_control/run_mission_from_file', 'waypoint_ui/SingleWaypointOp')
request = roslibpy.ServiceRequest({'request': 'helloworld'})

print('Calling service...')
result = service.call(request)
print('Service response: '+ str(result))

client.terminate()

