import mcpi.block as block
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
size = int(raw_input("size of area to clear?"))
mc.setBlocks(pos.x - size/2, pos.y, pos.z - size/2, pos.x + size/2, pos.y + size, pos.z + size/2, block.AIR.id)