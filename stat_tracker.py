# AC App Template by Hunter Vaners
# ------------------------------
#
# Don't forget to rename assettocorsa\apps\python\Template_Assetto_Corsa_App
#           by assettocorsa\apps\python\[Your_App_Name_Without_Spaces]
#  and
# the file Template_Assetto_Corsa_App.py
#           by Your_App_Name_Without_Spaces.py
#
# ------------------------------

import os
import ac
import acsys
from third_party.sim_info import *
import json


appName = "THP Stat Tracker"
width, height = 800 , 800 # width and height of the app's window

simInfo = SimInfo()

# directory_path = "/SteamLibrary/steamapps/common/assettocorsa/stat_logs"
# file_path = "/SteamLibrary/steamapps/common/assettocorsa/stat_logs/stats.json"

class Player:
    car_id = 0
    name = ""
    current_speed = 0
    top_speed = 0
    current_lap = "00:00:000"
    best_lap = "00:00:000"

    def __init__(self, car_id, name):
        self.car_id = car_id
        self.name = name
        self.current_speed = 0
        self.top_speed = 0
        self.current_lap = "00:00:000"
        self.best_lap = "00:00:000"


# def create_json_file_path_if_not_exist():
#     # check if the directory exists, and create it if it doesn't
#     if not os.path.exists(directory_path):
#         os.makedirs(directory_path)

#     # check if the file exists, and create it if it doesn't
#     if not os.path.exists(file_path):
#         with open(file_path, 'w'):
#             pass


# def write_to_stats_file():
#     with open(file_path, 'w') as json_file:
#         json.dump(server_info, json_file)


