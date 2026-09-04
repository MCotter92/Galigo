# galaga_clone
Its a galaga clone. Not 1:1. Just for fun.

## Setup

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# play the game
python3 main.py
```
Or just use `uv`

## Todo
### Up Next
- [x] add more enemiy types
- need to refactor level_generator() -> create_enemies() -> Enemy() 
    - get 3 different enemies on the screen. just do that.
    - I think what I really need to do is create some Level templates and just move to the next one when criteria is met or something?
    - So it looks like your score indicates what level (stage) you are in. Ill deal with that later. 
### Later
- [ ] add more enemy paths that more closely match what is in Galaga
- [ ] add sound? 
- [ ] learn about Galaga's menu, HUD, level system

