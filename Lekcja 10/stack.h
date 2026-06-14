//
// Created by Rafal Nowak on 23/04/2022.
//
#define QUEUE_SIZE 5
int queue_table[QUEUE_SIZE] = { 0 };
int queue_w_index = 0;
int queue_r_index = 0;
int size =0;

int isQueueEmpty(void)
{
    return (size==0 and queue_r_index==queue_w_index) ? 1 : 0;
}

int isQueueFull(void)
{
    return (size!=0 and queue_r_index==queue_w_index) ? 1 : 0;
}

int Pop(void)
{
    if (!isQueueEmpty())
    {
        queue_r_index++;
        size--;
        return queue_table[queue_r_index-1];

    }
    if (queue_r_index % QUEUE_SIZE == 0) {
        queue_r_index = 0;
    }

    return queue_table[0];
}

int First(void)
{
    if (!isQueueEmpty())
    {
        return queue_table[queue_r_index];
    }

    return queue_table[0];
}

void Push(int val)
{
    if (!isQueueFull())
    {
        queue_table[queue_w_index] = val;
        queue_w_index++;
        size++;
    }
    if (queue_w_index % QUEUE_SIZE == 0 ) {
        queue_w_index = 0;
    }
}