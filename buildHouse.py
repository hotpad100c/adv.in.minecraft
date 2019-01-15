import mcpi.block as block
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
SIZE = 40
pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z
midx = x + SIZE/2
midy = y + SIZE/2
mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE, block.TNT.id)
mc.setBlocks(x+1, y, z+1, x+SIZE-1, y+SIZE-1, z+SIZE-1, block.LAVA.id)
mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)
mc.setBlocks(x+3, y+SIZE-3, z, midx-3, midy+3, z, block.TNT.id)
mc.setBlocks(midx+3, y+SIZE-3, z, x+SIZE-3, midy+3, z, block.TNT.id)
mc.setBlocks(x, y+SIZE, z, x+SIZE, y+SIZE, z+SIZE, block.TNT.id)
mc.setBlocks(x+1, y-1, z+1, x+SIZE-1, y-1, z+SIZE-1, block.TNT.id, 100)