#include <stdio.h> // 표준 입출력 함수 
#include <stdlib.h> // 유틸리티 함수들 모아놓은 함수
#include <string.h> // C형식 문자열을 다룰 수 있는 함수
#include <unistd.h> // 리눅스에서 사용하는 C컴파일러 헤더
#include <sys/socket.h>  //socklen_t 타입을 가능하게 만들어주는 헤더 소켓관련 핵심기능
#include <arpa/inet.h> // 주소변환 기능을 사용할 경우 사용하는 헤더
#include <fcntl.h>

#define BUF_SIZE 2048

void error_handling(char *message);

int main(int argc, char * argv[])
{
	int serv_sock, clnt_sock; // 서버 클라이언트 소켓
	struct sockaddr_in  serv_addr, clnt_addr; // bind함수에 주소정보를 전달하는 용도
  socklen_t clnt_addr_size;
  char buffer[BUF_SIZE];
  char img_buffer[BUF_SIZE];
  
 char resmsg[] = "HTTP/1.1 200 OK\r\n"
 								 "Server:Linux Server\r\n"
 								 "Content-Type: text/html; charset=UTF-8\r\n\r\n"
 								 "<!DOCTYPE html>\r\n"
 								 "<html><head><title> My Web Page </title> \r\n"
 								 "<style>body {background-color: #FFFF00}</style></head?\r\n"
 								 "<body><center> <h1>Hello world!!</h1><br>\r\n"
 								 "<img src=\"test.jpg\"><center></body></html>\r\n";

	if(argc!=2)
	{
		printf("Usage : %s <port>\n", argv[0]);
		exit(1);
	}

	serv_sock = socket(PF_INET, SOCK_STREAM, 0);

	if(serv_sock == -1)
	{
		error_handling("socket() error");
	}

	memset(&serv_addr, 0, sizeof(serv_addr)); // serv_addr 초기화
	serv_addr.sin_family = AF_INET; // Ipv4
	serv_addr.sin_addr.s_addr = htonl(INADDR_ANY); // IP주소 32비트
	serv_addr.sin_port = htons(atoi(argv[1])); // 포트 번호

	if(bind(serv_sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) == -1)
	{
		error_handling("bind() error");
	}

	if(listen(serv_sock, 5) == -1)
	{
		error_handling("listen() error");
	}

	clnt_addr_size = sizeof(clnt_addr);

	while(1)
	{
		clnt_sock = accept(serv_sock, (struct sockaddr*)&clnt_addr, &clnt_addr_size);
	
		if(clnt_sock == -1)
		{
			error_handling("accept() error");
		}

		printf("Connected client IP: %s \n", inet_ntoa(clnt_addr.sin_addr)); // 네트워크를 문자로변환

		read(clnt_sock, buffer, BUF_SIZE); // 클라이언트에서 보낸 문자열 버퍼에 저장
		printf(buffer);

		write(clnt_sock, resmsg, strlen(resmsg));

		int file = open("test.jpg", O_RDONLY);
		
		if(file == -1)
		{
			error_handling("open() error");
		}

		ssize_t read_size;
		while((read_size = read(file, img_buffer, BUF_SIZE)) >0)
		{
			write(clnt_sock, img_buffer, read_size);
		}
		printf("%d",read_size);
		printf(img_buffer);
		close(file);
		close(clnt_sock);
	}
	close(serv_sock);

	return 0;
}

void error_handling(char *message)
{
	fputs(message, stderr);
	fputc('\n', stderr);
	exit(1);
}
