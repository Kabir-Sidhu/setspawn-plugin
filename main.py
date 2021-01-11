import os, json
from mcapi import *
from org.bukkit.event.player import PlayerRespawnEvent	
import org.bukkit.ChatColor

if not os.path.exists('spawnPluginThingyStuffs'):
    os.mkdir('spawnPluginThingyStuffs')
if not os.path.exists('spawnPluginThingyStuffs/stuffs.json'):
    open('spawnPluginThingyStuffs/stuffs.json','a').write(r"{}").close()

try:
    e = json.loads(open('spawnPluginThingyStuffs/stuffs.json').read())
except FileNotFoundError:
    open('spawnPluginThingyStuffs/stuffs.json','a').write(r"{}").close()
    e = json.loads(open('spawnPluginThingyStuffs/stuffs.json').read())
except Exception as exception:
    print(f'There was an unhandeled exception: {exception}')# check dc already smh

@asynchronous()
def spawncmd(caller, params):# so why don't we put player instead of params xd
    player = caller.getPlayer()
    playerid = player.getUniqueId()# nvm that xD
    try:# xDD check discord this cmd is working 
        player.teleport(e[playerid]['coords'].world,e[playerid]['coords'].x,e[playerid]['coords'].y,e[playerid]['coords'].z)
        yell("I have set your spawn to %s" % location(player))
    except KeyError:
        yell("&l&cYou dont have a spawn set. Please try again but first run the /setspawn command.")
# try again? okok 
# xd
# uwu# u need to import color from bukkit xd
@asynchronous()
def spawnset(caller, params):
    plr = caller.getPlayer()
    playerid = plr.getUniqueId()
    e[playerid] = {'coords':location(plr)}

add_command("spawn",spawncmd)
add_command("setspawn",spawnset)