def acMain(ac_version):#----------------------------- App window Init

    # Don't forget to put anything you'll need to update later as a global variables
    global appWindow # <- you'll need to update your window in other functions.
    global l_player_name1, l_current_speed1, l_top_speed1, l_current_lap1, l_best_lap1
    global l_player_name2, l_current_speed2, l_top_speed2, l_current_lap2, l_best_lap2
    global l_player_name3, l_current_speed3, l_top_speed3, l_current_lap3, l_best_lap3
    global l_player_name4, l_current_speed4, l_top_speed4, l_current_lap4, l_best_lap4
    global l_player_name5, l_current_speed5, l_top_speed5, l_current_lap5, l_best_lap5
    global connected_players, car_count

    connected_players = []
    car_count = ac.getCarsCount()

    # instantiate a new app
    appWindow = ac.newApp(appName)
    ac.setTitle(appWindow, appName)
    ac.setSize(appWindow, width, height)
    ac.drawBorder(appWindow,0)

    # set title label for new app
    league = "THP Race League"
    message = "Welcome to the THP Race League Stat Tracker"
    finalMessage = league + " : " + message
    lastMessageLabel = ac.addLabel(appWindow,finalMessage)
    ac.setPosition(lastMessageLabel,150,30)


    ac.addRenderCallback(appWindow, appGL) # -> links this app's window to an OpenGL render function


    ### ====================== Player 1 ====================== ###
    # label for player name
    l_player_name1 = ac.addLabel(appWindow, "Name: [player not connected]")
    ac.setPosition(l_player_name1, 3, 60)

    # label for player's current speed
    l_current_speed1 = ac.addLabel(appWindow, "Current Speed: 0 mph")
    ac.setPosition(l_current_speed1, 3, 80)

    # label for player's top speed
    l_top_speed1 = ac.addLabel(appWindow, "Top Speed: 0 mph")
    ac.setPosition(l_top_speed1, 3, 100)

    # label for player's current lap time
    l_current_lap1 = ac.addLabel(appWindow, "Current Lap Time: 00:00:00")
    ac.setPosition(l_current_lap1, 3, 120)

    # label for player's best lap time
    l_best_lap1 = ac.addLabel(appWindow, "Best Lap Time: 00:00:00")
    ac.setPosition(l_best_lap1, 3, 140)
    ### ====================== Player 1 ====================== ###


    ### ====================== Player 2 ====================== ###
    # label for player name
    l_player_name2 = ac.addLabel(appWindow, "Name: [player not connected]")
    ac.setPosition(l_player_name2, 3, 200)

    # label for player's current speed
    l_current_speed2 = ac.addLabel(appWindow, "Current Speed: 0 mph")
    ac.setPosition(l_current_speed2, 3, 220)

    # label for player's top speed
    l_top_speed2 = ac.addLabel(appWindow, "Top Speed: 0 mph")
    ac.setPosition(l_top_speed2, 3, 240)

    # label for player's current lap time
    l_current_lap2 = ac.addLabel(appWindow, "Current Lap Time: 00:00:00")
    ac.setPosition(l_current_lap2, 3, 260)

    # label for player's best lap time
    l_best_lap2 = ac.addLabel(appWindow, "Best Lap Time: 00:00:00")
    ac.setPosition(l_best_lap2, 3, 280)
    ### ====================== Player 2 ====================== ###


    ### ====================== Player 3 ====================== ###
    # label for player name
    l_player_name3 = ac.addLabel(appWindow, "Name: [player not connected]")
    ac.setPosition(l_player_name3, 3, 340)

    # label for player's current speed
    l_current_speed3 = ac.addLabel(appWindow, "Current Speed: 0 mph")
    ac.setPosition(l_current_speed3, 3, 360)

    # label for player's top speed
    l_top_speed3 = ac.addLabel(appWindow, "Top Speed: 0 mph")
    ac.setPosition(l_top_speed3, 3, 380)

    # label for player's current lap time
    l_current_lap3 = ac.addLabel(appWindow, "Current Lap Time: 00:00:00")
    ac.setPosition(l_current_lap3, 3, 400)

    # label for player's best lap time
    l_best_lap3 = ac.addLabel(appWindow, "Best Lap Time: 00:00:00")
    ac.setPosition(l_best_lap3, 3, 420)
    ### ====================== Player 3 ====================== ###


    ### ====================== Player 4 ====================== ###
    # label for player name
    l_player_name4 = ac.addLabel(appWindow, "Name: [player not connected]")
    ac.setPosition(l_player_name4, 3, 480)

    # label for player's current speed
    l_current_speed4 = ac.addLabel(appWindow, "Current Speed: 0 mph")
    ac.setPosition(l_current_speed4, 3, 500)

    # label for player's top speed
    l_top_speed4 = ac.addLabel(appWindow, "Top Speed: 0 mph")
    ac.setPosition(l_top_speed4, 3, 520)

    # label for player's current lap time
    l_current_lap4 = ac.addLabel(appWindow, "Current Lap Time: 00:00:00")
    ac.setPosition(l_current_lap4, 3, 540)

    # label for player's best lap time
    l_best_lap4 = ac.addLabel(appWindow, "Best Lap Time: 00:00:00")
    ac.setPosition(l_best_lap4, 3, 560)
    ### ====================== Player 4 ====================== ###


    ### ====================== Player 5 ====================== ###
    # label for player name
    l_player_name5 = ac.addLabel(appWindow, "Name: [player not connected]")
    ac.setPosition(l_player_name5, 3, 620)

    # label for player's current speed
    l_current_speed5 = ac.addLabel(appWindow, "Current Speed: 0 mph")
    ac.setPosition(l_current_speed5, 3, 640)

    # label for player's top speed
    l_top_speed5 = ac.addLabel(appWindow, "Top Speed: 0 mph")
    ac.setPosition(l_top_speed5, 3, 660)

    # label for player's current lap time
    l_current_lap5 = ac.addLabel(appWindow, "Current Lap Time: 00:00:00")
    ac.setPosition(l_current_lap5, 3, 680)

    # label for player's best lap time
    l_best_lap5 = ac.addLabel(appWindow, "Best Lap Time: 00:00:00")
    ac.setPosition(l_best_lap5, 3, 700)
    ### ====================== Player 5 ====================== ###




    return appName





def appGL(deltaT):#-------------------------------- OpenGL UPDATE
    """
    This is where you redraw your openGL graphics
    if you need to use them .
    """
    pass # -> Delete this line if you do something here !




