# Bumper

For when you crash into things

## Prerequisites

- `sudo apt-get install python-systemd`
- `pip install redis`
- You also need to follow the [PiFace setup](https://github.com/AmoebaThree/RaspberryPiSetup/blob/master/README.md#piface)

## Message Spec

Format: \<channel> "message"

**Inputs**

None

**Outputs**

* \<bumper-left> "left-on"
  * Left bumper falling edge, switch has been depressed
  * Triggered automatically
* \<bumper-left> "left-off"
  * Left bumper rising edge, switch has been released
  * Triggered automatically
* \<bumper-right> "right-on"
  * Right bumper falling edge, switch has been depressed
  * Triggered automatically
* \<bumper-right> "right-off"
  * Right bumper rising edge, switch has been released 
  * Triggered automatically
* \<bumper> "*"
  * This channel receives all messages as above
  * "left-on" "left-off" "right-on" "right-off"