# Cover_Letter_Analysis
Analyzing the content of resumes and cover letters to match job descriptions of job titles and job categories. The purpose of this product is to provide guidance to people looking for a new job, or a career-change.

The user will upload a document (resume or cover letter). Apache Tika is used to extract text data from the document, which is then passed through the RAKE algorithm to determine keywords and phrases. These keywords and phrases are treated as a bag of words, which are vectorized, and a similarity matrix is created with job descriptions taken from job listings from 30 different job categories from each of the 50 states. The 30 job categories, as defined by Google are:

* Accounting & Finance      * Cleaning & Facilities   * Entertainment & Travel                   * Management                            * Restaurant & Hospitality
* Admin & Office            * Computer IT             * Farming & Outdoors                       * Manufacturing & Warehouse             * Sales & Retail 
* Advertising & Marketing   * Construction            * Healthcare                               * Media, Communication & Writing        * Science & Engineering
* Animal Care               * Customer Service        * Human Resources                          * Personal Care & Services              * Social Services & NonProfit
* Art, Fashion & Design     * Education               * Installation, Maintenance & Repair       * Protective Services                   * Sports Fitness & Recreation           
* Business Operations       * Energy & Mining         * Legal                                    * Real Estate                           * Transportation & Logistics 

The similarity matrix is used to find the top matching job descriptions.                                                                          
                                                       
