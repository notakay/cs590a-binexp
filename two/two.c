#include <stdio.h>
#include <stdlib.h>

char binsh[] = "/bin/sh";

int main(void) {
	system(0);
	char buffer[64];
	setbuf(stdout, NULL);
	printf("Stack won't execute no more\n");
	printf("system at %p, /bin/sh at %#x\n", system, binsh);
	printf("Input: ");
	gets(buffer);
}
