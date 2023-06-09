from typing import List

from celery import shared_task
import time


@shared_task(bind=True,autoretry_for=(Exception,))
def computeFib(self, inputData:int):
    return fibRecur(inputData) 

def fibRecur(n)  -> int:
    #time.sleep(0.1)
    if n == 0 :
      return 0
    elif n == 1 : 
      return 1
    return fibRecur(n-1) + fibRecur(n-2)