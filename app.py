from flask import Flask,render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def main():
    df = pd.read_csv('arduinoprueba.csv')
    return render_template('index.html')
    df.to_html()

#    data = pd.read_excel('dummy_data.xlsx')
#    data.set_index(['Name'], inplace=True)
#    data.index.name=None
#    return render_template('view.html',tables=[females.to_html(classes='female'), males.to_html(classes='male')],

    
if __name__ == "__main__":
   app.run(debug=True)