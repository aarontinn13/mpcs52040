from flask import Flask, jsonify, request, render_template
import subprocess
import os
import itertools
import hashlib
import string

app = Flask(__name__)


@app.route('/passwordcracker', methods=['GET'])
def password_cracker():

    hashedPassword = request.json['password']       # hashed password we pass through
    maxLength = request.json['length']              # max length of the unhashed password
    workerTotal = request.json['threads']           # number of total threads
    worker = request.json['worker']                 # current thread
    chars = string.printable                        # all characters
    attempts = 0                                    # count of iteration attempts
    segment = (len(chars)//workerTotal)*worker      # where the worker will start searching

    print(('worker:', worker))
    for prefix in chars[segment:]:
        for password_length in range(0, maxLength):
            for guess in itertools.product(chars, repeat=password_length):

                attempts += 1
                guess = prefix+''.join(guess)

                if hashlib.md5(guess.encode()).hexdigest() == hashedPassword:
                    return jsonify({'password' : guess, 'attempts' : attempts, 'thread': worker})
    return "No Password could be found on this thread"

# Run the app server
app.run(host='0.0.0.0', port=5001, debug=True)
