from assets.spritesheet_registry import SPRITESHEET_REGISTRY


list = [
    "tinyShip1.png",
    "tinyShip2.png",
    "tinyShip3.png",
    "tinyShip4.png",
    "tinyShip5.png",
    "tinyShip6.png",
    "tinyShip7.png",
    "tinyShip8.png",
    "tinyShip9.png",
    "tinyShip10.png",
    "tinyShip11.png",
    "tinyShip12.png",
    "tinyShip13.png",
    "tinyShip14.png",
    "tinyShip15.png",
    "tinyShip16.png",
    "tinyShip17.png",
    "tinyShip18.png",
    "tinyShip19.png",
    "tinyShip20.png",
]
for i in list:
    print(type(SPRITESHEET_REGISTRY[i]), type(SPRITESHEET_REGISTRY[i]["rows"]))
    # dict, int
    print(SPRITESHEET_REGISTRY[i]["rows"])
