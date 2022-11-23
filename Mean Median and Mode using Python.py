{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3f0a979d",
   "metadata": {},
   "source": [
    "# Mean Median and Mode using Python\n",
    "##### Mean, Median and Mode are the fundamentals of statistics used in almost every domain where we deal with numbers. Python is one of the best programming languages for numerical calculations. So you should know how to calculate mean, median and mode using Python without using any built-in Python library or module. So in this article, I will take you through how to calculate mean, median, and mode using Python."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "785db589",
   "metadata": {},
   "source": [
    "# Mean\n",
    "The mean is the average value of all the values in a dataset. To calculate the mean value of a dataset, we first need to find the sum of all the values and then divide the sum of all the values by the total number of values. So here’s how to calculate the mean using Python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d616a006",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20.2\n"
     ]
    }
   ],
   "source": [
    "#Mean\n",
    "list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]\n",
    "mean = sum(list1)/len(list1)\n",
    "print(mean)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d19ccfb1",
   "metadata": {},
   "source": [
    "# Median\n",
    "The Median is the middle value among all the values in sorted order. Here we need to calculate the mid-value of all the values in a dataset. But before calculating the Median, we need to arrange all the values in sorted order. There are two different ways of calculating the median value:\n",
    "\n",
    "when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2\n",
    "when the total number of values is odd: Median = {(n+1)/2}thterm\n",
    "Now below is how you can calculate the median using Python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "88fd8ca6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Median\n",
    "list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]\n",
    "list1.sort()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "489401fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[12, 12, 16, 20, 20, 20, 23, 24, 25, 30]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5b57992b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20.0\n"
     ]
    }
   ],
   "source": [
    "if len(list1) % 2 == 0:\n",
    "    m1 = list1[len(list1)//2]\n",
    "    m2 = list1[len(list1)//2 - 1]\n",
    "    median = (m1 + m2)/2\n",
    "else:\n",
    "    median = list1[len(list1)//2]\n",
    "print(median)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7fbf3509",
   "metadata": {},
   "source": [
    "# Mode\n",
    "Mode is the most frequently occurring value among all the values. Below is how we can calculate the mode value of a dataset using Python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7de55552",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "# Mode\n",
    "list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]\n",
    "frequency = {}\n",
    "for i in list1:\n",
    "    frequency.setdefault(i, 0)\n",
    "    frequency[i]+=1\n",
    "\n",
    "frequent = max(frequency.values())\n",
    "for i, j in frequency.items():\n",
    "    if j == frequent:\n",
    "        mode = i\n",
    "print(mode)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "62c60dba",
   "metadata": {},
   "source": [
    "# Summary\n",
    "So this is how you can calculate mean, mid-value, and mode using Python without using any library or any inbuilt Python module. Python is one of the best programming languages for numerical calculations. So you should know how to calculate mean, median and mode using Python without using any built-in Python library or module. I hope you liked this article on calculating mean, median, and mode using Python. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4df15f19",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
