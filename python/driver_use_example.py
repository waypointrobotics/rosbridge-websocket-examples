from robot_driver import MyRosbridgeClient
import time

try:
    my_websocket_client = MyRosbridgeClient('ws://127.0.0.1:9090/')  # Change this IP address and port as needed
    my_websocket_client.connect()


    # This is an example script, uncomment relevant lines to try different functions

    """ Sending the robot to a waypoint:"""
    my_websocket_client.subscribe_to_navigation_result()
    my_websocket_client.go_to_named_waypoint('Start')
    while not my_websocket_client.navigation_finished:
        time.sleep(0.1)
    print("Navigation Succeeded: "+str(my_websocket_client.navigation_succeeded))
    
    """ Starting a mission/program"""
    #my_websocket_client.start_mission('my_mission')
    

    """ Current approximate robot position can be queried directly like this: """
    #print(my_websocket_client.robot_position_x)
    #print(my_websocket_client.robot_position_y)
    
    """ Use this method to stop any running playlist/mission/program """
    #my_websocket_client.stop_mission()    

    """ Use this method to get the x-y coordinates of a saved waypoint """
    #my_websocket_client.get_waypoint_coordinates('Start')
    
    """ If you want this script to run forever, uncomment this """
    #my_websocket_client.run_forever()
    # or
    #time.sleep(25)

    """ The robot's battery level is available on the battery_level attribute. """
    print(my_websocket_client.battery_level)

    """ The mission_is_running attribute keeps track of mission starts and finishes (this is just a rudimentary example, do not use for production) """
    #timeout = 0
    #while my_websocket_client.mission_is_running and timeout < 15:
    #    time.sleep(1)
    #    timeout = timeout + 1

except KeyboardInterrupt:
    my_websocket_client.close()
