app = Flask(__name__)

# configure MySQL database connection
cnx = mysql.connector.connect(user='admin', password='dSYhuuqh', host='mysql-122988-0.cloudclusters.net', database='mydatabase', port=10165)
cursor = cnx.cursor()

# define webhook endpoint
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # parse the JSON data from the request body
    data = request.get_json()

    # extract the firstname and surname fields from the JSON data
    firstname = data.get('firstname')
    surname = data.get('surname')

    # insert the data into the MySQL database
    query = "INSERT INTO details (firstname, surname) VALUES (%s, %s)"
    values = (firstname, surname)
    cursor.execute(query, values)
    cnx.commit()

    # return a response to the webhook
    return 'Webhook received successfully!'

# start the Flask app and listen for incoming requests
if __name__ == '__main__':
    app.run()