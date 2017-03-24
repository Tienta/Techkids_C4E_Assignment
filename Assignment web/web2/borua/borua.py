from flask import *

app = Flask(__name__)

tree_list = [
    {"image_link":"https://instagram.fhan2-2.fna.fbcdn.net/t51.2885-15/e35/17126240_605511066305000_7056512309618802688_n.jpg",
     "topic":"Tree Ngo Ngo",
     "text":"Chậu cây ngộ ngộ xinh xinh thế này mà đi tặng chị yêu cô giáo yêu thì thật là vui quá đi mất. Những điều ngọt ngào không cần đến từ những gì quá to tát hay lớn lao cả mà chỉ đơn giản ngộ nghĩnh như vậy thôi cũng đủ ấm lòng rất nhiều rồi"},
    {"image_link":"https://instagram.fhan2-2.fna.fbcdn.net/t51.2885-15/e35/17126240_605511066305000_7056512309618802688_n.jpg",
     "topic":"Tree Ngo Ngo",
     "text":"Chậu cây ngộ ngộ xinh xinh thế này mà đi tặng chị yêu cô giáo yêu thì thật là vui quá đi mất. Những điều ngọt ngào không cần đến từ những gì quá to tát hay lớn lao cả mà chỉ đơn giản ngộ nghĩnh như vậy thôi cũng đủ ấm lòng rất nhiều rồi"},
    {"image_link": "https://instagram.fhan2-2.fna.fbcdn.net/t51.2885-15/e35/17126240_605511066305000_7056512309618802688_n.jpg",
     "topic": "Tree Ngo Ngo",
     "text": "Chậu cây ngộ ngộ xinh xinh thế này mà đi tặng chị yêu cô giáo yêu thì thật là vui quá đi mất. Những điều ngọt ngào không cần đến từ những gì quá to tát hay lớn lao cả mà chỉ đơn giản ngộ nghĩnh như vậy thôi cũng đủ ấm lòng rất nhiều rồi"},
    {"image_link":"https://instagram.fhan2-2.fna.fbcdn.net/t51.2885-15/e35/17077633_140162856505582_6864397593540034560_n.jpg",
     "topic":"Tree Ngo Nghe",
     "text":"Góc vườn nho nhỏ của bọ"},
    {"image_link": "https://instagram.fhan2-2.fna.fbcdn.net/t51.2885-15/e35/17077633_140162856505582_6864397593540034560_n.jpg",
     "topic": "Tree Ngo Nghe",
     "text": "Góc vườn nho nhỏ của bọ"},
    {"image_link":"https://instagram.fhan2-2.fna.fbcdn.net/t51.2885-15/e35/17077633_140162856505582_6864397593540034560_n.jpg",
     "topic":"Tree Ngo Nghe",
     "text":"Góc vườn nho nhỏ của bọ"},
    {"image_link":"https://instagram.fhan2-1.fna.fbcdn.net/t51.2885-15/e35/17333025_418681021817660_1111101743053144064_n.jpg",
     "topic":"Tree inspire",
     "text":"Small beautiful conner"},
    {"image_link":"https://instagram.fhan2-1.fna.fbcdn.net/t51.2885-15/e35/17333025_418681021817660_1111101743053144064_n.jpg",
     "topic":"Tree inspire",
     "text":"Small beautiful conner"},
    {"image_link":"https://instagram.fhan2-1.fna.fbcdn.net/t51.2885-15/e35/17333025_418681021817660_1111101743053144064_n.jpg",
     "topic":"Tree inspire",
     "text":"Small beautiful conner"}
]

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/home')
def borua_home():
    return render_template('home.html', treelist=tree_list)


if __name__ == '__main__':
    app.run()

