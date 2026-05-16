from flask import Flask, render_template, abort

app = Flask(__name__)

# Барлық тауарлар туралы мәліметтер — бір жерде
PRODUCTS = {
    1: {
        "id": 1,
        "title": "Ұлттық күртеше 1",
        "price": "16 000 ₸",
        "image": "dress1.1.png",
        "detail_image": "dress1.jpg",
        "theme": "theme-1",
        "category": "women",
        "description": "Дәстүрлі қазақы ою-өрнекпен безендірілген, табиғи мақта-зығыр матадан тігілген жоғары сапалы ұлттық күртеше.",
        "material": "Жоғары сапалы мақта-зығыр",
        "color": "Қоңыр / Алтын",
        "sizes": ["S", "M", "L", "XL"],
    },
    2: {
        "id": 2,
        "title": "Ұлттық күртеше 2",
        "price": "16 000 ₸",
        "image": "dress2.1.png",
        "detail_image": "dress2.jpg",
        "theme": "theme-2",
        "category": "women",
        "description": "Жасыл реңкті ою-өрнектермен безендірілген, жеңіл және әдемі ұлттық киім.",
        "material": "Жоғары сапалы мақта",
        "color": "Жасыл / Крем",
        "sizes": ["S", "M", "L", "XL"],
    },
    3: {
        "id": 3,
        "title": "Ұлттық күртеше 3",
        "price": "16 000 ₸",
        "image": "dress3.1.png",
        "detail_image": "dress3.jpg",
        "theme": "theme-3",
        "category": "women",
        "description": "Жылы тондар мен дәстүрлі өрнектері бар сәнді ұлттық күртеше.",
        "material": "Зығыр-мақта қоспасы",
        "color": "Қоңыр / Жасыл",
        "sizes": ["S", "M", "L", "XL"],
    },
    4: {
        "id": 4,
        "title": "Ұлттық күртеше 4",
        "price": "16 000 ₸",
        "image": "dress4.1.png",
        "detail_image": "dress4.jpg",
        "theme": "theme-4",
        "category": "men",
        "description": "Алтын реңкті ою-өрнектермен безендірілген ерлерге арналған ұлттық киім.",
        "material": "Жоғары сапалы мақта",
        "color": "Алтын / Сары",
        "sizes": ["S", "M", "L", "XL", "XXL"],
    },
    5: {
        "id": 5,
        "title": "Ұлттық күртеше 5",
        "price": "16 000 ₸",
        "image": "dress5.1.png",
        "detail_image": "dress5.jpg",
        "theme": "theme-5",
        "category": "kids",
        "description": "Балаларға арналған ұлттық киім. Жеңіл, ыңғайлы және мейрамдарға жарайды.",
        "material": "Жұмсақ мақта",
        "color": "Аспан көк / Ақ",
        "sizes": ["3-4 жас", "5-6 жас", "7-8 жас", "9-10 жас"],
    },
    6: {
        "id": 6,
        "title": "Ұлттық күртеше 6",
        "price": "16 000 ₸",
        "image": "dress6.1.png",
        "detail_image": "dress6.jpg",
        "theme": "theme-6",
        "category": "kids",
        "description": "Балаларға арналған, шешіміне дейін сыртқы ою-өрнектермен безендірілген ұлттық киім.",
        "material": "Жұмсақ мақта-зығыр",
        "color": "Көк / Сұр",
        "sizes": ["3-4 жас", "5-6 жас", "7-8 жас", "9-10 жас"],
    },
    7: {
        "id": 7,
        "title": "Ұлттық күртеше 7",
        "price": "16 000 ₸",
        "image": "dress7.1.png",
        "detail_image": "dress7.jpg",
        "theme": "theme-7",
        "category": "men",
        "description": "Жылы реңктер мен дәстүрлі қазақы өрнектері бар ерлерге арналған ұлттық киім.",
        "material": "Жоғары сапалы мақта",
        "color": "Қызғылт сары / Алтын",
        "sizes": ["M", "L", "XL", "XXL"],
    },
}

CONTACT_PHONE = "+77773988869"
CONTACT_DISPLAY = "+7 777 398 8869"


@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS.values(), contact=CONTACT_DISPLAY)


@app.route('/women')
def women():
    filtered = [p for p in PRODUCTS.values() if p['category'] == 'women']
    return render_template('category.html', products=filtered, category="Қыздар", contact=CONTACT_DISPLAY)


@app.route('/men')
def men():
    filtered = [p for p in PRODUCTS.values() if p['category'] == 'men']
    return render_template('category.html', products=filtered, category="Ұлдар", contact=CONTACT_DISPLAY)


@app.route('/kids')
def kids():
    filtered = [p for p in PRODUCTS.values() if p['category'] == 'kids']
    return render_template('category.html', products=filtered, category="Балалар", contact=CONTACT_DISPLAY)


# Динамикалық тауар беті — 7 маршруттың орнына 1 маршрут
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = PRODUCTS.get(product_id)
    if not product:
        abort(404)
    return render_template('product_detail.html', product=product, contact=CONTACT_DISPLAY, phone=CONTACT_PHONE)


if __name__ == '__main__':
    app.run(debug=True)

    app.run(host='0.0.0.0', debug=True)