def acUpdate(deltaT):#-------------------------------- AC UPDATE
    global l_player_name1, l_current_speed1, l_top_speed1, l_current_lap1, l_best_lap1, player_name1, current_speed1, top_speed1, current_lap1, best_lap1  
    global l_player_name2, l_current_speed2, l_top_speed2, l_current_lap2, l_best_lap2, player_name2, current_speed2, top_speed2, current_lap2, best_lap2
    global l_player_name3, l_current_speed3, l_top_speed3, l_current_lap3, l_best_lap3, player_name3, current_speed3, top_speed3, current_lap3, best_lap3
    global l_player_name4, l_current_speed4, l_top_speed4, l_current_lap4, l_best_lap4, player_name4, current_speed4, top_speed4, current_lap4, best_lap4
    global l_player_name5, l_current_speed5, l_top_speed5, l_current_lap5, l_best_lap5, player_name5, current_speed5, top_speed5, current_lap5, best_lap5
    global connected_players, car_count

    update_name_string = "[player not connected]"
    update_lap_time_string = "00:00:00"

    player_name1 = update_name_string
    current_speed1 = top_speed1 = 0
    current_lap1 = best_lap1 = 0
    player_name2 = update_name_string
    current_speed2 = top_speed2 = 0
    current_lap2 = best_lap2 = 0
    player_name3 = update_name_string
    current_speed3 = top_speed3 = 0
    current_lap3 = best_lap3 = 0
    player_name4 = update_name_string
    current_speed4 = top_speed4 = 0
    current_lap4 = best_lap4 = 0
    player_name5 = update_name_string
    current_speed5 = top_speed5 = 0
    current_lap5 = best_lap5 = 0

    def update_player_ui(l_player_name, l_current_speed, l_top_speed, l_current_lap, l_best_lap, player_name, current_speed, top_speed, current_lap, best_lap, player_id):
        # update player_name
        player_name = ac.getDriverName(player_id)
        ac.setText(l_player_name, "Name: {}".format(player_name))

        # update current_speed
        current_speed = round(ac.getCarState(player_id, acsys.CS.SpeedMPH), 2)
        ac.setText(l_current_speed, "Current Speed: {:02} mph".format(current_speed))

        # update top_speed
        top_speed = connected_players[player_id].top_speed
        if current_speed > top_speed:
            connected_players[player_id].top_speed = current_speed
            top_speed = current_speed
            ac.setText(l_top_speed, "Top Speed: {:02} mph".format(top_speed))

        # update current lap time
        current_lap = ac.getCarState(player_id, acsys.CS.LapTime)
        current_lap = format_lap_time(current_lap)
        ac.setText(l_current_lap, "Current Lap Time: {}".format(current_lap))

        # update best lap time
        best_lap = ac.getCarState(player_id, acsys.CS.BestLap)
        best_lap = format_lap_time(best_lap)
        ac.setText(l_best_lap, "Best Lap Time: {}".format(best_lap))

    def format_lap_time(lap_time):
        seconds, milliseconds = divmod(lap_time, 1000)
        minutes, seconds = divmod(seconds, 60)

        # Format the result as "mm:ss:ms"
        time_format = "{:02d}:{:02d}:{:03d}".format(minutes, seconds, milliseconds)
        return time_format
    
    # get list of connected players
    def get_connected_players(connected_players):
        for i in range(0,car_count):
            if ac.isConnected(i):
                if "Traffic" in ac.getDriverName(i):
                    break
                if len(connected_players) == 0:
                    player_name = ac.getDriverName(i)
                    ac.console(player_name)
                    connected_player = Player(i, player_name)
                    connected_players.append(connected_player)
                else:
                    for obj in connected_players:
                        ## look here for changes to be made to stop infinite loop
                        ac.console(str(len(connected_players)))
                        ac.console("just inside for loop: " + str(obj.car_id))
                        if obj.car_id == i:
                            ac.console("player already exists")
                            break
                        else:
                            player_name = ac.getDriverName(i)
                            ac.console(player_name)
                            connected_player = Player(i, player_name)
                            connected_players.append(connected_player)
            elif not ac.isConnected(i):
                for obj in connected_players:
                    if obj.car_id == i:
                        disconnected_driver = ac.getDriverName(i)
                        ac.console(disconnected_driver + " disconnected from server")
                        connected_players.remove(obj)
                        ac.console(disconnected_driver + " was removed from the connected_players list")
                        


    get_connected_players(connected_players)

    ### update player stats based on number of players
    if len(connected_players) == 5:
        update_player_ui(l_player_name1, l_current_speed1, l_top_speed1, l_current_lap1, l_best_lap1, player_name1, current_speed1, top_speed1, current_lap1, best_lap1, connected_players[0].car_id)
        update_player_ui(l_player_name2, l_current_speed2, l_top_speed2, l_current_lap2, l_best_lap2, player_name2, current_speed2, top_speed2, current_lap2, best_lap2, connected_players[1].car_id)
        update_player_ui(l_player_name3, l_current_speed3, l_top_speed3, l_current_lap3, l_best_lap3, player_name3, current_speed3, top_speed3, current_lap3, best_lap3, connected_players[2].car_id)
        update_player_ui(l_player_name4, l_current_speed4, l_top_speed4, l_current_lap4, l_best_lap4, player_name4, current_speed4, top_speed4, current_lap4, best_lap4, connected_players[3].car_id)
        update_player_ui(l_player_name5, l_current_speed5, l_top_speed5, l_current_lap5, l_best_lap5, player_name5, current_speed5, top_speed5, current_lap5, best_lap5, connected_players[4].car_id)
    elif len(connected_players) == 4:
        update_player_ui(l_player_name1, l_current_speed1, l_top_speed1, l_current_lap1, l_best_lap1, player_name1, current_speed1, top_speed1, current_lap1, best_lap1, connected_players[0].car_id)
        update_player_ui(l_player_name2, l_current_speed2, l_top_speed2, l_current_lap2, l_best_lap2, player_name2, current_speed2, top_speed2, current_lap2, best_lap2, connected_players[1].car_id)
        update_player_ui(l_player_name3, l_current_speed3, l_top_speed3, l_current_lap3, l_best_lap3, player_name3, current_speed3, top_speed3, current_lap3, best_lap3, connected_players[2].car_id)
        update_player_ui(l_player_name4, l_current_speed4, l_top_speed4, l_current_lap4, l_best_lap4, player_name4, current_speed4, top_speed4, current_lap4, best_lap4, connected_players[3].car_id)
    elif len(connected_players) == 3:
        update_player_ui(l_player_name1, l_current_speed1, l_top_speed1, l_current_lap1, l_best_lap1, player_name1, current_speed1, top_speed1, current_lap1, best_lap1, connected_players[0].car_id)
        update_player_ui(l_player_name2, l_current_speed2, l_top_speed2, l_current_lap2, l_best_lap2, player_name2, current_speed2, top_speed2, current_lap2, best_lap2, connected_players[1].car_id)
        update_player_ui(l_player_name3, l_current_speed3, l_top_speed3, l_current_lap3, l_best_lap3, player_name3, current_speed3, top_speed3, current_lap3, best_lap3, connected_players[2].car_id)
    elif len(connected_players) == 2:
        update_player_ui(l_player_name1, l_current_speed1, l_top_speed1, l_current_lap1, l_best_lap1, player_name1, current_speed1, top_speed1, current_lap1, best_lap1, connected_players[0].car_id)
        update_player_ui(l_player_name2, l_current_speed2, l_top_speed2, l_current_lap2, l_best_lap2, player_name2, current_speed2, top_speed2, current_lap2, best_lap2, connected_players[1].car_id)
    elif len(connected_players) == 1:
        update_player_ui(l_player_name1, l_current_speed1, l_top_speed1, l_current_lap1, l_best_lap1, player_name1, current_speed1, top_speed1, current_lap1, best_lap1, connected_players[0].car_id)
