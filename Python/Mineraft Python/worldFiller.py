from mcpi.minecraft import Minecraft

mc = Minecraft.create()

air = 0
bedrock = 7

mc.setBlocks(-128, -64, -128, 129, 63, 129, bedrock)