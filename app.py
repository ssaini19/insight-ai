from flask import Flask, render_template

app = Flask(__name__)

REPORTS = [
  {
    'id': 1,
    'site': 'Christies Beach',
    'title': 'Clinical Indicators',
    'Month': 'August',
  },
  {
    'id': 2,
    'site': 'Casa Mia',
    'title': 'National Quality Clinical Indicators',
    'Month': 'August',
  },
  {
    'id': 3,
    'site': 'Edge Hill',
    'title': 'Monthly Clinical Indicators',
    'Month': 'August',
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html',
                         reports=REPORTS,
                         company_name='Insight Ai')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
