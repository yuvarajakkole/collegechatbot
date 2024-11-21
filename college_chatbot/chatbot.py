from flask import Flask, request, jsonify, render_template
from fuzzywuzzy import fuzz, process  # For fuzzy matching
import re  # For simple grammar handling

app = Flask(__name__)

# Predefined keyword categories for better matching
designer = ["designer", "maker","developer","design"]
greetings = ["hey", "hi", "hello", "greetings", "good morning", "good evening", "good afternoon"]
courses = ["courses", "programs", "majors", "degrees", "subjects", "offerings", "specializations", "fields"]
admission = ["admission", "apply", "enrollment", "registration", "joining", "eligibility", "criteria", "requirements"]
fees = ["fees", "cost", "tuition", "price", "payment", "scholarship", "financial aid"]
location = ["location", "where", "campus", "place", "address", "directions"]
contact = ["contact", "phone", "email", "reach", "support", "help", "call"]
achievements = ["achievements", "awards", "rankings", "recognition", "success", "milestones"]
events = ["events", "seminars", "workshops", "festivals", "celebrations", "competitions", "tech fest"]
faculty = ["faculty", "professors", "teachers", "lecturers", "staff", "instructors", "departments"]
research = ["research", "projects", "publications", "collaborations", "innovation"]
designer = ["designer", "maker","developer","design"]

# Helper function for fuzzy matching
def fuzzy_match(user_input, category_list, threshold=70):
    """This function checks if any item in the category list is a fuzzy match for the user_input."""
    match, score = process.extractOne(user_input, category_list)
    if score >= threshold:
        return True
    return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_input = request.json['question'].lower()
    
    # Clean user input to remove extra spaces, punctuation, etc.
    user_input = re.sub(r'[^\w\s]', '', user_input)

    # Check fuzzy matching for each category
    if fuzzy_match(user_input, greetings):
        answer = "Hello! How can I assist you with your college queries? Feel free to ask about courses, admissions, or anything else!"
    
    elif fuzzy_match(user_input, courses):
        answer = ("We offer a range of programs including:\n"
                  "- B.Tech (Computer Science, Electronics, Mechanical)\n"
                  "- M.Tech (AI, Robotics, Cybersecurity)\n"
                  "- MBA (Finance, Marketing, Human Resources)\n"
                  "- PhD in various disciplines\n"
                  "Would you like more information on any specific program?")
    
    elif fuzzy_match(user_input, admission):
        answer = ("Admissions are open for the current academic year! You can apply online through our website. "
                  "The basic eligibility criteria are:\n"
                  "- For B.Tech: 10+2 with a minimum of 60% in PCM\n"
                  "- For M.Tech: B.Tech degree with a valid GATE score\n"
                  "- For MBA: A bachelor's degree and a valid CAT/MAT score\n"
                  "Would you like to know about the application process or deadlines?")
    
    elif fuzzy_match(user_input, fees):
        answer = ("Our fee structure is as follows:\n"
                  "- B.Tech: $10,000 per year (scholarships available for meritorious students)\n"
                  "- M.Tech: $12,000 per year\n"
                  "- MBA: $15,000 per year\n"
                  "- PhD: $8,000 per year\n"
                  "We also offer scholarships and financial aid. Would you like more details?")
    
    elif fuzzy_match(user_input, location):
        answer = ("Our college is located at XYZ street, ABC city, and is well-connected by public transport. "
                  "You can find directions on Google Maps by searching for 'XYZ College'. "
                  "Would you like more information on transportation or nearby facilities?")
    
    elif fuzzy_match(user_input, contact):
        answer = ("You can contact our admissions office at:\n"
                  "- Phone: +123 456 7890\n"
                  "- Email: admissions@xyzcollege.edu\n"
                  "For general inquiries, you can email us at info@xyzcollege.edu. We're here to help!")
    
    elif fuzzy_match(user_input, achievements):
        answer = ("Our college has achieved numerous accolades, including:\n"
                  "- Ranked #1 in the state for engineering programs\n"
                  "- A 95% placement rate with top companies like Google, Microsoft, and Amazon\n"
                  "- Accredited with an 'A+' grade by NAAC\n"
                  "- Awarded 'Best Research Institute' for AI and Robotics in 2023\n"
                  "Would you like to know more about our recent achievements?")
    
    elif fuzzy_match(user_input, events):
        answer = ("We host a variety of events throughout the year, including:\n"
                  "- Annual Tech Fest (October 10, 2024)\n"
                  "- Alumni Meet (November 15, 2024)\n"
                  "- Workshops on AI and Robotics (Monthly)\n"
                  "Would you like to participate or know more about any of these events?")
    
    elif fuzzy_match(user_input, faculty):
        answer = ("Our faculty consists of highly experienced professionals and researchers:\n"
                  "- Dr. A. Sharma (Head of Computer Science Department, AI Expert)\n"
                  "- Dr. P. Rao (Mechanical Engineering, Robotics Specialist)\n"
                  "- Prof. S. Mehta (MBA Program, Finance)\n"
                  "Would you like to know more about specific departments or professors?")
    
    elif fuzzy_match(user_input, research):
        answer = ("Our college is renowned for research in AI, Robotics, and Cybersecurity. "
                  "We have ongoing projects in collaboration with industry leaders like Google and Intel. "
                  "Our research labs are equipped with the latest technology, and students are encouraged to participate. "
                  "Would you like to know more about our research areas or publications?")
    
    elif fuzzy_match(user_input,designer):
        answer = (" This website is a way to get easy and friendly communicating--\n"
                  "this will be designed to by group of 3 Enggenering students---\n"
                  "{-Yuvaraj A}\n"
                  "{-Dhanush B M}\n"
                  "{-B G vibhav}\n")

    else:
        answer = ("I'm sorry, I didn't understand that. Can you ask something else? You can inquire about admissions, courses, fees, and more!")

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
