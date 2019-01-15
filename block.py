#coding=utf-8
import mcpi.minecraft as minecraft
import time
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
time.sleep(3)
c = 1000
while c > 0:
    mc.setBlock(pos.x+c, pos.y, pos.z, block.TNT.id)
    mc.setBlock(pos.x + c, pos.y, pos.z + 1, block.TNT.id)
    mc.setBlock(pos.x + c, pos.y, pos.z + 2, block.TNT.id)
    c = c - 1