import mcpi.block as block
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
height = 50
size = 50
offset_x = size / 2
for y in range(height):
    for x in range(size):
        for z in range(size):
            mc.setBlock(pos.x + (size / 2 - x) + offset_x, pos.y + y, pos.z + (size / 2 - z), block.SAND.id)
    size = size - 2
