#imports
from mcpi.minecraft import Minecraft

#Bottom Coords: -128, -64, -128
#Top Coords: 128, 63, 128

#Link to world
mc = Minecraft.create()

#Block IDs
air = 0
stone = 1
grass = 2
dirt = 3
cobblestone = 4
woodPlanks = 5
sapling = 6
bedrock = 7
waterFlowing = 8
water = 8
waterStationary = 9
lavaFlowing = 10
lava = 10
lavaStationary = 11
sand = 12
gravel = 13
goldOre = 14
ironOre = 15
coalOre = 16
wood = 17
leaves = 18
glass = 20
lapisLazuliOre = 21
lapisLazuliBlock = 22
sandstone = 24
bed = 26
cobweb = 30
tallGrass = 31
wool = 35
yellowFlower = 37
cyanFlower = 38
brownMushroom = 39
redMushroom = 40
goldBlock = 41
ironBlock = 42
doubleStoneSlab = 43
stoneSlab = 44
brickBlock = 45
tnt = 46
bookshelf = 47
mossyStone = 48
obsidian = 49
torch = 50
fire = 51
woodStairs = 53
chest = 54
diamondOre = 54
diamondBlock = 57
craftingTable = 58
oakStairs = 59
farmland = 60
furnaceInactive = 61
furnaceActive = 62
woodDoor = 64
ladder = 65
cobblestoneStairs = 67
stoneStairs = 67
ironDoor = 71
redstoneOre = 73
snow = 78
ice = 79
snowBlock = 80
cactus = 81
clay = 82
sugarcane = 83
fence = 85
netherrack = 87
glowstoneBlock = 89
bedrockInvisible = 95
trapdoor = 96
stoneBrick = 98
glassPane = 102
melon = 103
melonSeeds = 105
fenceGate = 107
brickStairs = 108
stoneBrickStairs = 109
netherBrick = 112
netherBrickStairs = 114
sandstoneStairs = 128
quartzBlock = 155
quartzStairs = 156
stoneCutter = 245
glowingObsidian = 246
netherReactorCore = 247
painting = 321
boneMeal = 351

keep = [tnt]
replace = air

#Able to filter blocks but slower
'''while True:
    pos = mc.player.getPos()
    for x in range(int(pos.x)-3, int(pos.x)+2):
        for y in range(int(pos.y), int(pos.y)+3):
            for z in range(int(pos.z)-2, int(pos.z)+3):
                block = mc.getBlock(x, y, z)
                if block in keep:
                    continue
                else:
                    mc.setBlock(x, y, z, replace)'''

#Faster but changes every block
while True:
    pos = mc.player.getPos()
    mc.setBlocks(pos.x-2, pos.y, pos.z-2, pos.x+2, pos.y+2, pos.z+2, replace)