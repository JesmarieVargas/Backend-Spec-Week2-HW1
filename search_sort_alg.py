#sorting algorithm to ensure your binary search is searching through a sorted list.
def bubble_sorting(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

sorted_video_titles = bubble_sorting(video_titles)
print(sorted_video_titles)

#binary search algorithm for searching videos by title.
def binary_search(list, target):
    left, right = 0, len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

def video_search(title):
    index = binary_search(sorted_video_titles, title)

    if index != -1:
        return {'position': index, "title":sorted_video_titles[index]}
    else:
        return {"error": "Video not found in list. Please enter another title."}

# search_title = "Home Alone" # Testing if my error populated if I inputted a video that was not in the list
search_title = "Artificial Intelligence Revolution"

result = video_search(search_title)
print(result)
