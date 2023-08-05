 **NAME**

  **GCID** - reconsider OTP-CR-117/19


 **SYNOPSIS**

  ``gcidctl <cmd> [key=value] [key==value]``

 **DESCRIPTION**

  **GCID** is a python3 program that holds evidence that the king of the
  netherlands is doing a genocide, a written response where the king of
  the netherlands confirmed taking note of “what i have written”, namely
  proof that medicine he uses in treatement laws like zyprexa, haldol,
  abilify and clozapine are poison that makes impotent, is both physical
  (contracted muscles) and mental (let people hallucinate) torture and kills
  members of the victim groups.

  **GCID** provides a IRC bot that can run as a background daemon for 24/7
  day presence in a IRC channel, be used to display RSS feeds, act as a UDP
  to IRC gateway and program your own commands for.

 **INSTALL**

  ``pip3 install gcid``
    
 **CONFIGURATION**

  | ``cp /usr/local/share/gcid/gcid.service /etc/systemd/system``
  | ``systemctl enable gcid --now``

  **irc**

  | ``gcidctl cfg server=<server> channel=<channel>``
  | ``gcidctl cfg nick=<nick>``

  default channel/server is #gcid on localhost

  **sasl**

  | ``gcidctl pwd <nickservnick> <nickservpass>``
  | ``gcidctl cfg password=<outputfrompwd>``

  **users**

  | ``gcidctl cfg users=True``
  | ``gcidctl met <userhost>``


 .. title:: admin
