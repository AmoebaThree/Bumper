# Bumper

For when you crash into things

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