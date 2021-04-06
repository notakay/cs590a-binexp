# CS590A Binary Exploitation

Introduces basic binary exploitation concepts such as stack overflows, executable space protection, format strings and leveraging information leakage for exploits. The goal is to spawn root shells using the several vulnerable services.

Challenges are 32-bit executables, with PIE disabled.

- Challenge zero introduces a basic stack overflow, overwriting the return address.

- Challenge one is also a stack overflow, but jumps to a shell code that the attacker places onto the stack.

- Challenge two introduces the NX bit, making the stack not executable. The attacker uses code already part of the binary, the system function and the string "/bin/sh" to spawn a shell.

- Challenge three executable uses stack cookies but has a format string vulnerability. The goal is to leak the stack cookie and spawn a shell by calling the system function.

The Docker container can be built and started as follows:

```
sudo docker build -t test:0.1 .
sudo docker run --rm --name test0.1 -it test:0.1
```

The attacker has access to the docker container as the non-root user `ctf`, allowed to read source and the disassembly of the challenge executables under the `/opt` directory.

### Resources

[LiveOverflow's Binary Exploitation playlist](https://www.youtube.com/watch?v=iyAyN3GFM7A&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN)  
[SoK: Eternal War in Memory](https://people.eecs.berkeley.edu/~dawnsong/papers/Oakland13-SoK-CR.pdf)  
[CTFTime](https://www.ctftime.org)  
[pwntools](https://github.com/Gallopsled/pwntools)