# SNAKE!

A super classic game! Surely someone else has already built a terminal based version, but here is my take.
Built in python, a language meant to write a game about reptiles.

## Refactor to pygame
Decided to use PyGame to handle inputs, so now I want to refactor so
that the game is printed to the pygame screen.
See the file [[file:tests/pygame_inputs.py][testing out the pygame stuff]]

- [ ] refactor Gamerunner
- [ ] tweak grid, etc. to fit on pygame screen.
- [ ] FINALLY implement the user input system.

## What needs to be done
- [x] add snake movement
- [x] add death by touching walls
- [x] opening screen
- [ ] add user input
- [ ] add food spawning
- [ ] add score
- [ ] add ability to pause game

## DISTANT FUTURE FUN!
- [ ] multiplayer snake!
- [ ] play snake with friends remotely
- [ ] TWITCH COMMANDS SNAKE PLAY!!!

## dependencies

This game currently only requires python =3.10= but it will probably work with older python 3 versions


## what works now
There is no user input yet but you can see the snake move around by
```python
python -m app.main
```
