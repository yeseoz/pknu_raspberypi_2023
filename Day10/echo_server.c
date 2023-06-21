#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define BUF_SIZE 1024
void error_handling(char *message);

int main(int argc, char *argv[])
{
	int serv_sock, clnt_sock; // 클라이언트 / 서버 파일 디스크립트를 저장할 함수
	char message[BUF_SIZE];
	int str_len, i;

	struct sockaddr_in serv_adr, clnt_adr;
	socklen_t clnt_adr_sz;

	if(argc!=2)
	{
		printf("Usage : %s <port>\n", argv[0]);
		exit(1);
	}

	serv_sock = socket(PF_INET, SOCK_STREAM, 0); // ipv3, TCP, 0
	if(serv_sock == -1)
	{
		error_handling("socket() error");
	}

	memset(&serv_adr, 0, sizeof(serv_adr)); // 구조체 조기화  구조체 안에서 초기화가 안되기 때문에
	serv_adr.sin_family = AF_INET;
	serv_adr.sin_addr.s_addr = htonl(INADDR_ANY);
	serv_adr.sin_port = htons(atoi(argv[1]));

	if(bind(serv_sock, (struct sockaddr*)&serv_adr, sizeof(serv_adr))==-1) // 주소할당
	{
		error_handling("bind() error");
	}

	if(listen(serv_sock, 5) == -1)
	{
		error_handling("listen() error");
	}
	
	clnt_adr_sz = sizeof(clnt_adr);

	for(i = 0; i<5; i++) // 5번 대화가능
	{
		clnt_sock = accept(serv_sock, (struct sockaddr*)&clnt_adr, &clnt_adr_sz);
		if(clnt_sock== -1)
		{
			error_handling("accept() error");
		}
		else
		{
			printf("Conneccted client %d \n", i+1);
		}

		while((str_len = read(clnt_sock, message, BUF_SIZE))!=0)
		{
			write(clnt_sock, message, str_len);
		}

		close(clnt_sock);
	}

	close(serv_sock); // 서버 소켓을 닫는다
	return 0;
}

void error_handling(char *message)
{
	fputs(message, stderr);
	fputc('\n', stderr);
	exit(1);
}
			
