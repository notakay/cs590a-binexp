#include <stdio.h>
#include <stdlib.h>

void win(void) {
	printf("Spawning shell!");
	system("/bin/sh");
}

int main(void) {
	char buffer[16];
	printf("Redirect to %p to win!\n", win);
	printf("Input: ");
	gets(buffer);
}
