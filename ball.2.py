import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
pos = mc.player.getTilePos()
x = pos.x
y = pos.y - 20
z = pos.z
while 1>0:
  mcdrawing.drawSphere(x, y, z, 15, block.GLASS.id, 10)
  time.sleep(1)
  mcdrawing.drawSphere(x, y, z, 15, block.BEDROCK_INVISIBLE.id, 5)
  time.sleep(1)