from mcpi import minecraft

mc = minecraft.Minecraft.create()

mc.postToChat("Connected to Python")

position = mc.player.getPos()

mc.postToChat("Teleporting UP!")

mc.player.setPos(x, y+100, z)