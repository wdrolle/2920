Financial Crimes Enforcement Network Section 314(a) Policy 
Collections; Customer Service; Transaction Services 
Policy Owner: iCreditWorks 
Servicing Agent: Total Card, Inc. 
Product: iCreditWorks
BIN:   
GENERAL
The term "section 314(a)" refers to section 314(a) of the law Uniting and Strengthening America by Providing 
Appropriate Tools Required to Intercept and Obstruct Terrorism (USA Patriot Act) Act of 2001 Public Law 107-
1. iCreditWorks provides the 314(a) subject list to TCI every 2 weeks.  Upon review of the files, TCI conducts a one-
time search of its records to identify accounts of a named suspect.  The list is compared to the master file and TCI's 
internal purged accounts database to match social security number (SSN)/employer identification number (EIN), then 
name and/or address. 
TCI completes their search on all subjects listed in the 314(a) request and responds by email to iCreditWorks.  
A log is maintained with the date the request was received, the date the review was complete, if a match was found, the 
number of matches found, if the account was blocked, and the representative's name that worked the report and the 
resolution if any.  Under no circumstances is the customer to be informed that they are on the FinCEN list.  If the 
customer specifically asks if they are on the FinCEN list, you may tell them to contact FinCEN at 703-905-3770.
If TCI knows, suspects, or has reason to suspect that a customer may be linked to terrorist activity against the United 
States, TCI immediately notifies iCreditWorks.  A Suspicious Activity Narrative is filed within 10 days. 
A financial institution may only use the information to report the required information to FinCEN, to determine whether 
to establish or maintain an account or engage in a transaction, or to assist in BSA/AML compliance.  While the section 
314(a) list could be used to determine whether to establish or maintain an account, FinCEN strongly discourages financial 
institutions from using this as the sole factor in reaching a decision to do so unless the request specifically states 
otherwise.  Unlike the OFAC lists, section 314(a) lists are not permanent "watch lists."  In fact, section 314(a) lists 
generally relate to one-time inquiries and are not updated or corrected if an investigation is dropped, a prosecution is 
declined, or a subject is exonerated.  Further, the names do not correspond to convicted or indicted persons; rather a 314
(a) subject need only be "reasonably suspected" based on credible evidence of engaging in terrorist acts or money 
laundering.  Moreover, FinCEN advises that inclusion on a section 314(a) list should not be the sole factor used to 
determine whether to file a Suspicious Activity Report (SAR).  Financial institutions should establish a process for 
determining when and if a SAR should be filed.
Version Revised By Brief Summary of Changes Revision Date
1 Paul Fretham New Policy 5/6/19
Last Annual Review Completed by   on   
Next Review Date: 6/1/2020 
Fraud Prevention Procedures























Purpose and Scope
Purpose 
These procedures govern fraud prevention for iCreditWorks Mobile Platform at the Applicant, Device and Documentation level. This comprehensive approach covers verification of the user’s mobile phone number, device, IP address, email address, in addition to CIP, OFAC and income verification.
Scope
These procedures apply to all users of the iCreditWorks Mobile Platform during the application and servicing process.
Related Documents
These Procedures supplement and should be read in conjunction with iCreditWorks’ Credit Policy, Credit Standard Operating Procedures, Servicing Procedures Overview, Customer Identification Program Procedures, User Identification Procedures and the Identity Theft and Red Flags Procedures.
Definitions
Applicant:  A consumer who is seeking a loan under the iCreditWorks loan program as primary borrower or co-borrower and, as such, whose name appears on the credit application and whose income and credit history are used to qualify for a loan. 
iCreditWorks Mobile Platform: The consumer-facing iCreditWorks mobile interface used to facilitate the credit application process and, once the loan is funded, loan payments, inquiries and other administrative activities during the life of the loan.
Device ID:  A unique identifying ID with which a mobile device can be identified uniquely across the globe.
IP Address:  An Internet Protocol address (IP address) is a numerical label assigned to a User’s mobile phone.
Identity:  Identification of a user using a govt issued valid ID like driver’s license or passport.
User: An individual who registers as a user of the iCreditWorks Mobile Platform, including Applicants and Other Registered Users.
Other Registered User: An individual, other than the borrower or co-borrower, who registers to use the iCreditWorks Mobile Platform after a loan is funded. Other Registered Users include users authorized to access a loan account by the borrower (i.e., an authorized user), power of attorney holders, or third parties alleging fraud.
procedures
Any individual seeking to use the iCreditWorks Mobile Platform must download the app to their mobile phone and enter their mobile phone number. Fraud Procedures are performed on the User (Applicant or Borrower), Device (mobile device used) and Documentation uploaded by the user as following:
Process:
Device data elements are collected from the user’s device through a TransUnion (TU) SDK (software development kit) once the User downloads the iCW App
Identity and income data elements are entered by the user on the first screen: Name, DOB (date of birth), SSN, Address, Income, Mobile Phone Number
iCW connects with TU services (iovation/ID Vision) to verify all data elements collected from the user and user’s device. If there are discrepancies in the information collected or indications that the user or device have been involved in fraudulent activity, the user is asked to upload Government issued ID and/or other documentation and additional checks are performed:
Government ID is authenticated by Lexis Nexis and the information extracted from the document is cross referenced
Knowledge Based Authentication (KBA) is initiated by Lexis Nexis if the ID verification process is not satisfactory
Other documentation is authenticated as described in this document and related documents and the information extracted is cross referenced against information obtained from other sources
iCW also connects with TU to obtain a credit report and other underwriting information to validate the identity and income of user. If there are discrepancies with respect to CIP or income, the user is asked to upload documentation and additional checks are performed as described in this document and related documents
iCW performs an OFAC check based on information received from TU (IDVision)
iCW asks pre-approved applicants to register in order to finalize the approval and users need to provide a valid email address that is verified during the process   
As part of the registration process, iCW asks users to take a selfie using the tool embedded in the iCW app, and then uses Lexis Nexis to match the selfie to the photo in the ID by doing a multipoint biometric verification
If the user selects not to provide a selfie, then KBA is initiated using Lexis Nexis
To complete the loan approval process, iCW asks the dental partners to validate that the user is the patient they treat, based on either the selfie or a picture extracted from their Government ID, and that the amount requested is aligned with the required payment for the treatment
The dental provider is asked to confirm the beginning or completion of treatment before the loan amount is disbursed to the dental provider. The user is notified when the dental provider confirms that treatment was initiated or completed
If the user selects AutoPay, when the user connects his/her account we confirm that the user is owner or part-owner of that account
User verification procedures are automatically performed when an individual attempts to register as a User or when a registered User attempts to change this information in their User Profile. These procedures are described in the User Identification Procedures. If a discrepancy is identified, the User is prevented from proceeding with the registration process or the user profile change.
For Documents verification, procedures combine algorithmic checks with reviews conducted by fraud specialists and are performed by iCW and its partners: Ocrolus and LSI. They include:
Image Alteration Detection that automatically recognizes photoshopped and fabricated documents
Data Tampering Detection that leverages document metadata and harnesses fraud specialists and a business intelligence network with hundreds of other financial services that collaborate to stop bad actors and get ahead of the latest methods used by fraudsters
KBA Authentication
This configuration helps confirm a subject's identity by generating knowledge-based authentication questions that typically only an identity owner would know. In addition, authentication can dynamically adapt the difficulty level of a quiz based on certain high-risk events or business rules, as well as automatically adjust for minor input errors, name variations, and inconsistencies in public data. 
Email Risk Assessment
This configuration analyzes the subject's input email address for fraud risk. 
ID Verification
This configuration recognizes and validates government-issued IDs. The service captures the data from base64-encoded images of the ID, analyzes the graphic security elements for accuracy, and delivers the authentication results. 
Verification of Income
Verification of income is completed by comparing the stated income to an income estimate model provided by TransUnion’s “Credit Vision Income Estimator” (CVIE). If the stated income is no more than 125% of the CVIE income, or it is less than the CVIE income, the stated income will be used to calculate a debt to income ratio without any additional requests for supporting documentation.  If the stated income is more than 125% of the estimated income and if the applicant does not qualify for the loan using the lower estimated income from TransUnion, Company requests the applicant to provide proof of income using paystubs, w-2s or tax returns. If Company is unable to verify income, the loan will be declined, and an adverse action will be given within 30 days of the application.
IDVision

TransUnion’s IDVision Alerts facilitates compliance with sections of the Red Flags and Know-Your-Customer regulations and reduces fraud exposure by pinpointing identity and identity element misuse that may lead to payment defaults, chargeoffs and fraud-related costs. These TransUnion solutions can help detect true name and synthetic fraud, application velocity, identity relational and behavioral anomalies, SSNs belonging to deceased persons or minors,
consumer statements on credit files, identity verification issues, Social Security Number issuance and misuse, address misuse, etc. Alerts returned are based on the input and/or file-based identity elements. For launch, iCW will use the best-practice settings available for this solution, and, after launch, will configure each alert individually to help meet specific fraud, compliance and identity verification strategies based on real data. There are eighty-one (81) alerts available in the IDVision solution. The alerts are based on the consumer identity element (Social Security number, address, and telephone number) and subject matter content (consumer alerts and product status). For each alert, a risk level is provided based on industry best practices to assist in determining the associated risk as well as potential follow-up strategies. The risk levels are categorized as Red, Amber or Green, depending on the number and level (high/medium/low) of alerts.

Other Verifications
This configuration can help confirm the accuracy of subject-provided identity information (for example, name, address, phone, and DOB (date of birth). Verification checks whether the data about the subject matches the data that is collected from public records and other data sources. Verification can also identify potentially high-risk situations (for example, PO Box addresses or an SSN that is associated to a deceased person).

Roles and Responsibilities



Customer Identification Program Procedures
Effective Date: July 22, 2020




OVERVIEW
iCreditWorks’ (alternatively referred to as “iCW” or “Company”) Customer Identification Program (CIP) is a fundamental control in preventing the Company from becoming involved in money laundering, terrorist financing, or sanctions violations. As such, these CIP Procedures describe:
Identifying information that is obtained from every customer opening a new account
Technology utilized to verify identifying information provided by a customer in the course of opening an iCW account
Actions taken by iCW in the event that the Company is unable to form a reasonable belief that it knows the true identity of a customer
Records created and maintained by iCW with respect to its CIP
Government lists utilized at onboarding
Customer notice of iCW’s efforts to collect and maintain records related to the CIP

Scope
These Procedures govern all aspects of iCW’s CIP, and they are applicable to all personnel at iCW, including both employees and consultants. It is also applicable to all third parties with whom iCW has business arrangements for ongoing operational activities. Third parties include, but are not limited to, dental office partnerships, bank partnerships, and service providers.

Related Documents and governing law
Policies and Procedures:
BSA/AML and OFAC Policy
Compliance Management System Policy
Watchlist Screening Procedures
Data Handling and Retention Policy

Governing Law:
31 CFR § 1020.220

CUSTOMER INFORMATION REQUIRED

iCW’s CIP is fundamental in preventing the Company from becoming involved in money laundering, terrorist financing, or sanctions violations. In the course of onboarding a customer, iCW collects the following data: 


The Company will never open an account for customers who:
Are corporations or other entities;
Give only a Post Office Box as an address;
Give a foreign address;
Do not provide each of the required pieces of information described above;

IDENTITY VERIFICATION

iCW primarily employs non-documentary methodologies for verifying identifying details input by loan applicants, which consists of comparing applicant data with information obtained via a consumer reporting agency (TransUnion).

TransUnion specifically evaluates identity verification risk via analyzing applicant inputs (first name, last name, address, SSN, and date of birth) against multiple data sources and produces an output risk score for each applicant (pass, flag, or fail).

If an applicant’s TransUnion risk output is  “pass”, no serious identification red flags were uncovered, and the application will continue along a standard underwriting and processing path.

If an applicant’s risk output is “flag” based on a CIP-relevant datapoint, they will be asked to provide an answer to a knowledge-based authentication (KBA) question and prompted for additional verification documents to remediate the specific flag condition(s). The only instance in which a KBA alone may serve to verify a portion of the applicant’s identity are for instances when the specific flag condition generated is regarding the applicant’s address. All other flag conditions (name, SSN, and DOB) must be remedied with documentary evidence. If the additional verification is not received or does not validate the flag condition, the customer must be declined. The table below lists acceptable documents to remediate specific flag conditions.

*Document must be dated within 60 days of the application date. 

Finally, TransUnion may have a risk output of “fail”. In this instance, the loan application cannot proceed until the applicant remediates the matter directly with the credit bureau.

The nature of a mobile lending platform is such that applicants will not appear in person in a traditional brick and mortar financial institution. Due to this, applicants are also required to upload either a driver’s license, state ID, Military ID, or Passport into the App. The photo identification provided is then matched to the individual making the loan application either by utilizing facial recognition software via a “selfie” or by prompting them to correctly answer a KBA question. If the applicant has previously correctly answered a KBA question, the photo identification will be accepted without the need to do so again.

If the applicant is unable to pass verification, iCW will not form a customer relationship with the applicant. 

RECORDKEEPING

iCW retains all CIP information for a minimum five (5) years after the date the account was closed, in a manner consistent with the iCW Data Handling and Retention Policy. CIP records are retained on a secure Amazon Webservice database (Database).

Information retained in the Database must include – 
Customer name; date of birth; and physical address
Customer SSN
Whether the photo identification produced is a passport, military ID or state driver’s license/state ID
Whether the customer has opted to utilize the facial and vocal recognition features of the application (a description of non-documentary methods used to verify the identity of a customer)
If applicable, a description of the resolution of any substantive discrepancy discovered when verifying identifying information

COMPARISON WITH GOVERNMENT LISTS

The Office of Foreign Assets Control (OFAC) requires that all persons and entities in the United States block of freeze property, payment of any funds, transfers, and transactions with anyone on OFAC watchlists. Accordingly, iCW will not fund an account until further investigations reveals that the “hit” on the list is not a legitimate match.

To comply with this requirement at onboarding, iCW utilizes TransUnion’s OFAC Name Screen service, which screens consumer information against the following watchlists:

Specially Designated Nationals (SDN)
Specially Designated Terrorist (SDT)
Specially Designated Kingpins (SDNTK)
Foreign Sanctions Evaders (FSE)
Foreign Terrorist Organization (FTO)
Palestinian Legislative Council (PLC)
Specially Designated Narcotics Traffickers (SDNT)
Specially Designated Global Terrorist (SDGT)

TransUnion compares consumer name and date of birth against the aforementioned watchlists for potential matches and generates OFAC alerts if there is an 85 percent degree of matching or greater. 
What this means is that the matching logic utilized by TransUnion will detect certain misspellings or other incorrectly entered text, and will return near, or proximate matches. This 85 percent threshold is also referred to as a minimum name score.

Due Diligence: Given that the minimum name score is placed at 85, if TransUnion’s software detects a possible match, TransUnion will place an OFAC alert on the credit report and remit to Lending Solutions, Inc. (LSI) to determine whether it is a legitimate match.

LSI will either disposition a TransUnion OFAC alert as a “true match” or a “false positive” by manually checking the information contained within an OFAC list against information provided by the applicant. Regardless of the outcome, all OFAC alerts dispositioned by LSI must be shared with iCW immediately upon receipt and disposition.

In the event that LSI deems the match legitimate, the BSA/AML Manager (or a designee) at iCW will perform further due diligence using LexisNexis and information obtained via iCW’s Customer Identification Program (CIP). If the BSA/AML Manager believes that the individual is on an OFAC list, they must inform WebBank via Salesforce within one (1) business day of receiving the LSI disposition.

iCW will investigate all details surrounding the attempt to acquire a loan to ascertain if a Suspicious Activity Report is also required in accordance with the Suspicious Activity and Reporting Procedures

Instances of legitimate list matches are retained for five (5) years for audit and regulatory purposes.

CUSTOMER NOTICE

The following notice regarding CIP is embedded with the iCW application, which is available for customer review prior to officially opening an account:

In accordance with Section 326 of the USA PATRIOT Act signed October 26, 2001, all financial institutions are mandated to implement a Customer Identification Program (CIP) as a tool to protect the U.S. financial system from money laundering, terrorist financing, identity theft and other forms of fraud. iCreditWorks is required to: *Obtain customer identifying information from each customer prior to account opening and in identifying signatory individuals added to an existing or new account. *Maintain records of the information used to verify the person’s identity including name, address and other identifying means. In all cases protection of our customer’s identity and confidentiality is iCreditWorks pledge to you. We proudly support all efforts to protect and maintain the security of our customers and our country.

TESTING PROCEDURES AND CONTROLS

Independent testing: Annually, iCW will support WebBank to secure the services of an independent third party with credible industry experience to test its CIP procedures and controls at least once every calendar year as part of the iCW’s overall obligation to engage an independent party to audit its overall compliance program.

The independent testing report will include the name or qualifications of the independent auditor; objective and scope of the review; procedures performed, and transaction testing completed; and findings or recommendations identified including management’s response.  Any violations, policy or procedure exceptions, or other deficiencies and recommendations noted during the review will be reported in a timely manner to the iCW Board. The Board, through the Chief Compliance Officer, will track audit report findings and implement and document corrective actions.

Internal Review: At least once a year, iCW will provide a report to WebBank on the overall effectiveness of its Customer Identification Program. The report provided to the Bank by iCW will contain a write-up covering: 
The effectiveness of these Procedures in assessing customer identity;
Service provider arrangements;
Significant breaches of procedure and management response; and
Recommendations for needed changes in the Customer Identification Program.

ROLES AND RESPONSIBILITIES

Chief Compliance Officer:
Oversee and provide guidance to the overall administration to the CIP
Review and approve changes to the CIP Procedures

BSA/AML Manager:
Updates the CIP Procedures
Dispositioning alerts from relevant government lists (ascertains whether an alert or match is legitimate)

dOCUMENT mANAGEMENT

iCW will maintain the Procedures and supporting documentations in accordance with the iCW Data Handling and Retention Policy. iCW will ensure all employees understand their obligations in retaining documents and are aware of the processes for retention and disposal of records.


 
 
 
 
 
Transaction Monitoring and 
Investigations  Policy  
 
 
 
 
 
 
 
 
 
 
 
 
Date Issued  9th November 2017  
Issue Number  2.0 
Review Date  Annually  
Published on  Policies and Procedures Jam page  
 
Paysafe Internal  – for Paysafe internal use only  
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 2 
 Copyright © Paysafe Group   
 
All rights reserved. This document and the information it contains, or may be extracted from it, is subject to the terms 
and conditions of the agreement or contract under which the document was supplied to the recipient’s organisation.  
 
None of the info rmation contained in this document shall be disclosed outside of the recipient’s own organisation without 
prior written  permission of Paysafe Group , unless the terms of such agreement express ly allow.  
In the event of a conflict between this docume nt and a relevant law or regulation, the relevant law or regulation shall 
be followed. If the document creates a higher obligation, it shall be followed as long as this also achieves full 
compliance with the law or regulation.  
 
Use of language  
 
Throughout this document, the words ‘ may’ , ‘should’  and ‘ must ’ when used in the context  of actions of Paysafe Group  
or others, have specific meanings as follows:  
 
(a) ‘May’  is used where alternatives are equally acceptable.  
(b) ‘Should’  is used where a provision is preferred.  
(c) ‘Must ’ is used where a provision is mandatory.  
 
Note that alternative or preferred requirements may b e qualified by Paysafe Group  in another referenced document.  
 
Paysafe Group and the companies in which it d irectly or indirectly owns investments are separate and distinct entities. 
In this publication, however, the collective expression ‘ Paysafe ’ and ‘ Paysafe  Group ’ may be used for convenience where 
reference is made in general to those companies. Likewise, the words ‘ we’, ‘us’, ‘our’ and ‘ ourselves’  are used in some 
places to refer to the companies of the Paysafe Group in general. These expressions are also used whe re no useful 
purpose is served by identifying any particular company or companies.   
 
In this document, third party  means any individual or organisation you come into contact with during the course of your 
work for us, and includes actual and potential clie nts, customers, suppliers, distributors, business contacts, agents, 
advisers, and government and public bodies, including their advisors, representatives and officials, politicians and 
political parties.  
 
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 3 
 
 
 
 
 
Document Approval  
 
Date approved  Approved by  Signed by  Signature  
 
9th November 2017   
Elliott Wiseman  
General Counsel  and 
Chief Compliance 
Officer  
  
Maximilian von Both  
Senior Vice President, 
Compliance   
 
 
 
 
 
 
 
 
 
 Summary : 
The purp ose of this Compliance Policy  is to set out the  process relating to ongoing transaction monitoring and 
investigation and act as a reference to enable to make accurate decisions.  
 
Supporting Policy  
Global Compliance Policy  Review and maintenance  
This Policy  will be reviewed and maintained by the Head of Policy and Assurance at least  on an annual basis. The 
provisions of this policy  can be amended and supplemented from time to time by the Senior Vice President,  
Compliance .  
 
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 4 
TABLE OF CONTENTS  
 
1. INTRODUCTION  5 
1. WHO DOES THIS POLICY  APPLY TO?  6 
1. PAYSAFE’S APPROACH T O TRANSACTION MONITO RING  6 
1. ONGOING TRANSACTION MONITORING  8 
4.1. Review and update of Paysafe money laundering and terrorist financing 
typologies  9 
4.2. Review and update of automatic systems rules  10 
4.3. Information Sources  10 
1. INVESTIGATIONS  11 
5.1. When do we carry out investigations?  12 
5.2. AML/CTF initial investigation  12 
5.3. Compliance Department investigation  12 
1. COMPLIANCE SPOT CHEC KS 13 
6.1. Compliance reports to the responsible MLRO  14 
1. HOW WE HANDLE AND RE TAIN THE RECORDS OF ALL CHECKS CARRIED OUT 
BY US  14 
 
 
 
 
 
 
 
 
  
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 5 
1. Introduction  
 
It is Paysafe’s policy to conduct all of our business in an honest and 
ethical manner.  
The purp ose of this Compliance Policy  is to clearly set out the :  
• essential transaction monitoring of threats and patterns by 
Paysafe to prevent money laundering and terrorist financing 
and to detect suspicious transactions ; and  
 
• processes to be followed when transaction moni toring  systems  
detect  potentially suspicious activity.  
This Compliance Policy  must be followed unless there are exceptional 
circumstances justifying a variation.  
If an employee consider s that this Compliance Policy  is not applicable 
for an activity covered within the scope of this document, the 
individual must seek permission from the responsible MLRO or their 
approved delegate before deviating from this Complia nce Policy . 
A failure to follow this Compliance Policy could severely harm 
Paysafe’s reputation, financial standing and possibly breach the terms 
of the licences necessary to operate our business. Any such failure may 
result in disciplinary action or termination for any employee found to 
have breached this Com pliance Policy  and may constitute a criminal 
offence.  
This Compliance Policy  supersedes all previous group policies setting 
group policy regarding  transaction m onitoring and investigations  and 
is supplemented by the Transaction Monitoring and Investigations 
Guidance  Notes . It shou ld be read together with the :  
• Paysafe Code ;  
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 6 
• Global Compliance Policy ; 
• Customer Due Diligence  Policy ;  
• Merchant and Distributor Due Diligence  Policy ; and  
• Escalation and SAR Policy . 
This Compliance Policy  primarily focuses on European regulations, and 
sets a minimum group -wide standard, based on the strictest law within 
the EU. If specific local regulations, outside of the EU, require higher 
standards or stricter provisions, the local entity will always co mply 
with such local regulations. Less strict rules will only be implemented 
if they have a clear legal basis, are accepted by local supervisory 
authorities (where appropriate), and are approved by the  responsible  
MLRO.  
A glossary of defined terms is inclu ded at section 8 of this Compliance 
Policy . 
 
 
1. Who does this Policy  apply to?  
 
This Compliance Policy  applies to all Paysafe employees.  
1. Paysafe ’s approach to  transaction monitoring  
 
Paysafe is committed to:  
• establishing processes  and controls so that we can monitor our Where can I find further information?  
 
Further explanation of the detailed business processes descri bed in 
this Compliance Policy  can be found in the supporting Transaction 
Monitoring and Investigations Guidance  Notes . 
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 7 
user accounts (customers, merchants and distributors) and 
transactions on an on -going basis;  
 
• having clearly documented processes which are easily 
accessible and understood by our employees;  
 
• having documented service levels in place with any third party 
service providers who provide ongoing transaction monitoring  
services and monitoring performance against these 
agreements;  
 
• ensu ring that our staff are trained  on their responsibilities and 
can carry out their role effectively;  
 
• carrying out o ngoing monitoring, audits and reviews to confirm 
that our processes are effective and comply with applicable law 
and that senior management are regularly updated on the 
findings of these reviews.  
This Compliance  Policy  applies to the ongoing transaction monitoring 
of users (customers, merchants and distributors) for all Paysafe 
businesses and is split into the following areas:  
• Ongoing transaction monitoring;  
 
• Investigations;  
 
• Compliance spot checks; and 
 
• Document and data retention.  
 
 
 
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 8 
1. Ongoing Transaction Monitoring  
 
Paysafe monitor s all transactions (by customers, merchants and 
distributors) on an on -going basis  using  a risk -based approach. The 
intensity of our monitoring  depend s on the level and nat ure of the 
risks identified by Group Compliance . Where a higher risk of money 
laundering or terrorist financing is detected a more enhanced and 
focused approach is used and stricter thresholds and measures are 
implemented.  
 
Paysafe’s  transaction monitoring systems can detect suspicious 
activity based on money laundering and terrorist financing typologies 
and indicators. Based on our risk assessment of products, users, 
countries and delivery channels, we have identified potential high risks 
for Paysafe which we mitigate through stringent transaction 
monitoring.  
 
Our monitoring processes consist of  ongoing transaction monitoring 
through both assurance checks and automated transaction monitoring 
using rules that reflect our experience of  potentially suspicious 
transactions by:  
 
• use of our known  money laundering, terrorist financing and 
other illegal activity typologies (see Escalation and SAR Policy ); 
 
• identify ing discrepancies between submitted and detected data 
(for example th e IP addre sses used and the user’s country or 
origin);  
 
• cross referencing  submitted data against that for other accounts 
(for example credit cards used by multiple holders);  and  
 
• use of  systems that interface with third party sources to detect 
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 9 
criminal activities . 
 
If you identify  potentially suspicious behavior, you must  follow the 
process set out in Escalation and SAR Policy  to determine if any 
Internal SAR must  be made . 
 
We monitor transactions both in real time (i.e. when  a tra nsaction is 
about to take place)  as well as after the event, when  the transaction 
has already been executed. For this purpose Paysafe has defined 
several thresholds and rules and implemented automated reports with 
predefined criteria.  
 
As such, our transaction monitoring processes are desi gned to detect  
suspicious activities based on money laundering and terrorist financing 
typologies and indicators. The implemented thresholds, rules and 
reports are also based on the Compliance Department’s r isk 
assessment.  
 
4.1. Review and update of Paysafe mon ey laundering and 
terrorist financing typologies  
The Compliance  Department is responsible for ensuring that 
the money laundering, terrorist financing or other illegal 
activity typologies that relate to Paysafe products  are 
updated to reflect our ongoing experience.  
 
As such, the Compliance Department must  confirm to the 
responsible MLRO each quarter  that the:  
 
• typologies being used to identify potentially suspicious 
activity are current  and standardized across our 
busin esses to the extent appropriate given our risk 
assessment ;  
 
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 10 
• these typologies are reflected in our systems’ rules.  
 
Further information on these typologies is set out in 
Escalation  and SAR  Policy . 
4.2. Review and update of automatic systems rules  
Monitoring must  include a review of any applicable systems  
rules to ensure  that: 
 
• the rules remain relevant  and current ; 
 
• new rules are incorporated into the system promptly 
and effectively ; 
 
• the rules are correctly applied ; and 
 
• our system s are operating effectively.  
 
In addition, t he output of alerts from the systems  must  be 
sample checked on a quarterly  basis to ensure that the 
triaging of alerts is conducted in line with the set parameters.  
 
 
4.3. Information Sources   
Paysafe uses the following information sources to detect 
high -risk behavior : 
 
• Data Warehouse (DWH) – data source which 
aggregates a multitude of transactional and master 
data collected from Paysafe’s operations.  
 
• ThreatMetrix – data source which is an integrated 
online platform used for rule definitions on risk scoring 
of paysafecard  individual transactions and the review 
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 11 
of the monitored transactions.  
 
• Actimize  – an automated platform used for rule 
definition s on risk scoring of Neteller’s individual 
transaction s and the review of monitored  
transaction s. 
 
• Accertify  – an integrated online platform used for rule 
definitions on risk scoring of Skrill’s individual 
transactions and the review of the monitored 
transactions.  
 
• Jade, paysafecard and Skrill  Admin web interface – 
data source with account and registration information 
of customers  
 
• YUNA Customer Care web interface – internal data 
source with account and registration information of 
YUNA customers . 
 
• Salesforce – online platform for case managemen t and 
administration of customers , merchants, distributors, 
and investigations (including police inquiries and 
complaints) with regard to the Paysafe products.  
 
• LexisNexis Bridger Insight XG (BIXG) – hosted platform 
allowing access to watchlists  for sanctions and PEP 
screening, as well as custom watchlists for high -risk or 
blacklisted individuals.  
 
An analyst may also use publicly  available information for 
further checks  (e.g. web searches)  
 
1. Investigations  
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 12 
 
As part of our transaction monitoring processes, Paysafe is committed 
to having effective and transparent procedures for the accurate and 
prompt investigation of suspicious activities.  
 
 
5.1. When do we carry out investigations?  
An investigation into a user must  be carried out by the 
Compliance Department when:  
 
• an employee has escalated the matter following 
concerns they may have relating to the user’s activ ity; 
or 
 
• when Paysafe’s automatic systems generate an alert 
warning of potentially suspicious activity.  
5.2. AML/CTF initial investigation  
AML /CTF  cases are only referred to the Compliance  
Department  after  a thorough initial investigation by the 
relevant business.   
 
The referral must  contain full details of the investigation 
conducted using  the template provided by the Compliance  
Department . 
 
 
5.3. Compliance Department investigation  Where can I find further information?  
o Further information is set out in the  Escalation and SAR 
Policy . 
 
 
 
 
 
 
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 13 
AML /CTF  cases referred  to the Compliance Department  will 
be examined to detect any suspicious activity , following the 
procedures set out in the   Escalation and SAR Policy . 
 
 
 
 
 
 
 
 
 
 
1. Compliance spot checks  
 
As set out in the Global Compliance Policy , the responsible  MLRO s are 
responsible for the  design and implement ation of  systems and 
controls necessary to mitigate the money laundering and the financing 
of terrorism  risks  presented by our businesses.  
 
On behalf of Paysafe’s MLROs, the P olicy and Assurance Team has 
established risk -based internal compliance controls to ensur e 
compliance of business processes with policies and guidelines.  This 
includes the periodic spot checks of the following processes : 
 
• Transaction Monitoring ; 
 
• Customer Due Diligence ; 
 
• Merchant and Distributor  Due Diligence ; 
 
• Training and Awareness ; 
 
•  SAR Reporting ; 
 Where can I find further information?  
 
Further explanation of the investigative steps to be 
followed can be found in the  Escalation and SAR Policy . 
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 14 
• PEP and Sanction checks ; 
 
• Policies and Procedures;  
 
• Management Information ; 
 
• External Reporting & RFI s; 
 
• Customer Complaints & Police Requests ; 
 
• Risk Assessment (e.g. Risk Matrix and Country Blacklist) ; 
 
• Conduct (ABC, Gifts, Whistleblowing) . 
 
Checks are carried out on a risk assessed based - monthly, quarterly or 
yearly basis depending on the topic and the risks.  
6.1. Compliance reports to the responsible MLRO  
The Policy and Assurance team will report  monthly  to the responsible 
MLRO (or on an as needed basis):  
 
• Number of spot checks  
• Topics covered  
• Overview of all checks performed  
• Findings of the spot checks  
• Measures taken or Recommendations  
 
The responsible MRLO will then summarize the findings in his/her 
regular reporting to senior management . 
 
1. How we handle and retain the records of all checks carried out by us  
Transaction Monitoring and Investigation s Policy  
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERN AL 
 15 
 
All documents, data and other information will be kept a nd held in 
accordance with the Record  Retention Policy . 
 
The contents of all checks and investigations must  remain confidential 
to the Compliance Department , the responsible MLRO and General 
Counsel.  
 
All action taken by the Compliance Department must  be recorded . 
 
 





















BankClient 
BSA/AML/OFAC
COMPLIANCE PROGRAM:
POLICIES, PROCEDURES, 
AND INTERNAL CONTROLS
BankClient



1. Introduction
BankClient (“BankClient”), headquartered in Santa Clara, California, provides cross-border, 
business payment services. In providing these services. BankClient engages in the following MSB 
activities: money transmittals and foreign exchange.
BankClient also maintains a branch office in Hong Kong:

1. Firm Policy
It is the policy of BankClient to prohibit and actively prevent money laundering and any activity that 
facilitates money laundering or the funding of terrorist or criminal activities by complying with 
all applicable requirements under the Bank Secrecy Act (BSA) and its implementing regulations.
Our anti-money laundering policies, procedures and internal controls (collectively, our "AML 
Program”) are reasonably designed to ensure compliance with all applicable BSA regulations 
and will be reviewed and updated on a regular basis to ensure appropriate policies, procedures 
and internal controls are in place to account for both changes in regulations and changes in our 
business.
Our AML Program shall be commensurate with the risks posed by the location and size of, as 
well as the nature and volume of, the financial services provided by our firm.
Our AML Program shall be kept in writing and approved by Board of Directors. We w ill make 
copies of our AML Program available for inspection to the Department of the Treasury upon 
request.
a. Company Services Description
BankClient offers cross-border payment solutions among the US, China and Europe. The 
company utilizes blockchain technology which includes integrating with cryptocurrency 
exchanges and build smart apps on blockchain. BankClient only deals with corporation clients, 
and prohibits any transactions with individuals.
b. BSA/AML and OFAC Requirements
In her June 12, 2014, Remarks, FinCEN Director BankClient gave this description 
of the BSA:
As you likely already know, the Bank Secrecy Act, or “BSA,” is the common name for a 
series of statutes and regulations that form this country’s anti-money laundering and 
countering the financing of terrorism laws. Nearly every country around the world has 
similar laws in place at this point. These laws are meant to protect the integrity of the 
financial system by leveraging the assistance of financial institutions to make it more
4

transparent and resilient to crime and security threats, and by providing information 
useful to law enforcement and others to combat such threats.
The USA PATRIOT Act (2001) and 31 CFR Chapter X (2011) are among the BSA’s more recent 
and prominent statutes and regulations. The USA PATRIOT Act is one of several statutes 
referenced by the title Bank Secrecy Act. 31 CFR Chapter X contains the organized codification 
of BSA regulations. (The BSA’s implementing regulations organized by financial industry.)
As defined in 31 CFR Part 1010.1 OO(ff), MSB activities include (with certain limitations): 
dealings in foreign exchange; check cashing services; issuance or sales of traveler’s checks or 
money orders; provision of prepaid access services; money transmittal services; certain activities 
of the U.S. Postal Service; and sales of prepaid access.
Regulations governing these activities are found in 31 CFR Part 1022, Rules for Money Services 
Businesses. These regulations are divided into four main sections:
1) Programs (§1022.210). An MSB's AML program must include policies, procedures, and 
internal controls for:
a. Verifying customer identities;
b. Filing reports;
c. Creating and retaining records;
d. Responding to law enforcement requests.
2) Report Filings. MSBs are required to file various reports with FinCEN. These filings 
include reports of suspicious activities (SARs), currency transaction reports (CTRs); 
MSB registration (MSBR);
3) Maintenance of Records; and
4) Information Sharing.
A Note about OFAC: As an office of the US Treasury Department, the Office of Foreign Assets 
Control (“OFAC”) administers and enforces economic and trade sanctions against targeted 
foreign countries, organizations, and individuals. OFAC imposes controls on transactions and 
freezes assets under US jurisdiction. While OFAC sanctions are not part of the BSA, OFAC 
screenings are often conducted in conjunction with a financial institution’s BSA-compliance 
activities.
c. Money Laundering Description
Money laundering is generally defined as engaging in acts designed to conceal or disguise the 
true origins of criminally derived proceeds so that the proceeds appear to have derived from 
legitimate origins or constitute legitimate assets. Generally, money laundering occurs in three 
stages. Cash first enters the financial system at the "placement" stage, where the cash generated 
from criminal activities is converted into monetary instruments, such as money orders or 
traveler's checks, or deposited into accounts at financial institutions. At the "layering" stage, the 
funds are transferred or moved into other accounts or other financial institutions to further 
separate the money from its criminal origin. At the "integration" stage, the funds are reintroduced 
into the economy and used to purchase legitimate assets or to fund other criminal activities or 
legitimate businesses.
5

Terrorist financing may not involve the proceeds of criminal conduct, but rather an attempt to 
conceal either the origin of the funds or their intended use, which could be for criminal purposes. 
Legitimate sources of funds are a key difference between terrorist financiers and traditional 
criminal organizations. In addition to charitable donations, legitimate sources include foreign 
government sponsors, business ownership and personal employment. Although the motivation 
differs between traditional money launderers and terrorist financiers, the actual methods used to 
fund terrorist operations can be the same as or similar to methods used by other criminals to 
launder funds. Funding for terrorist attacks does not always require large sums of money and the 
associated transactions may not be complex.
1. MSB Registration (31 CFR § 1022.380)
a. Registration
We are currently registered with FinCEN as an MSB. Our MSB registration number is 
1. b. Registration Records
We shall retain a copy of the filed MSB registration form and other supporting documentation at 
the following US address:
3300 Central Expy, STE B
Santa Clara, CA 95051
We shall retain these registration documents for a period of at least five years.
c. Registration Renewal
We shall renew our registration by the end (December 31) of the second calendar year following 
our initial registration and by December 31 of every second calendar year thereafter.
d. Events Requiring Re-registration
If any of the following events occurs during a registration period (more than 180 days before the 
next renewal date), we shall re-file a registration form with information different from that 
reported on the form originally filed:
Change in Ownership or Control under State Law. There has been a change in ownership or 
control of the MSB that requires the MSB to be re-registered under State law.
Transfer of Voting Power or Equity Interest. More than 10 percent of the voting power or equity 
interest of the MSB has been transferred (except MSBs that must report such transfer to the 
Securities and Exchange Commission);
6

Increase in the Number of Agents. The number of agents of the MSB has increased by more than 
50 percent.
To re-register, we shall complete and file an RMSB no later than 180 days after the date on which 
the triggering event occurred.
e. List of Agents
We do not have any agents at this time and it may not apply to our current state. If it applies in 
the future, we shall prepare and maintain a list of our agents. We shall update this list by January 
1 of each year. We shall make our list of agents available to FinCEN, as well as other appropriate 
law enforcement agencies, including the IRS, upon request. Our agent list shall include:
• Name: The name of the agent, including any trade names or doing-business-as names.
• Address: The address of the agent, including street address, city, state, and ZIP code.
• Type of Services: The type of MSB services the agent provides on our behalf.
• Gross Transaction Amount: A listing of the individual months in the 12 months 
preceding the date of the agent list in which the agent’s gross transaction amount, for 
financial products or services issued by our firm, exceeded $100,000.
• Depository Institution: Name and address of any depository institution at which the agent 
maintains a transaction account for any of the funds received in or for the MSB services 
the agent provides on our behalf.
• Year Became Agent: The year in which the agent first became our agent.
• Branches: The number of branches and sub-agents the agent has, if any.
1. Risk Management
We have identified our BSA/AML and OFAC risks regarding products & services, customers & 
entities, and geographic locations.
a. Product & Service Risks
Our own services and third party services that we rely on may fail due to internal or external 
reasons. Our mitigating methods will make sure the residual risk is under our tolerance.
b. Customer & Entity Risks
Our clients may intend to deceive us by identify' fraud or other activities. Our internal control 
methods and automated system will prevent such activities from happening at the earliest stage.
c. Geographic Location Risks
Our clients may show evidence that they are related to any high-risk locations or jurisdictions. 
Our enhanced due diligence will identify such relationships, and reject or terminate those clients’ 
accounts accordingly.
7

We provide a detailed risk analysis table in our risk assessment file.
1. Giving AML Information to Federal Law Enforcement
Agencies and Other Financial Institutions
a. FinCEN Requests under USA PATRIOT Act Section 314(a)
As of the latest update to these procedures, FinCEN did not make regular 314(a) requests of most 
MSBs. Should FinCEN ever make a 314(a) request of our firm, we shall implement the following 
policies and procedures:
Upon receiving an information request under 31 C.F.R. § 1010.520, we shall designate one 
person to be the point of contact regarding the request and to receive similar requests for 
information from FinCEN in the future. When requested by FinCEN, we shall provide FinCEN 
with the name, title, mailing address, e-mail address, telephone number, and facsimile number of 
such person, in such manner as FinCEN may prescribe. After providing FinCEN with this contact 
information, we shall promptly notify FinCEN of any changes to such information.
As required by 31 C.F.R. § 1010.520(a)(3), “upon receiving an information request from FinCEN 
under [§ 1010.520, we shall] expeditiously search [our] records to determine whether [we 
maintain] or [have] maintained any account for, or [have] engaged in any transaction with, each 
individual, entity, or organization named in FinCEN’s request/’ If we find a match, our AML 
Compliance Officer will report it to FinCEN via FinCEN’s Web-based 314(a) Secure Information 
Sharing System within 14 days or within the time requested by FinCEN in the request. If the 
search parameters differ from those mentioned above (for example, if FinCEN limits the search to 
a geographic location), our AML Compliance Officer will structure our search accordingly.
When we search our records but do not find a matching account or transaction, we will not reply 
to the 314(a) request. We will maintain documentation that we have performed the required 
search by printing a search self-verification document from FinCEN’s 314(a) Secure Information 
Sharing System evidencing that we have searched the 314(a) subject information against our 
records.
We will not disclose the fact that FinCEN has requested or obtained information from us, except 
to the extent necessary to comply with the information request. Our AML Compliance Officer 
will review, maintain and implement procedures to protect the security and confidentiality of 
requests from FinCEN similar to those procedures established to satisfy the requirements of 
Section 501 of the Gramm-Leach-Bliley Act with regard to the protection of customers’ 
nonpublic information.
We will direct any questions we have about the 314(a) request to the requesting federal law 
enforcement agency as designated in the request. Unless otherwise stated in the 314(a) request, 
we will not be required to treat the information request as continuing in nature, and we will not be 
required to treat the periodic 314(a) Requests as a government provided list of suspected terrorists 
for purposes of the customer identification and verification requirements.
8

b. Voluntary Information Sharing with Other Financial Institutions 
under USA PATRIOT Act, Section 314(b) (31 C.F.R. § 1010.540)
We may share information with other financial institutions regarding individuals, entities, 
organizations and countries for purposes of identifying and, where appropriate, reporting 
activities that we suspect may involve possible terrorist activity or money laundering. Before 
doing so, our AML Compliance Officer will ensure that the firm files with FinCEN an initial 
notice before any sharing occurs and annual notices thereafter. We will use the notice form found 
at FinCEN's Web site. Before we share information with another financial institution, we will 
take reasonable steps to verify that the other financial institution has submitted the requisite 
notice to FinCEN, either by obtaining confirmation from the financial institution or by consulting 
a list of such financial institutions that FinCEN will make available. We understand that this 
requirement applies even to financial institutions with which we are affiliated. As with non­
affiliated firms, we will also obtain the requisite notices from affiliates and follow all required 
procedures.
We will employ strict procedures both to ensure that only relevant information is shared and to 
protect the security and confidentiality of this information.
We also will employ procedures to ensure that any information received from another financial 
institution shall not be used for any purpose other than:
• identifying and, where appropriate, reporting on money laundering or terrorist activities;
• determining whether to establish or maintain an account, or to engage in a transaction; or
• assisting the financial institution in complying with performing such activities.
1. System of Internal Controls
a. Customer Identification Program (31 C.F.R. § 1022.210(d)
As a provider of cross-border, business payment services, BankClient will only deal with business 
entity customers. BankClient will not provide services to individual persons.
To satisfy the Customer Identification Program (“CIP”) requirements found in 31 C.F.R. § 
1022.210(d)(1) and § 1022.410, we shall collect and verify certain identifying information for 
each business entity who effects a covered transaction with our firm. We shall record customer 
identification information and the verification methods and results.
Covered Transactions
Following is a list of covered transaction activities in which our firm may engage:
• Foreign exchange.
• Money transmittals.
Required Customer Information
9

Before effecting any transaction, we will record the name, address and taxpayer identification 
number of the entity.
Verifying Information
To comply with the requirements of 1022.210(d)(1) and § 1022.410, we will use risk-based 
procedures to verify the identity of each customer. We may verify the customer's identity by 
reviewing a formal document, such as: certified articles of incorporation, a government-issued 
business license, or a financial statement. We may also use an online identity verification service 
such as Blockscore (https://blockscorc.com/), FacelD (https://faceid.com/), or Qi Cha Cha 
(http://www.qichacha.com/).
Recordkeeping
We will document our verification, including all identifying information provided by a customer, 
the methods used and results of verification, and the resolution of any discrepancies identified in 
the verification process. We will keep records containing a description of any document that we 
relied on to verify a customer’s identity, noting the type of document, any identification number 
contained in the document, the place of issuance, and if any, the date of issuance and expiration 
date. With respect to non-documentary verification, we will retain documents that describe the 
methods and the results of any measures we took to verify the identity of a customer. We will 
also keep records containing a description of the resolution of each substantive discrepancy 
discovered when verifying the identifying information obtained. We will retain records of all 
identification information for five years after the date on which the transaction was effected; we 
will retain records made about verification of the customer's identity for five years after the 
record is made.
b. Know Your Merchant
Before providing any money transmittal or foreign exchange services to a business entity, 
BankClient will verify the legitimacy of the entity. As described above, verification will be 
performed through our use of an online identity verification system. We shall perform such 
verification actions to enable us to form a reasonable belief that we know the true identity of each 
business entity customer.
c. Enhanced Customer Due Diligence
For accounts we have deemed to be high risk using our risk score table and other methodologies, 
we will conduct enhanced due diligence, and obtain including but not limited to the following 
information:
• The source of funds;
• The beneficial owners of the business;
• The customers' clients list;
• Financial statements and banking references;
• Contracts or other proof of documents associated with each transaction.
d. Checking the Office of Foreign Assets Control Listings
10

Although not part of the BSA and its implementing regulations, Office of Foreign Assets Control 
(OFAC) compliance is often performed in conjunction with AML compliance. OFAC is an office 
of the U.S. Treasury that administers and enforces economic sanctions and embargoes based on 
U.S. foreign policy and national security goals that target geographic regions and governments 
(e.g., Cuba, Sudan and Syria), as well as individuals or entities that could be anywhere (e.g., 
international narcotics traffickers, foreign terrorists and proliferators of weapons of mass 
destruction). As part of its enforcement efforts. OFAC publishes a list of Specially Designated 
Nationals and Blocked Persons (SDN list), which includes names of companies and individuals 
who are connected with the sanctions targets. U.S. persons are prohibited from dealing with 
SDNs wherever they are located, and all SDN assets must be blocked.
Before conducting a transaction of any amount, we will check to ensure that a customer does not 
appear on the SDN list or is not engaging in transactions that are prohibited by the economic 
sanctions and embargoes administered and enforced by OFAC. To perform these checks, we may 
use the OFAC’s Sanctions List Search application found at
https://sanctionssearch.ofac.treas.gov/. Because the SDN list and listings of economic 
sanctions and embargoes are updated frequently, we will consult them on a regular basis and 
subscribe to receive any available updates when they occur. We will also document our reviews.
If we determine that a customer is on the SDN list or there is a possible match or is engaging in 
transactions that are prohibited by the economic sanctions and embargoes administered and 
enforced by OFAC, we will reject the money transmittal request and/or block the customer's 
assets and file a blocked assets and/or rejected transaction form with OFAC within 10 days. We 
will also call the OFAC Hotline at (800) 540-6322 immediately.
e. Monitoring Transactions for Suspicious Activity (31 C.F.R. 
§ 1022.320(a))
Transaction Reviews
To ensure our attentiveness to money laundering and terrorist financing activities, we will review 
all transactions conducted or attempted by, at or through our firm (including transactions 
conducted with agents) involving $2,000 or more of funds or assets (either individually or in the 
aggregate).
On a monthly basis, we will complete a transaction review form (“TRF”), on which we will 
document our reviews. To evidence our compliance with our requirement to identify and report 
suspicious transactions, we will maintain copies of our TRFs for at least five years from the date 
of the review.
Red Flags
We will use a Transaction Review Form (“TRF”) to document our reviews of transactions. With 
our TRF, we will consider whether or not a transaction has, at a minimum, any of the red flags 
identified by FinCEN in its publication: Money Laundering Prevention: A Money Services 
Business Guide (https://www.fincen.gov/sites/default/files/guidance/msb prevention guide.pdQ:
Red flags that signal possible money laundering or terrorist financing include, but are not 
limited to:
11

Customer ID or Information
• Customer uses false ID.
• Two/more customers use similar IDs.
• Customer alters transaction upon learning that he/she must show ID.
• Customer alters spelling or order of his/her full name.
Transactions Below Reporting or Recordkeeping Thresholds
• Customer conducts transactions just below relevant thresholds:
• Currency exchanges just under $ 1.000.
Multiple Customers or Locations
• Two or more customers working together to break one transaction into two or more 
transactions in order to evade the BSA reporting or recordkeeping requirement.
• Customer uses two or more locations or cashiers in the same day in order to break 
one transaction into smaller transactions and evade the BSA reporting or 
recordkeeping requirement.
Overt Illegal Customer Conduct
• Customer offers bribes or tips.
• Customer admits to criminal conduct.
Responding to Red Flags and Suspicious Activity
When an employee of the firm detects any red flag, or other activity that may be suspicious, he or 
she will notify our AML Compliance Officer. Under the direction of the AML Compliance 
Officer, the firm will determine whether or not and how to further investigate the matter. This 
may include gathering additional information internally or from third-party sources, contacting 
the government, and/or filing a SAR.
If the activity is initially deemed potentially suspicious but after review, our AML Compliance 
Officer decided that it is not reportable, then we will not file a SAR.
f. Foreign Agents and Counterparties (FinCEN Release No. 2004-
01:
https://www.fmcen.gov/sites/default/files/shared/msbagentadvisor 
ypdf)
We do not have any agents at this time. The following procedures regarding agents may not apply 
to our current state but may apply in the future.
Before entering into a relationship with any foreign agent or foreign counterparty, and on at least 
an annual basis after entering into any such relationship, we shall conduct risk-based due 
diligence and monitoring of activities:
Review Structure and Risk Profile
12

• Location of agent/counterparty - check FATF guidance regarding risks posed by 
jurisdiction.
• Ownership of agent/counterparty - run OFAC check against owners
• Require agent/counterparty to be subject to AML requirements in its jurisdiction and that 
it establish internal controls.
• Use web searches to check for any reports of AML issues with agent/counterparty.
• Review of agent/counterparty's business, the markets it serves, and the extent to which its 
structure presents an increased risk for money laundering or terrorist financing.
• Review the types and purposes of services to be provided to, and anticipated activity
with, the agent/counterparty.
• Consideration of the nature and duration of our relationship with the agent/counterparty.
• Identify material changes in the agent/counterparty's risk profile (ex: ownership, 
business, or the regulatory scrutiny to which it is subject).
Monitoring
• Review of transactions to identify and, where appropriate, report suspicious transactions, 
including:
o unusual wire activity;
o bulk sales or purchases of sequentially numbered instruments; 
o multiple purchases or sales that appear to be structured, and; 
o illegible or missing customer information.
• Review of agent/counterparty AML program to discern obvious breakdowns in the 
implementation of the program by the agent or counterparty.
• Review of agent/counterparty activities for signs of structuring or unnecessarily complex 
transmissions through multiple jurisdictions that may be indicative of layering or of 
efforts to evade detection.
Corrective Action and Termination
Agent/counterparty deficiencies noted in our due-diligence activities will be reported to the 
agent/counterparty. The agent/counterparty must promptly respond to and resolve each identified 
deficiency. Based on our assessment of the risk presented by each identified deficiency, we shall 
work with the agent/counterparty to set a resolution date.
Should an agent or counterparty fail to respond timely or appropriately to an identified 
deficiency, or should our management team determine that an identified deficiency presents an 
unacceptable risk, we shall take immediate actions to temporarily or permanently cease all 
business activities with the agent or counterparty. We shall take such actions should an agent or 
counterparty ever demonstrate systemic, willful, or repeated lapses in compliance with our AML 
procedures or requirements.
1. AML Compliance Officer Designation and Duties (31 
C.F.R. § 1022.210(d)(2))
13

BankClient has designated Xin Huang as its Anti-Money Laundering Compliance Officer (“AML 
Compliance Officer”), with full responsibility for the firm's AML Program. As our AML 
Compliance Officer, Mr. Huang will oversee ail aspects of BankClient’s compliance with AML 
regulations. Mr. Huang has a working knowledge of the BSA and its implementing regulations 
and is qualified by experience, knowledge and training. Mr. Huang has Master of Management 
Science & Engineering degree from Columbia University. He proceeded international accredited 
investors compliance (review and verification) when he was in Meixin Finance Group, a global 
investment company based in New York.
The responsibilities of our AML Compliance Officer shall specifically include assuring that:
• Our firm properly files reports, and creates and retains records, in accordance with 
applicable requirements of the BSA;
• Our AML Program is updated as necessary to reflect current requirements of the BSA, 
and related guidance issued by the Department of the Treasury; and
• Our firm provides appropriate training and education in accordance with 31 C.F.R. 
§ 1022.210(d)(3).
1. Agent Relationships
Citing 31 CFR § 1022.210(d)( 1 )(iii), in its March 11,2016, Guidance, FinCEN explained that, in 
MSB principal-agent relationships, “each MSB remains independently and wholly responsible for 
implementing adequate AML program requirements.”
FinCEN went on to explain that, as the principal MSB, we must “have procedures in place to 
identify those agents conducting activities that appear to lack commercial purpose, lack 
justification, or otherwise are not supported by verifiable documentation. The principal must 
implement risk-based procedures to monitor the agents' transactions to ensure that they are 
legitimate. The procedures must also ensure that, if the agents' transactions trigger reporting or 
recordkeeping requirements, the principal handles the information in accordance w ith regulatory' 
reporting and recordkeeping obligations. In addition, the MSB principal should implement 
procedures for handling non-compliant agents, including agent contract terminations.”
Recognizing our responsibility in each of these areas, even we do not have any agents at this time 
and it may not apply to our current state, we have implemented the following policies, 
procedures, and internal controls if they may apply in the future:
a. Transaction Reviews
We recognize the risks presented to our firm through the actions of our agents. To address these 
risks, we will monitor the activities of our agents.
As noted below, we will review transactions conducted through our agents. In performing these 
reviews, we will be attentive to agent activities that appear to lack commercial purpose, lack 
justification, or otherwise are not supported by verifiable documentation.
14

As part of these reviews, we will confirm that, for agent transactions which trigger BSA reporting 
or recordkeeping requirements, we have created the required records and filed the required 
reports.
b. AML Program Reviews
On at least an annual basis, we will also review the written AML policies and procedures of each 
of our agents. We will perform these reviews to ensure that our agents have effective AML 
programs. An effective AML program will address all relevant BSA requirements including: CIP, 
Transaction Monitoring. BSA Reporting, and Recordkeeping.
c. Agent Transactions - BSA Reporting and Recordkeeping
As specified in this program, BankClient accepts full responsibility for BSA reporting and 
recordkeeping requirements related to BankClient’s MSB activities. Whether transactions are 
conducted directly with us, or whether they are conducted through our agents, we will file all 
required reports and keep all required records.
d. Corrective Action and Termination
Agent deficiencies noted in our due-diligence activities will be reported to the agent. The agent 
must promptly respond to and resolve each identified deficiency. Based on our assessment of the 
risk presented by each identified deficiency, we shall work with the agent to set a resolution date.
Should an agent fail to respond timely or appropriately to an identified deficiency, or should our 
management team determine that an identified deficiency presents an unacceptable risk, we shall 
take immediate actions to temporarily or permanently cease all business activities with the agent. 
We shall take such actions should an agent ever demonstrate systemic, willful, or repeated lapses 
in compliance with our AML procedures or requirements.
1. BSA Reporting
a. Use of the BSA E-Filing System
We shall use the BSA E-Filing System to submit each SAR, CTR. FinCEN Form 114 (FBAR), 
and RMSB as applicable.
b. Currency Transaction Report (“CTR”) (31 C.F.R. § 1010.311)
We prohibit dealing with currency currently. There is little if not zero chance we make a currency 
transaction. Should we make such transactions, we shall implement the following policies and 
procedures:
For each deposit, withdrawal, exchange of currency or other payment or transfer, by, through or 
to us, which involves a transaction in currency of more than $10,000 and which is not between 
our firm and a commercial bank (see § 1010.315), we shall file with FinCEN a CTR. Also, we 
15

will treat multiple transactions involving currency as a single transaction for purposes of 
determining whether to file a CTR if they total more than $10,000 and are made by or on behalf 
of the same customer during any one business day. We shall file a CTR within 15 days following 
the day on which the reportable transaction occurred. We shall retain a copy of each CTR for a 
period of five years from the date of the report.
Identification Required (31 C.F.R. § 1010.312)
Before concluding any transaction with respect to which the filing of a CTR is required, we shall 
verify and record the name and address of the individual presenting the transaction, as well as 
record the identity, account number, and taxpayer identification number, if any, of any entity on 
whose behalf such transaction is to be effected. Verification of the identity of an individual who 
indicates that he or she is an alien or is not a resident of the United States shall be made by 
passport, alien identification card, or other official document evidencing nationality or residence.
In each instance, the specific identifying information used in verifying the identity of the 
customer shall be recorded on the report.
Aggregation (31 C.F.R. § 1010.313)
In determining whether or not we are obligated to file any CTR, we shall aggregate all transaction 
activities.
We shall treat multiple currency transactions as a single transaction if we have knowledge that 
these transactions are made by or on behalf of any customer and result in either cash in or cash 
out totaling more than $10,000 during any one business day.
c. Report of Transportation of Currency or Monetary Instruments 
(“CMIR”) (31 C.F.R. § 1010.340)
As required by 31 C.F.R. § 1010.340, we shall file a CMIR with the Commissioner of Customs if 
we discover that we have received or caused or attempted to receive from outside of the U.S. 
currency or other monetary instruments in an aggregate amount exceeding $10,000 at one time. 
We shall file such report within 15 days after receipt of the currency or other monetary 
instruments.
We shall also file a CMIR if we discover that we have physically transported, mailed or shipped 
or caused or attempted to physically transport, mail or ship by any means currency or other 
monetary instruments of more than $10,000 at one time. We shall file such report at the time of 
departure, mailing or shipping from the United States.
d. Report of Foreign Financial Accounts (31 C.F.R. § 1010.350 and
420)
As of the date of this program, we have no financial interest in, or signature or other authority 
over, a bank, securities, or other financial account in a foreign country.
Should we ever have a financial interest in, or signature or other authority over, a bank, securities, 
or other financial account in a foreign country, we shall report such relationship to the
16

Commissioner of Internal Revenue for each year in which such relationship exists and shall 
provide such information as shall be specified in a reporting form prescribed under 31 U.S.C. 
1. The form prescribed under section 5314 is the Report of Foreign Bank and Financial 
Accounts (FinCEN Form 114 or “FBAR”).
We shall file all FBARs with the Commissioner of Internal Revenue on or before June 30 of each 
calendar year with respect to foreign financial accounts exceeding $10,000 maintained during the 
previous calendar year. We shall retain such records for a period of five years and shall keep them 
at all times available for inspection as authorized by law.
e. SAR Filing (31 C.F.R. § 1022.320)
We will file a SAR with FinCEN for any transactions conducted or attempted by, at or through 
our firm involving $2,000 or more of funds or assets (either individually or in the aggregate) 
where we know, suspect or have reason to suspect that the transaction:
• involves funds derived from illegal activity or is intended or conducted in order to hide or 
disguise funds or assets derived from illegal activity as part of a plan to violate or evade 
federal law or regulation or to avoid any transaction reporting requirement under federal 
law or regulation;
• is designed, whether through structuring or otherwise, to evade any requirements of the 
BSA regulations;
• serves no business or apparent lawful purpose, and after examining the available facts, 
including the background and possible purpose of the transaction, we know of no 
reasonable explanation for the transaction; or
• involves the use of the firm to facilitate criminal activity.
We may voluntarily file a SAR for any suspicious transaction that we believe is relevant to the 
possible violation of any law or regulation but that is not required to be reported by us under the 
SAR rule. It is our policy that all SARs will be reported regularly to the Board of Directors and 
appropriate senior management, with a clear reminder of the need to maintain the confidentiality 
of the SAR.
We will file a SAR no later than 30 calendar days after the date of the initial detection of the facts 
that constitute a basis for filing a SAR. The phrase “initial detection'’ does not mean the moment 
a transaction is highlighted for review. The 30-day period begins when an appropriate review is 
conducted and a determination is made that the transaction under review is “suspicious” within 
the meaning of the SAR requirements. A review must be initiated promptly upon identification of 
unusual activity that warrants investigation.
f. Emergency Notification to Law Enforcement by Telephone (31
F.C.R. § 1022.320(b)(3))
In situations involving violations that require immediate attention, such as ongoing money 
laundering schemes, we will immediately call an appropriate law enforcement authority. In 
addition to local law enforcement authorities, we may also contact FinCEN’s Financial 
Institutions Hotline (866.556.3974) to report transactions relating to terrorist activity. If we notify 
the appropriate law' enforcement authority of any such activity, we must still file a timely SAR.
17

g. Joint Filing of SARs with Other Financial Institutions (31 C.F.R. 
§ 1022.320)
If we and one or more other party have an obligation to report a transaction, we may file a single 
SAR jointly with the other party.
When filing jointly, we will ensure that the filed SAR contains all relevant facts, including the 
name of each party involved in the transaction. We will also ensure that the SAR complies with 
all instructions applicable to joint filings, and that we keep a copy of the report filed, along with 
any supporting documentation.
If we determine it is appropriate to jointly file a SAR, we understand that we cannot disclose that 
we have filed a SAR to any party except the party that is filing jointly. If we determine it is not 
appropriate to file jointly (e.g., because the SAR concerns the other party or one of its 
employees), we understand that we cannot disclose that we have filed a SAR to any party.
1. BSA Recordkeeping
We will keep all required records (including C1P records, SAR filings, KYC, Program, policies 
and procedures, training, training logs, and other required records) for at least five years.
a. Required Records of Funds Transmittals (31 C.F.R. § 1010.410)
In addition to the maintenance of records referenced elsewhere in this program, we shall retain 
either the original or a copy of each of the following:
For funds transmittals under the Funds Transfer and Travel Rules (31 C.F.R. § 1010.410(e) and 
(0), when we are the transmitter’s financial institution in funds of $1,000 or more, we will retain 
a record of the transmittal order. We will record the following information on the transmittal 
order:
• the name and address of the transmitter;
• the amount of the transmittal order;
• the execution date of the transmittal order;
• any payment instructions received from the transmitter with the transmittal order;
• any form relating to the transmittal of funds that is completed or signed by the person 
placing the transmittal order, and
• the identity of the recipient’s financial institution.
In addition, we will include on the transmittal order as many of the following items of 
information as are received with the transmittal order:
• the name and address of the recipient;
• the account number of the recipient:
18

• any other specific identifier of the recipient; and
In the case of a transmittal order of $1,000 or more from a transmitter that is not an established 
customer, in addition to obtaining and retaining the information required by 31 C.F.R. 
§ 1010.410(e)( 1 )(i), we will follow the criteria specified by § 1010.410(e)(2)(i) and (ii):
• Verify identity of person placing the order.
• Retain a record of the following information of the person placing the order: name, 
address, tax id number or alien identification number or passport number, and copy of the 
presented identification.
• If we know that the person placing the order is not the transmitter, we shall retain a 
record of the transmitter's tax id number or alien identification number or passport 
number and country of issuance, if known by the person placing the order, or a notation 
in the record of the lack thereof.
If the transmittal order is not made in person, we shall retain a record of the following:
• Name and address of the person placing the transmittal order, the person's tax id number, 
alien identification number or passport number and country of issuance, or a notation in 
the record of the lack thereof, and a copy or record of the method of payment (e.g.. check 
or credit card transaction) for the transmittal of funds.
• If we know that the person placing the transmittal order is not the transmitter, we shall 
obtain and retain a record of the transmitter’s tax id number or alien identification number 
or passport number and country of issuance, if known by the person placing the order, or 
a notation in the record of the lack thereof.
For each transmittal order of $1,000 or more that we accept as a recipient's financial institution 
for a recipient that is not an established customer, in addition to obtaining and retaining the 
information required by 31 C.F.R. § 1010.410(e)( 1 )(iii), we shall also obtain the information 
required by 31 C.F.R. § 1010.410(eX3)(i) and (ii):
If the proceeds are delivered in person to the recipient or its representative or agent, we shall
• Verify the identity of the person receiving the proceeds, and
• Retain a record of the name and address, the type of identification reviewed, and the 
number of the identification document, as well as a record of the person's tax id number 
or alien identification number or passport number and country of issuance, or a notation 
in the record of the lack thereof.
If we have knowledge that the person receiving the proceeds is not the recipient, we shall obtain 
and retain the following:
• a record of the recipient's name and address, as well as the recipient's taxpayer id number 
or alien identification number or passport number and country of issuance, if known by 
the person receiving the proceeds, or a notation in the record of the lack thereof.
If the proceeds are delivered other than in person, we shall retain a copy of the check or other 
instrument used to effect payment, or the information contained thereon, as well as the name and 
address of the person to which it was sent.
19

b. Retrievability
Regarding the information that shall be retained under section “a”, above:
As the transmitter's financial institution, we shall retain information in a format that shall allow 
us to retrieve the information by reference to the name of the transmitter. If the transmitter is an 
established customer and has an account used for transmittals of funds, then the information also 
shall be retrievable by account number.
As the recipient’s financial institution, we shall retain information of our recipient in a format that 
shall allow us to retrieve the information by reference to the name of the recipient. If the recipient 
is an established customer and has an account used for transmittals of funds, then the information 
also shall be retrievable by account number.
c. Additional Records to Be Retained by Dealers in Foreign
Exchange (31 C.F.R. § 1022.410)
When conducting foreign exchange transactions, we shall retain either the original or a copy of 
each of the following:
• Statements of accounts from banks, including paid checks, charges or other debit entry 
memoranda, deposit slips and other credit memoranda representing the entries reflected 
on such statements;
• Daily work records, including purchase and sales slips or other memoranda needed to 
identify and reconstruct currency transactions with customers and foreign banks;
• A record of each exchange of currency involving transactions in excess of $1,000, 
including the name and address of the customer (and passport number or taxpayer 
identification number unless received by mail or common carrier) date and amount of the 
transaction and currency name, country, and total amount of each foreign currency ;
• Signature cards or other documents evidencing signature authority over each deposit or 
security account, containing the name of the depositor, street address, taxpayer 
identification number (TIN) or employer identification number (EIN) and the signature of 
the depositor or of a person authorized to sign on the account (if customer accounts are 
maintained in a code name, a record of the actual owner of the account);
• Each item, including checks, drafts, or transfers of credit, of more than $10,000 remitted 
or transferred to a person, account or place outside the United States;
• A record of each receipt of currency, other monetary instruments, investment securities 
and checks, and of each transfer of funds or credit, or more than $10,000 received on any 
one occasion directly and not through a domestic financial institution, from any person, 
account or place outside the United States;
• Records prepared or received by us in the ordinary course of business, that would be 
needed to reconstruct an account and trace a check in excess of $100 deposited in such 
account through our internal recordkeeping system to our depository institution, or to 
supply a description of a deposited check in excess of $100;
20

• A record maintaining the name, address and taxpayer identification number, if available, 
of any person presenting a certificate of deposit for payment, as well as a description of 
the instrument and date of transaction;
• A system of books and records that will enable us to prepare an accurate balance sheet 
and income statement.
d. SAR Maintenance and Confidentiality (31 C.F.R. § 1022.320)
We will retain copies of all SARs filed and any supporting documentation for five years from the 
date of filing the SAR.
We will not notify any person involved in the transaction that the transaction has been reported, 
except as permitted by the BSA regulations. We understand that anyone who is subpoenaed or 
required to disclose a SAR or the information contained in the SAR will, except where authorized 
by FinCEN, decline to produce the SAR or to provide any information that would disclose that a 
SAR was prepared or filed. We will notify FinCEN of any such request and our response.
We may share information with another financial institution about suspicious transactions in BankClient
order to determine whether we will jointly file a SAR according to the provisions of Section 4.e 
(above). In cases in which we file a joint SAR for a transaction that has been handled both by us 
and another financial institution, both financial institutions will maintain a copy of the filed SAR.
1. Education and Training Program (31 C.F.R. § 1022.210
(d)(3))
Under the direction of our AML Compliance Officer, we will provide ongoing education and 
training of appropriate personnel. This education and training will occur on at least an annual 
basis. It will explain the responsibilities of firm personnel under the firm’s AML compliance 
program, including education and training in the detection of suspicious transactions. If we have 
any branch offices or agents, we will ensure that they receive appropriate training.
Our training will include, at a minimum: (1) how to identify red flags and signs of money 
laundering that arise during the course of the employees' duties; (2) what to do once the risk is 
identified (including how, when and to whom to escalate unusual customer activity or other red 
flags for analysis and, where appropriate, the filing of SARs); (3) what employees' roles are in the 
firm's compliance efforts and how to perform them; (4) the firm's record retention policy; and (5) 
the disciplinary consequences (including civil and criminal penalties) for non-compliance with 
the BSA.
We will develop training in our firm, or contract for it. Delivery of the training may include 
educational pamphlets, videos, intranet systems, in-person lectures and explanatory memos. We 
will maintain records to show the names of persons trained, dates of training, and copies of 
training.
21

1. Independent Review of AML Program (31 CFR §
1022.210 (d)(4))
The review of our AML compliance program will be performed annually (on a calendar year 
basis) by Securities Industry Records Services, LLC (“SIRS"), an independent, third-party service 
provider, or by another, similarly qualified, service provider. We have evaluated SIRS' 
qualifications to ensure they have a w orking knowledge of applicable requirements under the 
BSA and its implementing regulations.
SIRS’ CEO. BankClient, is a Certified Anti-Money Laundering Specialist® (“CAMS") and is a 
member of the Association of Certified Anti-Money Laundering Specialists (“ACAMS"). He has 
passed multiple certification examinations and has participated in numerous industry-sponsored 
regulatory compliance and AML training programs. Mr. Klundt has also held the position of 
AML Compliance Officer with a BSA-regulated financial institution.
After the completion of each annual, independent review, Board of Directors will review the 
review report. We will promptly address each of the resulting recommendations and keep a 
record of how each noted deficiency was resolved.
1. Board of Directors Approval
Board of Directors of BankClient has approved this AML compliance program in writing as 
reasonably designed to achieve and monitor our firm’s ongoing compliance with the requirements 
of the BSA and the implementing regulations under it. This approval is indicated by the signature 
below.
Signed:
CEO
Date:
22

1. Revision History Page to Track Updates
February 26, 2017 — Initial version
March 2, 2017 -- Removed irrelevant parts
March 10, 2017 — Rephrased several parts
April 3, 2017 — Reviewed and revised by SIRS
23


APC Know Your Customer Policy Document Number: 1000.2.002 Approval Authority: BSA/AML Officer Policy Owner: BSA/AML Officer Last Renewal Date: 12/15/2017 Renewal Frequency: AnnuallyDocument Overview, Purpose, and Applicability: In this document,  BankClient Capital (“APC” or the “Company”) outlines requirements ‘Know Your Customer’ (“KYC”) activities, which support the Company’s BSA/AML/OFAC Program Policy.KYC activities enable the Company to form a reasonable belief as to a customer’s true identity, the nature of the customer’s business, and the level of risk the customer’s loan relationship may pose.This Policy is applicable to all lending application, funding, and account management activities.Statements:1. Customer Identification Program (including Beneficial Ownership) – APC has a “Customer Identification Program” which requires employees to collect and verify identification for customers in the lending application process in order to form a reasonable belief as to the true identity of the customer.The Company’s Chief Credit Officer will implement this program within pre-funding policies and procedures. 1.1. Customer Identification:1.1.1. To identify the business customer, the following information will be obtained with every application the company receives • Business entity’s official legal name; • Physical address (no P.O. Boxes or mail drops) of the business entity’s principal place of business or main office; • Employer Identification Number (EIN)/Tax Identification Number (TIN) of the entity (the Company does not accept TIN applications); and • List of Owners with at least 25% ownership in the entity (which may be a subset of a more comprehensive entity ownership list collected); before May 11, 2018, this list includes all owners with at least 25% ownership of the business entity; on or after May 11, 


2018, this includes a list of individuals1 with ownership stakes in the business totaling at least 25% and, if none of these individuals exercise significant managerial control over the entity, an additional individual who does exercise significant managerial control, even if not an owner 1.1.2.  BankClient Capital also collects the following information with every application the Company receives, even when the ownership group is the same as a previous/existing customer’s application: • Name of any individual(s) on the List of Owners with at least 25% ownership in the entity; • Physical address (no P.O. Boxes or mail drops) of the individual(s) on the List of Owners with at least 25% ownership in the entity; • Data of birth for the individual(s) on the List of Owners with at least 25% ownership in the entity; and • Social Security/Tax Identification Number (TIN) of the individual(s) on the List of Owners with at least 25% ownership in the entity. 1.1.3. In accordance with BSA/AML requirements and as part of initiating the application, the Company collects and documents a specific purpose for loans of $10,000 or more.The purpose collected must be more detailed than “Business” or “Commercial” 1.2. Verification of Customer Identity 1.2.1. Before qualifying any loan for funding, the Company must verify the identity of the business entity customer using at least one entity document from among the following: • Government-certified copy of a certificate of existence and good standing; • Unexpired business license; or • Articles of Organization or Partnership Agreement with ownership structure matching the declaration used for entity identification 1.2.2. The Company verifies the identity of individual who are on the List of Owners with at least 25% ownership of the entity.Given a variety of circumstances, verifying identification is accomplished through non-documentary methods or by reviewing documentation produced by the individuals.The following describes those methods acceptable for verifying identification information 1.2.2.1. Non-Documentary Methods: APC accounts are opened over the internet.APC deploys non-documentary methods for verifying identification of individuals.1 If a non-statutory trust owns at least 25% of the business, its trustee is included on the list; if the individual does not have capacity, the individual’s power-of-attorney is included on the list. 


Non-documentary methods allowed include independently verifying the customer’s identity through the comparison of information provided by the customer with information obtained from a consumer reporting agency public database, or other source. 1.2.2.2. Reviewing Documentation Provided By The Individual: When an individual’s identity cannot be verified through Non-Documentary Methods, the individual’s identity must be verified through a review of documentation provided by the individual.The documentation must be an unexpired government-issued identification, which provides evidence of a customer’s nationality or residence and bears a photograph or other similar safeguard, such as a driver’s license or passport.It must be an image of the original document or an image of a copy of the original document that appears reliable and does not show indications of alteration. 1.3. Customer Notice: As part of the application initiation process, the Company provides customers with the following Notice of Customer Identification Program in accordance with the regulations implanting Section 326: 1.4. Comparison with Government Lists: Customer identities must be compared against separate designated government lists of known or suspected terrorists or terrorist organizations; to date, the government has not designated any such list. 2. Customer Due Diligence – APC applies additional due diligence across all applicants and borrowers to meet the expectations of its business partners and to ensure it has sufficient information to evaluate the risk of money-laundering and terrorist financing by individual customers.APC applies enhanced scrutiny to some applicants and customers with indicators of higher risk. 2.1. Due Diligence Performed on All Loan Requests Before Funding 2.1.1. Additional Identification and Verification Due Diligence:  BankClient collects the same information collected in Section 1.1 on any additional individuals who are also personal guarantor(s) on the loan request, even if they are guarantor(s) on a previous/existing customer’s application; the Company verifies the identity of the same individuals using the methods described in Section 1.2 2.1.2. Customer Risk Rating at Application Stage: The Company applies enhanced due diligence to certain applicants and borrowers.In order to determine which entities require enhanced due diligence, each application for credit is evaluated for the presence of risk factors for enhanced due diligence: • Applicant/Borrower is a franchisor (as opposed to a franchisee) • Franchise Brand of Applicant/Borrower is in business less than 5 years and has fewer than 25 franchise units 


• Franchise Brand of Applicant/Borrower is a cash-intensive business (or there is a privately-owned ATM at the applicant/borrower’s location) • Ownership structure includes a non-resident alien owner with at least 25% ownership 2.2. Due Diligence Performed on All Loans Post-Funding:  BankClient applies Customer Identification and Verification requirements (Section 1.1 and Section 1.2 of this document) to any individuals who request to join the ownership structure of a business entity post-funding 2.3. Customer Risk Rating Adjustments: The Company may consider one or a number of objective mitigating factors to reduce the sum of Customer Risk Rating factors applicable to a given customer.Eligible factors will be approved by the AML/BSA Officer to be added to this policy before being applied to a given customer.To date, no such factors have been identified.The Company may judgmentally escalate any customer’s risk rating due to anomalous activity, negative news, or receipt of any government information request directly or through a partner. 2.4. Enhanced Due Diligence on High Risk Entities: Enhanced Due Diligence provides additional risk-based scrutiny on applicants, borrowers, and their activities for the sake of improving underwriting decisions and suspicious incident identification. 2.4.1. Applicants with at least three risk factors require the Head of Underwriting to investigate the application; the Head of Underwriting (or Chief Credit Officer or BSA/AML Officer) must approve the application to pass CIP and to be eligible for a loan commitment after underwriting 2.4.2. If funded, borrowers with at least three risk factors, after any mitigating or escalating adjustments, are included on an Executive Watchlist 3. Record Retention: The Company retains all records obtained to identify and verify the customer and beneficial owners (identifying information, the methods and results of measures taken to verify identity, and a record of any document relied on including the type of document, its number, dates of issuance and expiration, and place of issuance).The Company also retains the details of the loan (loan amount, nature/purpose, and date of loan).Records are retained for five (5) years after the account is closed. References:1000.2.001 BSA/AML/OFAC PolicyRevision History: Date of Action Responsible Party Description of Action November 2016 BSA/AML Officer Separate KYC Policy from AML/BSA Policy April 2017 BSA/AML Officer Reflect existing Business Entity verification and due diligence; 


add Customer Risk Rating and Enhanced Due Diligence requirements; incorporate May 11, 2018 rules regarding Beneficial Ownership July 2017 BSA/AML Officer Clarification of existing business practice regarding CIP requirements for repeat ownership groups and additional guarantors December 2017 BSA/AML Officer Full renewal 

Background and Policy Statement
BankClient has established goal of maintaining a Bank Secrecy Act (BSA) and Anti-Money Laundering (AML) compliance program with strong monitoring procedures in place. We have implemented a process by which we continuously identify and monitor the risks that could directly impact the quality of our BSA/AML compliance program.  By analyzing and understanding our BSA/AML risk profile, we have been able to apply appropriate risk management processes to, and controls within, the BSA/AML compliance program to mitigate risk.  
Board Oversight
The Board of Directors is ultimately responsible for ensuring the bank maintains an effective BSA/AML program. As a result, management is required to develop policies and procedures designed to limit and reasonably control BSA/AML risks identified in the risk assessment.   The Board is also responsible for designating a qualified BSA/AML Compliance Officer to oversee daily compliance. This designation must be made by formal Board resolution at least annually and noted within the minutes of the meeting in which the designation is made.  The Board of Directors is responsible for ensuring that the BSA Officer has sufficient authority and resources to administer an effective BSA/AML Program based on the bank’s risk profile.
BSA/AML Compliance Program Components
As required by law, our BSA/AML compliance program must be written, approved by the Board of Directors and noted in the Board minutes.  We must have a BSA/AML compliance program that is commensurate with our risk profile.  Our BSA/AML compliance program must be fully implemented and reasonably designed to meet BSA requirements.  We acknowledge that policy statements alone are not sufficient; our practices must coincide with our written policies, procedures and processes.  Our BSA/AML compliance program must provide for the following minimum requirements, also referred to as the “pillars” of BSA:
A system of internal controls to ensure ongoing compliance.
Independent testing of BSA/AML compliance.
Designation of an individual or individuals responsible for managing BSA compliance (i.e. BSA Officer).
Training for appropriate personnel.
Additionally, we must include a Customer Identification Program as part of our BSA/AML compliance program.  
BSA/AML Risk Assessment
We acknowledge the value in establishing a comprehensive risk assessment to aid us in applying appropriate risk management processes to, and controls within, our BSA/AML compliance program with the objective of mitigating that risk.  We also acknowledge that the risk assessment process has helped us in identifying and mitigating gaps in our controls.  In the 2Q2016, we undertook an initiative to overhaul the existing BSA/AML risk assessment to ensure that our resulting BSA/AML risk assessment is representative of our BSA/AML risk as presented by our operations, markets, customer base, products, services and risk management practices.  Based on the information analyzed within our risk assessment, we have identified our BSA/AML risk profile to be moderate.  
We also acknowledge that our risks will change as we implement new products and services, enter new markets, take on new customers and make changes operationally and strategically. As such, we have committed to maintaining a dynamic risk assessment that is proactively updated for any changes that could impact the bank’s risk profile.
Internal Control Requirements
The Board, acting through Senior Management, is ultimately responsible for ensuring that the bank maintains an effective BSA/AML internal control structure, including suspicious activity monitoring and reporting.  Internal controls are our policies, procedures and processes designed to limit and control risks and to achieve compliance with the BSA.  The following table highlights internal control requirements and the actions we have taken to ensure we have implemented satisfactory controls. Internal controls should:
  
Independent Testing Requirements
Under the pillars of BSA, we are required to ensure independent testing of the adequacy of our BSA/AML compliance program is conducted every 12-18 months. We acknowledge that our risk profile, driven by our products, services, customer base and markets, presents elevated BSA/AML risk and as such, it is the policy of BankClient to engage an independent third party to conduct the bank’s BSA/AML audit every 12 months, at a minimum.  It should be noted that two independent testing functions support one another in this endeavor:  one audit assesses the adequacy of the bank’s BSA/AML compliance program over the “core” bank, while a second audit, performed by a separate independent third party, assesses the adequacy of our BSA/AML controls over the bank’s prepaid card function.  The independent third parties performing such audits are subject to the bank’s vendor management process.  
We have laid out the following, in accordance with regulatory guidance, as minimum requirements for our BSA/AML independent testing process:

We require that the audit scope, procedures performed, transactional testing completed and findings from the review be defined and documented.  All audit documentation and work papers are available for examiner review.  
Any violations, policy or procedure exceptions or other deficiencies are outlined within an audit report that is provided to the Board upon completion of the audit.  
BSA Officer Responsibilities
The Board recognizes its responsibility to designate a qualified individual to serve as our bank’s BSA Compliance Officer.  The BSA Compliance Officer is responsible for coordinating and monitoring daily BSA/AML compliance.  The BSA Officer is also charged with managing all aspects of the BSA/AML compliance program and with managing the bank’s adherence to the BSA and its implementing regulations. The Board has designated a BSA Officer at the executive level who is responsible for daily oversight of the bank’s core and prepaid card BSA compliance programs.  The BSA Officer is supported by an Assistant BSA Officer.
Both the BSA Officer and Assistant BSA Officer maintain certifications through the Association of Certified Anti-Money Laundering Specialists and are expected to fulfill continuing education requirements to maintain these certifications and remain knowledgeable of BSA/AML requirements, emerging risks, and areas of regulatory concern.
The BSA Officer must provide quarterly reports to the Board of Directors that address the following, at a minimum:
Strengths and weaknesses within our BSA/AML program.
Results of our most recent independent audit(s).
Reports filed during the quarter.
Changes in our bank’s risk profile, including recommendations for change and/or updates to our BSA/AML risk assessment or policy.
Adequacy of resources, in terms of staffing, training and/or technology needs.  
Training Requirements
Ongoing and meaningful training is critical to effectively comply with the BSA and its supporting laws and regulations, as well as with our BSA/AML compliance program.  On an annual basis, we provide for classroom-style BSA training for our staff during the bank’s all-employee in-service day. For this training, staff is divided into areas of responsibility and BSA training content is tailored to those groups.  Senior Management also participates in these annual staff training sessions.  As noted within this policy, the BSA Officer and Assistant BSA Officer are expected to fulfill continuing education requirements to maintain ACAMS certifications and to remain knowledgeable of BSA/AML requirements, emerging risks, and areas of regulatory concern. Resources have been allotted to ensure these requirements are met.  The Board acknowledges that it must remain knowledgeable of BSA requirements and emerging issues. As such, resources have been dedicated to ensure the Board receives BSA compliance training annually, at a minimum.  
BankClient’s BSA/AML training initiatives are documented. Training and testing materials, dates of training sessions and attendance records are maintained by the bank’s Human Resources Officer and are available for examiner review.

The Money Laundering Process
In order to fully understand the purpose behind the practices and procedures incorporated in our BSA/AML compliance program, we must have an understanding of the money laundering process.  Money laundering is the criminal practice of processing ill-gotten gains or “dirty” money, through a series of transactions. In this way, funds are “cleaned” so that they appear to be proceeds from legal activities.  Money laundering generally does not involve currency at every stage of the laundering process. Although money laundering is a diverse and often complex process, it basically involved three independent steps that can occur simultaneously.
Placement:  The first and most vulnerable stage of money laundering.  The goal is to introduce the unlawful proceeds into the financial system without attracting the attention of financial institutions or law enforcement.  Placement techniques include structuring currency deposits in amounts to evade reporting requirements or commingling currency deposits of legal and illegal enterprises.  Examples may include:  dividing large amounts of currency into less conspicuous smaller sums that are deposited directly into a bank account, depositing a refund check from a cancelled vacation or insurance policy, or purchasing a series of monetary instruments that are collected and then deposited into accounts at another location or financial institutions.  

Layering:  Involved moving funds around the financial system, often in a complex series of transactions to create confusion and complicate the paper trail.  Examples may include:  exchanging monetary instruments for larger or smaller amounts, or wiring or transferring funds to and through numerous accounts in or more financial institutions

Integration:  Once the funds are in the financial system and insulated through the layering stage, the integration stage is used to create the appearance of legality through additional transactions.  These transactions further shield the criminal from recorded connection to the funds by providing a plausible explanation for the source of funds. Examples may include:  the purchase and resale of real estate, investment securities, foreign trusts or other assets

Additionally, we must understanding indications and risks of terrorist financing.  The motivation behind terrorist financing is ideological as opposed to profit-seeking, which is generally the motivation for most crimes associated with money laundering.  Terrorism is intended to intimidate a population or to compel a government or an international organization to do or to abstain from doing any specific act through the threat of violence.  Terrorist groups develop sources of funding that are relatively mobile to ensure that funds can be used to obtain material and other logistical items needed to commit terrorist acts.  As such, money laundering is often a vital component on terrorist financing.  
Terrorists generally finance their activities through both unlawful and legitimate sources.  Unlawful activities, such as extortion, kidnapping and narcotics trafficking, have been found to be a major source of funding.  Other observed activities involve smuggling, fraud, theft, robbery, identity theft and use of conflict diamonds as well as the improper use of charitable or relief funds.  In the last case, donors may have no knowledge that their donations have been diverted to support terrorist causes.  
It is crucial that we also address and understand elder financial exploitation. We can play a critical role in addressing elder financial exploitation through our knowledge of our customers and their accounts.  We may become aware of persons or entities perpetrating illicit activity against the elderly through monitoring transaction activity that is not consistent with expected behavior.  BankClient Bank may also become aware of such scams through our direct interactions with our customers who are being financially exploited.  If we observe possible elder abuse red flags, we must contact the BSA Officer. The BSA Officer is then required to review the circumstance of the situation and determine whether a SAR filing may be warranted.  

Customer Identification Program Overview
We are required by law to have a written Customer Identification Program (CIP).  Our CIP is intended to enable us to form a reasonable belief that we know the true identities of our customers.  Our CIP must include account opening procedures that specify the identifying information we obtain from each customer.  We must also include reasonable and practical risk-based procedures for verifying the identity of each customer.  
Under the CIP rule, an “account” is a formal banking relationship to provide or engage in services, dealings or other financial transactions and includes a deposit account, a transaction or asset account, a credit account or another extension of credit. An account also includes a relationship established to provide a safe deposit box or other safekeeping service or to provide cash management, custodian or trust services.  
An account does not include:
Products or services for which a formal banking relationship is not established with a person, such as check cashing, funds transfer or the sale of a check or money order.
Any account that the bank acquires. This may include single or multiple accounts as a result of a purchase of assets, acquisition, merger or assumption of liabilities.
Account opened to participate in an employee benefit plan established under the Employee Retirement Income Security Act of 1974.  
The CIP rule applies to a “customer”.  A customer is a person (an individual, corporation, partnership, trust, estate or any other entity recognized as a legal person) who opens a new account, an individual who opens a new account for another individual who lacks legal capacity and an individual who opens a new account for any entity that is not a legal person.  A customer does not include a person who does not receive banking services, such as a person whose loan application is denied. 
CIP | Documents Required for Individuals
At a minimum, we must obtain the following identifying information from each customer before opening an account:
Name
Date of birth
Address
Identification number
For an individual who does not have a residential or business street address, an Army Post Office (APO) or Fleet Post Office (FPO) box number, or the residential street address of the next of kin or of another contact individual may be accepted.
For a non-U.S. person, one or more of the following must be obtained:
TIN.
Passport number and country of issuance.
Alien identification card number.
Number and country of issuance of any other government-issued document evidencing nationality or residence and bearing a photograph or similar safeguard.
Identifying documents used to verify our customers’ identities must provide evidence of a customer’s nationality or residence and bear a photograph or similar safeguard.  We must obtain an unexpired, photo ID (e.g. driver’s license, passport, state-issued photo ID, resident alien card). 
CIP | Documents Required for Businesses 
At a minimum, we must obtain the following identifying information from each customer before opening an account:
Name
Address (principal place of business, local office or other physical location)
Identification number (including Amish)
For a person other than an individual, such as a corporation, partnership or trust, we must obtain documents showing the legal existence of the entity, such as certified articles of incorporation, an unexpired government-issued business license, a partnership agreement or a trust instrument.
CIP | Non-Documentary Verification Methods
We are not required to use non-documentary methods to verify a customer’s identity. However, in cases in which a customer may not have documents to satisfy our documentary identification methods, we may utilize non-documentary methods to verify a customer’s identity.  We may contact the customer; independently verify a customer’s identity through the comparison of information provided by the customer with information obtained from a consumer reporting agency, public database or other source; check references with other financial institutions; or, obtain a financial statement.  
The following situations may occur in the normal course of business. Please note BankClient’s procedure for addressing each situation. Note:  e-Funds queries are made for all new customers. For loan accounts, credit reports are obtained for all new customers.

For accounts opened online, we utilize e-Funds and/or a credit report to verify the customer’s identity.  We then follow up with customer contact to verify that the information provided is accurate.  For non-individuals, we obtain financial statements, business credit reports and perform customer contact.
CIP | Additional Identification Procedures for Specific Customers
There are situations where we obtain information about individuals with authority or control over an account, including signatories, in order to verify a customer’s identity.  This verification method applies only when we cannot verify the customer’s true identity through documentary or non-documentary methods.  For example, we may need to obtain information about and verify the identity of a sole proprietor or the principals in a partnership when we cannot otherwise satisfactorily identify the sole proprietor or the partnership.
We will obtain CIP information on signatories for new accounts opened by entities, and if the risk warrants, we will verify their identity using established verification methods.
For our Amish customers who do not maintain photo ID, we have established an alternative method to verify their identities.  We will accept a letter from the community’s Bishop attesting to the identity of our Amish customer who is requesting to open an account with BankClient.  Please note that the Amish customer must provide a TIN at the time of account opening.
CIP | Circumstances under which the Bank should Not Open an Account
When identification verification procedures do not result in a reasonable belief of the true identity of the customer, the account should not be opened.  
CIP | Exceptions
Excluded from the definition of customer (and therefore excluded from CIP) are federal regulated banks, banks regulated by a state bank regulator, governmental entities and publicly traded companies.  
Instead of obtaining a TIN from a customer prior to opening an account, an account may be opened without a taxpayer identification number where the customer has applied for, but has not yet received a taxpayer identification number.  Where this exception is utilized, a copy of the TIN application must be made and kept with the other account opening documentation.  The account should be flagged for review to ensure that the TIN was received within a reasonable time.  Generally, this time should not exceed 6-8 weeks from the time of account opening.  During this timeframe, the customer may have use of the account. If the TIN has not been received within this time period, customer contact should be made to determine its status. If the TIN is not forthcoming after contacting the customer, or if the bank has received notification that a TIN will not be issued, the account must be closed.  
CIP | When the Bank Should File a SAR
When an account is declined or closed due to the inability to verify the customer’s identity, the BSA Officer must be contacted to determine whether a SAR should be filed.  Similarly, the BSA Officer should be notified of any unusual or suspicious identification documents or behaviors (e.g. reluctance to provide required information) observed at the time of account opening to determine whether a SAR should be filed. 
CIP | Comparison with Government Lists
Our CIP must include procedures for determining whether a customer appears on any federal government list of known or suspected terrorists or terrorist organizations.  We are contacted by the U.S. Treasury in consultation with the FDIC when a list is issued.  At that time, we must compare customer names against the list within a reasonable time of account opening or earlier, if required by the government, and as must also follow any directives that accompany the list.  As of the date of this policy, there are no designated government lists to verify specifically for CIP purposes.  Customer comparisons to Office of Foreign Assets Control lists and 314(a) requests remain separate and distinct requirements.
CIP | Providing Customer Notice
We must provide customers with adequate notice that we will request information to verify their identities.  The notice must describe our identification requirements and we must provide the notice in a manner that is reasonably designed to allow a customer to view it or otherwise receive the notice before an account is opened.  The content of our CIP Notice has been provided as Exhibit A to this policy.
CIP | Reliance on another Financial Institution
We are permitted to rely on another financial institution to perform some or all of the elements of the CIP as long as the following criteria are met:
The relied-upon financial institution is subject to a rule implementing AML program requirements and is regulated by a federal functional regulator.
The customer has an account or is opening an account at the bank and at the other functionally regulated institution.
Reliance is reasonable under the circumstances.
The other financial institution enters into a contract requiring it to certify annually to the bank that is has implemented its AML program and it will perform (or its agent will perform) the specified requirements of the bank’s CIP.
CIP | Use of Third Parties
The CIP rule does not alter our authority to use a third party, such as an agent or service provider, to perform services on our behalf.  We are permitted to arrange for a third party, such as a car dealer or mortgage broker, acting as our agent in connection with ah loan, to verify the identity of our customer.  We can also arrange for a third party to maintain our records.  However, with any other responsibility performed by a third party, we are ultimately responsible for that third party’s compliance with our CIP requirements.  This requirement contrasts with the reliance provision of the CIP rule that permits the relied-upon party to take responsibility. 
Accounts may be opened by a third party, such a prepaid card program manager or IPI investment products.  In these instances, photo ID must be obtained, reviewed and documented for individuals.  Additional verification is performed through credit reports, e-Funds, or a telephone call.  For non-individuals, third parties must obtain articles of incorporation, government issued business licenses, partnership agreements, trust agreements, or certificates of good standing.   
CIP | Record Retention
At a minimum, we must retain the identifying information (name, address, date of birth for an individual, TIN and any other information required by the CIP) obtained at account opening for a period of 5 years after an account is closed. For credit cards, the retention period if 5 years after the account closes or becomes dormant.  We must also keep a description of the following for 5 years after the record was made:
Any document that was relied upon to verify identity, noting the type of document, the identification number, the place of issuance and, if any, the date of issuance and expiration date.
The method and results of any measures undertaken to verify identity.
The results of any substantive discrepancy discovered when verifying identity.
Customer Due Diligence
Our BSA/AML compliance program must include the adoption and implementation of comprehensive CDD policies, procedures and processes for all customers, particularly those who present higher risk for money laundering and terrorist financing. We must also include enhanced CDD for higher-risk customers and ongoing due diligence of our customer base.  CDD policies, procedures and processes are critical because they can aid us in:
Detecting and reporting unusual or suspicious transactions that potentially expose the bank to financial loss, increased expenses or reputational risk.
Avoiding criminal exposure from persons who use or attempt to use the bank’s products and services for illicit purposes.
Adhering to safe and sound banking practices.
CDD | Identifying Beneficial Owners
In May 2016, FinCEN issued Customer Due Diligence Requirements for Financial Institutions.  The final rule amends existing rules to explicitly reference key elements of customer due diligence and set forward minimum standards for CDD that are believed to be fundamental to an effective anti-money laundering program.  The rule becomes effective on July 11, 2016 and its requirements must be implemented by May 11, 2018.  
Under this rule, we must identify and verify the identity of beneficial owners of all legal entity customers at the time a new account is opened.  We verify the identity of the individuals identified as beneficial owners – NOT his or her status as a beneficial owner.  We are required to establish and maintain written policies and procedures reasonably designed to identify and verify the identities of beneficial owners of legal entity customers.  FinCEN is NOT imposing a categorical retroactive requirement. 
A beneficial owner is he natural person (as opposed to another legal entity). To aid in the determination of who meets the definition of a beneficial owner, FinCEN has provided for a two-prong test.  Each prong is intended to be an independent test.

In cases where an individual is both a 25% owner and meets the definition for control, that same individual could be identified as a beneficial owner under both prongs.  You may also identify other individuals that technically fall outside the proposed definition of “beneficial owner” in accordance with your risk mitigation and customer due diligence practices.  
Exclusions to the beneficial ownership rule include:  
Financial institutions regulated by a Federal functional regulator or a bank regulated by a State bank regulator
A department or agency of the United States, of any State, or of any political subdivision of a State
Any entity established under the laws of the United States, of any State, or of any political subdivision of any State, or under an interstate compact between two or more states, that exercises governmental authority on behalf of the U.S. or of any such State or political subdivision
Any entity (other than a bank)) whose common stock or analogous equity interests are listed on the New York, American or NASDAQ stock exchanges
Any entity organized under the laws of the United States or any State at least 51% of whose common stock or analogous equity interests are held in a listed entity.
An issuer of a class of securities registered under Section 12 of the Securities Exchange Act of 1934 or that is required to file reports under Section 15(d) of that Act
An investment company, as defined in Section 3 of the Investment Company Act of 1940, that is registered with the SEC under that Act
An investment adviser, as defined in Section 2022(a)(11) of the  Investment Advisors Act of 1940 that is registered with the SEC under that Act
An exchange or clearing agency, as defined in Section 3 of the Securities Exchange Act of 1934 that is registered under Section 6 or 17A of that Act
Any other entity registered with the SEC under the Securities and Exchange Act of 1934
A registered entity, commodity pool operators, commodity trading advisor, retail foreign exchange dealer, swap dealer, or major swap participant, each as defined in Section 1a of the Commodity Exchange Act that is registered with the CFTC
A public accounting firm registered under Section 102 of the Sarbanes-Oxley Act
A bank holding company, as defined in Section 2 of the Bank Holding Company Act of 1956 or a savings or loan holding company as defined in Section 10(n) of the Home Owners’ Loan Act
A pooled investment vehicle that is operated or advised by a financial institution excluded from the rule
An insurance company that is regulated by a State
A financial market utility designated by the Financial Stability Oversight Council under Title VIII of the Dodd-Frank Wall Street Reform and Consumer Protection Act of 2010
A foreign financial institution established in a jurisdiction where the regulator of such institution maintains beneficial ownership information regarding such institution
Non-excluded pooled investment vehicles
Intermediated account relationships
A non-U.S. governmental department, agency or political subdivision that engages only in governmental rather than commercial activities (As in the case of other legal entities lacking significant equity interests, financial institutions would be expected to collect beneficial ownership information under the control prong only)
Any legal entity only to the extent that it opens a private banking account subject to 31 CFR 1010.620
Non-profit entities whether or not tax exempt (from the ownership prong).  For purposes of this provision, a non-profit corporation or similar entity would include, among others, charitable, non-profit, not-for-profit, non-stock, public benefit or similar corporations
Accounts established for the purchase and financing of postage and for which payments are remitted directly by the financial institution to the provider of the postage products **
Commercial accounts to financial insurance premiums and for which payments are remitted directly by the financial institution to the insurance provider or broker **
Accounts to finance the purchase or lease of equipment and for which payments are remitted directly by the financial institution to the vendor or lessor of the equipment **

**   The three exemptions directly above are subject to further limitations to mitigate the remaining limited money laundering risks associated with them. (Refer to Page 22 of the Final rule for details)
The CDD Rule requires us to obtain information about the beneficial owners of a legal entity from the individual seeking to open a new account on behalf of the legal entity customer.  This individual could, but would not necessarily, be a beneficial owner. Please refer to the Beneficial Ownership Account Opening Procedures to guide you through the account opening process and the Customer Identification Program Procedures for information required to be obtained from each beneficial owner (i.e. CIP procedures for individuals) and acceptable documentary and non-documentary methods of verifying an individual’s identity.  
We must use beneficial ownership information as we use other information we gather regarding customers, including compliance with OFAC-administered sanctions. As such, we must screen each beneficial owner against the OFAC list prior to account opening and/or disbursement of loan proceeds.
FinCEN does not expect the information obtained under the CDD Rule to add additional 314(a) requirements.  The regulation implementing Section 314(a) does not require the reporting of beneficial ownership information associated with an account or transaction matching a named subject in a 314(a) request.  We are required to search our records for accounts or transactions matching a named subject and report whether a match exists using the identifying information provided in the request.  However, we have established as our policy, to include beneficial ownership in our investigation processes in addressing and responding to 314(a) requests [adjust this section if you policy is different].
CDD | Determining a Customer’s Risk Rating
At the time of account opening, staff complete a workflow within our BSA software platform designed to address both CIP and CDD requirements.  The workflow walks account opening personnel through questions about a customer’s occupation or nature of business, purpose of the account, sources of funds and wealth, ownership control, domicile, anticipated account activity and other critical information that helps us to form an understanding about the customer and his/her/its anticipated relationship (and associated risk) with BankClient.  

CDD | Responsibilities for Reviewing and Revising Customer Risk Ratings 
Customers rated High Risk at the time of account opening will be subject to an internal 60-day look-back to determine whether the high risk rating is appropriate given transaction activity conducted in the first three months of account opening.  A standard form has been developed to facilitate this look-back and document the assessment process.  
This form is also utilized to perform monitoring of High and Moderate Risk Customers (i.e. those who have been identified as High or Moderate Risk based on ongoing monitoring, transaction activity, nature of business, etc.).  
Criteria used to quantify risk and define/drive risk ratings has been outlined on the Customer Risk Assessment form.
CDD | Enhanced Due Diligence for Higher-Risk Customers
Customers who pose higher money laundering or terrorist financing risks present increased exposure to our bank.  Enhanced due diligence (EDD) for higher risk customers is especially critical in understanding their anticipated transactions and implementing a suspicious activity monitoring system that reduces our reputation, compliance and transaction risks.  Are noted above, customers that pose elevated risks (i.e. moderate and high risk customers) are subject to comprehensive periodic account reviews that are designed to ascertain whether transactions are reflective of the anticipated and “normal” activity for a given customer and whether there is any unusual or suspicious activity conducted during the timeframe reviewed.  Additionally, all customers are subject to ongoing behavior-based monitoring parameters within our BSA software platform.
CDD for Lending Relationships
Extensions of credit are incorporated into the bank’s behavior-based BSA monitoring system. [Insert bank process]  
CDD | High Risk Banking Functions
As part of our BSA/AML risk assessment process, we reviewed all of our banking functions to determine those that present elevated BSA/AML risk.  The most prominent of such functions include online account opening and the prepaid card function.  Please refer to BankClient’s BSA/AML risk assessment for complete details.
Suspicious Activity Reporting 
We must have processes in place to identify, evaluate and report suspicious activity.  Suspicious activity reports (SARs) must be filed for:
Criminal violations involving insider abuse in any amount.
Criminal violations aggregating to $5,000 or more when a suspect can be identified.
Criminal violations aggregating to $25,000 or more regardless of a potential suspect.
Transactions conducted or attempted by, at or through the bank and aggregating to $5,000 or more if you know, suspect or have reason to suspect that the transaction involves illegal activity, is designed to evade reporting requirements or has no apparent lawful purpose.
As SAR should also be filed when activity is inconsistent with an individual’s occupation, nature of business or does not reflect “normal” account activity.
Mandatory SAR Reporting of Cyber-Events
We are required to report a suspicious transaction conducted or attempted by, at or through the bank that involves or aggregates to $5,000 or more in funds or other assets.  If we suspect, or have reason to suspect that a cyber-event was intended, in whole or in part, to conduct, facilitate or affect a transaction or a series of transactions, it should be considered part of an attempt to conduct a suspicious transaction or series of transactions. 
In determining whether a cyber-event should be reported, we should consider all available information surrounding the cyber-event, including its nature and the information and systems targeted.  Similarly, to determine monetary amounts involved in the transactions or attempted transactions, we should consider in aggregate the funds and assets involved in or put at risk by the cyber event. 
When we report a cyber-event through a SAR, we should include, to the extent possible:
Description and magnitude of the event.
Known or suspected time, location and characteristics or signatures of the event.
Indicators of compromise.
Relevant IP addresses and their timestamps.
Device identifiers.
Methodologies used.
Other information we believe is relevant.
SAR Filing Requirements
SARs must be filed no later than 30 calendar days from the date of initial detection.  If no subject can be identified, the time period for filing is extended to 60 days.  The time period to file a SAR starts when we, in the course of our review or as a result of other factors, reach the conclusion that we know or have reason to suspect that activity meets one or more definitions of suspicious activity.  “Initial detection” should not necessarily be interpreted as meaning the moment a transaction is highlighted for review.  
When a SAR is filed, we must review account activity for the subsequent 90 days following the filing to determine whether the suspicious activity has persisted. If suspicious activity has continued, we must file a SAR for continuous suspicious activity.  FinCEN guidance allows for an expanded filing deadline for continuous suspicious activity.  We may file SARs for continuous suspicious activity after a 90-day review, with the filing deadline being 120 days after the date of the previously related SAR.
For situations requiring immediate attention, in addition to filing a timely SAR, we must immediately notify, by telephone, an “appropriate law enforcement authority” and, as necessary, our primary regulator.  For this initial notification, an appropriate law enforcement authority would generally be the local office of the IRS Criminal Investigation Unit or the FBI.  Notifying law enforcement of a suspicious activity does not relieve us of our obligation to file a SAR.
Suspicious Activity Reporting Safe Harbor
Federal law provides protection from civil liability for all reports of suspicious transactions made to appropriate authorities, including supporting documentation regardless of whether such reports are filed pursuant to SAR instructions. Specifically, the law provides that a bank and its directors, officers, employees and agents that make a disclosure to the appropriate authorities of any possible violation of law or regulation, including a disclosure in connection with the preparation of SARs, “shall not be liable to any person under any law or regulation of the United States, any constitution, law or regulation of any State or political subdivision of any State, or under any contract or other legally enforceable agreement (including any arbitration agreement), for such disclosure or for any failure to provide notice of such disclosure to the person who is the subject of the such disclosure or any other person identified in the disclosure”.  The safe harbor applies to SARs filed with the required reporting thresholds as well as SARs filed voluntarily on any activity below required thresholds.  
Systems to Identify, Research and Report Suspicious Activity
Suspicious activity monitoring and reporting are critical internal controls. Proper monitoring and reporting processes are essential to ensuring that the bank has an adequate and effective BSA compliance program.  Generally effective suspicious activity monitoring and reporting systems include 5 key components:  
Identification or alert of unusual activity, which may include:  employee identification, law enforcement inquiries other referrals and transaction and surveillance monitoring system output.  
Managing alerts.
SAR decision-making.
SAR completion and filing.
Monitoring and SAR filing on continuous activity.
These components are interdependent.  Breakdowns in any one or more of these components may adversely affect SAR reporting and BSA compliance.   
Identification of Unusual Activity
We use multiple methods to identify potentially suspicious activity, including but not limited to activity identified by employees during daily operations, law enforcement inquiries, advisories issued by regulatory or law enforcement agencies, transaction and surveillance monitoring system output or any combination of these methods.  
Employee Identification:  During the course of daily operations, employees may observe unusual or potentially suspicious transaction activity.  BankClient ensures bank staff receive BSA training annually, at a minimum, to ensure staff are knowledgeable of possible red flags] for suspicious activity.  [Describe escalation process Please refer to Appendix F of the FFIEC BSA/AML Examination Manual for examples of money laundering and terrorist financing “red flags”.

Law Enforcement Inquiries and Requests:  We must maintain processes for identifying subjects of law enforcement requires, monitoring the transaction activity of those subjects when appropriate, identifying unusual or potentially suspicious activity related to those subjects and filing, as appropriate, SARs related to those subject.  Law enforcement inquiries and requests can include grand jury subpoenas, National Security Letters and section 314(a) requests.

Mere receipt of any law enforcement inquiry does not, by itself, require the filing of a SAR by the bank. However, a law enforcement inquiry may be relevant to our customer and account risk assessments.  We should assess all the information we know about our customer, including the receipt of a law enforcement inquiry, in accordance with our BSA/AML compliance program.  We should determine whether a SAR should be filed based on all customer information available.  
Managing Alerts
Alert management focuses on processes used to investigate and evaluate identified unusual activity.  We must be aware of all methods of identification and should ensure our suspicious activity monitoring program includes processes to evaluate any unusual activity identified, regardless of the method of identification.  
SAR Decision-Making Process
After thorough research and analysis has been completed, findings are forwarded to [decision maker].  We have outlined the following escalation process from the point of initial detection to disposition of the investigation, as shown below.  [Describe escalation process]
We document our decisions to file a SAR, including specific reasons for not filing a SAR as thorough documentation provides a record of or SAR decision-making process, including final decisions not to file a SAR.  [Describe documentation and where it is maintained]
SAR Filing on Continuous Activity
One purpose of filing SARs is to identify violations or potential violations of law to the appropriate law enforcement authorities for criminal investigation.  This objective is accomplished by the filing of a SAR that identifies the activity of concern.  If this activity continues out a period of time, such information should be made known to law enforcement and the federal banking agencies.  FinCEN guidance allows for an expanded filing deadline for continuous suspicious activity.  We may file SARs for continuous suspicious activity after a 90-day review, with the filing deadline being 120 days after the date of the previously related SAR. However, we may file SARs on continuing activity earlier than the 120-dy deadline if we believe the activity warranted earlier review by law enforcement.  This practice notifies law enforcement of the continuing nature of activity in aggregate.  In addition, this practice reminds us that we should continue to review the suspicious activity to determine whether other actions may be appropriate (e.g. terminating the relationship with the customer who is the subject of the filing).  
Law enforcement may have an interest in ensuring certain accounts remain open notwithstanding suspicious or potential criminal activity in connection with those accounts. If a law enforcement agency requests that we maintain a particular account, we must ask for a written request.  The written request must indicate that the agency has requested that we maintain the account and the purpose and duration of the request.  Ultimately, however, the decision to maintain or close an account is ours.  As such, we have outlined the following escalation process for repeat SAR filings. [Describe escalation process]
SAR Completion and Filing
SAR completion and filing are a critical part of the SAR monitoring and reporting process.    [Describe process for SAR completion. Who is responsible for completing and filing SARs?  Is there an internal check to ensure narratives are adequate and that SARs are filed within regulatory timeframes?]
Notifying the Board of SAR Filings
We are required to notify the Board of Directors or an appropriate subcommittee, that SARs have been filed.  However, the regulations do not mandate a particular notification format.  We may, but are not required to, provide actual copies of SARs to the Board or a Board subcommittee. However, given the sensitivity of the information contained within SARs and liability for inadvertent or willing disclosure, we have opted to provide the Board summaries of SAR filings in general terms.  [What is the timeframe for reporting SARs to the Board?]
Closing an Account Due to Continuous Suspicious Activity
We may find it necessary to close an account due to continuing suspicious activity. Decisions to close an account due to ongoing continuous activity are subject to an escalation and decision-making process as outlined on the preceding pages.  
Law enforcement may have an interest in ensuring certain accounts remain open notwithstanding suspicious or potential criminal activity in connection with those accounts. If a law enforcement agency requests that we maintain a particular account, we must ask for a written request.  The written request must indicate that the agency has requested that we maintain the account and the purpose and duration of the request.  Ultimately, however, the decision to maintain or close an account is ours.
It is the responsibility of the Security Officer, the BSA Officer and the CEO to determine when it is prudent to close an account due to continuous suspicious activity.  
Prohibition of SAR Disclosure
No bank, and no director, officer, employee or agent of a bank that reports a suspicious transaction may notify any person involved in the transaction that the transaction has been reported.  A SAR and any information that would reveal the existence of a SAR, as confidential, except as is necessary to fulfill BSA obligations and responsibilities.  For example, the existence or even the non-existence of a SAR must be kept confidential, as well as the information contained in the SAR to the extent the information would reveal the existence of a SAR.  
Documentation of Circumstances in which SARs have been considered, but Not Filed
After reviewing facts and circumstances, we may determine that a SAR filing is not warranted for activity flagged as possibly suspicious. In these cases, documentation is retained to support our decision not to file a SAR.  For each of these circumstances, we review the files 90 days after the decision not to file a SAR is made to determine whether possibly suspicious activity has continued.  
Suspicious Activity Reporting Record Retention
We must retain copies of SARs and supporting documentation for 5 years from the filing date.   We must provide all documentation supporting the filing a SAR upon request by FinCEN or an appropriate law enforcement or federal banking agency.  
Currency Transaction Reporting
We must monitor for and report cash transactions in excess of $10,000 in one business day.  Total cash in and cash out must be considered. However, ins and outs are not combined; they are totaled separately.  Multiple transactions conducted on one business day will be aggregated to determine whether they exceed $10,000 and are therefore reportable.  Transactions include:  denomination exchanges, IRAs, deposits, withdrawals, loan payments, ATM transactions, purchases of CDs, exchanges, cash received for funds transfers, cash used to purchase monetary instruments, conversion of currency to prepaid access and transactions involving armored car services.  
Aggregation of Currency Transactions
Multiple currency transactional totaling more than $10,000 during any on business day are treated as a single transaction if we have knowledge that they are by or on behalf of the same person. [Describe aggregation process] In cases where multiple businesses share a common owner, the presumption is that separately incorporated entities are independent persons.  The currency transactions of separately incorporated businesses should not automatically be aggregated as being on behalf of any one person simply because those businesses are owned by the same person.  We must determine whether multiple businesses that share a common owner are being operated independently.  If we determine that these businesses (or one or more of the businesses and the private accounts of the owner) are not operating separately or independently of one another or their common owner (e.g. the businesses are staffed by the same employees and are located at the same address, the bank accounts of one business are repeatedly used to pay the expenses of another business, or the business bank accounts are repeatedly used to pay the payroll expenses of the owner) we may determine that aggregating the businesses’ transactions is appropriate because the transactions were made on behalf of a single person.
If we determine that the businesses are independent, we should not aggregate separate transactions for these businesses.   
CTR Completion and Filing
CTRs must be filed no later than 15 days after the transaction.  
Currency Transaction Reporting Exemptions
The Money Laundering Suppression Act of 1994 established a two-phase exemption process. Under Phase I exemptions, transactions in currency by banks, governmental departments or agencies and listed public companies and their subsidiaries are exempt from reporting.  Under Phase II exemptions, transactions in currency by smaller businesses that meet specific criteria may be exempted.  

We must file a one-time Designation of Exempt Person Report (DOEP) to exempt from currency transaction reporting:
Each eligible listed companies or eligible subsidiaries.

Phase II exemptions.
The report must be filed electronically through the BSA E-Filing System within 30 days after the first transaction in currency that the bank wishes to exempt. We do not need to file a DOEP Report for Phase I customers that are banks, federal, state or local governments, or entities exercising governmental authority.  
The information supporting each designation of a Phase I-exempt listed public company/subsidiary and Phase II exempt person must be reviewed and verified by the bank at least annually. We must document the annual review and verify at least annually that the Phase II exemptions are monitored for suspicious transactions.
An ineligible business is defined as a business engaged primarily in one or more of the following activities:
Serving as a financial institution or as agents for a financial institution of any type.
Purchasing or selling motor vehicles of any kind, vessels, aircraft, farm equipment or mobile homes.
Practicing law, accounting or medicine.
Auctioning of goods.
Chartering or operation of ships, buses or aircraft.
Operating a pawn brokerage.
Engaging in gaming of any kind.
Engaging in investment advisory services or investment banking services.
Operating a real estate brokerage.
Operating in title insurance activities and real estate closings.
Engaging in trade union activities.
Engaging in any other activity that may, from time to time, be specified by FinCEN, such as a marijuana-related business.
A business that engages in multiple business activities may qualify for an exemption as a non-listed business as long as no more than 50% of its gross revenues per year are derived from one or more of the ineligible business activities listed above.  
Safe Harbor for Failure to File CTRs
CTR rules provide a safe harbor that a bank is not liable for the failure to file a CTR for a transaction in currency by an exempt person, unless the bank knowingly provides false or incomplete information or has reason to believe that the customer does not qualify as an exempt customers.  In the absence of any specific knowledge or information indicating that a customer no longer meets the requirements of an exempt person, we are entitled to a safe harbor from civil penalties to the extent we continue to treat the customer has an exempt customer until the date of the customer’s annual review.
CTR Exemption Record Retention
We must retain copies of CTRs for 5 years from the date of filing.  
Information Sharing under the USA PATRIOT Act
On September 26, 2002, final regulations implementing section 314 of the USA PATRIOT Act became effective.  The regulations established procedures for information sharing to deter money laundering and terrorist activity. On February 5, 2010, FinCEN amended the regulations to allow state, local and certain foreign law enforcement agencies access to the information sharing program.
Section 314(a) Information Sharing
A federal, state, local or foreign law enforcement agency investigating terrorist activity or money laundering may request that FinCEN solicit, on its behalf, certain information from a financial institution or a group of financial institutions.  Upon receiving a completed written certification from a law enforcement agency, FinCEN may require us to search our records to determine whether we maintain or have maintained accounts for, or have engaged in transactions with, any specified individual, entity or organization
When we receive an information request, we must conduct a one-time search of our records to identify accounts or transactions of a named suspect.  Unless otherwise instructed by an information request, we must search our records for currency accounts, accounts maintained during the preceding 12 months and transactions conducted outside of an account by or on behalf of a named suspect during the preceding 6 months.  We must search or records and report any positive matches to FinCEN within 14 days, unless otherwise specified in the information request. [Who are the points of contact?  What is the search process?  How are searches documented?]
The contents of these requests are confidential and are subject to similar controls established to comply with section 501 of the Gramm-Leach-Bliley Act for the protection of customers’ non-public personal information.  
Section 314(b) Information Sharing
Section 314(b) encourages financial institutions and associations of financial institutions located in the U.S. to share information in order to identify and report activities that may involve terrorist activity or money laundering.  Section 314(b) also provides specific protection from civil liability.  To avail our bank to the statutory safe harbor from liability, we must notify FinCEN of our intent to engage in information sharing and communicate that we have established and will maintain adequate procedures to protect the security and confidentiality of information shared.  A notice to share is effective for 1 year.  BankClient does not participate in information sharing practices under Section 314(b).
Purchase and Sale of Monetary Instruments
Banks sell a variety of monetary instruments (e.g. bank checks or drafts, including foreign drafts, money orders, cashier’s checks and traveler’s checks) in exchange for currency.  Purchasing these instruments in amounts of less than $10,000 is a common method used by money launderers to evade large currency transaction reporting requirements.  Once converted from currency, criminals typically deposit these instruments in accounts with other banks to facilitate the movement of funds through the payment system.  In many cases, the persons involved do not have an account with the bank from which the instruments are purchased. [Indicate whether MIs are sold to non-customers]
We must verify the identity of personal purchasing monetary instruments for currency in amounts between $3,000 and $10,000 inclusive and to maintain records of all such sales.  Records must be retained for 5 years.
Contemporaneous purchases of the same or different types of instruments totaling $3,000 or more must be treated as one purchase. Multiple purchases during one business day totaling $3,000 or more must be aggregated and treated as one purchase if the bank has knowledge that the purchases have occurred.
We may have a policy to require customers who are deposit accountholders and who want to purchase monetary instruments in amounts between $3,000 and $10,000 with currency to first deposit the currency into their deposit accounts.  Nothing within the BSA or its implementing regulations prohibits a bank from instituting such a policy.  However, FinCEN has taken the position that when a customer purchases a monetary instrument in amounts between $3,000 and $10,000 using currency that the customer first deposits into the customer’s account, the transaction is still subject to recordkeeping requirements.  [Describe whether the bank requires that a customer deposits funds into an existing account in order to purchase a monetary instrument]

Recordkeeping Requirements for Monetary Instrument Sales
We must verify the identity of personal purchasing monetary instruments for currency in amounts between $3,000 and $10,000 inclusive and to maintain records of all such sales.  Records must be retained for 5 years.
Funds Transfers
Funds transfer systems enable the instantaneous transfer of funds, including both domestic and cross-border transfers. Consequently, these systems can present and attractive method to disguise the source of funds derived from illegal activity.  The BSA was amended by the Annunzio-Wylie Anti-Money Laundering Act of 1992 to authorize the U.S. Treasury and the Federal Reserve Board to prescribe regulations for domestic and international funds transfers.  
For each payment order in the amount of $3,000 or more that a bank accepts as an originator, we must obtain and retain:
The name and address of the originator.
Amount of the payment order.
Date of the payment order.
Any payment instructions.
Identity of the beneficiary’s institution.
As many of the following items are received with the payment order:
Name and address of the beneficiary.
Account number of the beneficiary.
Any other specific identifier of the beneficiary.
If the originator is not a bank customer, we must collect and retain the information listed above as well as additional information depending on whether the order is made in person.  

We must retain records of funds transfers of $3,000 or more for 5 years
Travel Rule:  For funds transfers of $3,000 or more, you must include the following information in the order at the time the order is sent to the receiving financial institution:
Name of the transmitter and if the payment was ordered from an account, the account number of the transmitter.
Address of the transmitter.
Amount of the transmittal order.
Date of the transmittal order.
Identity of the recipient’s financial institution.
As many of the following as are received with the order:  
Name and address of the recipient.
Account number of the recipient.
Any other specific identifier of the recipient.
Either the name and address or the numerical identifier of the transmitter’s financial institution.
There are no recordkeeping requirements in the Travel Rule.
If we are receiving a funds transfer, you must retain a record of the payment order for any payment order of $3,000 or more.  If the beneficiary is not an established customer of the bank, we must retain the following information for each payment order of $3,000 or more:

Funds Transfer Recordkeeping
Funds Transfers of $3,000 or More
Or recordkeeping requirements with respect to funds transfer vary based upon our role in the funds transfer transaction.  

Records to Retain as an Originator:
Name and address of originator
Amount of the payment order
Execution date of the payment order
Any payment instruction received from the originator with the payment order
Identity of the beneficiary’s bank
As many of the following items as are receive with the order:  name and address of the beneficiary, account number of the beneficiary, any other specific identifier of the beneficiary
For each payment order that the bank accepts for an originator that is not an established customer of the bank, we must obtain additional information under 31 CFR 1020.410(a)(2)

Records to Retain as an Intermediary or Beneficiary Bank:
We must retain a record of the payment order
For each payment order that the bank accepts for a beneficiary that is not an established customer of the bank, we must obtain additional information under 31 CFR 1020.410(a)(3)
Foreign Correspondent Account Recordkeeping, Reporting & Due Diligence
Foreign correspondent accounts can be a gateway into the U.S. financial system.  Banks are required to establish a due diligence program that includes appropriate, specific, risk-based and where necessary, enhanced policies, procedures and controls that are reasonably designed to enable us to detect and report, on an ongoing basis, any known or suspected money laundering activity conducted through or involving any correspondent account established, maintained, administered or managed by our bank. 
However, BankClient does not maintain any foreign correspondent accounts.  
Private Banking
Private banking can be broadly defined as providing personalized financial services to wealthy clients. Section 312 of the USA PATRIOT Act added a subsection that requires each U.S. financial institution that establishes, maintains, administers or manages a private banking account in the U.S. for a non-U.S. person to take certain AML measures with respect to these accounts. For purposes of 31 CFR 1010.620, a “private banking account” is an account or any combination of accounts maintained at a bank that satisfies all three of the following criteria:
Requires a minimum aggregate deposit of funds or other assets of not less than $1 million.
Is established on behalf of or for the benefit of one or more non-U.S. persons who are direct or beneficial owners of the account.
Is assigned to, or is administered by, in whole or in part, an officer, employee or agent of a bank acting as a liaison between a financial institution covered by the regulation and the direct or beneficial owner of the account.
BankClient does not maintain any private banking relationships as defined by regulatory guidance.
Special Measures under the USA PATRIOT Act
Section 311 of the USA PATRIOT Act authorizes the Secretary of the Treasury to require domestic financial agencies to take certain special measures against foreign jurisdictions, foreign financial institutions, classes of international transactions, or types of accounts of primary money laundering concern.  Section 311 provides the Secretary of the Treasury with a range of options that can be adapted to target specific money laundering and terrorist financing concerns. 
Orders and regulations implementing specific special measures taken under Section 311 are not static; they can be issued or rescinded over time as the Secretary of the Treasury determines that a subject jurisdiction, institution, class of transactions or type of account is no longer of primary money laundering concern.  Our BSA Department maintains several resources that are designed to alert us to any special measures issued. Additionally, we review FinCEN’s website on a monthly basis for current information on final special measures.  
International Transportation of Currency or Monetary Instruments Reporting
Each person, including a bank, who physically transports, mails or ships currency or monetary instruments in excess of $10,000 at one time out of or into the U.S. (and each person who causes such transportation, mailing or shipment) must file a Report of International Transportation of Currency or Monetary Instruments (CMIR).  A CMIR must be filed with the appropriate Bureau of Customs and Border Protection officer or with the commissioner of Customers at the time of entry or departure from the U.S.  When a person receives currency or monetary instruments in an amount exceeding $10,000 at one time that have been shipped from any place outside the U.S., a CMIR must be filed with the appropriate Bureau of Customs and Border Protection officer or with the commissioner of Customs within 15 days or receipt of the instruments, unless a report has already been filed.  The report is to be completed by or on behalf of the person request transfer of the currency or monetary instruments.  
Regardless of whether an exemption from filing a CMIR applies, we are not relieved of other monitoring and reporting obligations under the BSA.  We must report the receipt or disbursement of currency in excess of $10,000 on a CTR. 
As of June 2016, BankClient has not had any transactions conducted through the bank or for its customers that would require a CMIR filing. 
Report of Foreign Bank and Financial Assets
Each person, including a bank, subject to U.S. jurisdiction with a financial interest in, or signature or other authority over, a bank, a securities or other financial account in a foreign country must electronically file a Report of Foreign Bank and Financial Accounts (FBAR) if the aggregate value of these financial accounts exceeds $10,000 at any time during the calendar year.  An FBAR must be filed on or before June 30 of each calendar year for foreign financial accounts where the aggregate vale exceeded $10,000 at any time during the previous calendar year.
As of June 2016, BankClient did not maintain any such accounts that require FBAR filings.
OFAC
The Office of Foreign Assets Control, an office of the U.S. Treasury, administers and enforces economic trade sanctions based on U.S. foreign policy and national security goals against targeted individuals and entities such as foreign countries, regimes, terrorists, international narcotics traffickers and those engages in certain activities, such as the proliferation of weapons of mass destruction or transnational organized crime.  All U.S. persons, including U.S. banks, bank holding companies and non-bank subsidiaries, must compliance with OFAC’s regulations. In general, the regulations that OFAC administers require us to:
Block accounts and other property of specified countries, entities and individuals.
Prohibit or reject unlicensed trade and financial transactions with specified countries.
OFAC | Blocked Transactions
We must block transactions that:
Are by or on behalf of a blocked individual or entity; 
Are to go through a blocked entity; or,
Are in connection with a transactions in which a blocked individual or entity has an interest.
For example, if we would receive instructions to make a funds transfers payment that falls into one of these categories, we would execute the payment order and place the funds into a blocked account.  A payment order cannot be cancelled or amended after it is received by a U.S. bank in the absence of authorization by OFAC.
OFAC | Prohibited Transactions
In some cases, an underlying transaction may be prohibited, but there is no blockable interest in the transaction (i.e. the transaction should not be accepted, but there is no OFAC requirement to block the assets). In these cases, the transaction is simply rejected.  It is important to note that the OFAC regime specifying prohibitions against certain countries, entities and individuals is separate and distinct from the provision within the BSA’s CIP regulation that requires us to compare new accounts against government lists of known or suspected terrorists prior to account opening.  
OFAC | Licenses
OFAC has the authority, through a licensing process, to permit certain transactions that would otherwise be prohibited under its regulations.  OFAC can issue a license to engage in an otherwise prohibited transaction when it determines that the transaction does not undermine the U.S. policy objectives of particular sanctions programs or is other justified by U.S. national security or foreign policy objectives.  
BankClient does not maintain any licenses with OFAC.
OFAC | Reporting
We must report all blockings to OFAC within 10 business days of the occurrence and annually by September 30th concerning assets blocked (as of June 30th).  We must keep an accurate and full record of each rejected transaction for at least 5 years after the date of the transaction.  
As of June 2016, BankClient has not identified any transactions that require blocking (or subsequent reporting) to OFAC.  
OFAC | Compliance Program & Risk Assessment
While not required by specific regulation, but a matter of sound banking practice and in order to mitigate the risk of non-compliance with OFAC requirements, we must maintain an OFAC compliance program that identifies higher risk areas, provides for appropriate internal controls for screening and reporting, establishes independent testing for compliance, designates a bank employee or employees responsible for OFAC compliance and creates a training program for appropriate personnel in all relevant areas of the bank.  
BankClient’s OFAC Compliance Program is comprised of the following:
Risk Assessment:  We have utilized the FFIEC Risk Assessment Matrix to determine our level of risk of doing business with any individual, entity or other party on the OFAC list.  Based on this risk assessment, attached as Exhibit B to this policy, we have determined our level of risk to be Low.
Internal Controls:  We have implemented controls to ensure we do not do business with any individual, entity or other party on the OFAC list.  All potential customers must be compared to the OFAC list prior to account opening.  For incoming and outgoing wire transfers, the originator and beneficiary are screened against the OFAC list. The employee performing the OFAC check is required to mark the check box beside the originator and beneficiary and must initial the wire transfer form.  If a confirmed positive match is detected for an outgoing wire, the wire should not be sent and BSA Officer must be notified.  If a confirmed positive match is detected for an incoming wire, the funds must be frozen and the BSA Officer must be contacted.
Tellers are required to screen all non-customers against the OFAC list who initiate cash advances or for check cashing services equal to or greater than $1,000, including the sale of monetary instruments.  
Our customer base is screened against the OFAC list on a daily basis.  When the bank receives notification that the OFAC list has been updated, the updated list is imported into the bank’s system. When the report is complete, a full scan of the customer base is performed and possible matches are reviewed by the BSA Officer.  
Independent Testing:  The scope of our BSA audit (both for the core bank and prepaid card function) incorporates an assessment of OFAC compliance.  
Individual Responsible for OFAC Compliance:  The Board has designated individuals who are responsible for OFAC compliance, as outlined within the bank’s organizational chart.   These individuals are responsible for ongoing oversight and administration of our OFAC compliance program.
Training:  OFAC compliance requirements are incorporated into bank-wide BSA training that is primarily accomplished through our annual all-employee in-service day.  BSA training is also incorporated into Board compliance training.
Correspondent Accounts
Banks maintain correspondent relationships at other domestic banks to provide certain services that can be performed more economically or efficiency because of the other bank’s size, expertise in a certain line of business or geographic location.  Such services may include:
Deposit Accounts:  “Due from bank” accounts, which represent the bank’s primary operating account.
Funds Transfers: A transfer of funds between banks may result from the collection of checks or other cash items, transfer and settlement of securities transactions, transfer of participating loan funds, purchase or sale of federal funds or processing of customer transactions.
Other services:  Services include processing loan participations, facilitating secondary market loan sales, performing data processing and payroll services and exchanging foreign currency.
Because domestic banks must follow the same regulatory guidelines, BSA/AML risk in domestic correspondent baking, including bankers’ banks are minimal in comparison to other types of financial services.  
BankClient does not maintain any foreign correspondent banking relationships.
Bulk Shipments of Currency
Bulk shipments of currency entails the transportation of large volumes of U.S. or foreign bank notes. Bulk shipments of currency can be sent from sources either inside or outside the U.S. to a bank in the U.S. Shipments can also made from a bank in the U.S. to a recipient in a foreign jurisdiction. [Describe bank’s exposure to bulk shipments of currency]
Electronic Banking
E-banking systems, which provide electronic delivery of banking products to customers, include ATM transactions; online account opening; internet banking transactions; and, telephone banking.  BankClient offers Internet banking (e.g. online banking, bill pay, electronic statements, mobile banking, telephone banking and debit cards).  Mobile banking was introduced to customers in 2011, which allowed customers to access mobile banking via a mobile application; view account balances and activity; make transfers, schedule bill payments or delete a scheduled payment; and, find the nearest branch or ATM.  In 2014, BankClient introduced mobile deposit to allow customers to deposit checks from their smart phones using the mobile banking application.  Limitations (e.g. per check limits, daily limits and revolving 30-day limit) were implemented.  Each user must meet certain criteria to be approved to use the service, including length of time the deposit account has been opened, average deposit amounts, etc.  Due to the risk of check fraud and duplicate items through mobile deposit, deposited and rejected items are reviewed daily by the bank’s data processing department.
We must ensure that our monitoring systems adequately capture transactions conducted electronically.  We must be alert to anomalies in account behavior, such as velocity of funds in the account, or in the case of ATMs, the number of debit cards associated with an account.  
Remote Deposit Capture
Remote deposit capture (RDC) is a deposit transaction delivery system that has made check and monetary instrument processing (e.g. traveler’s checks or money orders) more efficient.  In broad terms, RDC allows our customers to scan a check or monetary instrument and then transmit the scanned image to our bank.  Scanning and transmission activities occur at remote locations.  RDC may expose us to various risks, including money laundering, fraud and information security.  Fraudulent, sequentially numbered or physically altered documents, particularly money orders and traveler’s checks, may be more difficult to detect when submitted by RDC and not inspected by a qualified person. 
We have implemented the following controls over our RDC products: [Describe RDC controls]

ACH Transactions
Traditionally, the ACH system has been used for the direct deposit of payroll and government benefit payments and for the direct payment of mortgages and loans.  However, usage has expanded to include one-time debits and check conversation.  Examples include credit payroll direct deposits, social security, dividends, interest payments, mortgage and other loan payments, insurance premiums and a variety of other consumer payments initiated through merchants or businesses. [Describe bank’s ACH exposure. Does the bank originate and receive?]
International ACH Payments
The IAT is a Standard Entry Class code for ACH payments that enables us to identify and monitor international ACH payments and perform screening to ensure compliance with OFAC requirements. [Describe bank’s IAT exposure and processes]
Third Party Service Providers
A third party service provider (TPSP) is an entity other than an originator, ODFI or RDFI that performs any functions on behalf of an originator, ODFI or RDFI with respect to the processing of ACH entries.  The ACH system was designed to transfer a high volume of low-dollar domestic transactions, which pose lower BSA/AML risks. However, the ability to send out high-dollar and international transactions may expose us to higher BSA/Aml risks.  ACH transactions that are originated through a TPSP may also increase BSA/AML risks, making it difficult for an IDFO to underwrite and review originator transactions for compliance with BSA/AML rules.  Risks are heightened when neither the TPSP nor the ODFI performs due diligence on the companies for whom they are originating payments. [Describe the bank’s TSPS exposure and controls]
Prepaid Access
BankClient has established a growing prepaid access line of business that has increased the bank’s risk profile with regard to the size and complexity of the programs as well as regulatory scrutiny over administration of this line of business.  Inherently, this line of business presents elevated levels of risk.  Law enforcement investigations have found that some prepaid cardholders have used false identification and funded their initial loads with stolen credit cards, or have purchased multiple prepaid cards under aliases.  In the placement phase of money laundering, criminals may load cash from illicit sources onto prepaid access products and send them to accomplices inside or outside the United States.  Investigations have disclosed that both open- and closed-loop prepaid cards have been used in conjunction with, or as a replacement to, bulk cash smuggling.  Transactions may pose the following unique risks to the bank:
Funds may be transferred to or from an unknown third party.
Verification of cardholder identity may be done entirely remotely, relying on third party program managers, processors or distributors.
As with other modes of electronic payments, holders may be able to use prepaid access products internationally, thus avoiding border restrictions and reporting requirements applicable to cash and monetary instruments.
Transactions may be credited or debited to the user’s payment product immediately, although there may be a lag in delivery of funds to the issuing bank, creating a load timing risk for the bank.
Specific holder activity may be difficult to determine by reviewing activity through a pooled account.
Data in underlying pooled accounts may be held or managed by third parties, separate from the issuing bank.
Marketing of payment products, customer service and onboarding of new customers may be handled primarily by third parties separate from the issuing bank.  
The customer may perceive the transactions as less transparent.
Source of payroll funding may come through an intermediary bank and may not be transparent.

To help mitigate BSA, fraud and other risks, as well as to address regulatory concern, BankClient has implemented several controls within its prepaid access function.  The bank created a Prepaid Card Program Committee, which has primary and ongoing oversight of the prepaid access function.  Over the last twelve (12) months, the committee has developed a multi-layered oversight process.  Detailed Fact Sheets were developed for each program. The data within these fact sheets was then used to create risk assessments for each program. Fact sheets and risk assessments provide consistency in program documentation and assessment.  In 2016, these documents were expanded to include a cover sheet that provides a “snapshot” of each program.  
The Committee has applied this process to new and existing programs.  These documents and the resulting risk then flows through to the bank’s Global Prepaid Card Risk Assessment and Policy, which lay out the framework for program administration.  

The bank relies on third-party program managers to employ identity verification processes to reasonably identify card applicants for programs that require KYC procedures.  Management has established testing procedures to ensure these processes are being followed by program managers.  Any CIP failures identified by the bank during testing are relayed back to the program manager for further information and possible blocking of cardholder funds until appropriate customer information is obtained.  

Each program has predetermined load and balance caps as well as other thresholds. Activity is monitored on an ongoing basis and any activity outside the established thresholds is brought to the attention of program managers. Depending on the severity of the issue (i.e. dollar amount involved and/or frequency of attempts) the card may be closed and/or a suspicious activity report filed.

Representatives from the Prepaid Card Program Committee routinely communicate with program managers.  The Committee meets on an ongoing basis via teleconference, with meeting typically held every other week. Meetings are conducted according to an established agenda and minutes of meeting discussions are formally documented.  

Ongoing education has been identified as critical to ongoing effective administration of the bank’s prepaid card function.  Each member of the committee has been assigned, and must successfully complete, training specifically designed for those involved in the prepaid industry.  Additionally, the BSA and Assistant BSA Officers successfully completed coursework and testing under the Certified Anti-Money Laundering Specialist program sponsored by the Association of Certified Anti-Money Laundering Specialists (ACAMS).    

Independent testing primarily focused on the bank’s prepaid access function has also been identified as a critical control. In 2015, BankClient engaged a third party (Crowe) to perform a comprehensive audit of the bank’s prepaid card function.  This audit resulted in the identification of several control and administrative weaknesses within the program.  Management has incorporated these findings into the bank’s BSA Program Action Plan. Progress in addressing prepaid, as well as all BSA-related findings, is routinely monitored, discussed and documented.  
Third Party Payment Processors
Non-bank or third party payment processors are bank customers that provide payment-processing services to merchants and other business entities. These processors are not generally subject to BSA/AML requirements. As a result, some processors may be vulnerable to money laundering, identity theft, fraud schemes or other illicit transactions, including those prohibited by OFAC. [Describe bank’s exposure TPPPs]
Brokered Deposits
The use of brokered deposits is a common funding source for many banks. Deposit brokers provide intermediary services for banks and investors. This activity is considered higher risk because each deposit broker operates under its own guidelines for obtaining deposits.  Money laundering and terrorist financing risks arise because we may not know the ultimate beneficial owners or the sources of funds.  The deposit broker could represent a range of clients that may be of higher risk for money laundering and terrorist financing.
BankClient acquires brokered deposits through US Sterling and Depository Trust Company (DTC).  US Sterling matches potential financial institution investors with an institution looking for brokered deposits. US Sterling is a federally regulated entity. CDs are opened in the names of client financial institutions. As such, the underlying financial institutions are exempt from CIP. However, BankClient screens the institutions against the OFAC list when wire deposits are received.
DTC brokered CDs are opened with a tax ID number of DTC and all CDs are titled as CEDE and Co, in care of DTC.  
US Sterling is registered with FINRA and maintains a BSA/AML compliance program that includes OFAC policies and procedures, all of which are on file at BankClient.  The procedures state that US Sterling is responsible for CIP, OFAC, FinCEN and Treasury recording and reporting.  DTC is a member of the Federal Reserve.  Brokered deposits from US Sterling and DTC are considered low risk due to their clients being financial institutions, which are federal regulated and therefore exempt from CIP requirements.  
Privately Owned ATMs
Privately owned ATMs are particularly susceptible to money laundering and fraud.  Privately owned ATMs are typically found in convenience stores, bars, restaurants, grocery stores or check cashing establishments.  Most dispense currency, but some dispense only a paper receipt (scrip) that the customer exchanges for goods or services.  Fees and surcharges for withdrawals, coupled with additional business generated by customer access to an ATM, make the operation of a privately owned ATM profitable.  Money laundering can occur through privately owned ATMs when an ATM is replenished with illicit currency that is subsequently withdrawn by legitimate customers.  [What is the bank’s exposure to privately owned ATMs?  What are the controls?]
The BSA software platform account opening workflow incorporates questions related to a potential customer’s operation of privately owned ATMs.
Non-Deposit Investment Products and Insurance
We offer non-deposit investment products and insurance through a joint marketing arrangement IPI Financial.  Under this relationship, BankClient maintains a dual employee arrangement with IPI Financial whereby the bank’s NDIP and insurance professional is dually employed by the bank and IPI Financial.  Because of this dual-employee arrangement, we retain responsibility over NDIP activities.  [What is this arrangement?  Per BSA guidance, even if contractual agreements establish the financial services corporation as being responsible for BSA/AML the bank needs to ensure proper oversight of its employees, including dual employees and their compliance with all regulatory requirements.]
Concentration Accounts
Concentration accounts are internal accounts established to facilitate the processing and settlement of multiple or individual customer transactions within the bank, usually on the same day.  Money laundering risk can arise in concentration accounts if the customer-identifying information, such as name, transaction amount and account number, is separated from the financial transaction.  If separation occurs, the audit trail is lost and accounts may be misused or administered improperly. [Describe the usage and internal controls over concentration accounts]
Custodial CDs
BankClient  maintains a custodial CD program.  Due to the nature of these products, associated risk, as defined by regulatory guidance, is considered to be high.  [Describe the controls over the custodial CD program.  What is the monitoring process?]
Check Cashing for Non-Customers
BankClient will cash on-us checks for non-customers. Tellers, frontline personnel and customer service representatives must record all BankClient checks cashed for non-customers when checks total $1,000 or more per item.  The following information must be logged for each such transaction:
The payee’s name.
Date of transaction.
Amount of the check presented.
Records must be maintained for 5 years.  Employees are responsible for monitoring transactions for suspicious activity, such as unsigned checks, blank payees and structured transactions.  
Lending Activities
Lending activities include, but are not limited to, real estate, trade finance, cash-secured, credit card, consumer, commercial and agricultural.  Lending activities can include multiple parties (e.g. guarantors, signatories, principals and loan participants).  The involvement of multiple parties may increase the risk of money laundering or terrorist financing when the source of funds are not transparent.  This lack of transparency can create opportunities in any of the three stages of money laundering or terrorist financing schemes.  All loans are considered to be accounts for purposes of the CIP regulations.  As such, we have implemented procedures to ensure all parties to loan transactions we originate are subject identity verification and OFAC screening prior to disbursement of loan proceeds.  Additionally, we have implemented procedures by which lending transactions are monitored for suspicious activity on an ongoing basis. [Describe procedures]
Trade Finance Activities
Trade finance typically involves short-term financing to facilitate the import and export of goods. These operations can involve payment if documentary requirements are met (i.e. letter of credit) or may instead involve payment if the original obligor defaults on the commercial terms of the transaction (e.g. guarantees or standby letters of credit).  In both cases, a bank’s involvement in trade finance minimizes payment risk to importers and exporters.  However, the international trade system is subject to a wide range of risks and vulnerabilities that provide criminal organizations with the opportunity to launder the proceeds of crime and move funds to terrorist organizations with a relatively low risk of detection.
As of June 2016, BankClient does not maintain any trade finance arrangements.
Trust and Asset Management Services
Trust accounts are generally defined as a legal arrangement in which one party transfers ownership of assets to a person or bank to be held or used for the benefit of others.  Trust and asset management accounts, including agency relationships, present BSA/AML concerns similar to those of deposit taking, lending and other traditional banking activities. Concerns are primarily due to the unique relationship structures involved when the bank handles trust and agency activities.
As of June 2016, BankClient does not offer trust or asset management services. 
High Balance Customers
We run an internal report every 6 months to identify all customers or related and aggregated accounts with a minimum of $1 million on deposit. The report is reviewed for unusual fluctuations, ACH activity, cash transactions or transactions outside of the customer’s typical activity pattern.
Non-Resident Aliens and Foreign Individuals
Foreign individuals maintaining relationships with U.S. banks can be divided into two categories:  aliens and non-resident aliens (NRAs).  For definitional purposes, an NRA is a non-U.S. citizen who:  is not a lawful permanent resident of the U.S. during the calendar year and who does not meet the substantial presence test OR has not been issued an alien registration receipt card (i.e. Green Card).  Although NRAs are not permanent residents, they may have a legitimate need to establish an account relationship with a U.S. bank.  NRAs use bank products and services for asset preservation, business expansion and investments.   It may be difficult to verify and authenticate an NRA accountholder’s identification, source of funds, and source of wealth, which may result in BSA/AML risks.  We have implemented procedures to identify NRAs at the time of account opening and to ascertain the level of risk each NRA may present to our bank, based on factors such as:
Accountholder’s home country.
Types of products and services used.
Forms of identification.
Source of wealth and funds.
Unusual account activity.
Risk levels are initially determined through completing the account opening workflow within our BSA software platform and are supported by ongoing behavior-based monitoring within the system.
When an NRA requests to open a deposit account, the account opening employee must notify the BSA Officer to ensure proper procedures are followed.  
Politically Exposed Persons
We must take reasonable steps to ensure that we do not knowingly or unwittingly assist in hiding or moving the proceeds of corruption by senior political figures (domestic and foreign), their families or their associates.  Because the risks presented by PEPs vary by customer, product and service, country and industry, identifying, monitoring and designing controls for these accounts and transactions must be risk-based.
To determine whether an accountholder is a domestic or foreign senior political figure, we utilize the account opening workflow in our BSA software platform to ask relevant questions that would surface such association. 
BankClient maintains no account relationships with domestic or foreign senior political figures.
Non-Bank Financial Institutions and MSBs
NBFIs are broadly defined as institutions other than banks that offer financial services.  Common examples of NBFIs include, but are not limited to:
Casinos and card clubs.
Securities and commodities firms.
Money service businesses.
Insurance companies.
Loan or finance companies.
Operators of credit card systems.
Other financial institutions (e.g. dealers in precious metals, stones or jewels; pawnbrokers).
NBFIs are extremely diverse, ranging from large multi-national corporations to small, independent businesses that offer financial services only as an ancillary component to their primary business (e.g. grocery store that offers check cashing).  The range of products and services offered, and the customer bases served by NBFIs, are equally diverse.  As a result of diversity, some NBFIs may be lower risk and some may be higher risk for money laundering.
To determine whether any existing or potential customer operates as an NBFI or MSB, we have built relevant questions into the our BSA software platform account opening workflow.
When an MSB is identified, we must follow specific procedures to ensure the MSB is appropriately registered with FinCEN as an MSB.  We must also undertake the following actions to mitigate BSA/AML risk associated with MSB activities:
Confirm the MSB is subject to examination for AML compliance by the IRS or state, as applicable.
Affirm the existence of a written BSA/AML program and verify the BSA Officer’s name and contact information.
Ensure the MSB’s established banking relations and/or account activity is consistent with expectations.
Ensure the MSB is an established business with an operating history.
Determine whether the MSB provides services only to local residents.
Determine whether the MSB is a principal with one or a few agents, or its acting like an agent for one principal.
Determine whether the MSB’s customers conduct routine transactions in low dollar amounts.
Determine whether the MSB’s business operations are consistent with information obtained at the time of account opening.
Determine whether money transmitting activities are limited to domestic entities or limited to lower dollar amounts.
As of June 2016, BankClient does not maintain any account relationships with NBFIs or MSBs within the “core” bank.  However, BankClient  has exposure to MSBs through or prepaid access/card program.  To monitor these relationships and conduct ongoing monitoring, we have implemented an MSB risk assessment that is designed to determine the level of risk posed to the bank from these ongoing relationships.
Professional Service Providers
A professional service provider (PSP) acts as an intermediary between its client and the bank. PSPs include lawyers, accountants, investment brokers and other third parties that act as financial liaisons for their clients.  These providers may conduct financial dealings for their clients.  For example, an attorney may perform services for a client, or arrange for services to be performed on the client’s behalf, such as settlement of real estate transactions, asset transfers, management of client monies, investment services and trust arrangements. A typical example is interest on lawyers’ trust accounts (i.e. IOLTA).  These accounts contain funds for a lawyer’s various clients and act as a standard bank account with one unique feature:  The interest earned on the account is ceded to the state bank association or another entity for public interest and pro bono purposes.
In contrast to escrow accounts that are set up to serve individual clients, PSP accounts allow for ongoing business transactions with multiple clients. Generally, we have no direct relationship with or knowledge of the beneficial owners of these accounts, who may be a constantly changing group of individuals and legal entities.
Within our account opening workflow in our BSA software platform, we ask specific questions designed to determine whether a customer could be classified as a PSP.  In rating the risk associated with any customer, including PSPs, our workflow takes into account risk factors, in addition to the nature of our customer’s business, to determine the level of BSA/AML risk exposure to our bank.
Non-Governmental Organizations and Charities
Within our account opening workflow in our BSA software platform, we ask specific questions designed to determine whether a customer could be classified as an NGO or charity.  In rating the risk associated with any customer, including NGOs and charities, our workflow takes into account risk factors, in addition to the nature of our customer’s business, to determine the level of BSA/AML risk exposure to our bank
Business Entities | Domestic and Foreign
Within our account opening workflow in our BSA software platform, we ask specific questions designed to determine whether a customer could be classified as a domestic or foreign business entity.  In rating the risk associated with any customer, including domestic and foreign business entities, our workflow takes into account risk factors, in addition to the nature of our customer’s business, to determine the level of BSA/AML risk exposure to our bank
As of June 2016, BankClient does not maintain account relationships with any foreign business entities.  Domestic business entities are subject to ongoing monitoring conducted through our BSA software platform. Accounts presenting moderate or high risk are subject to additional monitoring and review.
Cash Intensive Businesses
Within our account opening workflow in our BSA software platform, we ask specific questions designed to determine whether a customer could be classified as a cash intensive business.  In rating the risk associated with any customer, including cash intensive businesses, our workflow takes into account risk factors, in addition to the nature of our customer’s business, to determine the level of BSA/AML risk exposure to our bank
Cash intensive businesses are subject to ongoing monitoring conducted through our BSA software platform. Accounts presenting moderate or high risk are subject to additional monitoring and review.
Banking Marijuana-Related Businesses
The Controlled Substances Act (CSA) makes it illegal under federal law to manufacture, distribute or dispense marijuana.  Many states impose and enforce similar prohibition. Notwithstanding the federal ban, 29 states and the District of Columbus have legalized the use of medical marijuana, while 6 states have also legalized the use of recreational marijuana.  Because of the disconnect between federal and state laws concerning marijuana manufacture, distribution, dispensary and use, former United States Deputy Attorney General James M. Cole issued a memorandum (Cole Memo) to all U.S. Attorneys providing guidance to federal prosecutors concerning marijuana enforcement under the CSA.  The Cole Memo guidance applied to all Department of Justice enforcement activity, including civil enforcement and criminal investigations and prosecutions, concerning marijuana in all states.  
However, in January 2018, U.S. Attorney General Jeff Sessions announced his decision to rescind this policy, allowing federal prosecutors to bring forth criminal cases against marijuana manufacturers and distributors.  The decision to reverse policy, given the growth of the cannabis industry caused confusion among financial institutions about how to do business with marijuana manufacturers, distributors and dispensary without running afoul of federal money laundering laws.  
While this policy outlines the provisions of the rescinded Cole Memo and discusses the bank’s required actions to be taken in banking marijuana manufacturers, distributors and dispensaries, it is the policy of BankClient not to do business with identified marijuana-related businesses (MRBs) until resolution is achieved at the federal level.  [You will want to adjust this paragraph, should you do business or plan to do business with MRBs at the state level].
Please refer to the Banking Marijuana Policy maintained under separate cover.
Ponzi & Other Schemes
These types of schemes can offer consistent “profits” only as long as the number of investors continues to increase. The schemes are self-sustaining as long as cash outflows can be matched by monetary inflows. Ponzi schemes are based on fraudulent investment management services. Investors contribute money to the “portfolio manager” who promises them a high return and then when those investors want their money back, they are paid out with the incoming funds contributed by later investors. The individual organizing this fraud is in charge of controlling the entire operation. They merely transfer funds from one client to another and forgo any real investment activities. 
We have trained our staff to look for and report the following red flags that could indicate possible Ponzi schemes:
Customers who provide insufficient or suspicious information 
Customers who are reluctant to comply with reporting and recordkeeping requirements 
Funds transfers to or from a financial secrecy haven 
Unusual transfers of funds between related entities 
Sudden inconsistencies in currency transaction patterns 
Suspicious intracompany transfers and other banking activity by a company combined with establishment of a bank or a branch office in the company’s offices where, due to electronic connections between the bank and company’s systems, bank representatives could monitor all banking activity of the company 
Criminal history of a company’s principals combined with the company’s lack of legitimate business activities, irregular documentation, bank employee visits to discuss company’s business and majority of bank branch employees simultaneously working at the company 
Banking procedures that violated internal rules combined with personal or business ties between the bank and company such as overlapping Boards of Directors or bank employees who were relatives of the company’s principal 
Discovery by a bank of prior criminal history of a company principal, litigation accusing the company of wrongdoing or regulatory enforcement activity concerning the company 
Continued provision of banking services by bank or company even after bank conducted diligence on company’s operations and decided to liquidate bank’s own position in company’s investment funds 
Diversion of funds to accounts not listed in deposit instructions 
Diversion of funds to personal commodities trading accounts 
Attendance by bank representatives at investor meetings where misrepresentations of the bank’s role were made 
Institution of unusual systems by a bank necessary to ensure against repeated “bouncing” of checks by company. 
Activity will monitored through the normal transaction monitoring procedures and will be investigated by the BSA Officer in accordance with our SAR decision-making processes.  
Elder Financial Exploitation
We can play a key role in addressing elder financial exploitation due to the nature of the client relationship.  Older Americans hold a high concentration of wealth as compared to the general population. In the instances where elderly individuals experience declining cognitive or physical abilities, they may find themselves more reliant on specific individuals for their physical well-being, financial management, and social interaction. While anyone can be a victim of a financial crime such as identity theft, embezzlement, and fraudulent schemes, certain elderly individuals may be particularly vulnerable
We have trained our staff to monitor for and report to the BSA Officer the following red flags that may indicate the existence of elder financial exploitation. 
Erratic or unusual banking transactions, or changes in banking patterns: 
Frequent large withdrawals, including daily maximum currency withdrawals from an ATM;
Sudden Non-Sufficient Fund activity;
Uncharacteristic nonpayment for services, which may indicate a loss of funds or access to funds;
Debit transactions that are inconsistent for the elder;
Uncharacteristic attempts to wire large sums of money;
Closing of CDs or accounts without regard to penalties.
Interactions with customers or caregivers: 
A caregiver or other individual shows excessive interest in the elder's finances or assets, does not allow the elder to speak for himself, or is reluctant to leave the elder's side during conversations;
The elder shows an unusual degree of fear or submissiveness toward a caregiver, or expresses a fear of eviction or nursing home placement if money is not given to a caretaker;
The financial institution is unable to speak directly with the elder, despite repeated attempts to contact him or her;
A new caretaker, relative, or friend suddenly begins conducting financial transactions on behalf of the elder without proper documentation;
The customer moves away from existing relationships and toward new associations with other "friends" or strangers;
The elderly individual's financial management changes suddenly, such as through a change of power of attorney to a different family member or a new individual;
The elderly customer lacks knowledge about his or her financial status, or shows a sudden reluctance to discuss financial matters.
Consistent with the standard for reporting suspicious activity as provided for in 31 CFR Part 103 (future 31 CFR Chapter X), if we know, suspect, or have reason to suspect that a transaction has no business or apparent lawful purpose or is not the sort in which the particular customer would normally be expected to engage, and we know of no reasonable explanation for the transaction after examining the available facts, including the background and possible purpose of the transaction, we should file a Suspicious Activity Report, selecting the appropriate characterization of suspicious activity in the Suspicious Activity Information section of the SAR form and include the term "elder financial exploitation" in the narrative portion of all relevant SARs filed. It is important to note that the potential victim of elder financial exploitation should not be reported as the subject of the SAR. Rather, all available information on the victim should be included in the narrative portion of the SAR.
Elder abuse, including financial exploitation, is generally reported and investigated at the local level, with Adult Protective Services, District Attorney's offices, sheriff's offices, and police departments taking key roles. We emphasize that filers should continue to report all forms of elder abuse according to institutional policies and the requirements of state and local laws and regulations, where applicable. 
BSA Recordkeeping Requirements
The BSA establishes recordkeeping requirements related to various types of records including:  customer accounts (e.g. loan, deposits, etc.), BSA filing requirements, and records that document a bank’s compliance with the BSA.  In general, the BSA requires that we maintain most records for at least 5 years. These records can be maintained in many forms, including original, microfilm, electronic, copy or a reproduction.  Whatever the method, we must ensure that the records are accessible in a reasonable period of time.  
The records related to the transactions discussed below must be retained for 5 years. However, as noted, the records related to the identity of a bank customer must be maintained for 5 years after the account is closed. Additionally, on a case-by-case basis, we may be ordered or requested to maintain some of these records for longer periods (e.g. by U.S. Treasury Department Order or law enforcement investigation).
Penalties for Non-Compliance
Penalties for money laundering and terrorist financing can be severe.  A person convicted of money laundering can face up to 20 years in prison and a fine of up to $500,000.  Any property involved in a transaction or traceable to the proceeds of a criminal activity, including property such as loan collateral, personal property or bank accounts, may be subject to forfeiture.  Banks and individuals may incur criminal and civil liability for violating AML and terrorist financing laws.  For example, the Department of Justice may bring criminal actions for money laundering that may include criminal fines, imprisonment and forfeiture actions.  Additionally, we could risk losing our bank charter and bank employees could risk bring removed and barred from banking.  
There are also criminal penalties for willful violations of the BSA and its implementing regulations and for structuring transactions to evade BSA reporting requirements.  For example, a person, including a bank employee, willfully violating the BSA or its implementing regulations is subject to a criminal fine of up to $250,000 or 5 years in prison, or both.  A person who commits such a violation while also violating another U.S. law, or engaging in a pattern of criminal activity, is subject to  a fine of up to $500,000 or 10 years in prison, or both.  A bank that violates certain BSA provisions or special measures, faces criminal penalties up to the greater of $1 million or twice the value of the transaction.
The federal banking agencies and FinCEN can bring civil money penalty actions for violations of the BSA.  In addition to criminal and civil money penalty actions taken against them, individual may be removed from banking for a violation of AML laws.  
All of these actions are publicly available.

Employee Attestation
I, _____________________________, certify that I have received and read BankClient’s BSA Policy. As a condition of my employment with BankClient, I will comply with the requirements and provisions within this policy and its supporting procedures.




EXHIBIT A | CIP Notice

IMPORTANT INFORMATION ABOUT PROCEDURES FOR OPENING A NEW ACCOUNT – To help the government fight the funding of terrorism and money laundering activities, federal law requires all financial institutions to obtain, verify and record information that identifies each person who opens an account. What this means for you:  When you open an account, we will ask for your name, address, date of birth and other information that will allow us to identify you. We may also ask to see your driver’s license or other identifying documents.  








ANTI-MONEY  LAUNDERING
TABLE OF CONTENTS
Anti-Money Laundering/Know Your Customer Policy	2
Introduction	2
Objectives	2
Know Your Customer Standards	5
Prohibited Customers	5
Customer Identification Program (CIP)	6
New Account Review	9
OFAC Screening/Comparison with Government Lists	9
KYC Due Diligence Requirements	10
Money Laundering Risk Ratings	12
Beneficial Ownership Rule………	12
Additional KYC Due Diligence Requirements for Certain Customers, Related Parties, and Accounts	14
New High-Risk Customers	14
Politically Exposed Persons	15
Money Services Businesses	17
Hedge Funds	18
Onboarding of Peer-to-Peer Lending Companies	19
Reliance on Others	19
Ongoing Relationship/Customer/Account Activities	20
Special Measures	24
Information Sharing	24
Subpoenas Received from Law Enforcement	25
Currency Transaction Reporting and Exemptions	26
Safe Harbor Provision	27
Recordkeeping and Record Retention Requirements	27
AML Training	29
BSA/AML Compliance Officer	29
BSA/AML Risk Assessment	30
Independent Testing	30
Board Reporting	30
APPENDIX A	31
APPENDIX B	33
APPENDIX C	38
APPENDIX D	43
APPENDIX E	44
APPENDIX F	46
APPENDIX G	47
APPENDIX H	50
APPENDIX I	51

Anti-Money Laundering/Know Your Customer Policy
Introduction
This Policy establishes a set of minimum standards for identifying, accepting, documenting, and approving customers and maintaining customer relationships.  It also identifies a set of money laundering risk ratings, and includes standards for performing account surveillance, and maintaining records.
Non-compliance with the requirements of this policy could seriously undermine the reputation of and public confidence in the Bank and could result in disciplinary actions against the Bank and its employees, including civil and criminal penalties and other sanctions.
The U.S. Congress enacted the Bank Secrecy Act in October 1970 to prevent banks and other financial service providers from being used as intermediaries to hide the transfer or deposit of money derived from criminal activity.  Since its passage, Congress has amended the BSA a number of times to enhance law enforcement effectiveness.  The reporting and recordkeeping requirements of the BSA regulations create a paper trail for law enforcement to investigate money laundering schemes and other illegal activities.  This paper trail operates to deter illegal activity and provides a means to trace movements of money through the financial system.
The Uniting and Strengthening America by Providing Appropriate Tools Required to Intercept and Obstruct Terrorism Act (USA PATRIOT Act) was signed into law by President Bush on October 26, 2001, and contains strong measures to prevent, detect, and prosecute terrorist financing and international money laundering.  Title III of the USA PATRIOT Act is the International Money Laundering Abatement and Financial Anti-Terrorism Act of 2001.  It includes provisions for fighting international money laundering and blocking terrorist access to the U.S. financial systems.  
Objectives
The primary objective of this Policy is to help protect the good name and reputation of the Bank, and to secure its premises and systems against misuse as a vehicle for money laundering, terrorist financing, and other illegal activities.  Specific objectives include the following:
To ensure compliance with applicable U.S. and local anti-money laundering and anti-terrorist financing laws and regulations while protecting the financial privacy and relationship between the Bank and its customers
To establish minimum standards needed to determine and verify the identity of new customers and any other relevant account parties, and to require the application of enhanced due diligence standards to those customers considered higher-risk as a matter of law or regulations, or based upon the Bank’s own assessment of risk
To set appropriate standards for the ongoing conduct of customer relationships
To institute sound account/transaction surveillance standards as a mechanism for enabling Bank personnel to recognize, detect, and report money laundering, terrorist financing, and/or suspicious activity occurring through Bank accounts
To delineate the responsibilities of employees who implement the Bank’s AML processes.
Policy
The Bank will comply with the U.S. Bank Secrecy Act (BSA), the USA PATRIOT Act, and other applicable AML laws and regulations.  Also the Bank, consistent with applicable law, cooperates with governmental and law enforcement authorities in the enforcement of AML laws and regulations in connection with transactions involving the Bank.
No director, officer or employee of the Company shall:
Knowingly engage in, or assist any other person or entity in engaging in, any activity believed by such director, officer or employee to involve money laundering, terrorist financing or other suspicious or criminal activity
Assist any customer in structuring financial transactions in order to avoid disclosure to governmental or law enforcement authorities under applicable law
Advise any customer that their information has been, or will be, reported to governmental or law enforcement authorities (unless informing the customer is permissible, such as during the preparation of a Currency Transaction Report)
Make a conscious decision to avoid learning the truth about a customer’s suspected illegal activities.
Any director, officer or employee of the Company who fails to adhere to any of the foregoing policies may be subject to immediate demotion, reassignment or dismissal, and such failure may cause such individual and the Bank to be subject to severe civil and/or criminal penalties.
Money Laundering and Terrorist Financing
Money Laundering is the involvement in any one transaction, or series of transactions, which assists a person in keeping, concealing or disposing of the proceeds derived from illegal activities.  It is the criminal act of processing “dirty” money, through a series of transactions; in this way the funds are “cleaned” so that they appear to be proceeds from legal activities.  
Refer to Appendix A for examples of suspicious conduct and transactions related to money laundering
Although money laundering is a complex process, it basically involves the following three steps that can occur independently or simultaneously:
The first stage of laundering money is placement.  The goal is to introduce the unlawful proceeds into the financial system without attracting the attention of financial institutions or law enforcement.  Placement techniques include structuring currency deposits in an amount to evade reporting requirements or commingling currency deposits of legal and illegal enterprises.  An example may include dividing large amounts of currency such as purchasing a series of monetary instruments.
The second stage of the money laundering process is layering, which involves moving funds around the financial system, often in a complex series of transactions, to create confusion.  Examples of layering include wiring funds to and through numerous accounts at many institutions.
The final stage of the process is integration.  Once the funds are in the financial system and obstructed through the layering stage, the integration stage is used to further create the appearance of legal funds through additional transactions.  Examples include the real estate transactions or investment securities.
Terrorists generally finance their activities through both unlawful and legitimate sources.  Unlawful activities, such as extortion, kidnapping, and drug trafficking, have been found to be a major source of funding.  Other observed activities include improper use of charitable or relief funds that donors may have no knowledge that their donations have been diverted to support terrorist causes.  Other legitimate sources have also been found to provide terrorist organizations with funding; these legitimate sources are a key difference between terrorist financiers and traditional criminal organizations.
Prohibited Countries
The Bank may determine that it will not process transactions involving certain countries, or maintain or open new accounts for clients located in certain countries, because of publicly reported concerns of law enforcement agencies and regulators with respect to money laundering controls in those countries.  As events change, the Bank may add or delete countries from this prohibition.
Refer to Appendix B for Countries Tiering List         .

Know Your Customer Standards
Sound business practices include the concept of knowing your customer.  Observing the standards within this Policy can greatly reduce the risk that the Bank might be used for unlawful purposes.  A sound Know Your Customer Policy include, at a minimum:
Establishing the true identity of the customer and other related parties to the account, as appropriate
Screening customer and, as appropriate, related party names against government lists
Obtaining additional information/documentation as needed to understand the customer’s level of risk, determine the need for enhanced due diligence, and enable the detection of suspicious activity
Determining the customer source of funds
Understanding and recording the account’s purpose and anticipated transaction behavior
Maintaining up-to-date knowledge of the customer through ongoing client contact and periodic reviews.
Prohibited Customers
The Bank intends to do business with reputable customers whose identity can be verified.  The Bank will not knowingly do business with persons or entities with whom the Bank is prohibited from doing business because they are sanctioned under the U.S. Embargo Programs or any other official government lists that are identified and distributed throughout the Bank or are applicable in the local jurisdiction.  Also those with whom the Company has chosen not to do business based on prior experience.  In addition, Shell Banks which is one that does not have a physical presence in any country.  Physical presence is defined as a place of business that (1) is maintained by a non-U.S. bank; (2) is located at a fixed address in a country in which the non-U.S. bank is authorized to conduct banking activities, at which location the non-U.S. bank employs one or more individuals on a full-time basis and maintains operating records related to its banking activities; and (3) is subject to inspection by the banking authority that licensed the non-U.S. bank to conduct banking activities.
Also, the Bank will not knowingly do business with individuals or entities:
Whose character or financial conduct are suspect at the inception of the relationship or becomes suspect at any time during the relationship
Convicted of money laundering or related financial crime
Who attempt to establish anonymous accounts, accounts in obviously fictitious names or accounts where the identity of the true beneficial owner of the funds is required but cannot be obtained
Who refuse to provide information required by the Bank
Customer Identification Program (CIP)
Minimum identifying information must be obtained, recorded and verified for any new customer prior to opening their first account or providing their first product/service.  For the purpose of CIP requirements, a customer is defined as any person, including both individuals and entities (e.g., corporations, partnerships and trusts), that opens a new account, product or service, including deposit, transaction, asset, securities, safekeeping, collateral, or mutual fund accounts, credit, lending or borrowing activities, a safe deposit box, or cash management, custody, trust or estate services.  Typically, the customer is the accountholder.  In cases where an individual opens an account on behalf of a person who lacks legal capacity, such as a minor or an entity that is not a legal person, the individual opening the account is the customer.  The following entities are excluded from the definition of customer for CIP purposes:
Financial institutions regulated by a U.S. Federal functional regulator or banks regulated by a U.S. state bank regulator
Departments or agencies of the U.S., including any state or political subdivision of any state
Entities established under the laws of the U.S., state laws, political subdivision of any state, or under an interstate compact, that exercise governmental authority on behalf of the U.S., or any such State or political subdivision
Publicly listed entities whose common stock or similar equity interests are listed on the New York Stock Exchange, the American Stock Exchange, or the NASDAQ Stock Market.
For new customers who are individuals, including joint accountholders, the following identification information must be obtained and recorded:
Name
Date of birth
Primary residence address (and mailing address, if different from residence address).  For a customer who does not have a residential or mailing address, a business street address, an Army Post Office or Fleet Post Office box number or the residential or business address of next of kin or of another contact individual
Government issued identification number – For U.S. individuals, this number must be the Social Security Number.  For non-U.S. individuals/foreign based individuals, the number can be a taxpayer identification number, passport number, national identification number, resident’s identification number, alien identification number, or another government-issued identification number.
For new customers who are entities, the following identification information must be obtained and recorded:
Legal name
Principal place of business address (or local office address)
Government issued identification number – For U.S. entities (established or organized in the U.S.), this number must be the Taxpayer Identification Number (TIN/Employer Identification Number (EIN).  For non-U.S. entities/foreign based individuals, this number can be a taxpayer identification number, registration number, or another government-issued identification number.  Alternative government-issued documentation that certifies existence must be requested for any non-U.S. entities that do not have an identification number.
There may be instances (i.e., a newly formed entity) when the customer has applied for the TIN/EIN, but it has not been received at the time the account is requested.  In all cases, the TIN/EIN must be obtained by the Bank within 60 days or the account must be closed.  The Bank will track accounts opened without TINs/EINs, and may consider restricting account usage, such as limiting deposits, withdrawals, check writing, extension of credit or other measures while receipt of the TIN/EIN is pending.
The identification of each customer is typically verified before or at account opening.  For all businesses, verification must be accomplished no later than 30 days after account opening.  Identity verification can be accomplished through documentary or non-documentary means or a combination of both.  Depending on the risks associated with the customer, businesses may consider whether to restrict the customer’s activities until such time that the verification has been completed.
Documentary verification is accomplished by obtaining, reviewing, and making a record of one acceptable form of identification document.  For individual customers, acceptable identification documents include unexpired, government-issued photo IDs, such as:
Passport
Driver’s license or non-driver photo ID card
Military ID card
For businesses/entities, acceptable identification documents include:
Certificate of Incorporation/Filing Receipt
General or Limited Partnership Agreement
Articles of Organization or Association/Certification of Formation
Trust Instrument
Letters of Trusteeship or Executorship
U.S. Internal Revenue Code Sec. 501(c)(3) letter (for nonprofit organizations)
A government-issued business license
For foreign based entities, those legal documents issued by other countries that parallel the above and authenticate the entity will be accepted upon verification.
These documents are to be used to confirm the accuracy of the information provided by new customers.  A record of the document(s) used must be retained on file and should include:  a description (i.e., the type of document), its identification number, the place of issuance, the date of issuance, and the expiration date (as applicable).  A photocopy of the document (should the business choose to make and retain photocopies) will satisfy this requirement.
 Refer to Appendix C for further description of documentary verification documents         
The Bank may choose to perform non-documentary verification in addition to, or instead of, placing reliance on the documents named above.  Non-documentary verification may include, but is not limited to:
Contacting the customer at home after the relationship has been established
Obtaining references from reliable sources (e.g., credit bureaus, other financial institutions)
Performing a site visit at the entity customer’s place of business.
Even when not required, non-documentary verification may be considered an additional safeguard, particularly in higher-risk businesses and with high-risk customers.  When non-documentary verification is used, a record must be made and retained of the methods undertaken to verify the identity of a customer; this record should include a description of the methods and the results of verification performed.
During the course of verifying the identity of a customer, discrepancies may arise between the information obtained from the customer and the information obtained during the verification.  Resolutions resulting in the continuing the relationship need to be further documented and approved by a Vice President or above.
Bank employees are under no obligation to continue the customer identification and verification process if, at any time during this process, they determine that it is in the best interest of the Bank to terminate the relationship or discontinue the customer acceptance process.  If the decision to discontinue customer acceptance is based on a CIP failure and is deemed suspicious, an Incident Report Form must be filed even though accounts are not opened.
The USA PATRIOT Act requires that, prior to opening an account that the Bank notify its customers that it will be requesting information to verify their identity.  The Bank’s signage/brochure will include the following language:

Important Information About Procedures For Opening a New Account
To help the government fight the funding of terrorism and money laundering activities, financial institutions are required by Federal law to obtain, verify, and record information that identifies each individual or entity that opens an account or requests credit.
What this means for individuals:  When an individual opens an account or requests credit, we will ask for their name, residence address, date of birth, tax identification number, and other information that allows us to identify them.  We may also ask to see a driver’s license, passport or other identifying documents.
New Account Review
Within five business days, the branch manager or designee will review new account information and supporting documentation to determine whether all the necessary information was obtained, the account appears suspicious in any manner, the risk rating is proper and the type of account/business/customer is in compliance with bank policy.  Also as part of this review, the branch manager or designee validates the information on the Insight system to ensure accuracy.  The branch manager or designee signs the “Account Opening Data Entry Form” as evidence of the review and approval.
OFAC Screening/Comparison with Government Lists
Upon opening an account, the related party names are screened against the Office of Foreign Assets Control (OFAC) sanction list.  Upon receipt of an update of the OFAC sanction list, the entire portfolio is scanned against this sanction list.  Possible matches are investigated and any true matches are escalated to the OFAC Compliance Officer for resolution.
The new account will also be scanned to determine whether the customer appears on any list, should one be issued, of known or suspected terrorists or terrorist organizations issued by any Federal government agency and designated as such by Treasury in consultation with the Federal functional regulators.  Possible matches are investigated and any true matches are escalated to the BSA/AML Compliance Officer.  The BSA/AML Compliance Officer is responsible to ensure that all federal directives issued in connection with these lists are followed.
KYC Due Diligence Requirements
KYC due diligence must be performed on all new customers at the time the relationship with the Bank is first established.  
For the purposes of KYC, the customer is each person in whose name an account is opened or a product/service is initiated.  This person can be an individual, a company, an organization or other entity.  The Bank will obtain information and perform due diligence on related parties where appropriate.  Related parties include persons who have authority, or who are in a position of control, over the account, product or service, as well as the beneficial owner(s) of the assets and persons who are intended to receive a benefit from, or be a recipient under, the relationship.  The following are some examples of related parties:
The account’s nominal and/or beneficial owner(s)
For an account in the name of an agent, the principal
For a company account, the significant owners, principal officers, key senior managers, and directors of the company
For an account in the name of a trust, the donor, trustees, and executors.
When opening a new account for an existing customer, it is not necessary to re-perform customer identification/verification steps provided that the existing customer information is current and complete and the Bank maintains the reasonable belief that it knows the true identity of the customer.  Additional account level data, however, may be needed in certain circumstances relative to any additional accounts offered to existing customers.  Similar account level data may also be necessary when a new account is opened for a new customer.  Depending on the type of account, such additional information may include, but is not limited to:
Type and purpose of account
Source of initial and ongoing funding
Anticipated activity:  the anticipated usage, activity, types of transactions, volumes and dollar amounts
Beneficial Ownership Rule:

CRB staff is required to identify the beneficial owners of their legal entity customers-including corporations, limited liability companies, partnerships, business trusts, any other entity created by a filing with a state office, any similar entities formed under the laws of a non-US jurisdiction and similar entities-that open new accounts. 

The definition of “legal entity customer” does not include:
Natural persons
Sole Proprietorships
Unincorporated Associations (i.e. Boy Scouts, Girl Scouts, neighborhood associations)
Trusts, other than statutory trusts created by a filing with a state office

Specifically, CRB must identify and verify Beneficial owners defined as: 

one or more natural persons, if any, who directly or indirectly own 25% or more of a legal entity customer, through any contract, arrangement, understanding, relationship or otherwise, and; 
a natural person who "controls" the entity with significant responsibility to control, manage, or direct a legal entity customer, including:

An executive officer or senior manager (e.g., a Chief Executive Officer, Chief Financial Officer, Chief Operating Officer, Managing Member, General Partner, President, Vice President, or Treasurer); 
or any other individual who regularly performs similar functions.

Certain legal entities, including the following, are excluded from the Beneficial Ownership Rule:

Domestic banks in the United States (including domestic offices of foreign banks);
Entities listed on the New York, American, or NASDAQ stock exchanges;
Majority-owned subsidiaries of such listed entities;
Security issuers registered under Section 12 of the Securities Exchange Act of 1934;
Investment companies;
SEC- and CFTC- registered entities;
Bank holding companies;
Pooled investment vehicles operated by an entity that is not a legal entity customer;
State-regulated insurance companies;
Designated financial market utilities;
Foreign financial institutions whose regulator maintains beneficial ownership information;
Foreign government entities that do not engage in commercial activities; and
Legal entities only to the extent that they open a private bank account

Internal Account Requests:  The following policies apply when a bank employee submits an account opening request to the branch manager.
The person submitting the form (i.e. the person signing the “Requested by” field) to the branch manager will be the Relationship Owner of the account.
The Relationship Owner will be responsible for completing the following:
Gathering and ensuring that all information is complete to support the opening of the account;
Determining the money laundering risk rating
Any updating of Know Your Customer (KYC) information.  The Relationship Owner updates the KYC information, when there is a significant change in customer activity (for example new products added, or increase in transaction volume), ownership, or public information about the customer.  
Completing the periodic review - For high risk customers, the periodic review occurs one per year, whereas for medium risk customers, the periodic review occurs once every two years (based on the date the account was opened).  
Conducting site visits of high risk customers, in case there is a triggering event.  Triggering events include:  negative news; unusual increase/decrease in account activity; changes in the nature of the account activity; money laundering alerts that cannot be cleared; word of mouth tips; or reluctance from customer to provide information.  

Refer to Appendix D for a sample of the Internal New Account Request form
Money Laundering Risk Ratings
Money laundering risk ratings are an evaluation of the customer’s/account’s potential money laundering risk.  As such, they can impact the approvals needed to accept a customer or open the account, determine the extent of information and verification required, trigger the need for enhanced due diligence, and affect the frequency of periodic relationship reviews.
The relationship owner determines the money laundering risk rating but will be reviewed by another individual.  Money laundering risk ratings must be determined before a new customer is accepted, and at, or immediately after, a new account is opened.  They are to be re-evaluated and adjusted, as appropriate, during the periodic review process, or at any other time when the business learns of new information that affects the rating.  The branch manager is responsible for reviewing or approving changes to a client’s risk rating.
Money laundering risk ratings apply at both the customer and account level.  If a customer is high-risk by himself, because for example he is a politically exposed person or associated with a high-risk industry, then all of his accounts should be classified as high-risk.  If an account is rated high-risk, however, the associated customer is not automatically high-risk.
Risk determination is a two-part process.  First, the relationship owner must identify and understand the general operating and overall legal, regulatory and geopolitical environments in which their customers operate.  Second, the relationship owner must, at a minimum, understand the following to determine whether they want to enter into, or sustain, a relationship with a particular customer within their target market:
The nature of the customer, including their reputation and business or other financial activities
The products and services requested, and the customer’s purpose for and use of such products and services
The money laundering risks associated with the customer and the jurisdiction(s) with which the customer has significant contact.
Also the following risk factors will be considered:
Customer-Type – At a minimum, the following customers shall be considered high-risk:  Politically Exposed Persons, Money Services Businesses, Offshore International Business Corporations and Private Investment Companies, any customers associated with substantial negative public information.
Geography – At a minimum, customers associated with (i.e., located/domiciled in, a citizen or resident of, and/or has business activities in) a Tier 1 country shall be considered high-risk.  Refer to Appendix B for the Country Tiering List
Industry – At a minimum, customers associated with (i.e., one is principally engaged in or whose source of wealth was generated from) a high-risk industry shall be considered high-risk.  Refer to Appendix E for the High- and Medium-Risk Industries List
Products and Services – At a minimum, customers and/or accounts that use high-risk products or services shall be considered high-risk.  Refer to Appendix F for the Medium Risk Products List
Transaction Activity – Such as whether the customer’s expected transaction activity, including cash and/or wire activity, is determined to be high.
Money Laundering Risk Ratings for New Online Accounts
[Insert Financial Institution Here] recognizes that accounts which are opened without face-to-face or phone contact may pose a higher risk for money laundering for the following reasons:

More difficult to positively verify the individual’s identity;
Customer may be out of [Insert Financial Institution Here]’s targeted geographic area;
Customer may perceive the transactions as less transparent;
Transactions are instantaneous; and/or
May be used by a “front” company or unknown third party.

The Bank will obtain the same information as it would for a face-to-face account opening and will use ChexSystems’ QualiFile electronic inquiry response to authenticate identity.  The Bank has limited the geographic availability to New York, New Jersey, and Connecticut.  Due to the above considerations, all new online accounts will be deemed medium risk for the first three (3) months and if there is no unusual activity for that time period, then the account will be changed to low risk.  Pursuant to the Bank’s two (2) year periodic review process for medium risk accounts, if the customer’s activity warrants a change in risk rating, then the Bank will act accordingly.  
Please refer to the Bank’s Account Create Procedures. 
Additional KYC Due Diligence Requirements for Certain Customers, Related Parties, and Accounts

New High-Risk Customers
All new customer relationships that are deemed high-risk, and those escalated from medium or low to high-risk, are subject to review by the AML Officer.  The Standard Account Review Sheet is subject to completion, and review based on established requirements.  If, upon review, the AML officer deems that the Bank cannot continue with this relationship, the AML officer will make a recommendation to close the account.  Any decision to keep the account open after such recommendation will require approval from the Chairman of the Board.
Refer to Appendix G for Standard Account Review Sheet
Politically Exposed Persons
Customers/related parties who are Politically Exposed Persons (PEPs) increase the risk that the Bank could be exposed to involvement in money laundering or other illegal activities.  The financial activities of PEPs may be of public interest or might otherwise attract publicity within or beyond the borders of their home country, and their transactions with the Bank could potentially involve the proceeds of foreign official corruption.  If the Bank knowingly engages in financial transactions in violation of the money laundering laws of various jurisdictions, the Company will be exposed to significant legal and reputational harm.
PEPs are defined as a U.S. or non-U.S., current or former, senior official of the executive, legislative, administrative, military or judicial branches of a government, whether elected or not and include senior officials of a major political party or a senior executive of a government-owned commercial enterprise.  A senior official or executive is defined as an individual with substantial authority over policy, operations, or the use of government owned services.  PEP positions include, but are not limited to:
Heads of State, Government Heads or National Leaders, such as the President, Prime Minister, King, Queen, Emir, Sultan, Emperor, Monarch, Pope
National Cabinet Members and Department/Agency Heads, such as the Vice President, Chancellor, Secretary of State, Defense Minister, Chief of the Treasury, Head of the National Bank, and other key Department, Agency, Ministry, and Office Officials
Key National Legislative Officials, such as Congressmen, Senators, House Representatives, Parliament members, Assemblymen, Councilmen
Senior Military Leaders, such as the Army Secretary
Important National Justices, such as the Attorney General, Chief Justices, and Associate Judges
Political Party Leaders
Ambassadors/Consuls General, including the United Nation Representative
Governors
Mayors of cities with populations in excess of 1MM
Senior executives of government-owned enterprises, such as the Chairman, CEO and President of government airline.
The following customers/related parties are also PEPs and are therefore bound by the requirements of this section:
Corporations, businesses or entities formed by, or for the benefit of, or significantly owned or controlled by, a PEP; significant ownership is 25% or more; control includes holding a senior executive position of influence, such as the Chairman, CEO, and President
Any immediate family member of a PEP, including the spouse, parents, siblings, children, and spouses’ parents or siblings
A person who is widely and publicly known to be a close associate of any such individual
Foreign Embassies/Consulates/Ministries
Foreign political organizations.
Upon account opening, reasonable steps will be taken to determine whether customers and related parties are PEPs including the direct inquiry with the customer.  The customer’s KYC profile and account record must indicate that the client is a PEP.
Enhanced scrutiny is required whenever the Bank does business with a PEP.  This enhanced scrutiny includes the following:
Determining the identity of the PEP
Assessing the level of corruption and characteristics associated with the PEP’s country
Evaluating the PEP’s position, length of time in office, and reputation
Probing the PEP’s employment history and source of funds and wealth
Obtaining information on immediate family members or close associates having transaction authority over the account
Understanding the purpose of the account and expected volumes and nature of account activity
Considering the use of the account(s)
Performing appropriate database/internet checks to gather information
Obtaining Board of Directors approval before account opening (presentation to outline the nature of the request, explanation of the rationale for initiating or maintaining the PEP relationship and providing adequate information regarding the PEP, the due diligence steps taken in regard to the relationship and how the PEP’s ongoing activities with Bank will be monitored.)
On an annual basis, each Business Head must review the PEPs in his or her business to determine if their retention continues to be appropriate.  This review must be evidenced in writing. 
Refer to “PEP Scanning Procedures” for detailed processes for identifying Politically Exposed Persons.
Money Services Businesses
Money Service Businesses (MSBs) are high-risk because many:
Lack ongoing customer relationships and require minimal or no identification of customers
Maintain limited or inconsistent recordkeeping on customers and transactions
Engage in frequent currency transactions
Are subject to varying levels of regulatory requirements and oversight
Can quickly change their product mix or location and quickly enter or exit an operation
Sometimes operate with improper registration or licensing
MSBs are defined as any person doing business, whether or not on a regular basis or as an organized business concern, in one or more of the following capacities:
Currency dealer or exchanger
Check casher, including “payday” loan and check cashing services
Issuer of traveler’s checks, money orders or stored value products
Seller or redeemer of traveler’s checks, money orders or stored value products (including the United States Postal Service)
Money transmitter
It is the policy of the Bank not to do business with MSBs, except for:
U.S. or state-regulated mortgage banking firms
Recognized national or regional retail chain stores whose principal business is not money services.
For any other MSBs, Board of Directors approval is required.  In addition, the following baseline due diligence must be performed for all MSB relationships:
Confirm that the MSB is registered with FinCEN
Confirm state and local licensing, if applicable
Confirm agent status, if applicable
Conduct an on-site visit
Determine and review the ownership or senior management of the MSB.
Conducting a risk assessment of the MSB
Confirmation of MSB’s understanding that it will be subject to federal and state bank regulatory oversight in connection with activities conducted with and through CRB
Determining whether necessary insurance coverage, continuity plans, policies and procedures are in place
Identifying the MSB’s customers’ profile, potential issues, risks and concerns, and areas of customer complaints
Determining whether any conflicts of interest exist between management and insiders of CRB; 
Developing an MSB questionnaire to obtain additional information about each customer’s business. The questionnaire will ask the customer for information on its products and services, customer base, types of software used, employee training procedures, and other information; and 
Requesting copies of the MSB’s BSA/AML and OFAC policies and procedures. 
IT due diligence (depending on customer’s business model)
As part of its ongoing due diligence, the Bank will conduct periodic site visits of MSB customers.  In addition, MSB customers are required to periodically furnish the bank with: updated, board approved policies and procedures; and independent review of the BSA/AML program and management response.  
Refer to the “MSB White Paper” for details regarding MSB due diligence.
Hedge Funds
Hedge funds may be higher-risk because they provide customers with offshore investment vehicles.  Hedge funds are similar to mutual funds in that they both are pooled investment vehicles that accept investors’ money and generally invest it on a collective basis.  Hedge funds differ significantly from mutual funds, however, because hedge funds are not regulated.
Before opening an account for a hedge fund, the following due diligence will be performed:
Obtain and review a prospectus, offering document or other documentation describing the fund
Record the name of and background information for the investment advisor/management company and/or the general partners or other similar senior officers, such as the Chief Executive Officer, Chief Administrative Officer, Chief Information Officer, etc.
Perform OFAC screenings on the fund, the investment advisor/management company, and/or the general partners or other similar senior officers by conducting Internet research or another similar service or third-party confirmation.

Onboarding of Peer-to-Peer Lending Companies
[Insert Financial Institution Here] will partner with one or several Peer-To-Peer Lending Companies (“P2P”) to issue unsecured consumer and business loans to borrowers with certain credit profiles.  The Bank requires each P2P lending company to develop and implement a written BSA/AML program that is reasonably designed to prevent the company from being used to facilitate money laundering or the financing of terrorist activities.  At a minimum, the anti-money laundering program shall:  provide for policies and procedures to prevent money laundering and detect suspicious activity; designate a compliance officer; provide for ongoing training of appropriate persons; and provide for periodic independent testing of the AML program.  The Bank also requires each P2P lending company to adopt a Customer Identification Program that is in compliance with the Bank’s Customer Identification policies.  
The selection of the P2P lending companies will be based on, but not limited to, the following:
Adequacy of BSA/AML policies and procedures
Review of results from compliance, BSA/AML and IT audits

Bank management will request that BSA/AML audits be performed prior to the commencement of any funding.  For new companies, a 2-step process will be employed whereby the policies will be reviewed for adequacy and control and the transaction testing will be performed 60 days after program launch. The results will be reviewed thoroughly, and findings will be detailed in a memo to the BOD. 
Refer to the “Peer-to-Peer Lending Policy” for a detailed description of the requirements for P2P lending companies
Reliance on Others
In those instances in which a financial intermediary introduces its client to the Company and the intermediary’s customer opens an account and/or otherwise enters into a contractual relationship with one or more of the Bank’s business units, KYC due diligence on the contracting party is the responsibility of the business unit; however, businesses are permitted to rely on the customer identification and verification procedures of another financial institution to establish the identity of the customer.  Reliance, for purposes of such safe harbor, is appropriate when the other financial institution has established a similar banking/business relationship with the customer to that of the Company and when such reliance can be considered reasonable under the circumstances.  In order to be able to rely on the customer identification procedures of another financial institution, the other entity:
Must be subject to the AML program requirements set forth in the USA PATRIOT Act and implementing regulations
Must be regulated by a U.S. Federal functional regulator, and
Must enter into a contract with the Bank requiring the other financial institution to certify annually that it has implemented its AML program and that it, or its agent, will perform the customer identification and verification program requirements.
In instances in which the intermediary to be relied upon is not subject to the requirements of the USA PATRIOT Act, that intermediary:
Must be subject to money laundering control requirements under its local laws and regulations
Must be regulated by a recognizable financial services regulator in the country of jurisdiction
Must provide a letter of attestation to the Bank in which its attests to its compliance with all appropriate customer identification, verification, and other due diligence requirements.
In all cases in which a business is placing reliance upon an intermediary for the performance of any customer identification or other KYC due diligence steps, the prior, written approval must be obtained from the BSA/AML Compliance Officer.  This approval is required whether the entity relied upon is U.S. or non-U.S. intermediary.
KYC information provided by new employees who bring customers with them from other financial institutions must be independently obtained and verified by someone other than the new employee.
Ongoing Relationship/Customer/Account Activities
KYC records are intended to be dynamic and enhanced over time as knowledge of a customer grows.  The relationship owner will review and update KYC information whenever significant changes in activity, ownership, or public information about the client become known.
The Bank uses an automated monitoring system in order to monitor account activity, on an on-going basis.  The automated monitoring system analyzes transactions for unusual activity, and generates alerts for review.  A Compliance Analyst reviews these alerts on a daily basis.  
Also in regard to the ACH environment, the Operations Department will review the following reports on a daily basis for unusual activity and scanning:
Entries – Checking PL6570-01
Entries – Savings PL6570-06
Originating Entries PL5500-02
OFAC Screening – Org Final PL6579-04 (IATs)
OFAC Screening – Receiving Final PL6579-02 (IATs)
OFAC Screening – ACH OFAC Rec (PL6579-01)
ACH Originating Activity (PL2000-02)
Return/NOC Activity Listing (PL2000-01)
Special Edits Updates (PL6564-01)
Death Notification Report
International (IAT) RDFI Report
Receiver Setup Report
Notification of Change ODFI Report 
Originator Setup Report
Return Item-ODFI Report
In addition to the daily reports, the following ACH reports are reviewed monthly
ACH Volume Report per Originator
Return Ratio Report per Originator
Unusual activity may encompass the following:
Reviewing originators/recipients’ whose business or occupation does not warrant the volume or nature of ACH activity;
Originators whose origination activity suddenly exceeds projections/credit-debit limits with no reasonable explanation for such change;
Originators generating a high rate or high volume of invalid account returns or a high-rate or high volume of unauthorized returns/transactions;
Specific returns creations (RDFI) covering unauthorized, fraudulent, or revoked transactions, and Federal reclamations.
Unusual conditions will be investigated and handled appropriately by the reviewer.  Such examination of these daily reports must be evidenced by the reviewer by initialing the Daily Account Review Log or the report printout.
In order to monitor ongoing wire transfer records quarterly, the branch manager/designee will review the Wire Transfer Velocity Report for questionable and/or unusual patterns.  Particular attention will be paid to incidents where:
Unexplained or sudden extensive wire activity, especially in accounts that had little or no previous activity;
A large number of wire transfers to or from unrelated third parties inconsistent with the customer’s legitimated business purpose;
Wire transfers that have no apparent business purpose to or from a foreign country;
The customer’s account has inflows of funds or other assets well beyond the known income or resources of the customer;
Transactions in which the primary beneficiary or counter-party is undisclosed. 

The branch manager/designee will sign the quarterly report as evidence that the quarterly review was conducted.
Unusual Activity Detected by a P2P Lending Company:  Each Peer-To-Peer Lending Company (P2P) that [Insert Financial Institution Here] (the Bank) partners with is required to have an Anti-money Laundering program.  As part of the program, the P2P lending company must have policies and procedures to detect and identify suspicious activity.  When a P2P lending company identifies suspicious activity, they notify the Loan Service Department at [Insert Financial Institution Here] of the unusual activity.  The Loan Service Department works with the P2P lending company to prepare an Incident Report.   A Compliance Analyst and the Bank’s AML/BSA Officer, review the incident report to determine whether the activity warrants a Suspicious Activity Report filing.    
Suspicious Activity Report (SAR) Filing:   Upon detection of unusual activity, it is the Bank’s policy to file a SAR with respect to:
Criminal violations involving insider abuse in any amount;
Criminal violations aggregating $5,000 or more when a suspect can be identified;
Criminal violations aggregating $25,000 or more regardless of a potential suspect;
Transactions conducted or attempted by, at, or through the bank (or an affiliate) and aggregating $5,000 or more, if the bank or affiliate knows, suspects, or has reason to suspect the transaction:
May involve potential money laundering or other illegal activity;
Is designed to evade the BSA or its implementing regulations;
Has no business or apparent lawful purpose, or is not the type of transaction that the particular customer would normally be expected to engage in, and the Bank knows of no reasonable explanation for the transaction after examining the available facts, including the background and possible purpose of the transaction.
Note:  Because elderly individuals experience declining cognitive or physical abilities, they are more reliant on specific individuals for their physical well-being, financial management, and social interaction.  Therefore, certain elderly individuals may be particularly vulnerable to identity theft, embezzlement, and fraudulent schemes.  See Appendix I for Possible Signs of Elder Financial Exploitation.

An investigation will be conducted for any activity deemed suspicious and if necessary, a SAR will be filed.  
This Policy provides for a process of periodic, risk-based customer relationship reviews.  In the absence of an event that calls immediate attention to a relationship or to activity in the customer’s accounts, the periodic review provides the Bank with the opportunity to update KYC information, review the customer’s recent transactions and interactions with the Bank, and reaffirm that retaining the relationship continues to be appropriate.
The periodic review is to be performed by the relationship owner and should:
Ensure that KYC information is accurate, complete, and up-to-date
Consider the effects of any significant inflows, outflows, and any obvious changes in the accounts’ purposes, for appropriateness and consistency with expectations.
Evaluate the customers’ general transaction volumes and overall balances across all products and services for reasonableness and consistency with the customer’s financial situation and the relationship’s stated purpose.
Periodic reviews will occur at least every 12 months for high-risk customers and 24 for medium-risk customers.  The first month of each quarter, high risk accounts having a yearly anniversary in that quarter, based on the date of the assigned risk rating, will be identified.  During that three-month period, a review will be performed using the Standard Account Review Sheet.  The review method for medium risk accounts would be the same but based upon a two-year anniversary of the assigned risk rating date.  The Standard Account Review Sheet is subject to the necessary review and approval based on established requirements.
Refer to Appendix G for Standard Account Review Sheet
Special Measures
The USA PATRIOT Act gives the Secretary of the Treasury authority to impose special measures against foreign jurisdictions, foreign financial institutions, transactions involving such jurisdictions or institutions, or one or more types of accounts, that are determined to pose a “primary money laundering concern” to the United States.
The BSA/AML Compliance Officer will coordinate compliance with such special measures on a bank-wide basis.  It is the policy of the Bank to promptly comply with any special measures prescribed by the Secretary of the Treasury.  Whenever the Secretary imposes special measures, Compliance shall communicate the special measures to the affected businesses, which will take the steps necessary to terminate affected account relationships, communicate to customers, and/or amend existing policies, procedures, and controls or develop new ones to comply with the prescribed special measures.
Information Sharing
The USA PATRIOT Act provides for information sharing between the Government and Financial Institutions, as well as between financial institutions themselves, in an effort to deter money laundering and terrorist activities.
Section 314(a) of the Act establishes a mechanism for law enforcement agencies to communicate the names of suspected terrorists and money launderers to covered financial institutions for the purpose of promptly identifying accounts and transactions involving those suspects.  Under 314(a), information requests are batched and forwarded to covered financial institutions from FinCEN every two weeks (although single requests may be sent in urgent situations).  Note:  The designated points of contact for receiving 314(a) are reflected on the Bank’s Call Report Filings.
Upon receipt of a 314(a) request, Company covered financial institutions are required to search the following records:
Deposit account records
Funds transfer records
Records for the sale of monetary instruments
Loan records
The Bank will search its records for the preceding 12 months for accounts, and for the preceding 6 months for transactions, and report them to FinCEN.  As the Bank has several third party, and marketplace lenders, in addition to the scan of accounts, and transactions, the Bank will conduct a FinCEN scan for any retained loans as well as any loans funded within the last 12 months.  If other matching records are found in this process, they will also be reported to FinCEN, even if they fall outside of the requested time frame or pertain to an account or transaction in an area of the financial institution that was not required to be searched but were searched anyway, or pertain to a record that was not required to be maintained under federal law or regulation but existed nonetheless.
Searches are required to be completed and a response to be sent to FinCEN with any matches within two weeks of receiving the 314(a) request.
If there is a positive match for an account or a transaction, the following information will be gathered:
The identity of the individual, entity, or organization
The account number(s); opening date, type of transactions
All identifying information provided by the account holder in connection with the opening of the account, such as social security number, taxpayer identification number, passport information, date of birth, and address.
Names are highly confidential and should be shared only on a limited basis.  Under no circumstances should 314(a) names be shared with any other financial institution.  Records regarding 314(a) searches must be retained in a secure area.
If the 314(a) search results in a positive match, it is incumbent upon the Bank to conduct an investigation of the account relationship and/or transaction activity and should there be reasonable belief that suspicious activity occurred, an Incident Report must be drafted for SAR consideration. 
 If the Bank decides to close the account, it will first notify the law enforcement contact on the request to determine if closing the account would interfere with an active investigation.  If law enforcement requests that an account remain open, the bank will request written confirmation.
Note:  The bank does not participate in 314(b)
Refer to Appendix H for procedures concerning responses to information requests 

Subpoenas Received from Law Enforcement

The receipt of a grand jury subpoena will cause the bank to conduct a risk assessment and account relationship review of the subject customer.  The information resulting from the review, transactions, and accounts subject to the subpoena will be evaluated and a determination will be made as to whether additional account monitoring should be implemented, or a suspicious activity report filed.
Currency Transaction Reporting and Exemptions
In compliance with the BSA regulations, the following types of reports are submitted to the U.S. government:
FinCEN Form 112, Currency Transaction Report (CTR):  A CTR must be filed for each deposit, withdrawal, exchange of currency, or other payment or transfer, by, through or to a financial institution, which involves a transaction in currency of more than $10,000.  Multiple currency transactions must be treated as a single transaction if the financial institution has knowledge that:  (a) they are conducted by or on behalf of the same person; and, (b) they result in cash received or disbursed by the financial institution of more than $10,000.  A CTR must be filed within 15 days electronically from the date of the transaction with FinCEN.  The bank must retain copies of CTRs for five years from the date of the report.
FinCEN Form 105, Report of International Transportation of Currency or Monetary Instruments (CMIR):  Each person who physically transports, mails or ships, or causes to be physically transported, mailed, shipped or received, currency, traveler’s checks, and certain other monetary instruments in an aggregate amount exceeding $10,000 into or out of the United States must file a CMIR.
The preparation process of these reports will be through the Bank’s automated monitoring system. The automated monitoring system loads Cleartouch data into the system, and when reportable transactions are found, auto-generates populated CTRs. The branch manager is responsible for performing a secondary review to ensure accuracy and submitting the report.    
Currency transactions over $3,000 are recorded daily on the “Currency Transactions Greater Than $3,000 Log”.  Daily, this log is reviewed by the branch manager/designee to ensure that multiple currency transactions totaling over $10,000 for a customer are properly reported.  This log also must be reviewed for possible structuring situations and initialed as evidence of review.  On a monthly basis, the branch manager/designee will review this report on a cumulative basis to detect patterns or structuring trends.  The branch manager/designee will evidence this review by signing this monthly report. 
Structuring is the breaking up of transactions for the purpose of evading the BSA reporting and recordkeeping requirements and, if appropriate thresholds are met, should be reported as a suspicious transaction.  Structuring may be indicative of underlying illegal activity; further, structuring itself is unlawful under the BSA.
Penalties and asset forfeiture for money laundering can be severe under BSA:
Individuals, including employees of financial institutions, convicted of money laundering face up to 20 years in prison for each money-laundering transaction.
Businesses, including banks and individuals, face fines up to $1,000,000 or twice the value of the transaction, whichever is greater.
Financial Institutions can lose their charter/license, and employees risk being removed and barred from the business.
Any property involved in the transaction or traceable to the proceeds of the criminal activity, including loan collateral, personal property and, under certain conditions, entire bank accounts (even if some of the money in the account is legitimate) may be subject to forfeiture.
Safe Harbor Provision 
The Annunzio Wylie Anti-Money Laundering Act (1992) – U.S.C. 5318(g)(3) - provides a safe harbor for the bank and its employee from civil liability for reporting known or suspected criminal offenses or suspicious activity by filing a SAR. A bank employee should feel safe in reporting suspicious activity.  The government works closely with the bank to ensure that all employees are protected from any liability.  
Federal Law prohibits Employees from disclosing the fact that a SAR has been filed.  Never discuss any Suspicious Activity Reporting requirements with a customer. Voluntarily giving additional information to customers, such as when you completed an incident report for their suspicious activity makes the employee liable for prosecution for violating Anti-Money Laundering Laws.

Recordkeeping and Record Retention Requirements
The following rules apply to CIP-related records:
Identifying information (name, address, date of birth, and government-issued ID number) must be retained for five years after the date the account is closed
All other information and documentation required by CIP rules, such as other recorded customer information, copies of documents used to verify identity, records of the steps taken and the results of verification performed by non-documentary means, and the resolution of discrepancies that may have arisen between information provided by a customer and the documentary and non-documentary evidence used to verify such information, must be retained for five years after the record is made.
KYC-related records can be maintained in either hard copy or in electronic form, so long as the records are accurate and readily accessible within five calendar days.
The Bank must maintain a record of each funds transfer of $3,000 or more, which it originates, acts as an intermediary for, or receives for five years.  The amount and type of information that must be recorded and kept depends upon the Bank’s role in the funds transfer process.  Also, the Bank must pass certain information along to the next bank in the funds transfer chain when it acts as an originator or intermediary for a funds transfer


The Bank which provides for the purchase and sale of monetary instruments must require the retention of records of cash sale to a customer for bank checks, drafts, cashier’s checks, money orders, and traveler’s checks (which the Bank does not currently sell) between $3,000 and $10,000 inclusive for five years.  These records must include evidence of verification of the identity of the purchaser and other information as outlined below:
The name of the purchaser;
Date of purchase;
Types of instrument purchased;
Serial number of the instrument purchased; 
The amounts in dollars of each of the instruments purchased; and
Verification that the individual is a deposit holder/verification or the purchaser’s identity (address, SS#/Alien Identification #, DOB).
The following records will be retained for seven years:
A record of each extension of credit in an amount in excess of $10,000
Each document granting signature authority over each deposit or share account
Each statement, ledger card or other record on each deposit or share account, showing each transaction in, or with respect to, that account
Each check, clean draft, or money order drawn on the Company or issued and payable by it
Each item in excess of $100 comprising a debit to a customer’s deposit or share account
Records prepared or received in the ordinary course of business, which would be needed to reconstruct a transaction account and to trace a check in excess of $100
Each deposit slip or credit ticket reflecting a transaction in excess of $100.
AML Training
Annually the Bank shall maintain a regular training program for the purpose of educating its personnel and heightening their awareness so that they will be knowledgeable and vigilant in their efforts to recognize and report activity, which may constitute money laundering.
Within 60 days of hire, new employees will be trained in the basic aspect of AML.  Additionally, the new employee will be required to read and attest that they understand the contents of the Bank’s AML/BSA policies.
The appropriate attendance records and training materials will be retained for three years.   
Note:  Training will be conducted at least annually for the Board of Directors.
BSA/AML Compliance Officer
The BSA/AML Compliance Officer has day-to-day responsibility for managing all aspects of the Bank’s AML Program and compliance with AML laws and regulations.  The BSA/AML Compliance Officer is also responsible for the maintenance of this Policy and for considering deviations to this Policy.  In addition, the BSA/AML Compliance Officer advises staff regarding the application of anti-money laundering laws and regulations and on money laundering trends and patterns specific to certain businesses.
Despite changes in management or employee composition or structure, the BSA/AML Compliance Officer will ensure that all requirements of an effective BSA/AML program are implemented and that the program contains all appropriate aspects to be in compliance with all laws and regulations. 
BSA/AML Risk Assessment
The Bank has developed a risk assessment, which was approved by the Board of Directors, by identifying risks along with the associated mitigants.  The assessment will be periodically reviewed and presented to the Board for approval.
Independent Testing
Independent testing commensurate with the BSA/AML risk profile of the bank will be conducted every 12 to 18 months by outside auditors.  Upon completion, the auditors conducting the BSA/AML test will report the results to the Audit Committee.
Board Reporting
On an annual basis or more frequently as circumstances dictate, the BSA/AML Compliance Officer will present a report to the Board of Directors.  This report will include such important facts relating compliance initiatives, any deficiencies/corrective action noted, SAR filings relating to AML, etc.









APPENDIX A
EXAMPLES OF SUSPICIOUS CONDUCT AND TRANSACTIONS
The existence of one or more of these suspicious circumstances does not mean that money laundering activity is taking place, but that such circumstances should be scrutinized carefully.

Customers who are reluctant to provide normal information when opening an account or who provide fictitious or conflicting information.
Customers with no discernible reason for using the Bank’s services (e.g. customers with distant addresses who could find the same services nearer to home)
Business customers who are reluctant to provide complete information regarding the purpose, prior banking relationships, officers or directors, or location of their business.
Business customers who are reluctant to reveal details about their activities, or to provide financial statements, or whose financial statements are noticeably different from those of similar businesses.
Large cash deposits by an individual or business where checks and other instruments are the expected norm.
Structuring multiple cash deposits which are individually unexceptional, but significant in the aggregate.
Exchanging large quantities of low denomination currencies for those of higher denomination.
Deposit or withdrawal activity that is inconsistent with the activity normally associated with the customer or the customer’s type of business.
Funds transfers are sent or received from the same person to or from different accounts.
Funds activity is unexplained, repetitive, or shows unusual patterns.
A customer uses unusual or suspicious identification documents that cannot be readily verified.
The customer’s background differs from that which would be expected on the basis of his or her business activities.
A customer is reluctant to provide information needed to file a mandatory report, to have the report filed, or to proceed with a transaction after being informed that the report must be filed.
A person uses the automated teller machine to make several bank deposits below a specified threshold.
The currency transaction activity reflected a sudden change inconsistent with normal activities.
A customer purchases a number of cashier’s checks, money orders, or traveler’s checks for large amounts under a specified threshold.
Suspicious movements of funds occur from one bank to another and then funds are moved back to the first bank.
Deposits of large third-party checks endorsed in favor of the customer where such conduct is inconsistent with the customer’s normal activity.
Large numbers of individuals making payments into the same account without adequate explanation.
Unexpected repayment of problem loans.
Requests to provide or arrange financing where the source of the customer’s financial contribution to a deal is unclear, particularly where property is involved.
Employees whose habits or lifestyles change unexpectedly
Employees whose performance changes unexpectedly.
The stated occupation of the customer is not commensurate with the type of level of activity.
Regarding nonprofit or charitable organizations, financial transactions occur for which there appears to be no logical economic purpose or in which there appears to be no link between the stated activity of the organization and the other parties in the transaction.
For additional examples of Money Laundering and Terrorist Financing “Red Flags” see the FFIEC BSA/AML Examination Manual 11/17/2014.








APPENDIX B
COUNTRY TIERING LIST
Tier 1
Afghanistan		Albania				Angola		
Anguilla		Antigua/Barbuda	Argentina		Armenia
Azerbaijan		Bahamas		Bangladesh		Belarus		
Belize			Bolivia		Botswana		Brunei
Burkina Faso		Burundi		Cambodia		Cameroon	
Cape Verde		Chad			Colombia		Congo
Costa Rica		Cuba			Cyprus		Dominican Republic	
East Timor				Equatorial Guinea	Eritrea
Estonia		Ethiopia		Gabon			Gambia
Georgia		Ghana			Grenada		Guinea		
Guinea-Bissau	Haiti			Honduras		Indonesia		
Iran			Iraq			Ivory Coast		Kazakhstan		
Kenya			Kuwait		Kyrgyzstan		Laos			
Latvia			Lebanon		Lesotho		Liberia		
Libya			Lithuania		Macau			Malawi		
Maldives		Mali			Mexico		Moldova		
Mongolia		Montenegro		Montserrat		Morocco		
Myanmar		Namibia		Nauru			Nepal			
Nicaragua		Nigeria		Niue			North Korea
Pakistan		Palestinian		Panama		Papua New Guinea	
Paraguay		Peru			Philippines		Russia			
Rwanda		Sao Tome&Principe	Serbia/Montenegro	Seychelles		
Sierra Leone		Soloman Islands	Sri Lanka		St. Lucia		
			Syria			Tajikistan		Tanzania		
Thailand		Trindad & Tobago	Turkey		Turkmenistan	
Uganda		Ukraine		Uzbekistan		Venezuela		
Vietnam		Yemen			Zambia		Zimbabwe
Tier 2
Akrotiri Sovereign	Aland Islands		American Samoa	Andorra		
Antarctica		Aruba			Ashmore & Cartier	Azores			
Baker Island		Benin			Bermuda		Bhutan		
Bouvet Island		Brit Virgin Islands	British Oceania	Canary Islands
Cayman Islands	Central African Re	Christmas Island	Clipperton Island
Cocos			Comoros		Congo			Cook Islands
Coral Sea Islands	Croatia		Dhekelia Sov Base	El Salvador
Falkland Islands	Faroe Islands		Fed St Micronesia	Guiana
French Polynesia	French Southern	Ghana			Gibraltar
Greece			Greenland		Guadeloupe		Guam	
Guatemala		Guernsey		Guyana		Heard/Mcdonald Is
Howland Islands	India			Indonesia		Isle of Man
Jamaica		Jarvis Island		Jersey			Johnston Atoll
Jordan		Kingman Reef	Kiribati		Kosovo
Liechtenstein		Macedonia		Madagascar		Madiera		
Malaysia		Marshall Islands	Martinique		Mauritania		
Mayotte		Midway Islands	Monaco		Mozambique		
Navassa Island	Neth Antilles		New Caledonia	Niger			
Norfolk Island	North Mariana Is	Palau			Palmyra Atoll	
Paracel Islands	Pitcairn Islands	Qatar			Reunion		
Saint Helena		San Marino		Saudi Arabia		Senegal		
Somalia		South Georgia	South Korea		South Sandwich Islands
Spratly Islands	St Barthelemy	St Pierre/Miquelon	St Kitts/Nevis
St. Martin		St Vincent & Gren	Suriname		Svalbard/JanMayen
Togo			Tokelau		Tonga			Turks/Caicos		
Tuvalu		US Virgin Islands	United Arab Emirates			
Uruguay		Vanuatu		Vatican City		Wake Island		
Wallis & Futuna	Western Sahara	Western Samoa
Tier 3
Bahrain		Barbados		Bosnia-Hercegovina	Bulgaria
China			Djibouti		Dominica		Egypt	
Fiji			Hong Kong		Hungary		Israel
Luxembourg		Malta			Mauritius		Oman
Poland		Puerto Rico		Romania		Singapore
Slovakia		Slovenia		South Africa		Swaziland
Switzerland		Taiwan		Tunisia		
Tier 4
Australia		Austria		Belgium		Brazil
Canada		Chile			Czech Republic	Denmark
Finland		France			Germany		Iceland
Ireland		Italy			Japan			Netherlands
New Zealand		Norway		Portugal		Spain
Sweden		United Kingdom	United States





















APPENDIX C
DOCUMENTARY VERIFICATION DOCUMENTS – US Citizens

Required Business Documentation













APPENDIX D
Internal New Account Request
Name of Business/Entity________________________________________________________________
Nature of Business__________________________________________________________________________________________________________________________________________________________________________________________________________________________________
Type of Account Reqested______________________________________________________________________
Purpose of Account____________________________________________________________________________________________________________________________________________________
Description of anticipated activity, including check writing, ACH, domestic and international wire transfer volume:
______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
Any additional services requested, online banking, online domestic wire transfer, Business Debit Card:
__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
Requested by:
____________________________________________     _______________________
Signature						         Date
Relationship Manager__________________________________________________________

APPENDIX E
HIGH- AND MEDIUM-RISK INDUSTRIES LIST

High Risk Industries
Arms/Weapons Dealers – applies to clients engaged in the manufacture, sale or distribution of arms as well as agents, brokers or intermediaries in such activities
Art and Antique Dealers
Money Services Businesses
Cash Intensive Businesses – any retail business whose transaction profile shows $25,000 or more in cash transactions (aggregate of deposits and withdrawals) per week
Casinos and Other Gaming or Wagering Establishments – these are always high-risk, even if they are reputable and publicly traded entities
Charities, Endowments or Foundations – especially for organizations that accept funds from the public/third parties.  Exceptions not considered high-risk include large, well known reputable organizations such as the March of Dimes, United Way, and the Red Cross, organizations that administer U.S. Government sponsored programs, such as the Fullbright Scholarship program, and Charities, Endowments or Foundations that use funds from an individual, family, school, etc., where the source of funds is clearly bona fide and third-party donations are not accepted.
Deposit Brokers
Embassies, Consulates or Ministries
Third-party payment processors
Privately-owned ATM machines
Import/Export Brokers – those who never take possession of goods and/or have no physical location to demonstrate business
Leather Goods Stores
Off-Shore Personal Investment Companies, Money Management Businesses or Investment Management Businesses
Businesses That Accept Third-Party Checks – third party checks are checks made payable to one party and deposited into an account of a differently named party.  This does not include industries, such as collection agencies, where such conduct is not indicative of potential money laundering
Professional Service Providers acting in an intermediary capacity, such as a lawyers’ trust account (IOLTA) or an escrow account, where the Bank has no direct relationship with or knowledge of the beneficial owners of the accounts
Non-bank financial institutions that have accounts in the Private Wealth Management business.  Examples include:  securities/commodities firms, broker-dealers, mutual funds, hedge funds, commodity traders, investment advisors, dealers in precious metals, stones or jewels, pawnbrokers and loan or finance companies
Medium Risk Industries
Import/Export Businesses – also referred to as wholesale/distribution businesses which ship abroad or receive physical inventory from outside the U.S. and maintain a store or warehouse that can be observed
Internet Businesses – any business that sells goods and services over the Internet
















APPENDIX F
MEDIUM-RISK PRODUCTS LIST

The following products and services are deemed medium-risk:
Remote Deposit Capture Service – Product that enables business customers to make check deposits via an electronic check conversion service.


















APPENDIX G
STANDARD ACCOUNT REVIEW SHEET
To:	Chief Executive Officer

	From:								
	
	Date:			
	
	Re:	High – Risk Customer Submission





APPENDIX H
RESPONSES TO INFORMATION REQUESTS

According to Bank Policy, the BSA/AML Compliance Officer has been designated as the central Point of Contact for all 314(a) requests sent by FinCEN to the Bank.
 FinCEN posts on its secure website a list of individuals, entities and organizations which are under investigation by one or more federal agencies.  All financial institutions covered by 314(a) of the USA Patriot Act are required to quickly search their records to determine whether they maintain or have engaged in transactions with any of the named subjects.
If the Bank finds a match with a subject named on FinCEN’s 314(a) list, the match must be reported to FinCEN by making an entry on FinCEN’s secure website no later than fourteen (14) calendar days after the list was posted.  At that point, a federal agency may follow up with a subpoena for specified documents.  That subpoena is processed like any other subpoena from law enforcement.  If the Bank has no match, no response is necessary.
A search of all pertinent Bank systems that contain customer information to determine whether or not the Company has any “hits” for the names listed on the request.  The appropriate affirmative responses are entered on the FinCEN secure website.
Also the pertinent account or transactional activity is analyzed, and if the filing of a SAR is warranted, a SAR is prepared and filed.
All Bank employees involved in the processing and handling of 314(a) requests are required to keep the information confidential.  The fact that a 314(a) request has been made, or that responsive information has been found, may not be shared with anyone outside of the Bank, with the exception of FinCEN and appropriate law enforcement officers.  Moreover, the 314(a) requests and any supporting documentation must be maintained in secure files.
Note:  Refer to “314(a) Scanning Procedures” for detailed procedures regarding the process of down/up loading of files for filtering. 





APPENDIX I
POSSIBLE SIGNS OF ELDER FINANCIAL EXPLOITATION

Frequent large withdrawals, including daily maximum currency withdrawals from an ATM
Sudden non-sufficient fund activity
Uncharacteristic nonpayment for services, which may indicate a loss of funds or access to funds
Debit transactions that are inconsistent for the elder
Uncharacteristic attempts to wire large sums of money
Closing of CDs or accounts without regard to penalties
A caregiver or other individual shows excessive interest in the elder’s finances or assets, does not allow the elder to speak for himself, or is reluctant to leave the elder’s side during conversations
The elder shows an unusual degree of fear or submissiveness toward a caregiver, or expresses a fear of eviction or nursing home placement if money is not given to a caretaker
The financial institution is unable to speak directly with the elder, despite repeated attempts to contact him or her
A new caretaker, relative, or friend suddenly begins conducting financial transactions on behalf of the elder without proper documentation
The customer moves away from existing relationships and toward new associations with other friends or strangers
The elderly individual’s financial management changes suddenly, such as through a change of power of attorney to a different family member or a new individual
The elderly customer lacks knowledge about his or her financial status or shows a sudden reluctance to discuss financial matters.



“Insert Company Here”




Identity Theft and Red Flags Policy
Effective Date: XXXXXX, XX, XXXX



TABLE OF CONTENTS
1. OVERVIEW	3
1.1	Policy Overview	3
1.2	Purpose	3
1.3	Scope	3
1.4	Related Documents	4
1. DEFINITIONS	4
1. REQUIREMENTS	5
3.1	Program requirements	5
3.2	Training	6
3.3	Monitoring and testing	7
3.4	Issue Management	7
3.5	Documentation and Record Retention	7
1. ROLES AND RESPONSIBILITIES	7
1. EXCEPTIONS	8
1. POLICY ADMINISTRATION	9
6.1	Effective Date	9
6.2	Document Management	9
6.3	Approval Management	9


OVERVIEW

Policy Overview
[Insert Company Here] (“[Insert Company Here]” or the “Company”) is committed to preventing fraudulent use of personally identifiable information on its lending platform. This document (“Policy”) governs the oversight of the Identity Theft Red Flags used by [Insert Company Here] in connection with the lending program with [Insert Financial Institution Here] (“Bank”). This Policy also outlines the practices [Insert Company Here] uses to detect, prevent and mitigate instances of identity theft.

In November 2007, Federal Banking Agencies issued a set of regulations, known as the “Identity Theft Red Flags and Address Discrepancies Rule,” requiring that banks develop and implement written identity theft prevention and detection programs to protect consumers from identity theft. This rule implements sections 114 and 315 of the Fair and Accurate Credit Transactions Act of 2003 (“FACTA”), which amends the Fair Credit Reporting Act (“FCRA”).

[Insert Company Here] complies with all applicable laws, regulations and guidance pertaining to Identity Theft/Red Flags for regulated financial institutions.
 
Purpose 
The purpose of the Policy is to ensure that the risks related to Identity Theft Red Flags are understood and managed in a systematic fashion that is compliant with Bank policy, applicable laws, regulations and guidance, and serves the best interests of [Insert Company Here], the Bank, and consumers. This Policy is intended to assist [Insert Company Here] in:

Minimizing the threat of identity theft through disclosure or compromise of customer information held by the Company;
Responding to known or suspected identity theft involving the Company or its customers;
Aiding Company customers who may have been victims of identity theft;
Establishing processes or procedures for training Company personnel; and
Establishing processes or procedures for educating Company customers.

Except where specifically addressed herein, this Policy follows the Roles and Responsibilities, Training, Monitoring and Testing, Issue Management, and Document and Record Retention sections in the Compliance Management System Policy (“CMS”).

Scope
This Policy governs all aspects of [Insert Company Here]’s Red Flags/Identity Theft Program (“Program”), and is applicable to all personnel at [Insert Company Here], including both employees and consultants. It is also applicable to all third parties with whom [Insert Company Here] has entered into business arrangements for ongoing operational activities. Third parties include, but are not limited to, dental office partnerships, bank partnerships, and service providers.

Related Documents

Related Policies and Procedures
Compliance Management System Policy
BSA/AML and OFAC Policy
Data Handling and Retention Policy
Identity Theft and Red Flags Procedure

Applicable Law and Regulations
Fair Credit Reporting Act (FCRA)
Fair and Accurate Credit Transactions Act of 2003 (FACTA)

DEFINITIONS
For the purposes of this policy, the following terms are defined –

A Credit Reporting Agency (“CRA”) is a company that collects credit information on individual consumers from various sources and provides that individual’s borrowing and bill-paying history to financial institutions, creditors, and others.

A Covered Account is any consumer account [Insert Company Here] offers on behalf of its banking partners primarily for personal, family or household purposes, that involves multiple payments or transactions, for which there is a reasonably foreseeable risk of identity theft. All [Insert Company Here] consumer accounts are covered accounts.

Identifying Information encompasses any name or number that may be used, alone or in conjunction with any other information, to identify a specific person, including, but not limited to: name, address, telephone number, social security number, date of birth, government issued driver’s license or identification number, alien registration number, government passport number, employer or taxpayer identification number, unique electronic identification number, computer’s Internet Protocol address, or routing code. 

Identity Theft is fraud committed using the identifying information of another person.

A Red Flag is a pattern, practice, or specific activity that indicates the possible existence of identity theft.









 REQUIREMENTS
The processes listed below constitute the required Program elements as executed day-to-day. Standards, requirements and execution steps are further defined in supporting procedures. 

Program requirements

3.1.1 Periodic Review. [Insert Company Here]’s Red Flag Policy will be reviewed by the Bank and submitted to the Bank for review and approval. In addition, the Bank will conduct period reviews of [Insert Company Here]’s practices in this area, and through ongoing testing and periodic site visits, will ensure the Policy and programs are properly followed.

3.1.2 Policy Updates. [Insert Company Here] will update this Identity Theft Red Flags Policy (including the Red Flags determined to be relevant) periodically, to reflect change in risks to customers or to the safety and soundness of [Insert Company Here] or the Bank from Identity Theft. [Insert Company Here] will use risk assessments and other policies, and work with the Bank to make changes that may be necessary to the Identity Theft prevention and detection programs that [Insert Company Here] has developed and implemented. [Insert Company Here] will manage and administer an Identity Theft/Red Flags Program that is specifically tailored to the needs and experience of the program administered by [Insert Company Here]. [Insert Company Here] will assign a qualified individual with responsibility and accountability for overseeing the program. Changes to [Insert Company Here]’s policy or program may be required based on factors, including, but not limited to:
Previous experience with Identity Theft;
Changes in methods to detect, prevent, and mitigate Identity Theft;
Changes in types of accounts offered or maintained; and
Changes in business arrangements between [Insert Company Here] and its partners

3.1.3 Identity Theft Detection, Prevention and Mitigation. [Insert Company Here] will adhere to the guidelines presented in Appendix J to the Interagency Guidelines on Identity Theft Detection, Prevention and Mitigation. The Program shall include the following elements:
Identification of relevant Red Flags;
Detection of Red Flags that are part of the Program;
Responding appropriately to any detected Red Flags to prevent and mitigate Identity Theft; and
Ensuring the Program is updated periodically to reflect changes in risks

3.1.4 Third Party Servicers. [Insert Company Here]’s Program must also address the oversight of any third-party servicers that perform services in connection with Covered Accounts. 

3.1.5 Annual Reporting. [Insert Company Here] will provide a report to the Bank on the effectiveness of its Identity Theft/Red Flags Policy no less than annually. The report provided to the Bank by [Insert Company Here] should address material matters related to the Program and evaluate issues such as:
The effectiveness of the policies and procedure sin addressing the risk of Identity Theft in connection with the opening of Covered Accounts and with respect to existing Covered Accounts;
Service provider arrangements;
Significant instances involving Identity Theft and management response; and
Recommendations for material changes to the Program

3.1.6 Program Categories. The Rule requires all financial institutions and creditors to design and implement a risk-based program that is appropriate for the size, complexity, and nature of operations. Guidelines issues by the FDIC and other federal law enforcement agencies were used by [Insert Company Here] in designing its Program. A supplement to the Guidelines identifies 26 possible Red Flags. These Red Flags are not a checklist, but rather examples that may be used be used as a starting point in identifying concerns. [Insert Company Here]’s Program should ensure that they have appropriately addressed each of the five categories of Red Flags as necessary. These five categories are as follows:
Alerts, notifications, or warnings from a CRA or other service provider;
Suspicious Documents
Suspicious personally identifying information, such as a suspicious address change
Usual use of – or suspicious activity relating to – a Covered Account; and
Notices from customers, victims of Identity Theft, law enforcement authorities, or other businesses about possible Identity Theft in connection with Covered Accounts.

In addition to addressing these five categories, [Insert Company Here]’s Program includes a requirement for annual review and approval of the Red Flags Program, designation of a Program Administrator, and mandatory annual training.

3.1.7 Address Discrepancies. On behalf of the Bank, [Insert Company Here] must also develop and implement reasonable processes and procedure designed to handle notices of address discrepancy received from CRAs. Whenever [Insert Company Here] receives a notice of address discrepancy in connection with a new or existing account, it must take action to resolve the discrepancy and form a reasonable belief that the consumer report related to the consumer whose report was requested. See Fair Credit Reporting Act Policy and associated procedures for additional information related to handling address discrepancies.

Training
In accordance with the Compliance Management System Policy, all employees and, as appropriate, contractors and temporary staff receive training on the Red Flag Policy/Program at least annually. Additional training should occur commensurate with roles and responsibilities for personnel more actively involved in the execution and development of related-policies and procedures. Evidence of training is retained and made available upon request.


Monitoring and testing
[Insert Company Here] maintains appropriate monitoring and testing to reasonably detect and prevent control design or effectiveness failures. Additionally, [Insert Company Here] will provide necessary reporting or data to the Bank in support of its monitoring and testing requirements. The Bank and [Insert Company Here] will work closely to ensure effective coordination and communication of such activities

Issue Management
Issues or changes related to risk, process or control failures pertaining to Identity are tracked and managed by [Insert Company Here]. Issues logged have an owner, issue date, issue description, priority level, risk level, and an action plan for remediation, including a target date for closure. A summary of issues is reported to Risk Management Committee and the Bank on a monthly basis. Issues requiring action or management attention are managed through the issue escalation process.

Documentation and Record Retention
All activities supporting adherence to this Policy are documented and retained for review by the Bank and external auditors, including federal and state regulators in compliance with the Data Handling and Retention Policy. This includes policies and procedure, risk assessments, monitoring reports, training materials, and issues that are currently opened or closed.

ROLES AND RESPONSIBILITIES

EXCEPTIONS
From time to time, [Insert Company Here] may reasonably determine that a Policy exception is warranted. All exceptions must be approved in writing by the Policy Owner and reported to both the Compliance Committee and the Risk Management Committee. The Risk Management Committee must be appraised of potential risks associated with the exception as well as any proposed actions for mitigating risks.

Notwithstanding the foregoing, under no circumstances does this Policy permit an exception that would result in a violation of law.



POLICY ADMINISTRATION

Effective Date

Document Management 
This section is intended to track minor updates. Minor updates to the Policy/Program may be approved by the chair of the responsible management committee.


Approval Management 
(This section is intended to track formal approval dates/authority)



 
 
 
 
 
 
Escalation and SAR  Policy 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Date Issued  9th November 2017  
Issue Number  2.0 
Review Date  Annually  
Published on  Policies and Procedures Jam page  
Paysafe  Internal – for Paysafe internal  use only  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 2 
 Copyright © Paysafe Group  
 
All rights reserved. This document and the information it contains, or may be extracted from it, is subject to the terms 
and conditions of the agreement or contract under which the document was supplied to the recipient’s organisation.  
 
None of the information contained in this document shall be disclosed outs ide of the recipient’s own organisation without 
prior written permission of Paysafe Group, unless the terms of such agreement express ly allow.  
In the event of a conflict between this document and a relevant law or regulation, the relevant law or r egulation shall 
be followed. If the document creates a higher obligation, it shall be followed as long as this also achieves full 
compliance with the law or regulation.  
 
Use of language  
 
Throughout this document, the words ‘ may’ , ‘should’  and ‘ must ’ when used in the context of actions of Paysafe Group 
or others, have specific meanings as follows:  
 
(a) ‘May’  is used where alternatives are equally acceptable.  
(b) ‘Should’  is used where a provision is preferred.  
(c) ‘Must ’ is used where a provision is mandatory.  
 
Note that alternative or preferred requirements may be qualified by Paysafe Group in another referenced document.  
 
Paysafe  Group and the companies in which it directly or indirectly owns investments are separate and distinct entities. 
In this publication, however, the collective expression ‘ Paysafe’  and ‘ Paysafe  Group’  may be used for convenience where 
reference is made in ge neral to those companies. Likewise, the words ‘ we’, ‘us’, ‘our’  and ‘ ourselves’  are used in some 
places to refer to the companies of the Paysafe Group in general. These expressions are also used where no useful 
purpose is served by identifying any particul ar company or companies.   
 
In this document, third party  means any individual or organisation you come into contact with during the course of your 
work for us, and includes actual and potential clients, customers, suppliers, distributors, business contacts , agents, 
advisers, and government and public bodies, including their advisors, representatives and officials, politicians and 
political parties.  
 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 3 
 
 
 
Document Approval  
 
Date approved  Approved by  Signed by  Signature  
 
9th November 
2017   
Elliott Wiseman  
General Counse l and 
Chief Compliance 
Officer  
  
Maximilian von Both  
Senior Vice President, 
Compliance  
  
 
 
 
 
 
  Summary : 
The purpose of this Compliance Policy  is to assist all employees by clearly setting out the processes that must be 
followed if anyone has  knowledge, suspicion or reasonable grounds for suspicion that Paysafe product is being used 
for money laundering, terrorist financing or other criminal activities .   
 
Supporting Policy  
Global Compliance Policy  Review and maintenance  
This Policy  will be reviewed and maintained by the Paysafe Head of Policy  and Assurance at least on an annual basis. 
The provisions of this policy can be amended and supplemented from time to time by the Paysafe Senior Vice 
Presiden t, Compliance.   
 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 4 
TABLE OF CONTENTS  
1. INTRODUCTION  6 
1. WHO DOES THIS POLICY  APPLY TO?  7 
1. NOMINATED OFFICER – PROCEEDS OF CRIME ACT 2002 (POCA ) 8 
1. WHAT IS SUSPICIOUS A CTIVITY?  8 
4.1. Money laundering and terrorist financing  9 
4.2. Our experience  9 
4.3. High -risk activities  9 
1. OUR INTERNAL REPORTI NG PROCESS  11 
5.1. Suspicious activity identified  12 
5.2. Who is the responsible MLRO?  13 
5.3. Investigative steps to be considered  13 
5.4. Content of an Internal SAR  16 
5.5. Failure to make an Internal SAR  16 
5.6. Tipping off  17 
1. OUR EXTERNAL REPORTI NG PROCESS  17 
6.1. Who is responsible for external reporting?  17 
6.2. MLRO review  18 
1. COMMUNICATION AND DI SCLOSURE OF INFORMAT ION 19 
1. ONGOING MONITORING O F SAR ESCALATIONS AN D DECISIONS  19 
1. GLOSSARY  20 
APPENDIX 1  22 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 5 
INTERNAL SAR CHECKLIST  22 
APPENDIX 2  24 
KEY  TRAITS OF AN E -MONEY LAUNDERER  24 
APPENDIX 3 FURTHER GUIDANCE ON SUSPICIOUS ACTIVITY  26 
APPENDIX 4  33 
FURTHER GUIDANCE ON SUSPICIOUS ACTIVITY  33 
  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 6 
1. Introduction  
 
It is Paysafe’s policy to conduct all of our business in an honest and 
ethical manner.  
The purpose of this Compliance Policy  is to assist all employees by  
clearly setting out the processes that must be followed if anyone  has: 
• suspicions that a Paysafe product is being used for money 
laundering, terrorist financing or other criminal activities ; 
 
• reasonable grounds to suspect that any attempted, upcoming, 
ongoing or previously conducted transaction involving Paysafe  
products may constitute criminal conduct or have involved the 
proceeds or funding of criminal activity.  
This Compliance P olicy  must be followed unless there are exceptional 
circumstances justifying a variation.   
If an employee considers that this Complian ce Policy  is not applicable 
for an activity covered within the scope of this document, the 
individual must seek written permission from the responsible MLRO  or 
their approved delegate before deviating from this Compliance P olicy . 
A failure to follow this Compliance Policy  could severely harm 
Paysafe’s reputation, financial standing and possibly breach the terms 
of the licences necessary to operate our business. Any such failure may 
result in disciplinary action or termination for  any employee found to 
have breached this Escalation and SAR  Policy  and may constitute a 
criminal offence.  
This Compliance Policy  supersedes all previous group policies 
regarding  Escalation and SARs  and is supplement ed by  the Escalation 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 7 
and SAR Guidance N otes . It should be read together with the :  
• Paysafe Code ;  
• Global Compliance Policy ; 
• Customer Due Diligence  Policy ;  
• Merchant and Distributor Due Diligence  Policy ; and  
• Transaction Monitoring and Investigations  Policy . 
This Compliance Policy  primarily focuses on European regulations, and 
sets a minimum group -wide standard, based on the strictest law within 
the EU. If specific local regulations, outside of the EU, require higher 
standards or stricter provisions, the local entity will always co mply 
with such local regulations. Less strict rules will only be implemented 
if they have a clear legal basis, are accepted by local supervisory 
authorities (where appropriate), and are approved by the responsible 
MLRO.  
A glossary of define d terms is included at section 8  of this Compliance 
Policy . 
 
 
1. Who does this P olicy  apply to?  
 Where can I find further information?  
 
Further explanation of the detailed business processes described in 
this Global Compliance Policy can be found in the supporting 
Escalation and SAR  Guidance Notes . 
Please also see the Transaction Monitoring  and Investigations  
Policy . 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 8 
This Compliance P olicy  applies to all Paysafe  employees , directors and 
non-executives as well as all other work ers who work with us (whether 
as consultants, secondees, volunteers, sponsors or otherwise).  
 
1. Nominated Officer – Proceeds of  Crime Act  2002  (POCA)  
 
Paysafe Group has the responsibility to appoint a Nominated Officer  in 
accordance with  the Proceeds of  Crime Act 2002 (POCA), of sufficient 
seniority.   
The POCA is an Act of the Parliament of the United Kingdom which 
provides for the confiscation or civil recovery of the proceeds from crime 
and contains the principal money laundering legislation in the UK.  
Paysafe nominated the VP Regulatory Compliance team  as a Nominated 
Officer who is responsible for:  
 
• receiving reports of suspicious activity from any 
employee in the business ; 
• considering all reports and evaluating whether there is 
- or seems to be - any evidence of money laundering or 
terrorist financing ; 
• reporting any suspicious activity or transaction to the 
National Crime Agency (NCA) by completing and submitting 
a Suspicious Activity Report ; 
• asking the NCA for consent to continue with any 
transactions that they’ve reported, and making sure that no 
transactions are continued illegally ; 
1. What is suspicious activity?  
 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 9 
4.1. Money laundering  and terrorist financing  
Whilst there are specific definitions of “money laundering” 
and “terrorist financing” set o ut in the relevant legislation, in 
Paysafe we define m oney laundering  and terrorist financing 
together as:  
 
“Possessing, or in any way  dealing with, or concealing, the 
proceeds of any crime. It also involves similar activities 
relating to, terrorist funds, which include funds that are likely 
to be used for terrorism, as well as the proceeds of terrorism .” 
 
4.2. Our experience  
We have found a number of recurring money laundering , 
terrorist financing or other illegal activity  typologies that 
relate to Paysafe products. These almost all relate to various 
types of fraudulent activities that are “predicate offenc es to 
money laundering” (i.e. crimes  which underlie money 
laundering) or other illegal activity including terrorist 
financing . 
 
Based on our experience, we have identified certain activities 
that we treat as suspicious or high -risk (or very high -risk). If 
we identify such activity , we will investigate further and, if 
appropriate, notify the relevant authorities  following the 
process set out in this Compliance P olicy . 
4.3. High -risk activities  
A transaction is treated as high -risk or suspicious if it does 
not fit behavioral patterns asso ciated with the average 
member  (customer, merchant o r distributor) of Paysafe 
products. Behavioral patterns derive from historical data 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 10 
available to Paysafe. Transactions may also be defined as 
high -risk based on an analyst’s experience whenever new or 
evolved fraud patterns have been identified.  
 
A high risk or suspicious transaction must  be investigated to 
see whether it shows one of the following components:  
 
• fraud, theft or other known illegal activity;  
 
• breach of the contract terms between Paysafe  and 
merchants (or distributors) ; 
 
• breach of the contract terms between Paysafe and 
customers;  
 
• patterns of activity that cannot be explained for 
legitimate commercial reasons and that appear 
consistent with money laundering or other criminal 
activity.  
 
These patterns of activity do not always indicate that 
suspicious activity has in fact taken place. You must  always,  
however, investigate such observed suspicious patterns to 
determine what the causes of the pattern are likely to be.  
 
Depending on the risk  associated with the patterns ( e.g. the 
volume of money involved, or a high degree of similarity to a 
recent activity already determined to be suspicious) , we may  
choose to block involved vouchers, accounts or customers 
while we carry out our investigation . 
 
We will file a SAR , following the process set out in paragraph 
5 below , when we have : 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 11 
 
• suspicions that a merchant, distributor or customer 
account is being used for money laundering, terrorist 
financing or other criminal activity;  or 
 
• reasonable grounds  to suspect that any attempted, 
upcoming, ongoing or previously conducted 
transaction involving Paysafe products may constitute 
criminal conduct or involve the proceeds or funding of 
criminal activity.  
 
You must  ensure that you are familiar with the guidance 
includ ed in this Compliance Policy : 
 
• Appendix 2 sets out the key traits of an e-money 
launderer.  
 
• Table 1 of Appendix 3 gives further guidance (based on 
our Paysafe business’ experience) of key traits of 
suspicious activity.  
 
• Appendix 4 explains some of the key money 
laundering, terrorist financing and other illegal activity 
typologies that we are aware of.  
 
1. Our internal reporting process  
 
There is a statutory obligation on all employees to report suspicious 
transactions , activity or content .  
This Compliance P olicy  sets out the policy that must  be followed to 
escalate concerns that an account may be  being used for money 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 12 
laundering or terrorist financing.  
On escalation, the Regulatory  Compliance Dep artment  must   decide 
what further verification steps are to be taken or if the case needs to 
be reported  to law enforcement agencies. A record of all internal 
money laundering reports must be kept to ensure proper record 
keeping  and must be sent to the MLRO for Management Information .  
Our Internal Reporting Process  can be summarized as follows ( Figure 
1): 
 
 
5.1. Suspicious activity identified  
All employees  are responsible for  identify ing suspicious 
transactions , activity or content . 
 
• Suspicious activity must be reported as an Internal SAR 
to sar@paysafe.com . 
 
• The AML Investigation Team must review the internal 
suspicious  activity following the steps below to 
confirm the suspicion and then  prepare the SAR report 
Suspicious activity 
identified
Review by the AML 
Analyst
Internal SAR escalation to 
Regulatory Compliance 
for determination 
whether to submit an 
external SAR
Report to MLRO for 
Management Information
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 13 
for the  National Crime Agency  (NCA)1 (as well as any 
other applicable Financial Intelligence U nit (FIU)) . 
Regulatory  Compliance reviews and submits  the 
report to the NCA /applicable FIU  on behalf of the 
MLRO.  
5.2. Who is the r esponsible MLRO ? 
The responsible MLRO  with Paysafe are : 
 
• The Group MLRO of Paysafe  Group  or in his /her  
absence his /her  deputy ; 
 
• Germany MLRO for business of “paysafecard.com 
Deutschland, Zweigniederlassung der Pr epaid Services 
Company Limited”;   
  
• Swiss  MLRO for business of “paysafecard.com Schweiz 
GmbH” and MENA DMCC ; 
 
 
5.3. Investigative steps to be considered  
The exact steps to be followed when investigating potential 
suspicious activity  will depend on the circumstances and 
nature of the suspicion. In particular, when determining the 
appropriate level of investigation, you must  take into 
account the nature of:  
 
• the initial referral;  
 
• the suspicion itself ; 
 
                                                        
1 NCA is the FIU for the UK.  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 14 
• the degree of clarity around the suspicious activity ; 
 
• the number of accounts /products  concerned ; 
 
• contact from the customer ; 
 
• the products being used; and  
 
• the extent of knowledge about the account /products (s) 
concerned.  
The goal of all investigations and Internal SARs  review 
process  is to fully understand the activity a customer is using 
our products and services for, establish the customer ´s 
profile, define the suspicious behaviour or activity, 
investigate and document all relevant data and then provide 
a reasonable conclusion to aid the responsible MLRO (or duly 
authorised deleg ate) to determine if escalation to the 
authorities is appropriate.  
The following steps should  be followed when compiling a n 
Internal  SAR. These steps must  be considered in light of the 
Recommended Content of an Internal SAR (see paragraph 
5.4 below) : 
 
• an initial review is carried out of the relevant 
account(s) /product  customer  info section, transaction 
history, finan cial details, comments section, duplicates 
info, log -in information, KYC on file.  
 
• Member accounts linked by account information, 
behaviours  and/or memb er to member relationships are 
thoroughly reviewed  following a risk -based approach .  
 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 15 
• Transaction details are analysed to establish transactional 
behaviours or patterns, or changes in them, to identify 
possible suspicious transactions; often th e entire account 
history may look suspicious. When looking at transaction 
history, a number of criteria may need to be reviewed 
including: products being used,  risks as sociated to those 
products; and any subsequent associated source of funds 
information.  
 
• Sources of such information may include , inquiries with 
the payment processing teams, the business units, 
merchant enquiries, peer mates, and/or account review 
with the member.  
 
• The comments section of a member’s account is an 
ongoing archive of the member ’s data. The investigator 
can observe previously documented links, previously 
listed personal and financial information which has been 
changed, documentation collected/KYC notes, recorded 
email and live person exchanges, etc., all of which 
contribute to un derstanding the member’s profile.  
 
• Bank information or credit/debit card associated to the 
account should be observed.  
 
• Searching a member’s login IPs can be useful in 
establ ishing common IP users. For the purpose of a 
review, it is generally beneficial to  set the date range for 
one year.  
 
• Any known business relationships associated to the 
account (may be determined in the account review phase, 
noted in comments, flagged as an affiliate, business name 
in email domain, etc.) shou ld be taken into consideratio n. 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 16 
 
• Web  search  should be used to search for any possible 
adverse information.   
• Review of the Responses  of the member . 
 
• If KYC documents are relevant to the investigation, they 
should be reviewed for authenticity and the conclusion 
clearly noted in the Internal SAR. If they are deemed in 
some way to be fraudulent or questionable, copies will be 
placed into the SAR folder.  
 
• The SARs register  must be completed with all pertinent 
information. A n Internal  SAR form  must be populated, 
including a free form nar rative summary of findings, and 
any conclusion (or lack thereof) about the activity that 
was reported as suspicious. Should the responsible MLRO 
(or duly authorised delegate)  decide to escalate the case, 
the escalation would take place as soon as practicab le. 
 
5.4. Content of an Internal SAR  
You must  follow the recommended content checklist set out 
in Appendix 1 (Internal SAR checklist).  
5.5. Failure to make an Internal SAR 
A failure to make, without reasonable excuse, a report about 
a suspicious transaction is a breach of an employee ’s 
employment  contract and may have disciplinary 
consequences. It may also constitute a criminal offence2. 
                                                        
2 Under the Proceeds of Crime Act 2002  (POCA 2002) , it is a criminal offence for a 
person working in the regulated financial sector, if they fail to report where they have 
knowledge , suspicion or reasonable grounds for knowledge or suspicion that another 
person is laundering the proceeds of any criminal c onduct.  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 17 
5.6. Tipping off  
It is a criminal  offence for anyone to take any action to 
prejudice an investigation by informing the person who is  or 
might be  the subject of a suspicion report, or anybody else, 
that a disclosure has been made, or that the police or 
customs authorities are carrying out or intending to carry out 
a money laundering investigation3.  
This means that you must not  make any disclosure or do 
anything that you suspect might prejudice any investigation 
the police or other authorities may be undertaking  
The responsible  MLRO  (or duly authorised delegate)  must  
decide  (on a case -by-case basis ) how best to communicate 
with a suspicious customer /merchant (or distributor)  to 
ensure compliance with the se tipping off rules  but at the 
same time avoid complaints to escalate (e.g. block ed 
accounts).  
1. Our external reporting process  
 
We are required to report promptly  to the National Crime Agency  
(NCA) (as well as any other applicable financial intelligence unit (FIU)) 
any suspicious transactions and to maintain our internal control 
system  so that suspicious transactions can be verified.  
6.1. Who is responsible for external reporting?  
The responsible MLRO (or duly authorised delegate ) is 
responsible for submittin g Suspicious Activity Reports (SARs ) 
to the NCA  and Paysafe’s  other external money l aundering 
                                                        
3 Section 333 POCA 2002.  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 18 
reporting duties ( although  any employee  remains 
responsible to report any suspicious activity internally).  
The MLRO must  keep proper records of any decision not to 
make a report to the NCA . 
 
6.2. MLRO review  
The responsible MLRO (or duly authorised delegate)  must 
review the Internal SAR  without undue delay. All internal 
report s received by the responsible MLRO must  be recorded 
on the internal ”MLRO dashboard”.  
 
The MLRO may  then require further investigation (e.g. to 
contact the customer, merchant or  distributor involved 
asking for further information). The MLRO may  also ask for 
additional blocking/unblocking actions to be taken in 
connection with the Internal SAR, and must  record in writing 
the reasons for such requests.  
 
The responsible MLRO must  decide, in a timely manner, 
whether the available information provides sufficient 
grounds for reasonable suspicion to meet the standard 
required for filing a SAR with the financial intelligence unit 
(FIU) in the appropriate country. If that standard is me t, the 
responsible MLRO must  file an accurate, thorough, 
informative and timely SAR with the relevant FIU in 
accordance with regulatory guidelines and to complete any 
other notifications required to relevant  regulatory bodies in 
the MLRO’ s area of responsi bility.  
 
The responsible MLRO must ensure  that these actions are 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 19 
carried out in a timely and competent manner.  
 
If the responsible MLRO decides that the available 
information does not provide sufficient grounds for filing a 
SAR with the relevant FIU, the MLRO must  document in 
writing  the reasons for that decision.  
 
 
 
1. Communication and disclosure of information  
 
Once it has been decided that reasonable grounds for suspicion exist:  
 
• you must not  give any further information to external parties 
(other t han law enforcement and authoris ed regulatory 
entities) ; 
 
• the customer , merchant or distributor  may be notified that the 
account is still under account review , but must not  be told that 
suspicious activity is suspected or is being reviewed.  
All informati on connected with Internal SARs and the detection of 
suspicious activity must  be kept confidential wi thin Paysafe and must 
not be shared with other employees unless necessary for them to carry 
out their job.  
1. Ongoing monitoring of SAR escalations and decisions  
 
The Compliance  Department  seeks to ensure that timely, accurate, risk 
sensitive decisions are being made about how best to comply with our 
obligations and ensure that appropriate activity is identif ied and, as 
necessary reported.  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 20 
Periodic spot checks are made of accounts where pot entially 
suspicious activity has been identified and the process and decisions 
taken are reviewed by the Compliance Department . This includes 
cases in which the decision has been taken not to file a SAR with 
external bodies, to ensure that such decisions a re being taken and 
documented appropriately.  
The results of these reviews are reported to the responsible MLROs, 
the Group MLRO and the Paysafe Audit Committee . 
 
1. Glossary  
 
Customer means any non -commercial user of the system, who has 
opened an account through the Paysafe websites and has signified 
their willingness to start using our products.  
 
Device ID  means a  unique device identifier assigned by our monitoring 
system  to the comput ing device used to make a transaction  or to 
register for a new  account.  
 
EU means European Union.  
 
FIU means Financial Intelligence Unit.  
 
Internal SAR  means a suspicious activity report made by an employee 
to following the checklist at Appendix 1.  
 
KYC means  Know -your -customer, the process, which begins at the 
time of signup, through which the business verifies the identity (name 
& date of birth) as well as the residence (address) of the customer, in 
accordance with the guidelines, provided by the  UK Financial Conduct 
Authority ( FCA). 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 21 
 
Member  means any user of our services.  
 
MLRO means money laundering reporting office r. 
 
NCA  means National Crime Agency. NCA is the FIU for the UK.  
 
PEP means Politically Exposed P erson.  
 
SAR means Suspicious Activity R eport.  
 
Verification means the act of verifying that the provided details and/or 
documentation are valid, truthful and correspond to the customer's 
details that the business has on file.  
  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 22 
APPENDIX 1 
INTERNAL SAR CHECKLIST  
• What is the concrete suspicious activity (detailed description of the 
suspicious activity)?  
 
• Where  and when  has the suspicious activity taken place?  
 
• How did we become aware of the suspicious activity?  
 
• Why is the activity suspicious (i.e. suspicious in such a way that we are 
obliged to report it)? Include a detailed description of the facts that 
indicate a suspicion of money laundering/terrorist financing.  
 
• Who are the suspected persons (real individuals4 who have been 
identified in the course of the investigations)? Is it a PEP or a 
sanctioned person? Add all the information you have about these 
persons to the Internal SAR (personal data and information about their 
transaction behavio ur).  
 
• How did we gather information about the suspected persons? If you 
have contact ed a merchant, briefly describe what the merchant has 
been asked, what his answer was and how this information has been 
used in this Internal SAR.  
 
• For real persons identified as suspects, why do we believe that these 
persons played an active role in the s uspicious activity?  
 
• Are there any patterns and similarities that form links between 
suspects or activities that might otherwise appear unrelated? Include 
                                                        
4 Real individuals are persons whose identity was verified with the help of an official 
identification document (e.g. ID card, driver licence, passport).  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 23 
detailed descriptions of these patterns and similarities (e.g. when you 
have information that a group  of suspects work together, describe 
how  you have this information and how the individuals are linked ). 
 
• Have any Device IDs , accounts and/or cards  (e.g. MasterCard, 
paysafecard voucher)  been blocked? Add information about the 
blocked Device ID, account and/or card, date of block, reason for 
block, who blocked it.  
 
• Have any accounts of the suspected person been identified? If so, 
name the account number and describe the transaction behavi our of 
the account holder. Describe any abnormalities identified on the 
account.  
 
• Is there a link to an Internal SAR that has already been fi led with the 
responsible MLRO? Include the Internal SAR number and describe the 
connection.  
 
• What are the sources of information and is there any other 
information available that could be useful to the authorities?  
 
• Describe what steps you have taken to investigate the suspicious 
activity, name the documents (e.g. excel files) where the results of the 
relevant analyse s can be found and set out where any supplementary 
information can be found.  
 
  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 24 
APPENDIX 2 
KEY TRAITS OF AN E -MONEY LAUNDERER  
• Cross border transactions (IP Mismatches, Company Structure, 
Multiple Bank Accounts)  
 
• Layering of casino winnings won by multiple accounts connected to 
a master account controlling the scheme  
 
• Irregular or Short Term Account Usage. E.g. High value deposit, 
stays dormant for 6 months then withdrawn  
 
• U Turn Transactions – Money Passes from one person or company 
to another, and back to the original person or company  
 
• High Value One -off Transactions with no real explanation  
 
• Member is defensive when requested ID documents  
 
• Merchant activities are susp ect based on URL check ( in breach of 
the Paysafe Group Terms and Conditions , the w ebsite does not 
contain privacy statement, no legal documents supplied, missing 
Terms and Conditions, not registered with other regulated e -
money payment options)  
 
• Comments on account from the Fraud Department   
 
• Multiple accounts with no identity documents, false identity 
documents or spurious registration details. E.g. incomplete 
telephone numbers, irregular postal codes, nonsensical first and 
last names.  
 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 25 
• Suspect Country T raits – e.g. IP’s registered from countries such as 
considered high risk (e.g. see Merchant and Distributor Due 
Diligence Policy ).  
 
Please take note that the above criteria are a strong indicator, but 
it is also limited in its application and none of the above have to be 
present in order to identify an E - money launderer.  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 26 
APPENDIX 3 
FURTHER GUIDANCE ON SUSPICIOUS ACTIVITY  
TABLE 1 : FURTHER GUIDANCE ON SUSPICIOUS  ACTIVITY  
Suspicious 
Activity  
 Description  Trait  
Non -delivery 
(confirmed)  Suspect ecommerce URL or auction merchant selling goods 
that are subsequently not delivered.  The sellers usually sell 
their products and services by advertising them in social 
media and forums.  The merchant withdraws profits or sends 
to another account to start up a similar operation.  The sellers 
are usually unable to provide with delivery proof if such is 
requested for justifying the receipt of a  particular payment.  
In confirmed non -delivery cases the money launderer 
creates the URL or auction site to defraud multiple buyers (> 
5 complaints received). In a different variation of the scam 
the fraudster takes over a genuine auction site to process 
orders without delivering. Take over cases are achieved using 
phishing attacks, when the fraudster has gained access to an 
auction seller ID and password.  Non -response to ID request, multiple 
comp laints as goods never dispatched, and the 
merchant  has gone out of business, withdraws  
the profits of latest orders (previous good 
history), transactions serve a short -term 
purpose.  
 
Fraud 
Proceeds 
laundered  In these cases, the money launderer creates a set of multiple 
accounts using stolen identities to fraudulently obtain funds. 
A stolen identity (also known as “ID Fraud” or “ID Theft”) is 
when a fraudster has accessed a name, address and the 
financial detai ls of a victim he intends to defraud. How the 
fraudster collects and uses this information depends on his 
own creativity. In the section “Phishing Attacks” the most 
common method of identity theft is discussed.  
Once the fraudster has control of the victim ’s account he 
sends stolen funds to connected accounts. To disguise the Western European name and address, address 
verification  fails by name and/or post code , IP 
mismatch with country of registration, 
Occasionally Mr. <female>, connected to other 
accounts by : similar emails, ‘passmates’, IP 
Mates, date of birth , time of registration, 
transaction pattern and ZIP  code . When dialing 
telephone number person unknown by 
recipient.  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 27 
fraud,  he splits the payments, and then skims under 
transaction verification limits to avoid detection. Commonly, 
stolen identities are Western European or US profiles, with a 
transact ion limit of 1000 EUR. Eventually, the money 
launderer will collect the funds, and then withdraw to his 
own bank account. Or, he will use a stolen identity to buy 
resalable goods such as Voice -Over IP credits, lottery tickets, 
virtual game credits and web design templates.  
  
Betting fraud 
controller 
(BFC)  A betting fraud controller is the main suspect account who 
collects the pay -outs generated by fraudulent activity at a 
betting firm. Paysafe  ensure s confirmation that pay -outs are 
generated by fraudulent activity is received from the casino. 
This means the  casino will confirm either that a chargeback 
is received that confirms fraud; or that forensic evidence 
proves multiple accounts are connected (Forensic evidence 
includes password mates, IP mates and time of registration).  
 Winnings paid out simultaneously in similar 
values to a set of multiple accounts created 
using stolen Western European identities. The 
stolen identities are connected by IP or 
‘passmates’ and have no prior funding via the 
Paysafe  account. Fraudulent pay -outs are then 
collec ted by a main account or group with high -
risk country traits.  
 
Credit card 
fraud 
laundered 
(CC/ML)  A credit card fraud controller is similar to Betting Fraud, 
except that the main suspect collects the credit card fraud 
proceeds directly from the victim’s  accounts.  
 In a related scheme, CC payments are often 
from a set of cards with a similar BIN range 
(banking identification number is the first six 
digits of the card number). This type of CC fraud 
is known as ‘Credit Master Fraud’, which means 
a series of valid CC nu mbers are generated 
using a program that predicts card numbers, by 
analysing the algorithms of previously issued 
cards. Alternatively, CC/ML activity is a result of 
a Phishing Attack.  
Fraudulent Credit Card uploads will eventually  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 28 
result in chargeback. A chargeback is when the 
genuine card holder contacts the card issuer 
(e.g. Visa, Amex, MasterCard) to dispute a card 
transaction.  
 
Bank wire 
fraud 
laundered  A bank wire fraud controller is the main suspect account, 
who collects the proceeds of bank wire fraud deposits, into 
an account held with Paysafe .  
Bank wire fraud payments are usually connected to an 
auction platform. In these cases, the fraudster tricks the 
victim into sending money via bank transfer to pay for non -
existent goods. The fraudster will provide the customer with 
a reference to initiate the bank transfer. The reference is the 
customer account ID of Paysafe , created by the seller 
(fraudster) using the delivery address provided by the 
auction buyer (victim).  
The victim enters  the exchange in good faith, under the 
impression that wire transfer funds will be received by the 
fraudster. Concern arises when the victim receives his bank 
statement which displays the Paysafe  debit. Bank wire fraud 
cases are reported either by the vict im, bank or the police 
investigating the case. Any available balances are refunded 
to the victim.  
 Suspect connected to associate victim by 
password, similar emails, registered IP Address, 
time of registration, similar customer ID range, 
and transaction p attern. Bank Wire uploads of 
similar value in all associate victim accounts; 
then sent to main suspect account 
simultaneously.  
 
False ID  Suspicion of False ID sent in to verify an account held with 
Paysafe  e.g. Passport, driver’s license or identity card - 
blurred ID, low resolution copy, coat of arms omitted; 
signature or font appears in a courier typographic, photos 
are not aligned, MRZ  (Machine Readable Zone)  does not Linked by device, IP, password, time of 
registration, transa ction pattern and address – 
city, zip code, street.  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 29 
match the data in the document, the document template 
does not exist, details such as photograph, colouring, stamps 
look out of place. Depending on the quality of the false 
document it can be hard to spot.  
Employees authorised to complete document verifications 
undergo document verification training. According to the UK 
Fraud Act 2006, an offence is committed once false identity 
documents are submitted (Fraud Act 2006 (2) Fraud by false 
representation).  
Most common cases of false identification are related the 
verificat ion of groups of fake accounts created for the 
purpose of promotion abuse. To receive more bonuses, a 
bonus abuser must create a large number of accounts that 
will be funded from one master account where the real 
details of the abuser will be registered. T he other accounts 
will attempt verification with fake documents. When asked 
for explanation of activity, the customer provides unclear 
information that does not explain the transaction history.  
  
Phishing 
Attacks  Phishing attacks are predominantly designed by the 
fraudster to facilitate identity theft in order to ‘hack’ 
member  accounts and defraud them. The Account Take Over 
(Controller) uses spoof emails to trick the member  into 
disclosing their login details. The fraudster has altered the 
sender field of the e mail to make the victim think that the 
Paysafe  Group customer serv ices is requesting further 
information. Once the victim clicks on the Link to “update” 
information a fake website is displayed. The fake website will 
replicate the home page of the Paysafe  Group. Except t he 
URL supplied is not ww.paysafe .com.  
Often the Account Take Over (Controller) never reveals their Merchant or customer complains account is 
“hacked” or lost balance. IP address reveals 
suspect last login not  consistent with usual 
pattern of activity. Primary email address 
changed by fraudster. Series of false identities 
used to receive unauthorised payments, then 
subsequently sent to sports books/casinos or 
VOIP. Alternatively , fraudster receives 
payments the n withdraws to his bank account.  
We use two sub -categories to analyse phishing 
cases:  
Account Take Over (Victim): Genuine member  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 30 
true identity and uses a number of stolen identities to collect 
the Account Take Over (Victim) funds, then redeems via 
another merchant, e.g. Casino or a Voice Over IP service 
provider. In other cases, the Account Take Over (Controller) 
reveals their identity by withdrawing Account Take Over 
(Victim) funds to their verified bank account.  
 whose funds are withdrawn  
Account Take Over (Controller): Stolen identity 
or main suspect who redeems the funds via 
another merchant using their own bank 
account.  
 
Cheque 
fraud  Stolen Cheques used to deposit funds at the Paysafe  Group. 
Finance receives notification from the bank, or an instant 
payment method such as Bibit, that cheques  are stolen and 
subsequently charged back.  
  
Child 
exploitation 
(CE) Indecent images of young children under the age of 18. 
Images hosted anywhere in the world. It is “an offence in the 
UK “to take, permit to be taken, make, possess, show, 
distribute or advertise indecent images of children. Indecent 
should be taken as its dictionary meaning; as a guide it means 
any images of children, apparently under 18 years of age, 
involved in sexual activity or posed to be sexually 
provocative”.  
It is illegal both to distribute and to purchase indecent images 
of children. In particular , merchants offering a child modeling 
service must be automatically referred to the Compliance 
Department . Child modeling services can host private 
member pages with a pay per view opportunity. We report 
indecent images to both the Internet Watch Foundatio n and 
to NCA. 
 Child Modelling Agencies, private member 
pages, currency US dollars, slip ID reveals 
“model”, “girl”, private member  purchasing 
images  of children  
 
Infringement Unauthorised  attempts to make, use, sell or have made a Price substantially lower than expected (e.g.  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 31 
Intellectual 
Property 
Rights 
(confirmed)  property right owned by another. Merchant uses URL or 
auction platform to sell goods. This includes illegal 
downloads and pirated music, films, software, games etc.  
 Designer handbags sold for £50) . Key words 
found in slip IDs (Hand bags, Region 0, Region 
All, Replica, Louis Vuitton, DVDs, etc.) . Latest 
movie and music releases for sale or download, 
software at greatly reduced prices, hardware 
that allows pirated game s to be played on 
console.  
 
Money 
Exchange 
(Illegal)  Suspect transactions sent with a payment reference of “e ac 
num  xxx” or “exchange” to another, which are then 
forwarded on by the exchanger to a company based off shore 
with little or no CDD (Know Your Customer) requirements.  
Although Money Exchange can be a genuine activity, 
unregulated money exchange is regarded as  unacceptable at 
Paysafe. An exchanger is reported when associate activity is 
predominantly related to any other high risk suspect. E.g. 
Pyramid Seller, Account Take Over (Victim) money, Credit 
Card or Bank Wire fraud.  
 Payment instruction indicates “exchange”, 
account serves short term use, email address 
contains key words such as “forex” or “trader”.   
 
Illegal  
breach of 
Paysafe’s 
Acceptable 
Business 
Policy (see 
Global 
Compliance 
Policy para 
7) For example: Firearms, hard -core pornographic content, Sale 
of Illegal Drugs.  
  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 32 
Pyramid 
selling  Pyramid selling is illegal in the UK. A Pyramid seller will 
promote rewards or bonus pay -outs to subscribers using 
multi -level marketing, get rich schemes, au to surf or high 
yield investment programs (HYIP). Legal low risk customer 
referral schemes can involve multi levels and are free to join.  
 To be confirmed as a pyramid seller, the scheme 
will involve more than two “levels” in the 
commission structure, pai d membership and 
recruitment of new members.  
 
High risk 
transactions  When a new member  deposits ≥ EUR 10,000 we will request ID plus Postal Address Verification and an 
explanation.  
We request ID, address verification documents and a reason for the deposit for any first time high value deposit 
(≥ EUR 10,000). The deposit can only be processed upon approval from the MLRO or Compliance Department.  
 
Terrorism  Paysafe pays special attention to vulnerable industries such as charities, to prevent terrorist funding 
opportunities. On the surface terrorist funding will usually appear genuine, so it is therefore essential that 
effective Know Your Customer / Customer Due Dilig ence (CDD) checks are completed for all members . 
Additionally, for charities we collect the government registered charity number. For example: www.charity -
commission.gov.uk. By collecting CDD documents, we can respond appropriately to any potential police 
investigations.  
 
 
  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 33 
APPENDIX 4 
FURTHER GUIDANCE ON SUSPICIOUS ACTIVITY  
Below are examples of patterns of behaviour which would be regard ed as 
unusual activity and that may form the basis for investigation and 
ultimately a SAR.  
It should be note d that these patterns do not always indicate that 
suspicious activity is taking place. As such, when one of these suspicious 
patterns appears, further investigative steps  must be taken  to determine 
what the causes of the pattern are likely to be.  
a) Combinati on of multiple means of payment issued by Paysafe 
Group entities  
Several means of payment issued by Paysafe Group offer financial 
services that can be combined or used to top up respective balances:  
- paysafecard vouchers can be used to top up mypaysafecard  
accounts  
- mypaysafecard accounts can be used to top up Skrill wallets, 
Neteller wallets as well as paysafecard prepaid MasterCards  
- credit  cards can be used to cashout funds from Skrill and Neteller 
wallets  
The review of money laundering patterns and the review of involved 
individuals has shown that often a variety of means of payment is utilized 
for layering purposes when laundering money.  Bearing in mind that each 
money transfer adds costs for the end -user (fees deducted from the 
balance for every m oney transfer), questions arise related to the benefit 
of customers. Furthermore, knowing that the mentioned accounts and 
wallets offer almost the same access to webshops, checking for the add -
on value the customer aims for by transferring money is advisab le. 
There is behavior that can indicate possible money laundering intention:  
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 34 
- Newly registered mypaysafecard account customers who transfer 
money from their account to a Skrill or Neteller wallet as a first 
activity (instead of using any mypaysafecard accou nt services or 
frequenting any webshops directly with their mypaysafecard 
account).  
- Transfer of payouts from a mypaysafecard account to a Skrill or 
Neteller wallet, instead of using the cashout functionality or credit  
card with the mypaysafecard account di rectly.  
Logins to the mypaysafecard accounts or the registration itself showing 
different geo location details than the payment or money transfer 
activities themselves.  
b) Clustering of residential addresses (account registrations)  
We have found that, when a pplication fraud occurs, there will often be an 
unusually high number of payment accounts registered using the same or 
similar residential addresses. When multiple applications are registered 
in this way, there are typically a very small number of individu als actually 
controlling the accounts. As a result, they normally use a relatively small 
number of computing devices when setting up the accounts.  
Residential addresses are also available with point of sales (POS). When 
analyzing patterns the review of PO S locations can provide further 
evidence of linked individuals.  
c) Clustering of similar registration data (account registrations)  
Just as with clustering of residential addresses, we have found that groups 
of fraudulent account registrations often show clusters of similar 
usernames , email addresses  and security questions and answers  provided 
at registration. As with clusters of similar residential addresses, we find 
that clustering of usernames , email addresses  and security questions and 
answers  is highl y associated with fraudulent activity.  
d) Large transactions at a small set of merchants from a single device 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 35 
or IP address, where IP address and/or browser language do not 
match issuing country  
Whenever a large transaction volume at a single merchant, or a t a small 
set of merchants, coming from a single device or single IP address  is 
observed , there is a heightened risk that the transaction volume may 
represent suspicious activity.  
However, in the absence of additional factors, such increased volume may 
simply represent a  ”high roller”. One factor which increases the index of 
suspicion is a mismatch between the country of the IP address, and/or the 
language used in the browser settin gs, and the country where the account 
was set -up from.  
Mismatches between the IP address country and the country of account 
registration is more significant than “mismatch” between country of 
account registration and browser language, as in every country there will 
be substantial minorities who are most comfortable using a language 
other than an official language of the country in which they live. However, 
when this type of suspicious behavior occurs, often there will be a very 
specific set of characterist ics which recur across all transactions in the 
pattern, and consistent use of a specific browser language which is not an 
official language of the country where the account was opened is often a 
consistent characteristic across all transactions in a suspic ious group.  
Often, a highly specific pattern will be identified upon analysis, that will 
have a large enough number of distinctive features (which, in normal 
transaction activity, do not all typically appear together), and which is 
found to occur across m ore than one device and/or IP address.  
e) Spike in transaction volumes at a specific merchant  
A large spike in transaction volumes at a merchant is a high -risk pattern 
which is cause for concern, even when other known indicators of 
suspicious activity are not present. Whenever such a spike is detected, 
Escalation and SAR Policy   
 
NOTE: All printed copies of this document are NOT COPY CONTROLLED and are to be 
used for INFORMATION ONLY as printed copies will not be automatically updated.  Not 
to be shown outside Paysafe. This document may not be disclosed to any external 
party without the permission of the document owner.   
INTERNAL  
 36 
enquiries must be made with the merchant conce rning any knowledge 
they have about the abnormal transaction volumes, and investigation 
must be made to determine whether the transactions can be linked to 
other known suspicious activity.  
There can be many reasons why this type of spike may occur, and no t all 
of them are suspicious. As with the pattern described in the preceding 
section, this type of activity can result from a legitimate high roller who 
was not previously using our payment method or was using a different 
merchant. A spike could also occur  as the result of a promotion that drives 
additional traffic. It is important to understand all of the known factors 
which may account for a spike before making a determination that the 
transaction activity is suspicious and, therefore, reportable.  
f) High v olumes of ATM withdrawals on a single payment account  
An ATM facility is available only for accounts which have an associated 
physical MasterCard. Our experience with legitimate customers shows 
that it is very uncommon for them to make large or frequent A TM 
withdrawals. In cases involving suspicious ATM withdrawals, the pattern 
usually involves loading the account and then withdrawing the cash via 
ATM as soon as possible.  
Often, the ATM withdrawals take place in a city located at a considerable 
distance f rom the residential address provided at registration for the 
account, and sometimes several such accounts (i.e. showing high ATM 
withdrawals and possible application fraud) can be linked together due to 
the presence of ATM withdrawals at ATMs located withi n the same small 
geographic area. The index of suspicion is also raised if the ATM 
withdrawals take place in a different country from the one in which the 
payment account was issued, as this can indicate use of the payment 
account to transfer funds cross -border.  
-  Anti-Money Laundering/Know Your Customer Policy
Introduction
This Policy establishes a set of minimum standards for identifying, accepting, documenting, and approving customers and maintaining customer relationships.  It also identifies a set of money laundering risk ratings, and includes standards for performing account surveillance, and maintaining records.
Non-compliance with the requirements of this policy could seriously undermine the reputation of and public confidence in the Bank and could result in disciplinary actions against the Bank and its employees, including civil and criminal penalties and other sanctions.
The U.S. Congress enacted the Bank Secrecy Act in October 1970 to prevent banks and other financial service providers from being used as intermediaries to hide the transfer or deposit of money derived from criminal activity.  Since its passage, Congress has amended the BSA a number of times to enhance law enforcement effectiveness.  The reporting and recordkeeping requirements of the BSA regulations create a paper trail for law enforcement to investigate money laundering schemes and other illegal activities.  This paper trail operates to deter illegal activity and provides a means to trace movements of money through the financial system.
The Uniting and Strengthening America by Providing Appropriate Tools Required to Intercept and Obstruct Terrorism Act (USA PATRIOT Act) was signed into law by President Bush on October 26, 2001, and contains strong measures to prevent, detect, and prosecute terrorist financing and international money laundering.  Title III of the USA PATRIOT Act is the International Money Laundering Abatement and Financial Anti-Terrorism Act of 2001.  It includes provisions for fighting international money laundering and blocking terrorist access to the U.S. financial systems.  
Objectives
The primary objective of this Policy is to help protect the good name and reputation of the Bank, and to secure its premises and systems against misuse as a vehicle for money laundering, terrorist financing, and other illegal activities.  Specific objectives include the following:
To ensure compliance with applicable U.S. and local anti-money laundering and anti-terrorist financing laws and regulations while protecting the financial privacy and relationship between the Bank and its customers
To establish minimum standards needed to determine and verify the identity of new customers and any other relevant account parties, and to require the application of enhanced due diligence standards to those customers considered higher-risk as a matter of law or regulations, or based upon the Bank’s own assessment of risk
To set appropriate standards for the ongoing conduct of customer relationships
To institute sound account/transaction surveillance standards as a mechanism for enabling Bank personnel to recognize, detect, and report money laundering, terrorist financing, and/or suspicious activity occurring through Bank accounts
To delineate the responsibilities of employees who implement the Bank’s AML processes.
Policy
The Bank will comply with the U.S. Bank Secrecy Act (BSA), the USA PATRIOT Act, and other applicable AML laws and regulations.  Also the Bank, consistent with applicable law, cooperates with governmental and law enforcement authorities in the enforcement of AML laws and regulations in connection with transactions involving the Bank.
No director, officer or employee of the Company shall:
Knowingly engage in, or assist any other person or entity in engaging in, any activity believed by such director, officer or employee to involve money laundering, terrorist financing or other suspicious or criminal activity
Assist any customer in structuring financial transactions in order to avoid disclosure to governmental or law enforcement authorities under applicable law
Advise any customer that their information has been, or will be, reported to governmental or law enforcement authorities (unless informing the customer is permissible, such as during the preparation of a Currency Transaction Report)
Make a conscious decision to avoid learning the truth about a customer’s suspected illegal activities.
Any director, officer or employee of the Company who fails to adhere to any of the foregoing policies may be subject to immediate demotion, reassignment or dismissal, and such failure may cause such individual and the Bank to be subject to severe civil and/or criminal penalties.
Money Laundering and Terrorist Financing
Money Laundering is the involvement in any one transaction, or series of transactions, which assists a person in keeping, concealing or disposing of the proceeds derived from illegal activities.  It is the criminal act of processing “dirty” money, through a series of transactions; in this way the funds are “cleaned” so that they appear to be proceeds from legal activities.  
Refer to Appendix A for examples of suspicious conduct and transactions related to money laundering
Although money laundering is a complex process, it basically involves the following three steps that can occur independently or simultaneously:
The first stage of laundering money is placement.  The goal is to introduce the unlawful proceeds into the financial system without attracting the attention of financial institutions or law enforcement.  Placement techniques include structuring currency deposits in an amount to evade reporting requirements or commingling currency deposits of legal and illegal enterprises.  An example may include dividing large amounts of currency such as purchasing a series of monetary instruments.
The second stage of the money laundering process is layering, which involves moving funds around the financial system, often in a complex series of transactions, to create confusion.  Examples of layering include wiring funds to and through numerous accounts at many institutions.
The final stage of the process is integration.  Once the funds are in the financial system and obstructed through the layering stage, the integration stage is used to further create the appearance of legal funds through additional transactions.  Examples include the real estate transactions or investment securities.
Terrorists generally finance their activities through both unlawful and legitimate sources.  Unlawful activities, such as extortion, kidnapping, and drug trafficking, have been found to be a major source of funding.  Other observed activities include improper use of charitable or relief funds that donors may have no knowledge that their donations have been diverted to support terrorist causes.  Other legitimate sources have also been found to provide terrorist organizations with funding; these legitimate sources are a key difference between terrorist financiers and traditional criminal organizations.
Prohibited Countries
The Bank may determine that it will not process transactions involving certain countries, or maintain or open new accounts for clients located in certain countries, because of publicly reported concerns of law enforcement agencies and regulators with respect to money laundering controls in those countries.  As events change, the Bank may add or delete countries from this prohibition.
Refer to Appendix B for Countries Tiering List         .

Know Your Customer Standards
Sound business practices include the concept of knowing your customer.  Observing the standards within this Policy can greatly reduce the risk that the Bank might be used for unlawful purposes.  A sound Know Your Customer Policy include, at a minimum:
Establishing the true identity of the customer and other related parties to the account, as appropriate
Screening customer and, as appropriate, related party names against government lists
Obtaining additional information/documentation as needed to understand the customer’s level of risk, determine the need for enhanced due diligence, and enable the detection of suspicious activity
Determining the customer source of funds
Understanding and recording the account’s purpose and anticipated transaction behavior
Maintaining up-to-date knowledge of the customer through ongoing client contact and periodic reviews.
Prohibited Customers
The Bank intends to do business with reputable customers whose identity can be verified.  The Bank will not knowingly do business with persons or entities with whom the Bank is prohibited from doing business because they are sanctioned under the U.S. Embargo Programs or any other official government lists that are identified and distributed throughout the Bank or are applicable in the local jurisdiction.  Also those with whom the Company has chosen not to do business based on prior experience.  In addition, Shell Banks which is one that does not have a physical presence in any country.  Physical presence is defined as a place of business that (1) is maintained by a non-U.S. bank; (2) is located at a fixed address in a country in which the non-U.S. bank is authorized to conduct banking activities, at which location the non-U.S. bank employs one or more individuals on a full-time basis and maintains operating records related to its banking activities; and (3) is subject to inspection by the banking authority that licensed the non-U.S. bank to conduct banking activities.
Also, the Bank will not knowingly do business with individuals or entities:
Whose character or financial conduct are suspect at the inception of the relationship or becomes suspect at any time during the relationship
Convicted of money laundering or related financial crime
Who attempt to establish anonymous accounts, accounts in obviously fictitious names or accounts where the identity of the true beneficial owner of the funds is required but cannot be obtained
Who refuse to provide information required by the Bank
Customer Identification Program (CIP)
Minimum identifying information must be obtained, recorded and verified for any new customer prior to opening their first account or providing their first product/service.  For the purpose of CIP requirements, a customer is defined as any person, including both individuals and entities (e.g., corporations, partnerships and trusts), that opens a new account, product or service, including deposit, transaction, asset, securities, safekeeping, collateral, or mutual fund accounts, credit, lending or borrowing activities, a safe deposit box, or cash management, custody, trust or estate services.  Typically, the customer is the accountholder.  In cases where an individual opens an account on behalf of a person who lacks legal capacity, such as a minor or an entity that is not a legal person, the individual opening the account is the customer.  The following entities are excluded from the definition of customer for CIP purposes:
Financial institutions regulated by a U.S. Federal functional regulator or banks regulated by a U.S. state bank regulator
Departments or agencies of the U.S., including any state or political subdivision of any state
Entities established under the laws of the U.S., state laws, political subdivision of any state, or under an interstate compact, that exercise governmental authority on behalf of the U.S., or any such State or political subdivision
Publicly listed entities whose common stock or similar equity interests are listed on the New York Stock Exchange, the American Stock Exchange, or the NASDAQ Stock Market.
For new customers who are individuals, including joint accountholders, the following identification information must be obtained and recorded:
Name
Date of birth
Primary residence address (and mailing address, if different from residence address).  For a customer who does not have a residential or mailing address, a business street address, an Army Post Office or Fleet Post Office box number or the residential or business address of next of kin or of another contact individual
Government issued identification number – For U.S. individuals, this number must be the Social Security Number.  For non-U.S. individuals/foreign based individuals, the number can be a taxpayer identification number, passport number, national identification number, resident’s identification number, alien identification number, or another government-issued identification number.
For new customers who are entities, the following identification information must be obtained and recorded:
Legal name
Principal place of business address (or local office address)
Government issued identification number – For U.S. entities (established or organized in the U.S.), this number must be the Taxpayer Identification Number (TIN/Employer Identification Number (EIN).  For non-U.S. entities/foreign based individuals, this number can be a taxpayer identification number, registration number, or another government-issued identification number.  Alternative government-issued documentation that certifies existence must be requested for any non-U.S. entities that do not have an identification number.
There may be instances (i.e., a newly formed entity) when the customer has applied for the TIN/EIN, but it has not been received at the time the account is requested.  In all cases, the TIN/EIN must be obtained by the Bank within 60 days or the account must be closed.  The Bank will track accounts opened without TINs/EINs, and may consider restricting account usage, such as limiting deposits, withdrawals, check writing, extension of credit or other measures while receipt of the TIN/EIN is pending.
The identification of each customer is typically verified before or at account opening.  For all businesses, verification must be accomplished no later than 30 days after account opening.  Identity verification can be accomplished through documentary or non-documentary means or a combination of both.  Depending on the risks associated with the customer, businesses may consider whether to restrict the customer’s activities until such time that the verification has been completed.
Documentary verification is accomplished by obtaining, reviewing, and making a record of one acceptable form of identification document.  For individual customers, acceptable identification documents include unexpired, government-issued photo IDs, such as:
Passport
Driver’s license or non-driver photo ID card
Military ID card
For businesses/entities, acceptable identification documents include:
Certificate of Incorporation/Filing Receipt
General or Limited Partnership Agreement
Articles of Organization or Association/Certification of Formation
Trust Instrument
Letters of Trusteeship or Executorship
U.S. Internal Revenue Code Sec. 501(c)(3) letter (for nonprofit organizations)
A government-issued business license
For foreign based entities, those legal documents issued by other countries that parallel the above and authenticate the entity will be accepted upon verification.
These documents are to be used to confirm the accuracy of the information provided by new customers.  A record of the document(s) used must be retained on file and should include:  a description (i.e., the type of document), its identification number, the place of issuance, the date of issuance, and the expiration date (as applicable).  A photocopy of the document (should the business choose to make and retain photocopies) will satisfy this requirement.
 Refer to Appendix C for further description of documentary verification documents         
The Bank may choose to perform non-documentary verification in addition to, or instead of, placing reliance on the documents named above.  Non-documentary verification may include, but is not limited to:
Contacting the customer at home after the relationship has been established
Obtaining references from reliable sources (e.g., credit bureaus, other financial institutions)
Performing a site visit at the entity customer’s place of business.
Even when not required, non-documentary verification may be considered an additional safeguard, particularly in higher-risk businesses and with high-risk customers.  When non-documentary verification is used, a record must be made and retained of the methods undertaken to verify the identity of a customer; this record should include a description of the methods and the results of verification performed.
During the course of verifying the identity of a customer, discrepancies may arise between the information obtained from the customer and the information obtained during the verification.  Resolutions resulting in the continuing the relationship need to be further documented and approved by a Vice President or above.
Bank employees are under no obligation to continue the customer identification and verification process if, at any time during this process, they determine that it is in the best interest of the Bank to terminate the relationship or discontinue the customer acceptance process.  If the decision to discontinue customer acceptance is based on a CIP failure and is deemed suspicious, an Incident Report Form must be filed even though accounts are not opened.
The USA PATRIOT Act requires that, prior to opening an account that the Bank notify its customers that it will be requesting information to verify their identity.  The Bank’s signage/brochure will include the following language:
Important Information About Procedures For Opening a New Account
To help the government fight the funding of terrorism and money laundering activities, financial institutions are required by Federal law to obtain, verify, and record information that identifies each individual or entity that opens an account or requests credit.
What this means for individuals:  When an individual opens an account or requests credit, we will ask for their name, residence address, date of birth, tax identification number, and other information that allows us to identify them.  We may also ask to see a driver’s license, passport or other identifying documents.
What this means for other legal entities;  When a corporation, partnership, trust or other legal entity opens an account or requests credit, we will ask for the entity’s name, physical address, tax identification number, and other information that will allow us to identify the entity.  We may also ask to see other identifying documents, such as certified articles of incorporation, partnership agreements or a trust instrument.
New Account Review
Within five business days, the branch manager or designee will review new account information and supporting documentation to determine whether all the necessary information was obtained, the account appears suspicious in any manner, the risk rating is proper and the type of account/business/customer is in compliance with bank policy.  Also as part of this review, the branch manager or designee validates the information on the Insight system to ensure accuracy.  The branch manager or designee signs the “Account Opening Data Entry Form” as evidence of the review and approval.
OFAC Screening/Comparison with Government Lists
Upon opening an account, the related party names are screened against the Office of Foreign Assets Control (OFAC) sanction list.  Upon receipt of an update of the OFAC sanction list, the entire portfolio is scanned against this sanction list.  Possible matches are investigated and any true matches are escalated to the OFAC Compliance Officer for resolution.
The new account will also be scanned to determine whether the customer appears on any list of known or suspected terrorists or terrorist organizations issued by any Federal government agency and designated as such by Treasury in consultation with the Federal functional regulators.  Possible matches are investigated and any true matches are escalated to the BSA/AML Compliance Officer.  The BSA/AML Compliance Officer is responsible to ensure that all federal directives issued in connection with these lists are followed.
KYC Due Diligence Requirements
KYC due diligence must be performed on all new customers at the time the relationship with the Bank is first established.  
For the purposes of KYC, the customer is each person in whose name an account is opened or a product/service is initiated.  This person can be an individual, a company, an organization or other entity.  The Bank will obtain information and perform due diligence on related parties where appropriate.  Related parties include persons who have authority, or who are in a position of control, over the account, product or service, as well as the beneficial owner(s) of the assets and persons who are intended to receive a benefit from, or be a recipient under, the relationship.  The following are some examples of related parties:
The account’s nominal and/or beneficial owner(s)
For an account in the name of an agent, the principal
For a company account, the significant owners, principal officers, key senior managers, and directors of the company
For an account in the name of a trust, the donor, trustees, and executors.
When opening a new account for an existing customer, it is not necessary to re-perform customer identification/verification steps provided that the existing customer information is current and complete and the Bank maintains the reasonable belief that it knows the true identity of the customer.  Additional account level data, however, may be needed in certain circumstances relative to any additional accounts offered to existing customers.  Similar account level data may also be necessary when a new account is opened for a new customer.  Depending on the type of account, such additional information may include, but is not limited to:
Type and purpose of account
Source of initial and ongoing funding
Anticipated activity:  the anticipated usage, activity, types of transactions, volumes and dollar amounts
Money Laundering Risk Ratings
Money laundering risk ratings are an evaluation of the customer’s/account’s potential money laundering risk.  As such, they can impact the approvals needed to accept a customer or open the account, determine the extent of information and verification required, trigger the need for enhanced due diligence, and affect the frequency of periodic relationship reviews.
The relationship owner determines the money laundering risk rating but will be reviewed by another individual.  Money laundering risk ratings must be determined before a new customer is accepted, and at, or immediately after, a new account is opened.  They are to be re-evaluated and adjusted, as appropriate, during the periodic review process, or at any other time when the business learns of new information that affects the rating.  The branch manager is responsible for reviewing or approving changes to a client’s risk rating.
Money laundering risk ratings apply at both the customer and account level.  If a customer is high-risk by himself, because for example he is a politically exposed person or associated with a high-risk industry, then all of his accounts should be classified as high-risk.  If an account is rated high-risk, however, the associated customer is not automatically high-risk.
Risk determination is a two-part process.  First, the relationship owner must identify and understand the general operating and overall legal, regulatory and geopolitical environments in which their customers operate.  Second, the relationship owner must, at a minimum, understand the following to determine whether they want to enter into, or sustain, a relationship with a particular customer within their target market:
The nature of the customer, including their reputation and business or other financial activities
The products and services requested, and the customer’s purpose for and use of such products and services
The money laundering risks associated with the customer and the jurisdiction(s) with which the customer has significant contact.
Also the following risk factors will be considered:
Customer-Type – At a minimum, the following customers shall be considered high-risk:  Politically Exposed Persons, Money Services Businesses, Offshore International Business Corporations and Private Investment Companies, any customers associated with substantial negative public information.
Geography – At a minimum, customers associated with (i.e., located/domiciled in, a citizen or resident of, and/or has business activities in) a Tier 1 country shall be considered high-risk.  Refer to Appendix B for the Country Tiering List
Industry – At a minimum, customers associated with (i.e., one is principally engaged in or whose source of wealth was generated from) a high-risk industry shall be considered high-risk.  Refer to Appendix D for the High- and Medium-Risk Industries List
Products and Services – At a minimum, customers and/or accounts that use high-risk products or services shall be considered high-risk.  Refer to Appendix E for the High-Risk Products List
Transaction Activity – Such as whether the customer’s expected transaction activity, including cash and/or wire activity, is determined to be high.
Additional KYC Due Diligence Requirements for Certain Customers, Related Parties, and Accounts
New High-Risk Customers
All new customer relationships that are deemed high-risk, and those escalated from medium or low to high-risk, are subject to review and approval by the Chairman of the Board.  The Standard Account Review Sheet is subject to completion, review and approval based on established requirements.
Refer to Appendix F for Standard Account Review Sheet
Politically Exposed Persons
Customers/related parties who are Politically Exposed Persons (PEPs) increase the risk that the Bank could be exposed to involvement in money laundering or other illegal activities.  The financial activities of PEPs may be of public interest or might otherwise attract publicity within or beyond the borders of their home country, and their transactions with the Bank could potentially involve the proceeds of foreign official corruption.  If the Bank knowingly engages in financial transactions in violation of the money laundering laws of various jurisdictions, the Company will be exposed to significant legal and reputational harm.
PEPs are defined as a U.S. or non-U.S., current or former, senior official of the executive, legislative, administrative, military or judicial branches of a government, whether elected or not and include senior officials of a major political party or a senior executive of a government-owned commercial enterprise.  A senior official or executive is defined as an individual with substantial authority over policy, operations, or the use of government owned services.  PEP positions include, but are not limited to:
Heads of State, Government Heads or National Leaders, such as the President, Prime Minister, King, Queen, Emir, Sultan, Emperor, Monarch, Pope
National Cabinet Members and Department/Agency Heads, such as the Vice President, Chancellor, Secretary of State, Defense Minister, Chief of the Treasury, Head of the National Bank, and other key Department, Agency, Ministry, and Office Officials
Key National Legislative Officials, such as Congressmen, Senators, House Representatives, Parliament members, Assemblymen, Councilmen
Senior Military Leaders, such as the Army Secretary
Important National Justices, such as the Attorney General, Chief Justices, and Associate Judges
Political Party Leaders
Ambassadors/Consuls General, including the United Nation Representative
Governors
Mayors of cities with populations in excess of 1MM
Senior executives of government-owned enterprises, such as the Chairman, CEO and President of government airline.
The following customers/related parties are also PEPs and are therefore bound by the requirements of this section:
Corporations, businesses or entities formed by, or for the benefit of, or significantly owned or controlled by, a PEP; significant ownership is 25% or more; control includes holding a senior executive position of influence, such as the Chairman, CEO, and President
Any immediate family member of a PEP, including the spouse, parents, siblings, children, and spouses’ parents or siblings
A person who is widely and publicly known to be a close associate of any such individual
Foreign Embassies/Consulates/Ministries
Foreign political organizations.
Upon account opening, reasonable steps will be taken to determine whether customers and related parties are PEPs including the direct inquiry with the customer.  The customer’s KYC profile and account record must indicate that the client is a PEP.
Enhanced scrutiny is required whenever the Bank does business with a PEP.  This enhanced scrutiny includes the following:
Determining the identity of the PEP
Assessing the level of corruption and characteristics associated with the PEP’s country
Evaluating the PEP’s position, length of time in office, and reputation
Probing the PEP’s employment history and source of funds and wealth
Obtaining information on immediate family members or close associates having transaction authority over the account
Understanding the purpose of the account and expected volumes and nature of account activity
Considering the use of the account(s)
Performing appropriate database/internet checks to gather information
Obtaining Board of Directors approval before account opening (presentation to outline the nature of the request, explanation of the rationale for initiating or maintaining the PEP relationship and providing adequate information regarding the PEP, the due diligence steps taken in regard to the relationship and how the PEP’s ongoing activities with Bank will be monitored.)
On an annual basis, each Business Head must review the PEPs in his or her business to determine if their retention continues to be appropriate.  This review must be evidenced in writing. 
Money Services Businesses
Money Service Businesses (MSBs) are high-risk because many:
Lack ongoing customer relationships and require minimal or no identification of customers
Maintain limited or inconsistent recordkeeping on customers and transactions
Engage in frequent currency transactions
Are subject to varying levels of regulatory requirements and oversight
Can quickly change their product mix or location and quickly enter or exit an operation
Sometimes operate with improper registration or licensing
MSBs are defined as any person doing business, whether or not on a regular basis or as an organized business concern, in one or more of the following capacities:
Currency dealer or exchanger
Check casher, including “payday” loan and check cashing services
Issuer of traveler’s checks, money orders or stored value products
Seller or redeemer of traveler’s checks, money orders or stored value products (including the United States Postal Service)
Money transmitter
It is the policy of the Bank not to do business with MSBs, except for:
U.S. or state-regulated mortgage banking firms
Recognized national or regional retail chain stores whose principal business is not money services.
For any other MSBs, Board of Directors approval is required.  In addition, the following due diligence must be performed for all MSB relationships, whether or not Board approval is required:
Confirm that the MSB is registered with FinCEN
Confirm state and local licensing, if applicable
Confirm agent status, if applicable
Conduct an on-site visit
Determine and review the ownership of the MSB.
Hedge Funds
Hedge funds may be higher-risk because they provide customers with offshore investment vehicles.  Hedge funds are similar to mutual funds in that they both are pooled investment vehicles that accept investors’ money and generally invest it on a collective basis.  Hedge funds differ significantly from mutual funds, however, because hedge funds are not regulated.
Before opening an account for a hedge fund, the following due diligence will be performed:
Obtain and review a prospectus, offering document or other documentation describing the fund
Record the name of and background information for the investment advisor/management company and/or the general partners or other similar senior officers, such as the Chief Executive Officer, Chief Administrative Officer, Chief Information Officer, etc.
Perform OFAC screenings on the fund, the investment advisor/management company, and/or the general partners or other similar senior officers by conducting Internet research or another similar service or third party confirmation.
Reliance on Others
In those instances in which a financial intermediary introduces its client to the Company and the intermediary’s customer opens an account and/or otherwise enters into a contractual relationship with one or more of the Bank’s business units, KYC due diligence on the contracting party is the responsibility of the business unit; however, businesses are permitted to rely on the customer identification and verification procedures of another financial institution to establish the identity of the customer.  Reliance, for purposes of such safe harbor, is appropriate when the other financial institution has established a similar banking/business relationship with the customer to that of the Company and when such reliance can be considered reasonable under the circumstances.  In order to be able to rely on the customer identification procedures of another financial institution, the other entity:
Must be subject to the AML program requirements set forth in the USA PATRIOT Act and implementing regulations
Must be regulated by a U.S. Federal functional regulator, and
Must enter into a contract with the Bank requiring the other financial institution to certify annually that it has implemented its AML program and that it, or its agent, will perform the customer identification and verification program requirements.
In instances in which the intermediary to be relied upon is not subject to the requirements of the USA PATRIOT Act, that intermediary:
Must be subject to money laundering control requirements under its local laws and regulations
Must be regulated by a recognizable financial services regulator in the country of jurisdiction
Must provide a letter of attestation to the Bank in which its attests to its compliance with all appropriate customer identification, verification, and other due diligence requirements.
In all cases in which a business is placing reliance upon an intermediary for the performance of any customer identification or other KYC due diligence steps, the prior, written approval must be obtained from the BSA/AML Compliance Officer.  This approval is required whether the entity relied upon is U.S. or non-U.S. intermediary.
KYC information provided by new employees who bring customers with them from other financial institutions must be independently obtained and verified by someone other than the new employee.
Ongoing Relationship/Customer/Account Activities
KYC records are intended to be dynamic and enhanced over time as knowledge of a customer grows.  The relationship owner will review and update KYC information whenever significant changes in activity, ownership, or public information about the client become known.
In order to monitor account activity, on an on-going basis, for unusual activity, the following specific system reports have been selected for review on a daily basis by the Compliance Liaison:
High Dollar Cash Item Report
Draws Against Uncollected/Unavailable Funds PDD750-14
Balance Changes – Significant Report PDD750-07
Also in regards to the ACH environment, the Operations Manager will review the following reports on a daily basis for unusual activity and scanning:
Entries – Checking PL6570-01
Entries – Savings PL6570-06
Originating Entries PL5500-02
OFAC Screening – Receiving PL6570-01 (IATs)
OFAC Screening – Receiving Final PL6579-02 (IATs)
Unusual activity may encompass the following:
Reviewing originators/recipients’ whose business or occupation does not warrant the volume or nature of ACH activity;
Originators whose origination activity suddenly exceeds projections/credit-debit limits with no reasonable explanation for such change;
Originators generating a high rate or high volume of invalid account returns or a high-rate or high volume of unauthorized returns/transactions;
Specific returns creations (RDFI) covering unauthorized, fraudulent, or revoked transactions, and Federal reclamations.
Unusual conditions will be investigated and handled appropriately by the reviewer.  Such examination of these daily reports must be evidenced by the reviewer by initialing the Daily Account Review Log or the report printout.
In order to monitor ongoing wire transfer records quarterly, the branch manager/designee will review the Wire Transfer Velocity Report for questionable and/or unusual patterns.  Particular attention will be paid to incidents where:
Unexplained or sudden extensive wire activity, especially in accounts that had little or no previous activity;
A large number of wire transfers to or from unrelated third parties inconsistent with the customer’s legitimated business purpose;
Wire transfers that have no apparent business purpose to or from a foreign country;
The customer’s account has inflows of funds or other assets well beyond the known income or resources of the customer;
Transactions in which the primary beneficiary or counter-party is undisclosed. 

Note:  Because elderly individuals experience declining cognitive or physical abilities, they are more reliant on specific individuals for their physical well-being, financial management, and social interaction.  Therefore, certain elderly individuals may be particularly vulnerable to identity theft, embezzlement, and fraudulent schemes.  See Appendix H for Possible Signs of Elder Financial Exploitation.

An investigation will be conducted for any activity deemed suspicious and if necessary, a SAR will be filed.  The branch manager/designee will sign the quarterly report as evidence that the quarterly review was conducted. 
This Policy provides for a process of periodic, risk-based customer relationship reviews.  In the absence of an event that calls immediate attention to a relationship or to activity in the customer’s accounts, the periodic review provides the Bank with the opportunity to update KYC information, review the customer’s recent transactions and interactions with the Bank, and reaffirm that retaining the relationship continues to be appropriate.
The periodic review is to be performed by the relationship owner and should:
Ensure that KYC information is accurate, complete, and up-to-date
Consider the effects of any significant inflows, outflows, and any obvious changes in the accounts’ purposes, for appropriateness and consistency with expectations.
Evaluate the customers’ general transaction volumes and overall balances across all products and services for reasonableness and consistency with the customer’s financial situation and the relationship’s stated purpose.
Periodic reviews will occur at least every 12 months for high-risk customers and 24 for medium-risk customers.  The first month of each quarter, high risk accounts having a yearly anniversary in that quarter, based on the date of the assigned risk rating, will be identified.  During that three-month period, a review will be performed using the Standard Account Review Sheet.  The review method for medium risk accounts would be the same but based upon a two-year anniversary of the assigned risk rating date.  The Standard Account Review Sheet is subject to the necessary review and approval based on established requirements.
Refer to Appendix F for Standard Account Review Sheet
Special Measures
The USA PATRIOT Act gives the Secretary of the Treasury authority to impose special measures against foreign jurisdictions, foreign financial institutions, transactions involving such jurisdictions or institutions, or one or more types of accounts, that are determined to pose a “primary money laundering concern” to the United States.
The BSA/AML Compliance Officer will coordinate compliance with such special measures on a bank-wide basis.  It is the policy of the Bank to promptly comply with any special measures prescribed by the Secretary of the Treasury.  Whenever the Secretary imposes special measures, Compliance shall communicate the special measures to the affected businesses, which will take the steps necessary to terminate affected account relationships, communicate to customers, and/or amend existing policies, procedures, and controls or develop new ones to comply with the prescribed special measures.
Information Sharing
The USA PATRIOT Act provides for information sharing between the Government and Financial Institutions, as well as between financial institutions themselves, in an effort to deter money laundering and terrorist activities.
Section 314(a) of the Act establishes a mechanism for law enforcement agencies to communicate the names of suspected terrorists and money launderers to covered financial institutions for the purpose of promptly identifying accounts and transactions involving those suspects.  Under 314(a), information requests are batched and forwarded to covered financial institutions from FinCEN every two weeks (although single requests may be sent in urgent situations).
Upon receipt of a 314(a) request, Company covered financial institutions are required to search the following records:
Deposit account records
Funds transfer records
Records for the sale of monetary instruments
Loan records
The Bank will search its records for the preceding 12 months for accounts, and for the preceding 6 months for transactions, and report them to FinCEN.  If other matching records are found in this process, they will also be reported to FinCEN, even if they fall outside of the requested time frame, or pertain to an account or transaction in an area of the financial institution that was not required to be searched but were searched anyway, or pertain to a record that was not required to be maintained under federal law or regulation but existed nonetheless.
Searches are required to be completed and a response to be sent to FinCEN with any matches within two weeks of receiving the 314(a) request.
If there is a positive match for an account or a transaction, the following information will be gathered:
The identity of the individual, entity, or organization
The account number(s); opening date, type of transactions
All identifying information provided by the account holder in connection with the opening of the account, such as social security number, taxpayer identification number, passport information, date of birth, and address.
Names are highly confidential and should be shared only on a limited basis.  Under no circumstances should 314(a) names be shared with any other financial institution.  Records regarding 314(a) searches must be retained in a secure area.
If the 314(a) search results in a positive match, it is incumbent upon the Bank to conduct an investigation of the account relationship and/or transaction activity and should there be reasonable belief that suspicious activity occurred, an Incident Report must be drafted for SAR consideration. 
 If the Bank decides to close the account, it will first notify the law enforcement contact on the request to determine if closing the account would interfere with an active investigation.  If law enforcement requests that an account remain open, the bank will request written confirmation.
Note:  The bank does not participate in 314(b)
Refer to Appendix G for procedures concerning responses to information requests 


Subpoenas Received from Law Enforcement

The receipt of a grand jury subpoena will cause the bank to conduct a risk assessment and account relationship review of the subject customer.  The information resulting from the review, transactions, and accounts subject to the subpoena will be evaluated and a determination will be made as to whether additional account monitoring should be implemented or a suspicious activity report filed.
Currency Transaction Reporting and Exemptions
In compliance with the BSA regulations, the following types of reports are submitted to the U.S. government:
FinCEN Form 104, Currency Transaction Report (CTR):  A CTR must be filed for each deposit, withdrawal, exchange of currency, or other payment or transfer, by, through or to a financial institution, which involves a transaction in currency of more than $10,000.  Multiple currency transactions must be treated as a single transaction if the financial institution has knowledge that:  (a) they are conducted by or on behalf of the same person; and, (b) they result in cash received or disbursed by the financial institution of more than $10,000.  A CTR must be filed within 15 days paperless or 25 days on magnetic tape following the date of reportable transaction with the Internal Revenue Service.  The bank must retain copies of CTRs for five years from the date of the report.
FinCEN Form 105, Report of International Transportation of Currency or Monetary Instruments (CMIR):  Each person who physically transports, mails or ships, or causes to be physically transported, mailed, shipped or received, currency, traveler’s checks, and certain other monetary instruments in an aggregate amount exceeding $10,000 into or out of the United States must file a CMIR.
Note:  The Bank will not grant customer Exemptions at this time.
Currency transactions over $3,000 are recorded daily on the “Currency Transactions Greater Than $3,000 Log”.  Daily, this log is reviewed by the Compliance Liaison to ensure that multiple currency transactions totaling over $10,000 for a customer are properly reported.  This log also must be reviewed for possible structuring situations and initialed as evidence of review.  On a monthly basis, the branch manager/designnee will review this report on a cumulative basis to detect patterns or structuring trends.  The branch manager/designee will evidence this review by signing this monthly report. 
Structuring is the breaking up of transactions for the purpose of evading the BSA reporting and recordkeeping requirements and, if appropriate thresholds are met, should be reported as a suspicious transaction.  Structuring may be indicative of underlying illegal activity; further, structuring itself is unlawful under the BSA.
Penalties and asset forfeiture for money laundering can be severe under BSA:
Individuals, including employees of financial institutions, convicted of money laundering face up to 20 years in prison for each money-laundering transaction.
Businesses, including banks and individuals, face fines up to $1,000,000 or twice the value of the transaction, whichever is greater.
Financial Institutions can lose their charter/license, and employees risk being removed and barred from the business.
Any property involved in the transaction or traceable to the proceeds of the criminal activity, including loan collateral, personal property and, under certain conditions, entire bank accounts (even if some of the money in the account is legitimate) may be subject to forfeiture.
 Safe Harbor Provision 
The Annunzio Wylie Anti-Money Laundering Act (1992) – U.S.C. 5318(g)(3) - provides a safe harbor for the bank and its employee from civil liability for reporting known or suspected criminal offenses or suspicious activity by filing a SAR. A bank employee should feel safe in reporting suspicious activity.  The government works closely with the bank to ensure that all employees are protected from any liability.  
Federal Law prohibits Employees from disclosing the fact that a SAR has been filed.  Never discuss any Suspicious Activity Reporting requirements with a customer. Voluntarily giving additional information to customers, such as when you completed an incident report for their suspicious activity makes the employee liable for prosecution for violating Anti-Money Laundering Laws.
Recordkeeping and Record Retention Requirements
The following rules apply to CIP-related records:
Identifying information (name, address, date of birth, and government-issued ID number) must be retained for five years after the date the account is closed
All other information and documentation required by CIP rules, such as other recorded customer information, copies of documents used to verify identity, records of the steps taken and the results of verification performed by non-documentary means, and the resolution of discrepancies that may have arisen between information provided by a customer and the documentary and non-documentary evidence used to verify such information, must be retained for five years after the record is made.
KYC-related records can be maintained in either hard copy or in electronic form, so long as the records are accurate and readily accessible within five calendar days.
The Bank must maintain a record of each funds transfer of $3,000 or more, which it originates, acts as an intermediary for, or receives for five years.  The amount and type of information that must be recorded and kept depends upon the Bank’s role in the funds transfer process.  Also, the Bank must pass certain information along to the next bank in the funds transfer chain when it acts as an originator or intermediary for a funds transfer.

The Bank which provides for the purchase and sale of monetary instruments must require the retention of records of cash sale to a customer for bank checks, drafts, cashier’s checks, money orders, and traveler’s checks (which the Bank does not currently sell) between $3,000 and $10,000 inclusive for five years.  These records must include evidence of verification of the identity of the purchaser and other information as outlined below:
The name of the purchaser;
Date of purchase;
Types of instrument purchased;
Serial number of the instrument purchased; 
The amounts in dollars of each of the instruments purchased; and
Verification that the individual is a deposit holder/verification or the purchaser’s identity (address, SS#/Alien Identification #, DOB).
The following records will be retained for seven years:
A record of each extension of credit in an amount in excess of $10,000
Each document granting signature authority over each deposit or share account
Each statement, ledger card or other record on each deposit or share account, showing each transaction in, or with respect to, that account
Each check, clean draft, or money order drawn on the Company or issued and payable by it
Each item in excess of $100 comprising a debit to a customer’s deposit or share account
Records prepared or received in the ordinary course of business, which would be needed to reconstruct a transaction account and to trace a check in excess of $100
Each deposit slip or credit ticket reflecting a transaction in excess of $100.
AML Training
Twice a year, the Bank shall maintain a regular training program for the purpose of educating its personnel and heightening their awareness so that they will be knowledgeable and vigilant in their efforts to recognize and report activity, which may constitute money laundering.
Within 30 days of hire, new employees will be trained in the basic aspect of AML.  Additionally the new employee will be required to read and attest that they understand the contents of the Bank’s AML/BSA policies.
Note:  Training will be conducted at least annually for the Board of Directors.
BSA/AML Compliance Officer
The BSA/AML Compliance Officer has day-to-day responsibility for managing all aspects of the Bank’s AML Program and compliance with AML laws and regulations.  The BSA/AML Compliance Officer is also responsible for the maintenance of this Policy and for considering deviations to this Policy.  In addition, the BSA/AML Compliance Officer advises staff regarding the application of anti-money laundering laws and regulations and on money laundering trends and patterns specific to certain businesses.

BSA/AML Risk Assessment
The Bank has developed a risk assessment, which was approved by the Board of Directors, by identifying risks along with the associated mitigants.  The assessment will be periodically reviewed and presented to the Board for approval.

Independent Testing
Independent testing commensurate with the BSA/AML risk profile of the bank will be conducted every 12 to 18 months by outside auditors.  Upon completion, the auditors conducting the BSA/AML test will report the results to the Audit Committee.

















APPENDIX A
EXAMPLES OF SUSPICIOUS CONDUCT AND TRANSACTIONS
The existence of one or more of these suspicious circumstances does not mean that money laundering activity is taking place, but that such circumstances should be scrutinized carefully.

Customers who are reluctant to provide normal information when opening an account or who provide fictitious or conflicting information.
Customers with no discernible reason for using the Bank’s services (e.g. customers with distant addresses who could find the same services nearer to home)
Business customers who are reluctant to provide complete information regarding the purpose, prior banking relationships, officers or directors, or location of their business.
Business customers who are reluctant to reveal details about their activities, or to provide financial statements, or whose financial statements are noticeably different from those of similar businesses.
Large cash deposits by an individual or business where checks and other instruments are the expected norm.
Structuring multiple cash deposits which are individually unexceptional, but significant in the aggregate.
Exchanging large quantities of low denomination currencies for those of higher denomination.
Deposit or withdrawal activity that is inconsistent with the activity normally associated with the customer or the customer’s type of business.
Funds transfers are sent or received from the same person to or from different accounts.
Funds activity is unexplained, repetitive, or shows unusual patterns.
A customer uses unusual or suspicious identification documents that cannot be readily verified.
The customer’s background differs from that which would be expected on the basis of his or her business activities.
A customer is reluctant to provide information needed to file a mandatory report, to have the report filed, or to proceed with a transaction after being informed that the report must be filed.
A person uses the automated teller machine to make several bank deposits below a specified threshold.
The currency transaction activity reflect a sudden change inconsistent with normal activities.
A customer purchases a number of cashier’s checks, money orders, or traveler’s checks for large amounts under a specified threshold.
Suspicious movements of funds occur from one bank to another and then funds are moved back to the first bank.
Deposits of large third-party checks endorsed in favor of the customer where such conduct is inconsistent with the customer’s normal activity.
Large numbers of individuals making payments into the same account without adequate explanation.
Unexpected repayment of problem loans.
Requests to provide or arrange financing where the source of the customer’s financial contribution to a deal is unclear, particularly where property is involved.
Employees whose habits or lifestyles change unexpectedly
Employees whose performance changes unexpectedly.
The stated occupation of the customer is not commensurate with the type of level of activity.
Regarding nonprofit or charitable organizations, financial transactions occur for which there appears to be no logical economic purpose or in which there appears to be no link between the stated activity of the organization and the other parties in the transaction.
For additional examples of Money Laundering and Terrorist Financing “Red Flags” see the FFIEC BSA/AML Examination Manual 4/29/2010.











APPENDIX B
COUNTRY TIERING LIST
Tier 1
Afghanistan		Albania		Algeria		Angola		
Anguilla		Antigua/Barbuda	Argentina		Armenia
Azerbaijan		Bahamas		Bangladesh		Belarus		
Belize			Bolivia		Botswana		Brunei
Burkina Faso		Burundi		Cambodia		Cameroon	
Cape Verde		Chad			Colombia		Congo
Costa Rica		Cuba			Cyprus		Dominican Republic	
East Timor		Ecuador		Equatorial Guinea	Eritrea
Estonia		Ethiopia		Gabon			Gambia
Georgia		Ghana			Grenada		Guinea		
Guinea-Bissau	Haiti			Honduras		Indonesia		
Iran			Iraq			Ivory Coast		Kazakhstan		
Kenya			Kuwait		Kyrgyzstan		Laos			
Latvia			Lebanon		Lesotho		Liberia		
Libya			Lithuania		Macau			Malawi		
Maldives		Mali			Mexico		Moldova		
Mongolia		Montenegro		Montserrat		Morocco		
Myanmar		Namibia		Nauru			Nepal			
Nicaragua		Nigeria		Niue			North Korea
Pakistan		Palestinian		Panama		Papua New Guinea	
Paraguay		Peru			Philippines		Russia			
Rwanda		Sao Tome&Principe	Serbia/Montenegro	Seychelles		
Sierra Leone		Soloman Islands	Sri Lanka		St. Lucia		
Sudan			Syria			Tajikistan		Tanzania		
Thailand		Trindad & Tobago	Turkey		Turkmenistan	
Uganda		Ukraine		Uzbekistan		Venezuela		
Vietnam		Yemen			Zambia		Zimbabwe
Tier 2
Akrotiri Sovereign	Aland Islands		American Samoa	Andorra		
Antarctica		Aruba			Ashmore & Cartier	Azores			
Baker Island		Benin			Bermuda		Bhutan		
Bouvet Island		Brit Virgin Islands	British Oceania	Canary Islands
Cayman Islands	Central African Re	Christmas Island	Clipperton Island
Cocos			Comoros		Congo			Cook Islands
Coral Sea Islands	Croatia		Dhekelia Sov Base	El Salvador
Falkland Islands	Faroe Islands		Fed St Micronesia	Guiana
French Polynesia	French Southern	Ghana			Gibraltar
Greece			Greenland		Guadeloupe		Guam	
Guatemala		Guernsey		Guyana		Heard/Mcdonald Is
Howland Islands	India			Indonesia		Isle of Man
Jamaica		Jarvis Island		Jersey			Johnston Atoll
Jordan		Kingman Reef	Kiribati		Kosovo
Liechtenstein		Macedonia		Madagascar		Madiera		
Malaysia		Marshall Islands	Martinique		Mauritania		
Mayotte		Midway Islands	Monaco		Mozambique		
Navassa Island	Neth Antilles		New Caledonia	Niger			
Norfolk Island	North Mariana Is	Palau			Palmyra Atoll	
Paracel Islands	Pitcairn Islands	Qatar			Reunion		
Saint Helena		San Marino		Saudi Arabia		Senegal		
Somalia		South Georgia	South Korea		South Sandwich Islands
Spratly Islands	St Barthelemy	St Pierre/Miquelon	St Kitts/Nevis
St. Martin		St Vincent & Gren	Suriname		Svalbard/JanMayen
Togo			Tokelau		Tonga			Turks/Caicos		
Tuvalu		US Virgin Islands	United Arab Emirates			
Uruguay		Vanuatu		Vatican City		Wake Island		
Wallis & Futuna	Western Sahara	Western Samoa
Tier 3
Bahrain		Barbados		Bosnia-Hercegovina	Bulgaria
China			Djibouti		Dominica		Egypt	
Fiji			Hong Kong		Hungary		Israel
Luxembourg		Malta			Mauritius		Oman
Poland		Puerto Rico		Romania		Singapore
Slovakia		Slovenia		South Africa		Swaziland
Switzerland		Taiwan		Tunisia		
Tier 4
Australia		Austria		Belgium		Brazil
Canada		Chile			Czech Republic	Denmark
Finland		France			Germany		Iceland
Ireland		Italy			Japan			Netherlands
New Zealand		Norway		Portugal		Spain
Sweden		United Kingdom	United States





















APPENDIX C
DOCUMENTARY VERIFICATION DOCUMENTS – US Citizens

Required Business Documentation















APPENDIX D
HIGH- AND MEDIUM-RISK INDUSTRIES LIST

High Risk Industries
Arms/Weapons Dealers – applies to clients engaged in the manufacture, sale or distribution of arms as well as agents, brokers or intermediaries in such activities
Art and Antique Dealers
Money Services Businesses
Cash Intensive Businesses – any retail business whose transaction profile shows $25,000 or more in cash transactions (aggregate of deposits and withdrawals) per week
Casinos and Other Gaming or Wagering Establishments – these are always high-risk, even if they are reputable and publicly traded entities
Charities, Endowments or Foundations – especially for organizations that accept funds from the public/third parties.  Exceptions not considered high-risk include large, well known reputable organizations such as the March of Dimes, United Way, and the Red Cross, organizations that administer U.S. Government sponsored programs, such as the Fullbright Scholarship program, and Charities, Endowments or Foundations that use funds from an individual, family, school, etc., where the source of funds is clearly bona fide and third party donations are not accepted.
Deposit Brokers
Embassies, Consulates or Ministries
Third-party payment processors
Privately-owned ATM machines
Import/Export Brokers – those who never take possession of goods and/or have no physical location to demonstrate business
Leather Goods Stores
Off-Shore Personal Investment Companies, Money Management Businesses or Investment Management Businesses
Businesses That Accept Third-Party Checks – third party checks are checks made payable to one party and deposited into an account of a differently named party.  This does not include industries, such as collection agencies, where such conduct is not indicative of potential money laundering
Professional Service Providers acting in an intermediary capacity, such as a lawyers’ trust account (IOLTA) or an escrow account, where the Bank has no direct relationship with or knowledge of the beneficial owners of the accounts
Non-bank financial institutions that have accounts in the Private Wealth Management business.  Examples include:  securities/commodities firms, broker-dealers, mutual funds, hedge funds, commodity traders, investment advisors, dealers in precious metals, stones or jewels, pawnbrokers and loan or finance companies
Medium Risk Industries
Import/Export Businesses – also referred to as wholesale/distribution businesses which ship abroad or receive physical inventory from outside the U.S. and maintain a store or warehouse that can be observed
Internet Businesses – any business that sells goods and services over the Internet

















APPENDIX E
HIGH-RISK PRODUCTS LIST

The following products and services are deemed high-risk:
Funds Transfer – Products that enable institutional customers to initiate funds transfers electronically.
Remote Deposit Capture Service – Product that enables business customers to make check deposits via an electronic check conversion service.

















APPENDIX F
STANDARD ACCOUNT REVIEW SHEET
To:	Chief Executive Officer

	From:								
	
	Date:			
	
	Re:	High – Risk Customer Submission





APPENDIX G
RESPONSES TO INFORMATION REQUESTS

According to Bank Policy, the BSA/AML Compliance Officer has been designated as the central Point of Contact for all 314(a) requests sent by FinCEN to the Bank.
 FinCEN posts on its secure website a list of individuals, entities and organizations which are under investigation by one or more federal agencies.  All financial institutions covered by 314(a) of the USA Patriot Act are required to quickly search their records to determine whether they maintain or have engaged in transactions with any of the named subjects.
If the Bank finds a match with a subject named on FinCEN’s 314(a) list, the match must be reported to FinCEN by making an entry on FinCEN’s secure website no later than fourteen (14) calendar days after the list was posted.  At that point, a federal agency may follow up with a subpoena for specified documents.  That subpoena is processed like any other subpoena from law enforcement.  If the Bank has no match, no response is necessary.
A search of all pertinent Bank systems that contain customer information to determine whether or not the Company has any “hits” for the names listed on the request.  The appropriate affirmative responses are entered on the FinCEN secure website.
Also the pertinent account or transactional activity is analyzed, and if the filing of a SAR is warranted, a SAR is prepared and filed.
All Bank employees involved in the processing and handling of 314(a) requests are required to keep the information confidential.  The fact that a 314(a) request has been made, or that responsive information has been found, may not be shared with anyone outside of the Bank, with the exception of FinCEN and appropriate law enforcement officers.  Moreover, the 314(a) requests and any supporting documentation must be maintained in secure files.
Note:  See detailed procedures regarding the process of down/up loading of files for filtering. 





APPENDIX H
POSSIBLE SIGNS OF ELDER FINANCIAL EXPLOITATION

Frequent large withdrawals, including daily maximum currency withdrawals from an ATM
Sudden non-sufficient fund activity
Uncharacteristic nonpayment for services, which may indicate a loss of funds or access to funds
Debit transactions that are inconsistent for the elder
Uncharacteristic attempts to wire large sums of money
Closing of CDs or accounts without regard to penalties
A caregiver or other individual shows excessive interest in the elder’s finances or assets, does not allow the elder to speak for himself, or is reluctant to leave the elder’s side during conversations
The elder shows an unusual degree of fear or submissiveness toward a caregiver, or expresses a fear of eviction or nursing home placement if money is not given to a caretaker
The financial institution is unable to speak directly with the elder, despite repeated attempts to contact him or her
A new caretaker, relative, or friend suddenly begins conducting financial transactions on behalf of the elder without proper documentation
The customer moves away from existing relationships and toward new associations with other friends or strangers
The elderly individual’s financial management changes suddenly, such as through a change of power of attorney to a different family member or a new individual
The elderly customer lacks knowledge about his or her financial status, or shows a sudden reluctance to discuss financial matters.







“Insert Company Here”






BSA/AML and OFAC Policy
Effective Date: XXXXXX, XX, XXXX


1. OBJECTIVES	4
1.1	General	4
1.2	Purpose	4
1.3	Scope	4
1.4	Consequences of Non-Compliance	5
1. DEFINITIONS	5
1. POLICY REQUIREMENTS	6
3.1	Overview	6
3.2	Designation of BSA Officer and Governance Structure	7
3.3	Internal Controls	8
3.3.1	BSA/AML and OFAC Risk Assessment	8
3.3.2	KYC Program	8
3.3.3	Standards for Loan Disbursements, Payments, and Refunds	9
3.3.4	OFAC Compliance	10
3.3.5	Transaction Monitoring	10
3.3.6	Referrals for Potentially Suspicious Activity	11
3.3.7	Regulatory Reporting and Recordkeeping	12
3.3.8	Information Sharing	13
3.3.9	Mechanisms Designed to Monitor Ongoing Compliance	13
3.4	Training and Development	14
3.5	Independent Testing	15
1. ROLES AND RESPONSIBILITIES	15
1. EXCEPTIONS	17
1. POLICY ADMINISTRATION	18
6.1	Document Management	18
6.2	Approval Management	18
6.3	Related Documents	18
6.3.1	Related Procedures	18
6.3.2	Applicable Law and Regulations	18

OBJECTIVES

General

[Insert Company Here] (“Insert Company Here” or the “Company”), its senior management, and its Board of Directors (the “Board”) are committed to deterring customers, partners, and outside parties from using the Company as a conduit for illegal activity and to supporting [Insert Financial Institution Here]’s BSA/AML and OFAC compliance efforts. 

This BSA/AML and OFAC Policy (“Policy”) and its program establish a framework for effective compliance with the BSA/AML and OFAC laws and regulations applicable directly to [Insert Company Here] or its business partners and to communicate its clear commitment to strong compliance culture. 

Title III of the Uniting and Strengthening America by Providing Appropriate Tools Required to intercept and Obstruct Terrorism Act of 2001 (“USA PATRIOT Act”), the Bank Secrecy Act (“BSA”), and Office of Foreign Assets Control (“OFAC”) regulations require that U.S. persons comply with applicable anti-money laundering (“AML”) and sanctions regulations. [Insert Company Here] is not a “financial institution” (as defined in the BSA at 31 U.S. Code § 5312) and therefore is not required by law to implement a BSA/AML program. However, [Insert Company Here] has made a commitment to implement an effective BSA/AML program that incorporates the regulatory expectations of its bank partners, including regulations relating to Know Your Customer (“KYC”) program and Customer Identification Program (“CIP”), transaction monitoring, referrals of potentially suspicious activity, and a comprehensive sanctions screening process.

Purpose

The purpose of the Policy is to ensure that a program is in place to detect, prevent, and report illicit criminal activities such as money laundering and terrorist financing, as well as to ensure adherence to sanctions laws. The program should seek to understand and manage such risks in a systematic fashion that is compliant with Bank policy, applicable laws, regulations and guidance, and serves the best interests of [Insert Company Here], the Bank and their collective customers.

Scope

This Policy applies to all origination and servicing activities performed by [Insert Company Here] associated with the Bank’s products or services in accordance with its individual program agreement with [Insert Company Here].

This Policy applies to all Business Lines and relevant support personnel at [Insert Company Here] as well as third-party partners and vendors with whom [Insert Company Here] has entered into business arrangements for ongoing operational activities. [Insert Company Here] third-party relationships include payment processors, systems providers, bank partners, and consultants, among others.

Consequences of Non-Compliance

[Insert Company Here] recognizes that non-compliance with BSA/AML and OFAC rules and regulations can expose the Company to substantial risk, potentially including civil or criminal penalties. All employees are responsible for understanding this Policy and undertaking any specific BSA/AML and OFAC compliance responsibilities assigned to them.

Non-compliance with, or violation of, the Policy’s requirements by employees may result in:
Disciplinary action, including termination in appropriate cases; and/or
Civil and/or criminal penalties.

Willful blindness to, or tipping off a customer about, a potential money laundering violation can expose the Company and individuals to potential liability.

DEFINITIONS

Money Laundering: Money laundering is the movement of cash or cash equivalent proceeds derived from illegal or criminal activities (“illicit funds”) into, out of, or through the financial system in a manner that can give such funds an appearance of legality. Money laundering involves funds derived from criminal activities, including but not limited to drug trafficking, smuggling, human trafficking, fraud, and corruption. This typically occurs in three stages: 

Placement, during which illicit funds are introduced into the financial system without attracting the attention of financial institutions or law enforcement;
Layering, during which illicit funds are moved through numerous layers of financial transactions in an attempt to disguise and/or conceal the true origin and ownership of those illicit funds; and
Integration, during which the now seemingly clean funds are retrieved through apparently legitimate transactions. 

Office of Foreign Assets Control: OFAC administers and enforces economic sanctions programs primarily against countries and groups of individuals, such as terrorists and narcotics traffickers. The sanctions can be either comprehensive or selective, using the blocking of assets and trade restrictions to accomplish foreign policy and national security goals. 

Terrorist Financing: Terrorist financing involves the solicitation, collection, or provision of funds to support terrorist acts or organizations. Funds used to finance terrorist activities may be derived either from criminal activity or from legal sources (e.g., charities), and the nature of the funding sources may vary according to the type of terrorist organization. 

This Policy does not distinguish between money laundering risk and terrorist financing risk, which are together referred to as “AML risk.”

Tipping Off: Tipping off means alerting a customer to suspicions of money laundering or disclosing to a customer confidential actions taken by the Company for BSA/AML and OFAC compliance purposes, such as filing a Suspicious Activity Report (“SAR”).	

Willful Blindness: Willful blindness means turning a blind eye or consciously avoiding facts or suspicions of money laundering or terrorist financing.

POLICY REQUIREMENTS

Overview

Although [Insert Company Here] is not required by law to implement a BSA/AML program, [Insert Company Here] has made a commitment to implement an effective BSA/AML program that reflects its contractual obligations as a service provider and is consistent with the regulatory expectations of its bank partners. As a U.S. company, [Insert Company Here] understands that it must comply with OFAC requirements. 

This Policy requires that [Insert Company Here] develop a BSA/AML and OFAC program that includes the following components:

Designation of a BSA Officer and governance structure;
Internal controls, including:
A BSA/AML and OFAC risk assessment;
KYC program;
Standards for loan disbursements, payments, and refunds;
OFAC compliance;
Transaction monitoring
Referrals for potentially suspicious activity;
Regulatory reporting and recordkeeping;
Information sharing;
Mechanisms designed to monitor ongoing compliance; 
Ongoing employee training and development; and
Independent testing.

Designation of BSA Officer and Governance Structure

The Board designates an experienced and knowledgeable Chief Compliance Officer (“CCO”) as the BSA Officer, who has responsibility for day-to-day oversight of the Company’s BSA/AML and OFAC compliance. The Board ensures that the CCO has sufficient authority and resources to effectively execute all duties. The CCO reports directly to the Chief Executive Officer (“CEO”) and regularly apprises the Board and senior management of ongoing compliance with the BSA/AML and OFAC. The BSA Compliance Officer is designated as [Insert Company Here]’s responsible individual for day-to-day execution and oversight of the BSA/AML and OFAC programs including:

Manage aspects of the [Insert Financial Institution Here] Bank Secrecy Act (BSA), Anti-Money Laundering (AML) and OFAC programs that are outsourced to the Partner.
Participate in Partner governance routines including new product development
Maintain proficient knowledge of the rules and regulations, including but not limited to, the Bank Secrecy Act (BSA), USA Patriot Act, and OFAC.
Maintain awareness of industry tools, systems and processes that will keep program scalable and competitive.
Coordinate the administration of independent auditor engagements and Partners testing requests.
Regularly report health of program to [Insert Financial Institution Here] and Partner Committees
Submit ([Insert Financial Institution Here]) BSA policy exception and exemption requests to [Insert Financial Institution Here]
Oversee suspicious activity monitoring operations including maintenance of surveillance software systems
Conduct suspicious activity investigations as needed
Submit Suspicious Activity Report escalations to [Insert Financial Institution Here] as needed
Manage fraud systems and operations as applicable
Assist with annual review procedures that align with this role
Oversee all efforts to conduct due diligence reviews of customers, strategic partners, employees, vendors, and contractors
Manage watchlist screen and other KYC systems and processes including 314(a)
Manage information sharing requests including Partners requests for info
Monitor and track BSA-AML high-risk customers processes.
Assist in annual review of procedures that align with this role
Maintain BSA program documentation (Procedures, Risk Assessment requests, etc.)
Assist in the administration of independent audits and Partners testing request.
Identify, track and drive the correction of program deficiencies (Issues Management)
Track BSA policy exception and exemption requests
Plan and execute ongoing monitoring of FCC operations
Administer BSA training program

Internal Controls

BSA/AML and OFAC Risk Assessment
The CCO conducts an annual risk assessment to identify the Program’s inherent BSA/AML and OFAC risk and the effectiveness of its controls. In conjunction with performing the risk assessment, the CCO will adopt a risk assessment methodology to support [Insert Company Here]’s risk assessment and any related BSA/AML and OFAC compliance processes.

Consistent with the regulatory obligations of covered financial institutions, the risk assessment process assigns an inherent risk rating based on an assessment of customers, product and services, and geographic risks. The CCO then assesses the adequacy of the design and implementation of mitigating controls to determine the residual risk.  

As part of this risk assessment, the CCO will:
Identify the Company’s current overall BSA/AML and OFAC risk profile;
Determine the adequacy and effectiveness of BSA/AML and OFAC controls;
Evaluate the adequacy and application of BSA/AML and OFAC resources;
Identify the existence of any unmitigated and/or unacceptable BSA/AML and OFAC risk; and
If necessary, recommend and implement modifications to the BSA/AML and OFAC program (and the underlying strategy, policies, and procedures) to bring the Company’s BSA/AML and OFAC risk to an acceptable level.

The CCO reports the results of the BSA/AML and OFAC risk assessment to the Board for review and approval. The CCO makes the assessment available to other functions within the organization.  

KYC Program 
[Insert Company Here]’s KYC program allows the Company to identify and verify the identity of its customers with reasonable assurance. 

Customer Identification Program
[Insert Company Here]’s CIP is a fundamental control in preventing the Company from becoming involved in money laundering, terrorist financing, or sanctions violations. [Insert Company Here]’s policy is to collect the following identity information for all of its customers, all of whom are individuals (the Company does not accept legal entities or businesses as customers):
Full legal name;
Date of birth;
Social Security Number (“SSN”); and
Current physical U.S. street address.

In addition, [Insert Company Here] may collect information for other purposes that will deepen its understanding of customer identity. Examples could include mobile telephone numbers and device ID.
[Insert Company Here] will collect this information using its proprietary mobile application and will not open an account until it has verified this information (“customer verification”) through at least one of the following criteria:
Images of photo identification documents provided by the customer;
[Insert Company Here]’s existing CIP data (for repeat customers);
Information provided by a credit reporting agency; and/or
Data from external identity verification or fraud detection service providers approved by the CCO.

[Insert Company Here]’s policy is not to open an account for persons who fail customer verification. 
The Company will never open an account for customers who:
Are corporations or other entities;
Give only a P.O. Box address;
Give a foreign address;
Do not provide each of the required pieces of information identified above;
Have previously had an account closed by the Company for BSA/AML or risk/loss management reasons; or
Are subject to U.S. sanctions (see section 3.3.4 OFAC Compliance below).

[Insert Company Here] will ensure that it provides written notification to its customers of the USA PATRIOT Act’s customer identification requirements and will retain all CIP information for at least five years after the date of the customer’s most recent transaction or transaction attempt.

Standards for Loan Disbursements, Payments, and Refunds
The Company understands that loans and monetary refunds to customers pose a potential risk for money laundering and/or terrorist financing. As a result, the Company will strictly adhere to certain standards surrounding loan disbursements, payments, and refunds, including the following:
Loan proceeds may only be disbursed directly to the dental providers from whom the customers receive the treatments financed by their loans;
Loan proceeds may not be disbursed to the customers or any other parties;
The maximum amount of each loan is limited to the amount required for a given treatment;
Customers may not make loan payments to [Insert Company Here] by cash or monetary instruments (i.e., cashier's checks, traveler's checks, and money orders) – they may through ACH transfers or by personal checks;
Credit may not be refunded to an account other than the one from which the customer made the payment; and
Credit may not be refunded to an individual other than the original customer.

OFAC Compliance
The CCO will establish controls to ensure that [Insert Company Here] complies with OFAC regulations to enforce economic and trade sanctions based on U.S. foreign policy and national security goals. The OFAC controls will apply to all parties with which the Company does business including, but not limited to, customers, suppliers, vendors, and [Insert Company Here] employees. The CCO will establish systems and procedures to ensure that the Company:
Screens each customer against OFAC sanctions programs and the Specially Designated Nationals and Blocked Persons (“SDN”) List prior to approving a loan;
Screens suppliers, vendors, and employees prior to conducting business with them;
Updates internal OFAC lists in a timely fashion when the OFAC announces changes to sanctions programs and/or SDN List;
Screens all existing customers, suppliers, vendors, and employees against the SDN List when the list is updated;
Blocks or rejects transactions as appropriate under U.S. sanctions law; and
Reports blocked and rejected items to OFAC and prepares annual reports to OFAC on the total of blocked funds.

All potential matches to the SDN list will be reviewed as appropriate and either cleared or escalated timely. If a potential match cannot be confirmed as a false positive it will be promptly escalated to [Insert Company Here] BSA Compliance Officer.  Accounts or transactions that appear to be positive matches should be either blocked or rejected as appropriate.  		

If a match with the SDN list is confirmed, [Insert Company Here] BSA Compliance Officer will within one day of taking any action to reject or block an account or transaction, will provide notification to the [Insert Company Here] BSA Officer in order to enable the filing of a blocked assets or rejected transactions report to OFAC. 

A comprehensive report of all blocked transactions through the annual period ending on June 30th of each calendar year shall be gathered and sent to the Bank in order to meet annual OFAC filing requirements.

Transaction Monitoring 
[Insert Company Here] utilizes both automated and manual systems to monitor customer activity and to detect unusual or potentially suspicious transactions. [Insert Company Here]’s policy is to take a conservative approach to monitoring by setting low dollar monitoring thresholds and by denying accounts that display unusual activity. At a minimum, the Company will monitor for:
Loan payments by third parties;
Sudden/unexpected payment on loans with no evidence of refinancing or other explanation;
High volumes of loan applications at a single dental practice;
High volumes of fraud claims associated with a given dental practice, both by dollar amount and number of transactions;
Fraudulent loan applications;
Excessive overpayments or refunds;
Patterns that may indicate potential criminal activity; and
Excessive accounts or transactions assigned to one SSN, address, or telephone number.

In addition, the Company requires all its employees to report unusual or potentially suspicious activity to the CCO, including but not limited to activity identified by fraud detection systems. The CCO will ensure that all employees receive training on how to report suspicious activity as part of the BSA/AML and OFAC training program (see section 3.4 Training and Development below).

The CCO will set transaction monitoring thresholds and will have authority to make changes as needed in response to emerging patterns of activity. The CCO will document the reason for raising or eliminating a monitoring threshold and report that to the Risk Management Committee. The Board must also ratify lowering a monitoring threshold or imposing a new threshold. However, in the event that new patterns of suspicious activity emerge between meetings, the CCO is authorized to impose new thresholds pending the next Board meeting. The CCO will ensure that the rationale for all changes in thresholds is documented and retained.

Referrals for Potentially Suspicious Activity 
Under federal law, covered financial institutions must file a SAR when a transaction is suspicious. While [Insert Company Here] is not obligated to file SARs, its relationship with its bank partners requires that it refer potentially suspicious activities that it observes as part of the customer onboarding and monitoring processes. 

[Insert Company Here] has implemented procedures for referring potentially suspicious activity to its bank partners and, consistent with BSA legal requirements, maintains records for customer account information (including the information obtained during the customer vetting process) for the time period required by federal obligations. 

The CCO oversees investigations and determines whether the Company needs to take actions, including but not limited to, referral for potentially suspicious activity and account closure. Where a referral is not made, the Company will document the basis for that decision. 

[Insert Company Here] will refer potentially suspicious activity to the relevant bank partner within 20 business days of reasonably becoming aware of the activity. The Company prohibits all employees from “tipping off” users that they are under investigation or that [Insert Company Here] has made referrals for their potentially suspicious activity.  

In addition, the CCO may, at his or her discretion, alert law enforcement directly of activity that he or she believes will be of immediate use to a particular agency. Reportable unusual activity includes:
Criminal violations involving insider abuse in any amount (insiders include directors, officers, employees, agents or other institution affiliated parties);
Criminal violations aggregating $5,000 or more when a suspect can be identified;
Criminal violations aggregating $25,000 or more regardless of potential suspect;
Transactions conducted or attempted by, at or through   and aggregating $5,000 or more if   or the Bank suspects or has reasons to suspect the transaction:
May involve potential money laundering or other illegal activity
Is designed to evade the BSA or its implementing regulations
Has no business or apparent lawful purpose or is not the type of transaction that the particular customer would normally be expected to engage in, and   or the Bank knows of no reasonable explanation for the transaction after examining the available facts, including the background and possible purpose of the transaction.

All information provided to the Bank to support these activities will be strictly confidential, including processes and controls within [Insert Company Here] to prevent unauthorized access or dissemination of such information.

Final SAR filing decisions and activities are entirely at the discretion of the Bank.

Regulatory Reporting and Recordkeeping
Currency Transaction Reporting
The Currency Transaction Report (“CTR”) requirements do not currently apply to [Insert Company Here] because the Company does not accept currency as defined by the Internal Revenue Service (“IRS”).  
If, due to a change in the IRS’s filing requirements or [Insert Company Here] business activities, [Insert Company Here] begins accepting currency as defined by the IRS, the CCO will amend this Policy and develop procedures for filing CTRs in accordance with the relevant regulations.

Purchase and Sale of Monetary Instruments Recordkeeping
The Company has no plans to purchase or sell monetary instruments.
If in the future the Company develops plans to do so, the CCO will ensure that the Company develops recordkeeping procedures in advance of commencing the activity.

Funds Transfer Recordkeeping
The Company allows customers and dental providers to make and receive funds transfers only through ACH payments, which are exempt from funds transfer recordkeeping requirements.
If in future the Company develops plans to allow other types of funds transfers, the CCO will ensure that the Company develops recordkeeping procedures in advance of the activity commencing.

Reports of International Transportation of Currency or Monetary Instruments (“CMIRs”)
The CMIRs requirements do not currently apply to [Insert Company Here] because the Company does not plan to undertake any activities that would involve transporting, mailing, or shipping monetary instruments out of or into the United States in any amount.
 If in the future the Company develops plans to allow other types of funds transfers, the CCO will ensure that the Company develops reporting procedures in advance of the activity commencing.

Information Sharing
The Company will cooperate fully with federal government authorities, law enforcement authorities, and financial institution partners on BSA/AML investigations to the extent allowable under applicable privacy and other laws.
The CCO will establish systems and procedures to ensure that the Company:
Establishes a central process for receiving, documenting and responding to requests for information sharing and subpoenas; and
Promptly evaluates all information sharing requests received, including those from its bank partners, and provides timely responses providing all information [Insert Company Here] is legally allowed to share.

Mechanisms Designed to Monitor Ongoing Compliance

Staffing
The CCO will ensure that he or she has adequate staffing, both in numbers and qualifications, to implement the Company’s BSA/AML and OFAC program effectively. At least annually, the CCO will present his or her approach to staffing to the Risk Management Committee for approval and will ensure that all activities performed on behalf of the Company comply with Company policies and procedures and all applicable regulatory requirements regardless of the personnel performing the tasks.

New Products  
New or modified products and business practices require, among other things, sign-off by the CCO through a separate process coordinated pursuant to the Company’s Compliance Policy and related procedure. The CCO evaluates the potential BSA/AML and OFAC risks of new or changed products and services from a compliance perspective to ensure that any BSA/AML and OFAC risks are appropriately identified and mitigated.

Quality Assurance/Testing
The CCO will put in place a regular quality assurance program to ensure that the Company maintains a high quality BSA/AML and OFAC program. At a minimum, this Quality Assurance Program will review the Company’s:
KYC program;
Quality of transaction monitoring;
Timeliness and quality of referrals to bank partners;
Information sharing;
OFAC screening; and
Recordkeeping.

The CCO will ensure that the approach to testing BSA/AML and OFAC compliance is consistent with the Company’s overarching compliance testing approach.

Reporting
To ensure effective management and Board oversight of the BSA/AML and OFAC Policy and program, the CCO reports quarterly to the Risk Management Committee and annually to the Board on:
BSA/AML and OFAC compliance trends; 
BSA/AML and OFAC quality assurance/testing results;
Material BSA/AML and OFAC compliance issues and/or escalated issues;
Status of BSA/AML and OFAC corrective actions;
Independent testing findings, bank partner concerns, and/or regulatory concerns; and
Emerging BSA/AML and OFAC compliance issues which the Company will need to address.

The annual report to the Board on the state of BSA/AML compliance and any significant emerging issues will assist the Board in evaluating any Policy changes that may be appropriate.
[Insert Company Here] will provide the applicable reporting to the Bank in the timeframes agreed upon between the two parties. [Insert Company Here] will also provide any required reporting to demonstrate adherence to this Policy in a format and timeframe as deemed reasonable.

Training and Development

The Company requires that all employees of both [Insert Company Here] and its third-party service providers, as well as the Board, receive BSA/AML and OFAC training appropriate to their roles and responsibilities. The first training will have to be within 30 days of start date after which employees need to complete training on an annual basis.

The goals of [Insert Company Here]’s BSA/AML and OFAC training program are to:
Ensure [Insert Company Here]’s employees are familiar with relevant BSA/AML and OFAC requirements pertaining to their specific job functions and that they receive the most current information available;
Ensure that the Board is knowledgeable regarding [Insert Company Here]’s obligations and responsibilities under BSA/AML law;
Inculcate an understanding of the significance of [Insert Company Here]’s BSA/AML and OFAC compliance efforts and help develop a strong culture of compliance across the Company; and
Develop a cadre of staff and managers throughout [Insert Company Here] to detect, escalate, and manage BSA/AML and OFAC compliance-related risks as and when they arise.
Consistent with [Insert Company Here]’s Compliance Policy, the CCO is responsible to ensure that the BSA/AML and OFAC training program is incorporated into the annual compliance training plan.

Independent Testing

The Board oversees the completion, at least annually, of an independent test of [Insert Company Here]’s BSA/AML compliance by a qualified third-party firm, for assessing the implementation and effectiveness of the Company’s BSA/AML and OFAC Program and the adequacy of its controls over BSA/AML and OFAC compliance risk. The CCO is responsible for updating [Insert Company Here]’s risk assessment in light of any issues raised during the independent testing and taking necessary corrective action to remediate findings.  The engagement will include, at a minimum:
An evaluation of the overall effectiveness of the BSA/AML/Sanctions Compliance Program, including related Policies, SOPs, and processes
Risk-based transaction testing to verify the adherence to BSA/AML/Sanctions recordkeeping and reporting requirements
An evaluation of Management’s efforts to resolve violations and deficiencies noted in previous audits and/or regulatory examinations
A review of BSA/AML staff training for adequacy, accuracy, and completeness
A review of the effectiveness of the suspicious activity monitoring systems used for BSA/AML compliance.
An assessment of the overall process for identifying and reporting suspicious activity to [Insert Financial Institution Here], including a review of filed or prepared SARs for accuracy, timeliness, completeness, and adherence to the Policy.
An assessment of the integrity and accuracy of Management Information Systems (MIS) used in the BSA/AML/Sanctions Compliance Program.

Draft and final reports will be made available to the Bank and issues noted within the report will include [Insert Company Here] management response and will be tracked and remediated in a timely manner.

ROLES AND RESPONSIBILITIES


EXCEPTIONS

From time to time, [Insert Company Here] may reasonably determine that a Policy exception is warranted. This Policy requires the CCO to sign off on any such exceptions and to provide reporting to the Risk Management Committee. For exceptions involving critical relationships, the CCO should advise the Board on potential risks associated with the exception as well as any proposed actions for mitigating risks. Certain exceptions should be escalated to [Insert financial Institution Here] for approval.
Notwithstanding the foregoing, under no circumstances does [Insert Company Here] allow Policy exceptions that would result in a violation of law.

POLICY ADMINISTRATION

Document Management 


Approval Management 

Related Documents

Related Procedures 
BSA/AML and OFAC Procedures

Applicable Law and Regulations
The following are non-exclusive but key laws and regulations that apply to this Policy: 
Bank Secrecy Act, including the following:
31 U.S.C. 5311-5332
31 U.S.C. 1951-1959e
Bank Secrecy Act Regulation, including the following:
31 CFR Chapter X
Office of Foreign Assets Control, including the following:
31 CFR Part 500, et seq.
List of Specially Designated Nationals and Blocked Entities
Uniting and Strengthening America by Providing Appropriate Tools Required to Intercept and Obstruct Terrorism Act of 2001 (“USA PATRIOT Act”)
Public Law 107-56
