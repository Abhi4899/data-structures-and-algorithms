#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

int main(void)
{
	struct node
	{
		int info;
		struct node* next;
	};

	int choice;
	struct node *head=NULL, *newnode, *temp;

	printf("Enter your choice 0/1: ");
	scanf("%d",&choice);
	while(choice==1)
	{
		newnode = (struct node*)(malloc(sizeof(struct node)));
		printf("Enter a value: ");
		scanf("%d",&newnode->info);
		if(head==NULL)
		{
			head=newnode;
			temp=newnode;
		}
		else
		{
			temp->next=newnode;
			temp=newnode;
		}
		printf("Enter your choice 0/1: ");
		scanf("%d",&choice);
	}
	temp->next=NULL;
	temp=head;
	while(temp!=NULL)
	{
		printf("%d\n",temp->info);
		temp=temp->next;
	}
}
