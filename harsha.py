{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ac800c8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The maximally occurring character is 'p' & occurrence count is 3\n"
     ]
    }
   ],
   "source": [
    "from collections import Counter\n",
    "\n",
    "def filter_alphabets(input_string):\n",
    "  \n",
    "    filtered_string = ''.join(c for c in input_string if c.isalpha()).lower()\n",
    "    return filtered_string\n",
    "\n",
    "def count_characters(filtered_string):\n",
    "    return Counter(filtered_string)\n",
    "\n",
    "def find_highest_occurrence(counter):\n",
    "   \n",
    "    if not counter:\n",
    "        return None, 0\n",
    "    highest_char = max(counter, key=counter.get)\n",
    "    highest_count = counter[highest_char]\n",
    "    return highest_char, highest_count\n",
    "\n",
    "def main(input_string):\n",
    "    filtered_string = filter_alphabets(input_string)\n",
    "    \n",
    "    character_counts = count_characters(filtered_string)\n",
    "    \n",
    "    highest_char, highest_count = find_highest_occurrence(character_counts)\n",
    "    \n",
    "    return highest_char, highest_count\n",
    "\n",
    "input_string = \"hippopotamus\"\n",
    "char, count = main(input_string)\n",
    "print(f\"The maximally occurring character is '{char}' & occurrence count is {count}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "036d7fd2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The range of the list is 8\n"
     ]
    }
   ],
   "source": [
    "def validate_list(number_list):\n",
    "    \n",
    "    return len(number_list) >= 3\n",
    "\n",
    "def calculate_range(number_list):\n",
    "   \n",
    "    min_value = min(number_list)\n",
    "    max_value = max(number_list)\n",
    "    return max_value - min_value\n",
    "\n",
    "def main(number_list):\n",
    "    \n",
    "    if not validate_list(number_list):\n",
    "        return \"Range determination not possible\"\n",
    "    \n",
    "    return calculate_range(number_list)\n",
    "\n",
    "\n",
    "number_list = [5, 3, 8, 1, 0, 4]\n",
    "result = main(number_list)\n",
    "print(f\"The range of the list is {result}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "914cb7f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5dd8f1f9",
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
