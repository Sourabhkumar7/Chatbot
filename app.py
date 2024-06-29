

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    try:
        cf = fetch_conversion_factor(source_currency, target_currency)
        final_amount = round(amount * cf, 2)
        response_text = "{} {} is {} {}".format(amount, source_currency, final_amount, target_currency)
    except Exception as e:
        response_text = str(e)

    response = {
        'fulfillmentText': response_text
    }
    return jsonify(response)


def fetch_conversion_factor(source, target):
    api_key = "7aba1bb0cef80497dad9c268"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{source}"

    response = requests.get(url)
    data = response.json()

    if 'conversion_rates' not in data:
        raise Exception("Error fetching conversion rate")

    conversion_rate = data['conversion_rates'].get(target)

    if conversion_rate is None:
        raise Exception(f"Conversion rate for {target} not found")

    return conversion_rate


if __name__ == "__main__":
    app.run(debug=True)

