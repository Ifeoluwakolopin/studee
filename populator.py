import sys
import firebase_admin
import requests
from firebase_admin import credentials, firestore
from read import readfile

def connect_to_db():
    cred = credentials.Certificate("config.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    course_outlines = db.collection("course_outline")
    unilag = course_outlines.document("unilag")
    collection = unilag.collection("engineering")
    return collection

def write_to_db(courses):
    """
    This writes the courses to the firestore collection.
    """
    for course in courses:
        #collection.document(course["code"]).set(course)
        print("Writing {} to db...".format(course["code"]))
    print("Wrote {} documents to db".format(len(courses)))

def usage():
    print("""
    +-------------------------------+
    |         POPULATOR             |
    +-------------------------------+
    """.center(10))
    print ('''
    YOUR TEXTFILE SHOULD HAVE THIS FORMAT
    - Course code and Course Title in CAPITAL LETTERS
    - Each different course must be separated by an empty line.
    - View example.txt for an example of how to setup your textfile.
    
    USAGE:

    python3 populator.py [textfile] --> Read the specified file for course outlines
    python3 populator.py [textfile] -j --> Populate and save to json file.
    python3 populator.py [textfile] -h --> Instructions on how to use
    
    Example:
    python3 populator.py example.txt
    ''')
    sys.exit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    elif len(sys.argv) > 2 and sys.argv[2] == "-h":
        usage()
    elif len(sys.argv) > 2 and sys.argv[2] == "-j":
        courses = readfile(sys.argv[1], save=True)
        collection = connect_to_db()
        write_to_db(courses)
    else:
        courses = readfile(sys.argv[1])
        collection = connect_to_db()
        write_to_db(courses)