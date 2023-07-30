#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
/**
 * main - the entry point of the program
 * Return: an integer value 1 otherwise 0
 */
int infinite_while(void);
int main(void)
{
	int i = 0;
	pid_t pid;

	for (; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
			printf("Zombie process created, PID: %d\n", getpid());
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - an infinite loop
 * Return: an integer value
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
