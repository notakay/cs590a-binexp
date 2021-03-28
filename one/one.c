#include <stdio.h>

int main(void) {
	char buffer[64];
	printf("Overflow this 64-byte buffer at %#x to spawn a shell!\n", buffer);
	printf("Input: ");
	gets(buffer);
}
