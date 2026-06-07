# galaga_clone

## Setup

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# play the game
python3 main.py
```
## Todo
### Up Next
- [x] fix collision detection efficiency. 
    - ideas
        - distance detection
        - hash table
        - tile map: overkill? 
        - quadtree: overkill? 
    - efficiency wasn't the issue. the rects were not in sync with surfaces.
- [x] make bullets skinner 
- [ ] add more enemy types and paths that more closely match what is in Galaga
    - thinking about using these assets going forward
        - https://disruptorart.itch.io/tiny-ships-free-spaceships
    - and one of these backgrounds
        - https://hexadecimalwtf.itch.io/space-pixels 
    - they seem closer to galaga (at least the background does). I don't mind the player and enemy assets being different as long as they behave as close to their Galaga counterparts as possible.
    - [ ] get spritesheets working.



# Later
- [ ] add sound? 
- [ ] learn about Galaga's menu, HUD, level system

