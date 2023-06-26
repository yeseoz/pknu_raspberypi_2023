#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <pthread.h>
#define BUF_SIZE 2048
#define MAX_CLNT 256 

void * handle_clnt(void * arg);
void error_handling(char *msg);

int clnt_cnt = 0;
int clnt_socks[MAX_CLNT];
pthread_mutex_t mutx;

char webpage[]= "HTTP/1.1 200 OK\r\n"
"Server:Linux Web Server\r\n"
"Content-Type: text/html; charset=UTF-8\r\n\r\n"
"<!DOCTYPE html>\r\n"
"<html><head><title> My Web Page </title> \r\n"
"<style>body {background-color: #FFFF00}</style></head>\r\n"
"<body><center> <h1>Hello world!!</h1><br>\r\n"
"<img src=\"game.jpg\"></center></body></html>\r\n";


int main(int argc, char *argv[])
{
	int serv_sock, clnt_sock;
	struct sockaddr_in serv_adr, clnt_adr;
	int clnt_adr_sz;
	pthread_t t_id;
	char buffer[BUF_SIZE];
//	FILE *file;

	if(argc!=2)
	{
		printf("Usage :%s <port>\n", argv[0]);
		exit(1);
	}
	
	pthread_mutex_init(&mutx, NULL);
	serv_sock = socket(PF_INET, SOCK_STREAM, 0);

	memset(&serv_adr, 0, sizeof(serv_adr));
	serv_adr.sin_family = AF_INET;
	serv_adr.sin_addr.s_addr = htonl(INADDR_ANY);
	serv_adr.sin_port = htons(atoi(argv[1]));

	if(bind(serv_sock, (struct sockaddr*) &serv_adr, sizeof(serv_adr))==-1)
	{
		error_handling("bind() error");
	}

	if(listen(serv_sock, 5) ==-1)
	{
		error_handling("lister() error");
	}

	while(1)
	{
		clnt_adr_sz = sizeof(clnt_adr);
		clnt_sock = accept(serv_sock, (struct sockaddr*) &clnt_adr, &clnt_adr_sz);
		
		printf("Connected client IP: %s \n", inet_ntoa(clnt_adr.sin_addr));

		read(clnt_sock, buffer, BUF_SIZE); // 버퍼에 클라이언트에서 보낸 문자열 저장
		
		if(strstr(buffer, "game.jpg") != NULL)
		{
			printf("힝..");
		}
		else
		{
			write(clnt_sock, webpage, sizeof(webpage));
		}
	
		close(clnt_sock);
	}
	close(serv_sock);
	return 0;
}

void *handle_clnt(void *arg)
{
	int clnt_sock = *((int*)arg);
	int str_len = 0, i;
	char msg[BUF_SIZE];

	pthread_mutex_lock(&mutx);
	for(i = 0; i < clnt_cnt; i++)
	{
		if(clnt_sock == clnt_socks[i])
		{
			while(i++<clnt_cnt-1)
			{
				clnt_socks[i] = clnt_socks[i +1];
			}
			break;
		}
	}
	clnt_cnt--;
	pthread_mutex_unlock(&mutx);
	close(clnt_sock);
	return NULL;
}

void error_handling(char *msg)
{
	fputs(msg, stderr);
	fputc('\n', stderr);
	exit(1);
}
