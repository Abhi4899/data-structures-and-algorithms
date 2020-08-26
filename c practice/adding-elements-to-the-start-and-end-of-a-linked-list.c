#include<stdio.h>
#include<stdlib.h>
int main(void)
{
    struct node
    {
        int data;
        struct node* next;
    };
    
    struct node *head=NULL, *newnode, *temp;
    newnode = (struct node*)malloc(sizeof(struct node));
    int choice;
    printf("Enter your choice 0/1: ");
    scanf("%d",&choice);
    while(choice)
    {
        
        if(head==NULL)
        {
            head=newnode;
            printf("Enter an integer value: ");
            scanf("%d",&head->data);
            temp=newnode;
        }
        else
        {
            newnode=(struct node*)malloc(sizeof(struct node));
            temp->next=newnode;
            temp=newnode;
            printf("Enter an integer value: ");
            scanf("%d",&temp->data);
        }
        
        printf("Choice 0/1: ");
        scanf("%d",&choice);
    }
        temp->next=NULL;
        
        
        
        
        //adding a node to the start of a inked list
        printf("Before adding new element to start of the linked list\n");
        temp=head;
        while(temp!=NULL)
        {
            printf("%d\n",temp->data);
            temp=temp->next;
        }
        
        
        temp=head; //to store the address of existing head
        newnode=(struct node*)malloc(sizeof(struct node)); //storing address of new node in newnode
        head=newnode; //updating head to point to this new node 
        printf("Enter the value you want to add at the start: ");
        scanf("%d",&head->data);
        head->next=temp; //storing the memory adress of the initial first node to make it second
        
        
        printf("After adding new element to start of the linked list\n");
        temp=head;
        while(temp!=NULL)
        {
            printf("%d\n",temp->data);
            temp=temp->next;
        }
        
        
        
        //adding a node to the end of a linked list
        struct node *lastadd;
        temp=head;
        while(1)
        {
            lastadd=temp;
            temp=temp->next;
            if(temp==NULL)
            break;
        }
        newnode=(struct node*)malloc(sizeof(struct node));
        lastadd->next=newnode;
        printf("Enter the value you want to add at the end: ");
        scanf("%d",&newnode->data);
        newnode->next=NULL;
        
        printf("After adding new element to end of the linked list\n");
        temp=head;
        while(temp!=NULL)
        {
            printf("%d\n",temp->data);
            temp=temp->next;
        }
}