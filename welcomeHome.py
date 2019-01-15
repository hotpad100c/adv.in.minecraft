#coding=utf-8
import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
while True :
    time.sleep(1)
    pos = mc.player.getTilePos()
    if abs(pos.x - -185) < 5 and abs(pos.z - 232) < 5:
        mc.postToChat(pos.x)
        mc.postToChat(pos.z)
        mc.postToChat("啊！屁瓜！！！")