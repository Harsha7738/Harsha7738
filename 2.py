{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "10cf2278",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'count_pairs' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 20\u001b[0m\n\u001b[0;32m     18\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNo.of pairs with sum = \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28msum\u001b[39m\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m is \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mpairs_count\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124mpairs\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     19\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[1;32m---> 20\u001b[0m     main()\n",
      "Cell \u001b[1;32mIn[1], line 17\u001b[0m, in \u001b[0;36mmain\u001b[1;34m()\u001b[0m\n\u001b[0;32m     15\u001b[0m numbers\u001b[38;5;241m=\u001b[39m[\u001b[38;5;241m2\u001b[39m,\u001b[38;5;241m7\u001b[39m,\u001b[38;5;241m4\u001b[39m,\u001b[38;5;241m1\u001b[39m,\u001b[38;5;241m3\u001b[39m,\u001b[38;5;241m6\u001b[39m]\n\u001b[0;32m     16\u001b[0m \u001b[38;5;28msum\u001b[39m\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m10\u001b[39m\n\u001b[1;32m---> 17\u001b[0m pairs_count\u001b[38;5;241m=\u001b[39mcount_pairs(numbers,\u001b[38;5;28msum\u001b[39m)\n\u001b[0;32m     18\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNo.of pairs with sum = \u001b[39m\u001b[38;5;132;01m{\u001b[39;00m\u001b[38;5;28msum\u001b[39m\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m is \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mpairs_count\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124mpairs\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'count_pairs' is not defined"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cca0011f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter size of list 8\n",
      "Enter element 1: 2\n",
      "Enter element 2: 3\n",
      "Enter element 3: 4\n",
      "Enter element 4: 5\n",
      "Enter element 5: 6\n",
      "Enter element 6: 7\n",
      "Enter element 7: 3\n",
      "Enter element 8: 2\n",
      "The range of list is  5\n"
     ]
    }
   ],
   "source": [
    "def difference(arr):\n",
    "  if (len(arr) <=  3 ):\n",
    "    return -1\n",
    "  maxi = max(arr)\n",
    "  mini = min(arr)\n",
    "  return (int(maxi) - int(mini))\n",
    "list_size = int(input(\"Enter size of list \"))\n",
    "arr = []\n",
    "for i in range(list_size):\n",
    "  element = input(f\"Enter element {i+1}: \")\n",
    "  arr.append(element)\n",
    "range1 = difference(arr)\n",
    "if range1 <= 0:\n",
    "  print(\"Range determination not possible\")\n",
    "else:\n",
    "  print(\"The range of list is \", range1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c72218a4",
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
