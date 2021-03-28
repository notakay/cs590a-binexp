#include <stdio.h>

char binsh[] = "/bin/sh";

void vuln(void) {
	char buffer[8];
	printf("Entery query:");
	gets(buffer);
	printf(buffer);
	printf("Enter payload:");
	gets(buffer);
	printf(buffer);
}

int main(void) {
	system(0);

	setbuf(stdout, NULL);
	printf("Stack won't execute no more v2\n");
	printf("system at %p, /bin/sh at %#x\n", system, binsh);

	vuln();
}
