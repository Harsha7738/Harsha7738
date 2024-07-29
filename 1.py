{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "89ec0e49",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6 pairs\n"
     ]
    }
   ],
   "source": [
    "a = [2,7,4,1,3,6,9]\n",
    "def find(a):\n",
    "    count = 0\n",
    "    for i in range(0,len(a)):\n",
    "        for j in range(0,len(a)):\n",
    "            if(a[i] + a[j] == 10):\n",
    "                #print(a[i],a[j])\n",
    "                count+=1\n",
    "    return count\n",
    "count = find(a)\n",
    "print(count, \"pairs\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf3f810e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
