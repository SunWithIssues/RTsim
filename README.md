# RTsim
So, I read (some of) an essay on Hard Real Time Computer Systems; after reading, I wanted to start a project on it. More explanations in README.

As of now, the code does not take outside environments as variables; variables are randomized to imitate different situations.
The time of the whole process is counted, and the time of each operation is also counted. GOAL: To minimize operation time.
The program's scenario is missile detection; if the missile hits the city or misses the city.
As of now, the city has an area of 100; the missile has an area of 10201 (0 is counted within the command, random.randint).

WANTED ADDS/CHANGES:
  The missile area is super large (imo) - shrink it.
  Add missile power - a nuke has more range than a pistol.
  Evacuation procedures.


Link to Essay: http://what-when-how.com/Tutorial/topic-424vv9g/Hard-Real-Time-Computing-Systems-Predictable-Scheduling-Algorithms-and-Applications-18.html
