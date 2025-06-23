from flask import Flask, render_template_string, render_template, request, redirect
import json

app = Flask(__name__)

todo = ['Погулять', 'Посмотреть фильм', 'Выучить джаваскрипт']
todo = [
    {'name': 'Погулять', 'status': 'Не выполнено'},
    {'name': 'Посмотреть фильм', 'status': 'Не выполнено'}
]


class Database():
    def get_countries(self):
        countries = self._load_from_file()
        return countries

    def get_country(self, name):
        countries = self.get_countries()
        for country in countries:
            if country['name'] == name:
                return country
    def add_country(self, name, capital, population):
        country = {
            'name':name,
            'capital': capital,
            'people': population
        }
        countries = self.get_countries()
        countries.append(country)
        self._load_to_file(countries)

    def delete_country(self, name):
        pass

    def _load_from_file(self):
        with open('countries.json', encoding='utf-8') as f:
            return json.load(f)
    def _load_to_file(self, countries):
        with open('countries.json', 'w', encoding='utf-8') as f:
            return json.dump(countries, f)

db = Database()

@app.route('/')
def index():
    return render_template('index.html', data=todo)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/countries')
def countries():
    countries_data = db.get_countries()
    return render_template('countries.html', countries=countries_data)

@app.route('/countries/<string:country_name>')
def countries_detail(country_name):
    # написать логику поиска страны по имени и передать ее в шаблон
    # перебрать список стран и найти ту, что в country_name

    country = db.get_country(country_name)
    if country:
        return render_template('countries_detail.html', country=country)
    return 'Такой страны нет'


@app.route('/countries/add', methods=['POST'])
def countries_add():
    # добавить словарь request.form в общий список, но так, чтобы ключи совпадали!
    db.add_country(request.form['name'], request.form['capital'], request.form['population'])
    return redirect('/countries')


@app.route('/countries/<string:country_name>/delete', methods=['POST'])
def countries_delete(country_name):
    # удалить словарь из списка стран при совпадении названия
    for index, country in enumerate(countries_data):
        if country['name'] == country_name:
            countries_data.pop(index)
    return redirect('/countries')

app.run(debug=True)