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
            - these images contain sprite sheets, not just a single picture. I need to find a way to loop over the sub-images(?) in each image. This will
            give the illusion of animation for my sprites which I think is worth the effort.
            - I think this link could teach me how: https://ehmatthes.github.io/pcc_2e/beyond_pcc/pygame_sprite_sheets/
            - or this: https://pyga.me/docs/ref/surface.html#pygame.Surface.subsurface
    - and one of these backgrounds
        - https://hexadecimalwtf.itch.io/space-pixels 
    - they seem closer to galaga (at least the background does). I don't mind the player and enemy assets being different as long as they behave as close to their Galaga counterparts as possible.
    - [ ] get spritesheets working.



# Later
- [ ] add sound? 
- [ ] learn about Galaga's menu, HUD, level system

