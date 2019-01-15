import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
def  buildBridge():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    if b == block.AIR.id or b == block.LAVA_STATIONARY.id or b == block.LAVA_STATIONARY.id or b == block.WATER_STATIONARY.id or b == block.LAVA_FLOWING.id:
        mc.setBlock(pos.x, pos.y-1, pos.z, block.TNT.id)
        mc.postToChat("not safe++++++++++++++")
    else:
        mc.postToChat("safe ----------------")

while True:
    buildBridge()