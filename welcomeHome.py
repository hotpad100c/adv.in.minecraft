#coding=utf-8
import mcpi.minecraft as minecraft
import time
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos1 = mc.player.getTilePos()
mc.setBlock(pos1.x, pos1.y, pos1.z, block.TNT.id)
while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if abs(pos.x - pos1.x) < 5 and abs(pos.z - pos1.z) < 5:
        mc.postToChat(pos.x)
        mc.postToChat(pos.z)
        mc.postToChat("啊！屁瓜！！！")