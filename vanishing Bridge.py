import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
bridge = []
def  buildBridge():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    if b == block.STONE.id or b == block.TNT.id or b == block.AIR.id or b == block.LAVA_STATIONARY.id or b == block.LAVA_STATIONARY.id or b == block.WATER_STATIONARY.id or b == block.WATER_FLOWING.id:
        mc.setBlock(pos.x, pos.y-1, pos.z, block.SAPLING.id)
        coordinate = [pos.x, pos.y-1, pos.z]
        bridge.append(coordinate)
        mc.postToChat("not safe++++++++++++++" + str(len(bridge)))
    else:
        mc.postToChat("safe ----------------" + str(len(bridge)))
        if b != block.SAPLING.id:
            while len(bridge) > 0:
                coordinate = bridge.pop()
                mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
                mc.postToChat("safe ----------------" + str(len(bridge)))
                time.sleep(0.15)

while True:
    time.sleep(0.05)
    buildBridge()