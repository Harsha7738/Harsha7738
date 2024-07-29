{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cc45631a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[7, 10]\n",
      "[15, 22]\n"
     ]
    }
   ],
   "source": [
    "def matrix_multi(A, B):\n",
    "    n = len(A)\n",
    "    C = [[0] * n for _ in range(n)]\n",
    "    for i in range(n):\n",
    "        for j in range(n):\n",
    "            for k in range(n):\n",
    "                C[i][j] += A[i][k] * B[k][j]\n",
    "    return C\n",
    "def matrix_power(A, m):\n",
    "    n = len(A)\n",
    "    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]\n",
    "    base = A\n",
    "    while m > 0:\n",
    "        if m % 2 == 1:\n",
    "            result = matrix_multi(result, base)\n",
    "        base = matrix_multi(base, base)\n",
    "        m //= 2\n",
    "    return result\n",
    "A = [[1, 2],\n",
    "     [3, 4]]\n",
    "m = 2\n",
    "result = matrix_power(A, m)\n",
    "for row in result:\n",
    "    print(row)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f08374f",
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
