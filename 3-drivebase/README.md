# Lesson 3: DriveBase

Goal: make the robot drive straight, turn, and follow a repeatable path.

## Run These First

1. `drivebase_straightturn.py` - drive forward, turn, and back up.
2. `drivebase_moveslow.py` - test slower driving.
3. `drivebase_movefast.py` - test faster driving.
4. `drivebase_drivesquare.py` - drive a square with a function.

## Change One Thing

- Change a straight distance from `500` to `300`.
- Change a turn from `90` to `45` or `180`.
- Change the speed settings and compare accuracy.

## Robot Setup Check

Before blaming the code, check these:

- left motor and right motor are plugged into the expected ports
- `wheel_diameter` matches the wheel on the robot
- `axle_track` is close to the distance between the left and right wheels
- one motor may need `Direction.COUNTERCLOCKWISE`

## Challenge

Make the robot:

- leave base
- drive to a target spot
- turn toward home
- come back

Measure the final error. Then change only one number and try again.
