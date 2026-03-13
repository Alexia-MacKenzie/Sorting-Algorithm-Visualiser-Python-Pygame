# Sorting-Algorithm-Visualiser-Python-Pygame


This application allows users to simulate and visualise different sorting algorithms in ascending order, and allows them to visually compare the difference between them.

Overview:

What the app does

This pygame programme allows for users to see the difference between bubble, insertion and merge sort.


Who it’s for

Users of this application could vary from students to teachers. It is a suitable application to teach anyone from GCSE level and above about the three main sorting algorithms which are first introduced at the GCSE level. It is particularly useful for:
- Students who are struggling to wrap their heads around the concept of these three sorting algorithms and can visually view them
- Teachers who may want to show their students a visual guide of the algorithms to aid their teaching materials
- Students who simply want to revise visually with these sorting algorithms

Users of this app can easily choose which algorithm they wish to view, choose their number of sorting items they want, and watch the graphic sort the bars in ascending order. They can also adjust the speed at which the algorithm runs, helping them track the bars to their speed of choice.


Motivation

I built this application because it is a topic of computer science which I really enjoy. Searching and sorting have always been fascinating to me and I wanted to create an educational programme on a topic which I take great interest in. This is a programme which I could show to students who are struggling with these concepts, and as I really like to help people, I would hope that my programme I created could help fulfil this need. I programmed my A-Level Computer Science project in pygame, so I wanted to brush up on these skills and create a project using pygame.


Features:
- Choose which sorting algorithm you want to simulate
- Select the number of sorting items you want
- Run the visual sort and watch the bars go from red (unsorted) to green (sorted)
- If running merge sort, grouped elements will turn yellow when being sorted in their separate arrays
- Change the speed in which the sorting algorithm runs at
- Use the compare page to watch bubble and insertion sort run at the same time and compare their number of comparisons and swaps, as well as the speed they run at


Tech stack
- Python
- Pygame

How it works 
This project utilises pygame libraries to render sorting logic into a visual experience which runs in real time. I have implemented Bubble, Insertion and Merge sorting algorithms to interact with the main running loop and displays bars of different heights and colours based on the state of the array. The array is created through using the random library and creates bars of random heights.

For the single sort views, I have implemented pygame.time.delay() and display.update() which allow for the functions to animate the steps of the sort, For the comparison mode, I have used Python Generators (yield) to run both Bubble and Insertion sort concurrently, which ensures they step through the algorithm in the same frame.

The bar widths and positions in on the page are dynamically calculated and created based on the users input of their chosen sample size. I have implemented a colour coding system (Red for unsorted, Yellow for active merging, and Green for completed) which helps the user to visualise the algorithm's progress.


Challenges and Learning
Whilst this project was created in a language which I do feel quite comfortable in, I did come across multiple issues. Firstly, I definitely had to brush up on my Pygame skills, because I had not worked in Pygame for quite some time. However, the skills came back to be very quicjly, and I soon built my confidence up even more, since implementing the visual sorting elements was quite difficult. One thing which I really wanted to do was to include all three sorts in the comparison page. However, I had implemented Merge Sort using recursion, since this is the most sophisticated and standard way of implementing it. However, I soon learnt that the best way for me to implement the sorts happening at the same time on this page was to use generators, which I soon discovered were quite difficult to use in recursion. So I decided that for this version of the code, I would only create the comparison page for bubble and insertion sort. I had to learn how to use generators and what the yield keyword was, which was very interesting to discover. 


Future improvements
In the future, there are quite a few additional functionalities I could include in this project. Firstly, I would try to implement the merge sort on the comparison page with the other two sorting algorithms, as this is definitely achievable, but quite difficult. I would also try to add more types of sorting algorithm onto the application, such as quick sort or selecton sort. Another great expansion of this application would be to include a searching algorithm page, where users could compare linear and binary search, since I really like searching algorithms too.

Setup instructions
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install any required libraries (requirements.txt).
4. Run application locally.
