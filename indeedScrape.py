import requests
import re
from bs4 import BeautifulSoup

header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'}

def getSource():
    url = 'https://www.indeed.com/jobs?q=software%20engineer&l=remote&start=10'
    r = requests.get(url, header)
    return r.text

def getJobKeys():
  sourceCode = str(getSource())
  rawJobKeys = re.findall('jobKeysWithInfo\[.*\]', sourceCode)[:-1]
  return [item[17:-2] for item in rawJobKeys]

def getIndividualJob(jobKey):
    url = f'https://www.indeed.com/viewjob?jk={jobKey}'
    r = requests.get(url, header)
    soup = BeautifulSoup(r.content, 'html.parser')
    return (soup, url)

def getJobs(jobKeyList):
  jobs = []
  for jobKey in jobKeyList:
    soup, url = getIndividualJob(jobKey)
    info = soup.find('div', class_ = 'jobsearch-ViewJobLayout-jobDisplay')
    #print(str(info))

    #* Job title
    jobTitle = info.find('h1', class_ = 'jobsearch-JobInfoHeader-title').text

    #* Company Name
    companyName = info.find('div', class_ = 'jobsearch-InlineCompanyRating').find('a').text

    #* Details Section
    detailsSection = [item.text for item in info.find('div', class_ = 'jobsearch-JobDescriptionSection-section').find_all('div', 'jobsearch-JobDescriptionSection-sectionItem')]

    #* Qualifications
    try:
      qualifications = info.find('div', class_ = 'jobsearch-ReqAndQualSection-item--title').text
    except:
      qualifications = None

    #* Benefits
    try:
      benefits = info.find('div', class_ = 'coinfp-benefits-panel').text
    except:
      benefits = None

    #* Description
    #description = info.find('div', class_ = 'jobsearch-jobDescriptionText')
    description = str(info.find('div', class_ ='jobsearch-jobDescriptionText').text).strip().replace('\n', '')

    #* Apply link is 'url'

    currentJob = {
      'jobTitle': jobTitle,
      'companyName': companyName,
      'detailsSection': detailsSection,
      'qualifications': qualifications,
      'benefits': benefits,
      'description': description,
      'url': url
    }
    jobs.append(currentJob)
  return jobs

jobList = getJobs(getJobKeys())
[print(item) for item in jobList]