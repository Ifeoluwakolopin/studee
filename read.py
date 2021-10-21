import re, sys, json

result = []

def clean(course):
    """
    This takes in a whole string containing info about a course
    and finds useful info from it
    """
    # regex to find course code
    code = re.findall(r"\b[A-Z]+[\s]+\d\d\d*\b", course)[0]
    course = re.sub(code, '', course).replace(":", "")
    # regex to find title
    title = re.findall(r"\b[A-Z]+(?:[\s&]+[A-Z]+)*\b", course)[0]
    course = re.sub(title, '', course)
    # regex to find units
    unit = re.findall(r"\d\s+[Uu]nits", course)[0]
    course = re.sub(unit, '', course)

    # formated results
    outline = course.replace(":", "").replace("\n", ",").strip()
    title = title.capitalize()
    code = code.lower().replace(" ", "")
    level = "Year{}".format(code[3])
    if code[4] == "2":
        semester = "second"
    else:
        semester = "first"
    
    return {
        "outline":outline,
        "title":title,
        "semester":semester,
        "Unit":unit,
        "code":code,
        "level":level
    }


def openfile(filename):
    """
    This opens up the file.
    File must be in txt format
    """
    file = open("{}".format(filename), "r")
    doc = file.read()
    courses = doc.split("\n\n")
    print("Found {} courses in {}\nGetting data from courses...".format(len(courses), filename))
    return courses


def save_to_json(c):
    """
    This saves results to a json file
    """
    with open('results.json', 'a') as r:
        json.dump(c, r, indent=4)

def readfile(filename, save=False):
    """
    This takes in a txt file and returns a dictionary of courses and related info
    Args:
    filename: name of txt file in the same directory
    save: Boolean (if True results will be saved to a json file.)
    """
    
    count = 0
    courses = openfile(filename)
    for course in courses:
        try:
            c = clean(course)
            result.append(c)
            count += 1
        except Exception as e:
            print("Error getting data for {}".format(course[0:9]))
            print(e)
    print("Extracted courses: {0}\nTotal courses: {1}".format(
        count, len(courses)
    ))
    if save:
        save_to_json({"courses":result})
    return result

def usage():
    print ('''
     ==================TEXTFILE FORMAT===============
    Your textfile containing the list of courses must have this format.
    - Course code and Course Title in CAPITAL LETTERS
    - Each different course must be separated by an empty line.
    ===View example.txt for an example of how to setup your textfile.
    
    USAGE:

    python3 read.py [textfile] --> Read the specified file for course outlines
    python3 read.py [textfile] -j --> Read and save to json file.
    python3 read.py [textfile] -h --> Instructions on how to use
    
    Example:
    python3 read.py example.txt
    ''')
    sys.exit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    elif len(sys.argv) > 2 and sys.argv[2] == "-h":
        usage()
    elif len(sys.argv) > 2 and sys.argv[2] == "-j":
        (readfile(sys.argv[1], save=True))
    else:
        readfile(sys.argv[1])