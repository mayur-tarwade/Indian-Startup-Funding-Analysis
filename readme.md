### Indian Startup Analysis Model

The dataset you uploaded contains information about startup funding events in India. Here’s an explanation of its structure:
### Dataset Overview

•	Total Rows: 2,846 (each row represents a unique funding event)

•	Total Columns: 8

Column Descriptions
1.	Date:
The date on which the funding event occurred. (Format: YYYY-MM-DD)
2.	Startup:
The name of the startup that received funding.
3.	Vertical:
The broad industry or sector the startup belongs to (e.g., E-Tech, FinTech, Transportation).
4.	Subvertical:
A more specific description of the business area (e.g., E-learning, App based shuttle service).
 Note: This column has missing values in some rows.
5.	City:
The location where the startup is headquartered or where the funding was reported.
6.	Investors:
The name(s) of the investor(s) involved in the funding round.
7.	Round:
The type or stage of the funding round (e.g., Seed Round, Series A, Private Equity Round).
8.	Amount:
The amount of funding received (in an unspecified currency, likely INR or USD). Stored as a float.

### Top 10 Cities by Number of Funding Events:

| City      | Count |
| --------- | ----- |
| Bangalore | 699   |
| Mumbai    | 565   |
| New Delhi | 421   |
| Gurgaon   | 286   |
| Bengaluru | 139   |
| Pune      | 105   |
| Hyderabad | 99    |
| Chennai   | 97    |
| Noida     | 92    |
| Gurugram  | 50    |




###  Top 10 Industry Verticals by Total Funding:

| Vertical                         | Total Funding |
| -------------------------------- | ------------- |
| Consumer Internet                | ₹51,588M      |
| eCommerce                        | ₹41,271M      |
| Transportation                   | ₹32,312M      |
| Technology                       | ₹18,395M      |
| Finance                          | ₹16,264M      |
| ECommerce                        | ₹15,500M      |
| FinTech                          | ₹10,071M      |
| E-Commerce                       | ₹8,277M       |
| Online Marketplace               | ₹5,776M       |
| E-Commerce & M-Commerce platform | ₹5,610M       |

### Total Funding by Year:

| Year | Total Funding (₹ Million) |
| ---- | ------------------------- |
| 2015 | 60,462                    |
| 2016 | 31,581                    |
| 2017 | 86,042                    |
| 2018 | 42,260                    |
| 2019 | 78,077                    |
| 2020 | 3,219                     |



 ![image](https://github.com/user-attachments/assets/941d7cb3-9228-4353-acf0-3dc91ea1d436)
 ![image](https://github.com/user-attachments/assets/a06307ed-7dce-4b79-8076-3c4631374262)
 ![image](https://github.com/user-attachments/assets/a2590da7-3585-4f8e-a98f-f401ca607fca)




 
 


### Here are the visualizations:
1.	Top Cities by Number of Funding Events
Bangalore, Mumbai, and New Delhi dominate startup activity in India.
2.	Top Industry Verticals by Total Funding
"Consumer Internet", "eCommerce", and "Transportation" have received the highest overall funding. Note the inconsistency in how similar sectors are named (e.g., eCommerce vs. E-Commerce).
3.	Funding Trend Over the Years
There was a peak in funding in 2017 and 2019, followed by a major dip in 2020—likely due to the global pandemic



#### Streamlit App Link - https://indian-startup-funding-analysis-wwyavzedjk9vp3g5rxsyez.streamlit.app
