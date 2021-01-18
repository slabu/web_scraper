from flask import Flask, request, redirect, render_template, jsonify

from web_scraping_script import WebScraper

app = Flask(__name__)

app.config['SECRET_KEY'] = "super_secret_key"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results_python')
def results_python():

    scraping_data = WebScraper('https://www.ampereanalysis.com')
    
    #scrapping_data = dict(scrapping_data)

    #print(scrapping_data)

    return render_template('results_python.html', scraped_data=scraping_data.scraping_method_results)

@app.route('/results_javascript')
def results_javascript():

    scraped_data = WebScraper('https://www.ampereanalysis.com')

    #return jsonify(scrapped_data.scrapping_method_results)
    return render_template('results_javascript.html', scraped_data=scraped_data.scraping_method_results)




if __name__ == "__main__":
    app.run(port=5000, debug=True)