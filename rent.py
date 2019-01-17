#coding=utf-8
import mcpi.minecraft as minecraft
import time
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
x1 = pos.x
z1 = pos.z
x2 = x1 - 20
z2 = z1 - 20
blockid = 124
blockid2 = 152
mc.setBlock(x1, pos.y, z1, blockid)
mc.setBlock(x2, pos.y, z2, blockid)
mc.setBlock(x2, pos.y, z1, blockid)
mc.setBlock(x1, pos.y, z2, blockid)
mc.setBlock(x1, pos.y+1,z1, blockid2)
mc.setBlock(x2, pos.y+1,z2, blockid2)
mc.setBlock(x2, pos.y+1,z1, blockid2)
mc.setBlock(x1, pos.y+1,z2, blockid2)
rent = 0
inField = 0
HOME_x = x2 - 2
HOME_y = 300
HOME_z = z2 - 2
while True :
    time.sleep(1)
    pos = mc.player.getTilePos()
    mc.postToChat(pos.x)
    mc.postToChat(pos.y)
    mc.postToChat(pos.z)
    mc.postToChat("--------++++++++++++----------")
    if x2<pos.x and pos.x<x1 and z2<pos.z and pos.z<z1:
        rent = rent + 1
        mc.postToChat("you owe rent:" + str(rent))
        inField = inField+1
        if inField > 4:
            mc.postToChat("too slow!")
            while pos.y < HOME_y:
                pos.y = pos.y + 1
                mc.player.setPos(pos.x, pos.y, pos.z)
                pos = mc.player.getTilePos()
            mc.player.setPos(HOME_x, pos.y, HOME_z)
    else: # 不在区域内
        inField = 0
