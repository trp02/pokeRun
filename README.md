<a name="br1"></a>**PokeRun Intro**

The game is called PokeRun

There is a start screen that summarizes how to play the game visually. It’s mostly self
explanatory. How much damage you take from an obstacle will depend on which pokemon you
use to run through it. Also health can only be picked up by the pokemon of the same type.




<a name="br2"></a>**To play the game:**

\- git clone [https://github.com/trp02/pokeRun.git
](https://github.com/trp02/pokeRun.git)- have pygame installed

\- run **main.py**

\- versions used: **python 3.9.13**, **pygame 2.1.3**, should work on Windows and MacOS. Didn’t
work on clemson SoC virtual desktop due to “no audio device” error. Primary way I ran it was on
VSCode with pygame installed.

\- **Controls** : Left click to cycle character and space to jump

**Game Design**

The game is an infinite side scroller. The player will have to cycle through characters and dodge
obstacles that spawn randomly. As the game goes on it will become faster until it hits a cap and
from there the goal is to last as long as possible. The gimmick is that there are obstacles that
you can’t jump over. Rather you have to pick which character to cycle to in order to not take
damage. And if you mess up the player will take damage based on how effective the obstacle
type is compared to the pokemon running through it. Most other side scroller games from my
experience have power ups that you can pick up for temporary boosts but in my game the
“power up” is already there, you just have to learn when to pull it out.

There is no real story, just **survive**.

The primary emotion I want the player to feel is frustration. The game is simple on the surface
but as the pace picks up the player will have less and less time to react to their surroundings
and once they accidentally mess up once and lose health it’ll rattle them and lose concentration
leading them to die soon after. The biggest challenge will be to find a rhythm and figure out a
pattern for switching characters. So they’ll think something like: “Ok I need to switch to
charmander to pick up this fire health pack and immediately after left click twice to change to
bulbasaur to run through the water wall”. They will also need cold hands because if they
accidentally click one too many times there might not be enough time to cycle back, essentially
crippling any plan they had. The player will have to react quickly and more importantly, stay
calm.

The aim is to get the high score and nothing else will be recorded because if you’re not first
you’re last.

**Game Design Changes Original Concept:**

At the base level the game will run in a familiar way. The player will be controlling a character
and the goal is to keep them alive. As the game progresses it will become faster and it will be
important to execute moves with precision and speed. The player will be able to switch between
three characters which will be cycled in a set order. The player will have the freedom to switch
as many times as they want. Each character will have a unique nature indicated by their color:
fire, water and grass. If the player chooses the wrong character or gets hit by a neutral object
they will die.




<a name="br3"></a>**Changes**:

Overall the gameplay itself is very similar to what was originally proposed. Most of the changes
were visually. For most of the early development I was planning on the game having a much
smoother style of graphics - not pixelated. But over time I realized in order to accomplish that I
would need to create the art myself because it’s hard to find assets that mesh well together. For
that reason I switch to pixel style.

Mechanics and gimmick are identical to what was originally envisioned.

**Development/Documentation**

**Bugs**:

Game spawn works with real time so if you are playing the game and click on top to drag the
window, obstacles spawning will screw up and clump together.

Also there has been a range of performance issues. From personal experience the game runs
perfectly fine on my Windows desktop(as seen in video) but on my Macbook I’ve consistently
encountered screen tearing. Possibly due to hardware and optimized code.




<a name="br4"></a>**Roles, Tasks, Performance** Tirth- 100%

Obstacle system, animations, asset/hitbox adjustment, collisions, health system, input
mechanics, interaction adjustment, game time, bug fixes, game movement, game docs, asset
search, etc.

Milestone 1: Added rudimentary obstacle system, one character animations/movement, basic
collision detection

Milestone 2: Added assets/animation for remaining characters, game pacing, remaining
obstacles, game input/controls, adjusted hitboxes

Final: Health system, individual interaction finalized, eliminated bugs, highscore system and
loading screens

Assets: <https://sprites.pmdcollab.org>, itch.io and other websites who I’m pretty sure just stole the
art.

**DEMO:**

<https://www.youtube.com/watch?v=H4QhCFWzs68>
