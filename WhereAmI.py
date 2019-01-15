import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos= mc.player.getTilePos()
print(pos.x)
print(pos.y)
print(pos.z)

mc.postToChat(pos.x)
mc.postToChat(pos.y)
mc.postToChat(pos.z)
