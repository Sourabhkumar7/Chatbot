Currency Exchange Chatbot Project 

In this project, I developed a sophisticated chatbot using Dialogflow, designed specifically as a currency exchange calculator. This chatbot is capable of understanding user intents and extracting relevant entities to perform accurate currency conversions. The project seamlessly integrates multiple technologies to provide a user-friendly interface and reliable backend operations.

Dialogflow for NLP:

Intents: These are predefined purposes or goals that the user might have while interacting with the chatbot. For instance, asking for the current exchange rate between two currencies.
Entities: These are data points that Dialogflow extracts from user inputs, such as the names of the currencies and the amount to be converted.

Flask for User Interface:

Flask is used to create a web interface where users can interact with the chatbot. This interface is intuitive and responsive, ensuring a smooth user experience.
The Flask application serves as a bridge between the user's input and the Dialogflow backend.


Ngrok for Exposing Local Server:

Ngrok is utilized to expose your local Flask server to the internet securely, allowing external access to your chatbot during development and testing phases.
This setup enables seamless interaction with the chatbot from any location and facilitates the integration of real-time currency exchange rate APIs, ensuring accurate and up-to-date information.


Telegram Integration:

To extend the chatbot's reach and usability, it is integrated with Telegram. This allows users to interact with the currency exchange calculator directly from the Telegram app.
The integration ensures that the chatbot can cater to users on a popular messaging platform, enhancing its accessibility and convenience.

How It Works

User Interaction:

Users interact with the chatbot via the Flask web interface or through Telegram. They input queries such as "What is the exchange rate from USD to EUR?" or "Convert 100 USD to JPY."

Intent and Entity Recognition:

Dialogflow processes the input, recognizing the user's intent (e.g., currency conversion) and extracting relevant entities (e.g., source currency, target currency, amount).

API Call:

The backend, powered by Flask and securely exposed to the internet via Ngrok, fetches the latest exchange rates from a reliable external API.


Response Generation:

The chatbot processes the fetched data and calculates the conversion. It then generates a response that includes the converted amount and exchange rate details.


Displaying Results:

The result is displayed on the web interface or sent back through Telegram, providing the user with accurate and real-time currency exchange information.
