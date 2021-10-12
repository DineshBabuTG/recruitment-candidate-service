"""Service to manage candidates
"""
import os
import json
import logging
import candidate_dao

logger = logging.getLogger('candidate_service')
dir_path = os.path.dirname(os.path.realpath(__file__))
print("dir path is ", dir_path)

def addCandidate(name, address, qualification, jobskill, yearsofexperience, postedresumefilepath):
    print("In Add Candidate API")
    logger.info("In Add Candidate API")

    logger.info("name " + str(name) + " address " + str(address) + " qualification " + str(qualification) + " jobskill " + str(jobskill) + " yearsofexperience "  + str(yearsofexperience))
    print("name " + str(name) + " address " + str(address) + " qualification " + str(qualification) + " jobskill " + str(jobskill) + " yearsofexperience "  + str(yearsofexperience))
    candidate_dao.addCandidateDAO(name, address, qualification, jobskill, yearsofexperience, postedresumefilepath)
    return "Successfully added the candidate"

def getAllCandidates():
    print("In Get All Candidates API")
    logger.info("In Ger All Candidates API")
    #Sample Candidate Data
    #candidate1 = dict({'name': 'test1', 'address': 'abc', 'qualification': 'sadf1', 'jobskill': 'asdf1',
    #                         'yearsofexperience': '5'})
    #candidate2 = dict({'name': 'test2', 'address': 'abc', 'qualification': 'sadf2', 'jobskill': 'asdf2',
    #                   'yearsofexperience': '5'})
    candidateList = []
    candidatesFromDB = candidate_dao.getCandidatesDAO()
    for row in candidatesFromDB:
        candidate = dict({'candidateid': row[0], 'name': row[1], 'address': row[2], 'qualification': row[3], 'jobskill': row[4], 'yearsofexperience': row[5]})
        candidateList.append(candidate)
    logger.info(candidateList)
    data = json.dumps(candidateList)
    return data