from flask import Flask, abort, request
import logging.config
import json
import candidate_service
app = Flask(__name__)

logging.config.fileConfig('logging.conf')
# create logger
logger = logging.getLogger('candidate_service_app')

@app.route('/', methods=["GET"])
def candidate_service_home():
    return "Candidate Service App..."

@app.route('/candidateservice/addcandidate', methods=["POST"])
def add_candidate():
    if not request.files:
        logger.info('The Request Body is not the Files Type... Hence throwing 400 error code...')
        abort(400)
    data = json.load(request.files['data'])
    logger.info('JSON Request: ' + str(data))
    print(str(data))

    name = data['name']
    logger.info('name: ' + name)
    print('name: ' + name)
    address = data['address']
    qualification = data['qualification']
    jobskill = data['jobskill']
    yearsofexperience = data['yearsofexperience']
    postedresumefile = request.files['document']
    postedresumefilepath = "resumefiles/" + postedresumefile.filename
    logger.info("Resume File name retrieved is " + postedresumefile.filename)
    postedresumefile.save(postedresumefilepath)
    logger.info('Going to call add candidate API...')
    candidateAdded = candidate_service.addCandidate(name=name, address=address, qualification=qualification, jobskill=jobskill, yearsofexperience=yearsofexperience, postedresumefilepath=postedresumefilepath)
    print("Candidate Added " + str(candidateAdded))
    return str(candidateAdded)

@app.route('/candidateservice/getallcandidates', methods=["GET"])
def get_All_Candidates():
    candidatesList = candidate_service.getAllCandidates()

    return candidatesList

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)