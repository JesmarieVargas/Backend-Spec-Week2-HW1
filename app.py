
from flask import Flask, request, jsonify;
from search_sort_alg import bubble_sorting, binary_search;

#http://127.0.0.1:5000/search?title=some-movie

app = Flask(__name__)


def bubble_sorting(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list

#List of video titles
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

@app.route('/search', methods=['GET'])
def search_videos():
    title = request.args.get('title', '')
    if not title:
        return jsonify({"error": "Video not found in list. Please enter another title."}), 400

    index = binary_search(sorted_video_titles, title)
    if index != -1:
        return jsonify({"position": index, "title": sorted_video_titles[index]})
    else:
        return jsonify({"error": "Video not found in list. Please enter another title."}), 404

@app.route('/search', methods=['POST'])
def search_video_post():
    data = request.get_json()
    title = data.get('title', '')
    if not title:
        return jsonify({"error": "Video not found in list. Please enter another title."}), 400

    index = binary_search(sorted_video_titles, title)
    if index != -1:
        return jsonify({"position": index, "title": sorted_video_titles[index]})
    else:
        return jsonify({"error": "Video not found in list. Please enter another title."}), 404

@app.route('/search/<title>', methods=['GET'])
def search_video_get(title):
    if not title:
        return jsonify({"error": "Video not found in list. Please enter another title."}), 400

    index = binary_search(sorted_video_titles, title)
    if index != -1:
        return jsonify({"position": index, "title": sorted_video_titles[index]})
    else:
        return jsonify({"error": "Video not found in list. Please enter another title."}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
