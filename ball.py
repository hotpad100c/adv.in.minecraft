import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time
mcdrawing = minecraftstuff.MinecraftDrawing(mc)
pos = mc.player.getTilePos()

mcdrawing.drawSphere(pos.x, pos.y + -20, pos.z, 15, block.TNT.id, 5)
mcdrawing.drawSphere(pos.x, pos.y + -20, pos.z, 5, block.LAVA.id, 5)