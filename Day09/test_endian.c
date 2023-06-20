#include <stdio.h>
#include <arpa/inet.h>

int main()
{
	int data = 0x12345678;
	char* ptr = (char*)&data;

	for(long i = 0; i <sizeof(int); i++)
	{
		printf("%d, %#x\n", &ptr[i],  ptr[i]);
	}

	return 0;
}
	
