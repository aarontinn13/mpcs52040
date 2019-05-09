from flask import Flask, jsonify, request
import itertools
import hashlib
import string
import sys


app = Flask(__name__)
PORT = sys.argv[1]

# cache
answers = {}

@app.route('/passwordcracker', methods=['GET'])
def password_cracker():

    hashedPassword = request.json['password']           # hashed password we pass through
    prefix = request.json['prefix']                     # prefix to search
    maxLength = request.json['length']                  # max length of the unhashed password
    chars = string.printable                            # all characters
    attempts = 0                                        # count of iteration attempts

    # return the result if it is cached
    if hashedPassword in answers:
        return jsonify({'password' : answers[hashedPassword], 'threads attempts' : "{}, the result was cached".format(attempts)})

    # start calcs
    for password_length in range(0, maxLength):
        for guess in itertools.product(chars, repeat=password_length):

            attempts += 1
            guess = prefix+''.join(guess)

            #cache result
            Password = hashlib.md5(guess.encode()).hexdigest()
            answers[Password] = guess

            if Password == hashedPassword:
                return jsonify({'password' : guess, 'threads attempts' : attempts})
    return "No answer"

# Run the app server
app.run(host='127.0.0.1', port=PORT, debug=True)
