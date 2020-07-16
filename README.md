# Cover Letter Analysis
Analyzing the content of resumes and cover letters to match job descriptions of job titles and job categories. The purpose of this product is to provide guidance to people looking for a new job, or a career-change.

The user will upload a document (resume or cover letter). Apache Tika is used to extract text data from the document, which is then passed through the RAKE algorithm to determine keywords and phrases. These keywords and phrases are treated as a bag of words, which are vectorized, and a similarity matrix is created with job descriptions taken from job listings from 30 different job categories from each of the 50 states. The 30 job categories, as defined by Google are:

* Accounting & Finance                                                      
* Admin & Office                                                            
* Advertising & Marketing                                                     
* Animal Care                                                              
* Art, Fashion & Design                                                       
* Business Operations                                                                             
* Cleaning & Facilities
* Computer IT  
* Construction 
* Customer Service
* Education 
* Energy & Mining
* Entertainment & Travel 
* Farming & Outdoors
* Healthcare
* Human Resources
* Installation, Maintenance & Repair 
* Legal 
* Management 
* Manufacturing & Warehouse
* Media, Communication & Writing
* Personal Care & Services 
* Protective Services
* Real Estate  
* Restaurant & Hospitality
* Sales & Retail
* Science & Engineering
* Social Services & NonProfit
* Sports Fitness & Recreation
* Transportation & Logistics

## Future Features          

- [ ] Deploy interactive website
- [ ] Develop summary visualizations
- [ ] Develop deep learning method of implementation
- [ ] Teach computer how to interpret and understand resume text data
