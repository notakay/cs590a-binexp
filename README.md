# CS590A Binary Exploitation

Introduces basic binary exploitation concepts such as stack overflows, executable space protection, format strings and leveraging information leakage for exploits.

Challenges are 32-bit executables, with PIE disabled.

Challenge zero introduces a basic stack overflow, overwriting the return address.

Challenge one is also a stack overflow, but jumps to a shell code that the attacker places onto the stack.

Challenge two introduces the NX bit, making the stack not executable. The attacker uses code already part of the binary, the system function and the string "/bin/sh" to spawn a shell.

Challenge three executable uses stack cookies but has a format string vulnerability. The goal is to leak the stack cookie and spawn a shell by calling the system function.