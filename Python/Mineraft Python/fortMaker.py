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

#Initial info
chosen = brickBlock
pos = mc.player.getPos()
x = int(pos.x)
y = int(pos.y)
z = int(pos.z)
if (x < 0):
    x = x-1
if (z < 0):
    z = z-1
heights = []

#Heights
for a in range(x-7, x+8):
    for c in range(z-7, z+8):
        height = mc.getHeight(a, c)
        heights.append(height)

#Foundation
lowest = min(heights)
highest = max(heights)+1
if ((y-1) > highest):
    highest = y
floor = lowest-3
for b in range(floor, highest):
    for a in range(x-7, x+8):
        for c in range(z-7, z+8):
            mc.setBlock(a, b, c, chosen)
            if (b > y):
                mc.player.setPos(x+0.5, b, z+0.5)
                y = b

#Walls and ceiling
mc.setBlocks(x-7, y, z+7, x+7, y+3, z+7, chosen)
mc.setBlocks(x-7, y, z-7, x-7, y+3, z+7, chosen)
mc.setBlocks(x-7, y, z-7, x+7, y+3, z-7, chosen)
mc.setBlocks(x+7, y, z-7, x+7, y+3, z+7, chosen)
mc.setBlocks(x-7, y+3, z-7, x+7, y+3, z+7, chosen)
mc.setBlocks(x-6, y, z-6, x+6, y+2, z+6, air)
mc.setBlock(x, y+3, z, glass)
mc.setBlock(x-5, y+3, z-5, glass)
mc.setBlock(x-5, y+3, z+5, glass)
mc.setBlock(x+5, y+3, z-5, glass)
mc.setBlock(x+5, y+3, z+5, glass)

#Doors
mc.setBlock(x+7, y+1, z, air)
mc.setBlock(x-7, y+1, z, air)
mc.setBlock(x, y+1, z+7, air)
mc.setBlock(x, y+1, z-7, air)
mc.setBlock(x+7, y, z, ironDoor, 2)
mc.setBlock(x-7, y, z, ironDoor, 0)
mc.setBlock(x, y, z+7, ironDoor, 3)
mc.setBlock(x, y, z-7, ironDoor, 1)