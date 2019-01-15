import mcpi.block as block
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
size = 16
height = size + 1
offset_x = size / 2
for y in range(height):
    for x in range(abs(size)):
        for z in range(abs(size)):
            mc.setBlock(pos.x + (abs(size) / 2 - x) + offset_x, pos.y + y, pos.z + (abs(size) / 2 - z), block.WATER.id)
    size = size - 2
