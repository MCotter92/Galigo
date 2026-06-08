# new spritesheet strategy.

# main.py                 Player/Enemy                       SPRITESHEET_REGISTRY
# ─────────               ──────────────────                 ────────────────────
# "tinyShip3.png"  ──→   look up filename in registry  ──→  {"cols": 5, "rows": 2}
# width=54, height=54    load raw sheet                       extract frames,
#                       scale each to (54,54)                store in self.frames

SPRITESHEET_REGISTRY = {
    "tinyShip1.png": {
        "path": "assets/images/tiny-spaceships/tinyShip1.png",
        "cols": 6,
        "rows": 3,
    },
    "tinyShip2.png": {
        "path": "assets/images/tiny-spaceships/tinyShip2.png",
        "cols": 6,
        "rows": 3,
    },
    "tinyShip3.png": {
        "path": "assets/images/tiny-spaceships/tinyShip3.png",
        "cols": 5,
        "rows": 2,
    },
    "tinyShip4.png": {
        "path": "assets/images/tiny-spaceships/tinyShip4.png",
        "cols": 7,
        "rows": 3,
    },
    "tinyShip5.png": {
        "path": "assets/images/tiny-spaceships/tinyShip5.png",
        "cols": 5,
        "rows": 2,
    },
    "tinyShip6.png": {
        "path": "assets/images/tiny-spaceships/tinyShip6.png",
        "cols": 5,
        "rows": 1,
    },
    "tinyShip7.png": {
        "path": "assets/images/tiny-spaceships/tinyShip7.png",
        "cols": 5,
        "rows": 3,
    },
    "tinyShip8.png": {
        "path": "assets/images/tiny-spaceships/tinyShip8.png",
        "cols": 6,
        "rows": 1,
    },
    "tinyShip9.png": {
        "path": "assets/images/tiny-spaceships/tinyShip9.png",
        "cols": 5,
        "rows": 2,
    },
    "tinyShip10.png": {
        "path": "assets/images/tiny-spaceships/tinyShip10.png",
        "cols": 4,
        "rows": 1,
    },
    "tinyShip11.png": {
        "path": "assets/images/tiny-spaceships/tinyShip11.png",
        "cols": 7,
        "rows": 2,
    },
    "tinyShip12.png": {
        "path": "assets/images/tiny-spaceships/tinyShip12.png",
        "cols": 4,
        "rows": 3,
    },
    "tinyShip13.png": {
        "path": "assets/images/tiny-spaceships/tinyShip13.png",
        "cols": 8,
        "rows": 2,
    },
    "tinyShip14.png": {
        "path": "assets/images/tiny-spaceships/tinyShip14.png",
        "cols": 4,
        "rows": 2,
    },
    "tinyShip15.png": {
        "path": "assets/images/tiny-spaceships/tinyShip15.png",
        "cols": 6,
        "rows": 2,
    },
    "tinyShip16.png": {
        "path": "assets/images/tiny-spaceships/tinyShip16.png",
        "cols": 4,
        "rows": 3,
    },
    "tinyShip17.png": {
        "path": "assets/images/tiny-spaceships/tinyShip17.png",
        "cols": 6,
        "rows": 2,
    },
    "tinyShip18.png": {
        "path": "assets/images/tiny-spaceships/tinyShip18.png",
        "cols": 4,
        "rows": 2,
    },
    "tinyShip19.png": {
        "path": "assets/images/tiny-spaceships/tinyShip19.png",
        "cols": 4,
        "rows": 2,
    },
    "tinyShip20.png": {
        "path": "assets/images/tiny-spaceships/tinyShip20.png",
        "cols": 5,
        "rows": 3,
    },
}
