# Bumper

For when you crash into things

## Prerequisites

- `sudo apt-get install python-systemd`
- `pip install redis`
- You also need to follow the [PiFace setup](https://github.com/AmoebaThree/RaspberryPiSetup/blob/master/README.md#piface)

## Message Spec

**Inputs**

None

**Outputs**

Format: \<channel> "message"

* \<bumper-left> "left-on"
  * Left bumper falling edge, switch has been depressed
* \<bumper-left> "left-off"
  * Left bumper rising edge, switch has been released
* \<bumper-right> "right-on"
  * Right bumper falling edge, switch has been depressed
* \<bumper-right> "right-off"
  * Right bumper rising edge, switch has been released 