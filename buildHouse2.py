import mcpi.block as block
import mcpi.minecraft as minecraft
import random

mc = minecraft.Minecraft.create()
SIZE = 20
x = 0

def house():
    c = random.randint(1, 15)
    midx = x + SIZE/2
    midy = y + SIZE/2
    mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE, block.WOOL.id,c)
    mc.setBlocks(x+1, y, z+1, x+SIZE-1, y+SIZE-1, z+SIZE-1, block.FIRE.id,c)
    mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)
    mc.setBlocks(x+3, y+SIZE-3, z, midx-3, midy+3, z, block.WOOL.id,c)
    mc.setBlocks(midx+3, y+SIZE-3, z, x+SIZE-3, midy+3, z, block.GLASS.id)
    mc.setBlocks(x, y+SIZE, z, x+SIZE, y+SIZE, z+SIZE, block.WOOL.id)
    mc.setBlocks(x+1, y-1, z+1, x+SIZE-1, y-1, z+SIZE-1, block.WOOL.id,c)

pos = mc.player.getTilePos()
x = pos.x + 2
y = pos.y
z = pos.z

for a in range(10):
    house()
    z = z + SIZE
