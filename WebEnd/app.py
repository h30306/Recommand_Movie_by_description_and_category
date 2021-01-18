from flask import Flask, request, render_template, jsonify
import requests
import json
import pickle

app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template("combine.html")


@app.route('/', methods=['GET', 'POST'])
def index():
    movies = {}
    movies['movie1'] = 'Action'
    movies['movie2'] = 'Romantic'

    categorys = {'category_0': ['https://picsum.photos/id/100/400/400', 'Action'],
 'category_1': ['https://picsum.photos/id/101/400/400', 'Adventure'],
 'category_2': ['https://picsum.photos/id/102/400/400', 'Animation'],
 'category_3': ['https://picsum.photos/id/103/400/400', 'Biography'],
 'category_4': ['https://picsum.photos/id/104/400/400', 'Comedy'],
 'category_5': ['https://picsum.photos/id/105/400/400', 'Crime'],
 'category_6': ['https://picsum.photos/id/106/400/400', 'Documentary'],
 'category_7': ['https://picsum.photos/id/107/400/400', 'Drama'],
 'category_8': ['https://picsum.photos/id/108/400/400', 'Family'],
 'category_9': ['https://picsum.photos/id/109/400/400', 'Fantasy'],
 'category_10': ['https://picsum.photos/id/110/400/400', 'Film-Noir'],
 'category_11': ['https://picsum.photos/id/111/400/400', 'History'],
 'category_12': ['https://picsum.photos/id/112/400/400', 'Horror'],
 'category_13': ['https://picsum.photos/id/113/400/400', 'Music'],
 'category_14': ['https://picsum.photos/id/114/400/400', 'Musical'],
 'category_15': ['https://picsum.photos/id/115/400/400', 'Mystery'],
 'category_16': ['https://picsum.photos/id/116/400/400', 'Romance'],
 'category_17': ['https://picsum.photos/id/117/400/400', 'Sci-Fi'],
 'category_18': ['https://picsum.photos/id/118/400/400', 'Sport'],
 'category_19': ['https://picsum.photos/id/119/400/400', 'Thriller'],
 'category_20': ['https://picsum.photos/id/120/400/400', 'War'],
 'category_21': ['https://picsum.photos/id/121/400/400', 'Western']}


    def process_category(req, ques):
        category = []
        for q in ques:
            if req[q] == 'None':
                pass
            else:
                category.append(req[q])
        return category

    def get_(result):
        Genres = []
        for i in result['Genres']:
            Genres.append(','.join(eval(i)))
        result_Genres = Genres
        result_StoryLine = result['StoryLine']
        result_category = result['category']
        result_name = result['name']
        result_rating_count = result['rating_count']
        rating_value = result['rating_value']
        jnjbus_info=zip(result_Genres, result_StoryLine, result_category, result_name, result_rating_count,rating_value)
        return jnjbus_info

    if request.method == 'POST':
        req = request.values
        categorys = process_category(req, list(categorys.keys()))
        categorys = ' '.join(categorys)
        pass_data = {'category': categorys, 'input': req['text']}
        print(pass_data)
        url = 'http://IP:port/RecommandWebsite'
        req2 = requests.post(url, verify=False, data=pass_data, timeout=120)
        result = json.loads(req2.text)
        print(result)
        test = get_(result)
        return render_template("result.html", result=test)
        # return jsonify({'mag':'success'})

    return render_template("combine.html", categorys=categorys)


@app.route('/test', methods=['GET', 'POST'])
def test():
    # req2 = '{"Genres":["g1", "g2"]}'
    # result = json.loads(req2)
    result = {"Genres":["g1", "g2"]}
    return render_template("test.html", result=result)


if __name__ == '__main__':
    app.debug = True
    app.run()
