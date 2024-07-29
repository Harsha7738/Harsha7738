{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e2d0ec61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a string: hippopatamus\n",
      "The character with the maximum occurrence  is ['p'] having occurence count is 3 times.\n"
     ]
    }
   ],
   "source": [
    "def highest_occurrence_char(s):\n",
    "    char_count = {}\n",
    "    for char in s:\n",
    "        if char != ' ':\n",
    "            char_count[char] = char_count.get(char, 0) + 1\n",
    "    max_count = max(char_count.values())\n",
    "    max_char = [char for char, count in char_count.items() if count == max_count]\n",
    "    print(\"The character with the maximum occurrence  is\", max_char, \"having occurence count is\", max_count, \"times.\")\n",
    "s = input(\"Enter a string: \")\n",
    "highest_occurrence_char(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f5150cf",
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
