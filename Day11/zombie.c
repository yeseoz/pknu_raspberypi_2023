#include <stdio.h>
#include <unistd.h>

int main()
{
	pid_t pid = fork();

	if(pid == 0) // Child
	{
		puts("Hi, I am a child process");
	}
	else
	{
		printf("Child Process ID : %d \n", pid);
		sleep(30); // 30 sec
	}

	if(pid == 0)
	{
		puts("End child process");
	}
	else
	{
		puts("End parent process");
	}

	return 0;
}
