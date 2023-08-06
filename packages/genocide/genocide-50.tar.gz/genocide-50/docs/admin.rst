 **NAME**

  **GENOCIDE** - reconsider OTP-CR-117/19

 **SYNOPSIS**

  ``gcdctl <cmd> [key=value] [key==value]``

 **DESCRIPTION**

  **GENOCIDE** is a python3 program that holds evidence that the king of the
  netherlands is doing a genocide, a written response where the king of
  the netherlands confirmed taking note of “what i have written”, namely
  proof that medicine he uses in treatement laws like zyprexa, haldol,
  abilify and clozapine are poison that makes impotent, is both physical
  (contracted muscles) and mental (let people hallucinate) torture and kills
  members of the victim groups.

  **GENOCIDE** provides a IRC bot that can run as a background daemon for 24/7
  day presence in a IRC channel, be used to display RSS feeds, act as a UDP
  to IRC gateway and program your own commands for.

 **INSTALL**

  ``pip3 install genocide``

 **CONFIGURATION**

  | ``cp /usr/local/share/genocide/genocide.service /etc/systemd/system``
  | ``systemctl enable genocide --now``

  **irc**

  | ``gcdctl cfg server=<server> channel=<channel>``
  | ``gcdctl cfg nick=<nick>``

  default channel/server is #genocide on localhost

  **sasl**

  | ``gcdctl pwd <nickservnick> <nickservpass>``
  | ``gcdctl cfg password=<outputfrompwd>``

  **users**

  | ``gcdctl cfg users=True``
  | ``gcdctl met <userhost>``


 .. title:: admin
