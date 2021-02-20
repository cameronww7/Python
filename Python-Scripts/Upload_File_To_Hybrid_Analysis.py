"""
Python Exercise:

Create an account on https://www.hybrid-analysis.com/
.
View the API documentation: https://www.hybrid-analysis.com/docs/api/v2#/

Create a script that can submit a file to Hybrid Analysis for scanning and return the results.
The script should have two ways to be executed.

1. The first will be to submit the file for scanning.  It should take an input of a filename.
    The script will submit the file to Hybrid Analysis and return the job information for the scan.

2. The second option of the script should take a job ID and return the JSON details from that scan.

Use the Python Requests module to interact with Hybrid Analysis.  Do not use the pre-built Python connector.
"""

import requests
import os
# Used for Testing
import time

class HybridAnalysisAPI:
    """
        Class for Hybrid Analysis API
    """
    def __init__(self, xAPIKey=None):
        """
            Constructor for the HybridAnalysisAPI class.
            Parameters:
                xApi_Key (str): Hybrid Analysis API key
        """
        self.apiKey = xAPIKey
        self.base_url = "https://www.hybrid-analysis.com/api/v2/"
        self.headers = {"api-key": self.apiKey,
                        "Accept": "application/json",
                        "user-agent": "Falcon Sandbox"}

        self.fileToScan = ""
        self.jobId = ""

        self.environments = 110

        if xAPIKey is None:
            raise Exception("You must provide a valid API key")

    def getFile(self):
        return self.fileToScan

    def setFile(self, xFile):
        self.fileToScan = xFile

    def getJobID(self):
        return self.jobId

    def setJobID(self, xJobId):
        self.jobId = xJobId

    def setAPIKey(self, xAPIKey):
        self.api_key = xAPIKey

    def testAPIConnection(self):
        """
            The goal of this def to test an API key and make sure its working
            :return: API Status Code of the Call
        """
        options = {"hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"}

        response = requests.post("{}search/hash".format(self.base_url),
                                 headers=self.headers,
                                 data=options)

        self.printResponse(response.json()[0])

        return response.status_code

    def uploadFile(self, FileToUpload):
        """
            Goal of this def is to upload a file to HA and return its Job ID
            :return: API Status Code of the Call
        """
        if not os.path.isfile(FileToUpload):
            raise Exception("File not found. Please submit an existing file.")
        else:
            print("Uploading File - {}".format(FileToUpload))

        fileUpload = {'file': ('{}'.format(os.path.basename(FileToUpload)), '{}'.format(open(FileToUpload, 'rb')))}
        options = {'environment_id': self.environments}

        response = requests.post('{}submit/file'.format(self.base_url),
                                 headers=self.headers,
                                 data=options,
                                 files=fileUpload)

        self.printResponse(response.json())

        if response.status_code == 201:
            jobId = response.json()["job_id"]
            self.jobId = jobId
            return jobId
        else:
            print("Failed - {}".format(response.status_code))
            return response.status_code

    def grabFileAnalysis(self, xJobId):
        """
            Goal of this def is to grab the results of the file upload
            :return: API Status Code of the Call
        """
        response = requests.get("{}report/{}/summary".format(self.base_url, xJobId),
                                 headers=self.headers)

        self.printResponse(response.json())

        return response.status_code

    def uploadHash(self, xHashToCheck):
        """
            Goal of this def is to upload a file hash to HA and get the Job ID for it
            :return: API Status Code of the Call
        """
        options = {"hash": xHashToCheck}

        response = requests.post("{}search/hash".format(self.base_url),
                                 headers=self.headers,
                                 data=options)

        self.printResponse(response.json()[0])

        return response.status_code

    def printResponse(self, response):
        """
            Goal of this def is to Display an API Response in a line by line format
            :return: NO RETURN
        """
        for key in response:
            print(key, " : ", response[key])

    def promptUser(self):
        """
            Goal of this def is to prompt the user for 2 options and excute depending on the option
            chosen by the user.
            :return:
        """
        print("Hybrid Analysis Program"
              "\n-----------------------"
              "\nOption 1 : Upload a File Path to be Scanned"
              "\nOption 2 : Get Results from a Scan")
        while True:
            try:
                # First Attempt - will be successful if an Int comes in
                val = int(input("Please enter an Option: "))

            except:
                # If an error pops it will display an Error and re-prompted the user for an Int
                print("Looks like you did not enter an integer!")
                continue

            else:
                # Breaks the infinite while loop if a int is entered
                if val == 1:
                    fileToImput = input("Please enter a File To be Scan: ")
                    self.fileToScan = fileToImput
                    self.uploadFile(fileToImput)
                elif val == 2:
                    jobIDToImput = input("Please enter a Job ID: ")
                    self.grabFileAnalysis(jobIDToImput)
                break


#print("\nCreating HAAPI Class")
HAAPI = HybridAnalysisAPI("oxj546f1de933007j914knjy811f46c58l98hnkqdaa1b62bixvin0iybf30cd96")

HAAPI.promptUser()

"""
print("\nTesting Connection")
print("___________________________________")
print(HAAPI.testAPIConnection())

print("\nCreating Uploading File")
print("___________________________________")
jobID = HAAPI.uploadFile("test.txt")

print("\nPrinting Job ID")
print("___________________________________")
print(jobID)

print("\nHalting for 60 Seconds")
print("___________________________________")
time.sleep(60)

print("\nGrabbing File Upload Results")
print("___________________________________")
print(HAAPI.grabFileAnalysis(jobID))
"""

