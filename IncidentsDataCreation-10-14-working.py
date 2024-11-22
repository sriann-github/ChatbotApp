import pandas as pd
import random
import datetime
import time

# Helper functions to generate random data
def random_date(start, end):
    return start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def random_phone():
    return f"555-{random.randint(1000, 9999)}"

def random_status():
    return random.choice(['Open', 'In Progress', 'Closed'])
  
def random_severity():
    return random.choice(['High','Medium','Low'])

def random_date(start, end):  
    return start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

# Data for Incident Categories table
def generate_categories():
    categories = [
        {'category_Id': '100',
         'category_name': 'Website Performance',
         'subcategories': [
            {'subctg_Id': '101', 'subctg_name':'Slow Page Load'}, 
            {'subctg_Id': '102', 'subctg_name':'Server Downtime'}, 
            {'subctg_Id': '103', 'subctg_name':'High Response Time'}, 
            {'subctg_Id': '104', 'subctg_name':'CDN Issues'}, 
            {'subctg_Id': '105', 'subctg_name':'Caching Problems'}, 
            {'subctg_Id': '106', 'subctg_name':'Image Loading Issues'}, 
            {'subctg_Id': '107', 'subctg_name':'Broken Links'}, 
            {'subctg_Id': '108', 'subctg_name':'CSS Not Loading'},
            {'subctg_Id': '109', 'subctg_name':'JavaScript Errors'}, 
            {'subctg_Id': '110', 'subctg_name':'Third-Party Script Issues'}
        ]},
        {'category_Id': '200', 'category_name': 'Checkout Failures', 'subcategories': [
            {'subctg_Id': '201', 'subctg_name':'Payment Gateway Error'}, 
            {'subctg_Id': '202', 'subctg_name':'Order Processing Failure'}, 
            {'subctg_Id': '203', 'subctg_name':'Cart Not Updating'}, 
            {'subctg_Id': '204', 'subctg_name':'Shipping Address Error'}, 
            {'subctg_Id': '205', 'subctg_name':'Tax Calculation Issues'}, 
            {'subctg_Id': '206', 'subctg_name':'Order Duplication'}, 
            {'subctg_Id': '207', 'subctg_name':'Invalid Promo Code'}, 
            {'subctg_Id': '208', 'subctg_name':'Discount Calculation Errors'}, 
            {'subctg_Id': '209', 'subctg_name':'Checkout Timeout'}, 
            {'subctg_Id': '210', 'subctg_name':'Guest Checkout Not Working'}
        ]},
        {'category_Id': '300', 'category_name': 'User Authentication Issues', 'subcategories': [
            {'subctg_Id': '301', 'subctg_name':'Login Failures'}, {'subctg_Id': '302', 'subctg_name':'Password Reset Issues'}, 
            {'subctg_Id': '303', 'subctg_name':'Two-Factor Authentication Failure'}, {'subctg_Id': '304', 'subctg_name':'OAuth Token Expiry'}, {'subctg_Id': '305', 'subctg_name':'Session Timeout'},
            {'subctg_Id': '306', 'subctg_name':'Account Creation Errors'}, {'subctg_Id': '307', 'subctg_name':'Social Login Failures'}, {'subctg_Id': '308', 'subctg_name':'Email Confirmation Error'}, 
            {'subctg_Id': '309', 'subctg_name':'Invalid Credentials'}, {'subctg_Id': '302', 'subctg_name':'Account Lockouts'}
        ]},
        {'category_Id': '400', 'category_name': 'Product Catalog', 'subcategories': [
            {'subctg_Id': '401', 'subctg_name':'Missing Products'}, {'subctg_Id': '402', 'subctg_name':'Search Issues'}, {'subctg_Id': '403', 'subctg_name':'Incorrect Prices'}, {'subctg_Id': '404', 'subctg_name':'Product Unavailable'}, 
            {'subctg_Id': '405', 'subctg_name':'Outdated Stock Information'}, {'subctg_Id': '406', 'subctg_name':'Product Description Errors'}, {'subctg_Id': '407', 'subctg_name':'Product Image Missing'},
            {'subctg_Id': '408', 'subctg_name':'Category Not Displaying'}, {'subctg_Id': '409', 'subctg_name':'Related Products Missing'}, {'subctg_Id': '410', 'subctg_name':'Product Filtering Issues'}
        ]},
        {'category_Id': '500', 'category_name': 'Order Fulfillment', 'subcategories': [
            {'subctg_Id': '501', 'subctg_name':'Shipping Delays'}, {'subctg_Id': '502', 'subctg_name':'Tracking Number Errors'}, {'subctg_Id': '503', 'subctg_name':'Order Not Processed'}, 
            {'subctg_Id': '504', 'subctg_name':'Warehouse Stock Errors'}, {'subctg_Id': '505', 'subctg_name':'Incorrect Order Shipment'}, {'subctg_Id': '506', 'subctg_name':'Order Cancellation Failed'},
            {'subctg_Id': '507', 'subctg_name':'Order Not Received'}, {'subctg_Id': '508', 'subctg_name':'Return Not Processed'}, {'subctg_Id': '509', 'subctg_name':'Exchange Delays'}, {'subctg_Id': '510', 'subctg_name':'Wrong Order Status'}
        ]},
        {'category_Id': '600', 'category_name': 'Promotions and Discounts', 'subcategories': [
            {'subctg_Id': '601', 'subctg_name':'Promo Code Not Working'}, {'subctg_Id': '602', 'subctg_name':'Discount Misapplied'}, {'subctg_Id': '603', 'subctg_name':'Sale Price Incorrect'}, 
            {'subctg_Id': '604', 'subctg_name':'Discount Expired Early'}, {'subctg_Id': '605', 'subctg_name':'Promotion Not Visible'}, {'subctg_Id': '606', 'subctg_name':'Free Shipping Not Applied'}, 
            {'subctg_Id': '607', 'subctg_name':'Bundle Discount Error'}, {'subctg_Id': '608', 'subctg_name':'Flash Sale Issue'}, {'subctg_Id': '609', 'subctg_name':'Promotion Overlapping'}, 
            {'subctg_Id': '610', 'subctg_name':'Loyalty Points Not Applied'}
        ]},
        {'category_Id': '700', 'category_name': 'Customer Support Integration', 'subcategories': [
            {'subctg_Id': '701', 'subctg_name':'Live Chat Unavailable'}, {'subctg_Id': '702', 'subctg_name':'Support Ticket Delays'}, {'subctg_Id': '703', 'subctg_name':'Incorrect Support Information'}, 
            {'subctg_Id': '704', 'subctg_name':'Automated Response Error'}, {'subctg_Id': '705', 'subctg_name':'Chatbot Not Responding'}, {'subctg_Id': '706', 'subctg_name':'Support Ticket Not Created'}, 
            {'subctg_Id': '707', 'subctg_name':'Escalation Failure'}, {'subctg_Id': '708', 'subctg_name':'Callback Request Failed'}, {'subctg_Id': '709', 'subctg_name':'Support Chat Disconnected'}, 
            {'subctg_Id': '710', 'subctg_name':'No Support Agent Available'}
        ]},
        {'category_Id': '800', 'category_name': 'Security Breaches', 'subcategories': [
            {'subctg_Id': '801', 'subctg_name':'Unauthorized Access'}, {'subctg_Id': '802', 'subctg_name':'Suspicious Activity'}, {'subctg_Id': '803', 'subctg_name':'Data Breach'}, 
            {'subctg_Id': '804', 'subctg_name':'Phishing Attempt'}, {'subctg_Id': '805', 'subctg_name':'Account Compromise'}, {'subctg_Id': '806', 'subctg_name':'Malware Detection'}, 
            {'subctg_Id': '807', 'subctg_name':'SQL Injection'}, {'subctg_Id': '808', 'subctg_name':'Cross-Site Scripting (XSS)'}, {'subctg_Id': '809', 'subctg_name':'Brute Force Attack'},
            {'subctg_Id': '810', 'subctg_name':'Privilege Escalation'}
        ]},
        {'category_Id': '900', 'category_name': 'Database Failures', 'subcategories': [
            {'subctg_Id': '901', 'subctg_name':'Connection Timeout'}, {'subctg_Id': '902', 'subctg_name':'Data Corruption'}, {'subctg_Id': '903', 'subctg_name':'Synchronization Issues'}, 
            {'subctg_Id': '904', 'subctg_name':'Database Migration Errors'}, {'subctg_Id': '905', 'subctg_name':'Query Performance Issues'}, {'subctg_Id': '906', 'subctg_name':'Data Backup Failure'}, 
            {'subctg_Id': '907', 'subctg_name':'Data Loss'}, {'subctg_Id': '908', 'subctg_name':'Primary Key Violation'}, {'subctg_Id': '909', 'subctg_name':'Foreign Key Constraint Error'}, 
            {'subctg_Id': '910', 'subctg_name':'Database Locking'}
        ]},
        {'category_Id': '1000', 'category_name': 'API Failures', 'subcategories': [
            {'subctg_Id': '1001', 'subctg_name': 'Third-Party Service Error'}, {'subctg_Id': '1002', 'subctg_name':'API Response Timeout'}, {'subctg_Id': '1003', 'subctg_name':'Incorrect API Data'}, 
            {'subctg_Id': '1004', 'subctg_name':'Authentication Failure'}, {'subctg_Id': '1005', 'subctg_name':'Rate Limiting'}, {'subctg_Id': '1006', 'subctg_name':'Webhook Failure'}, 
            {'subctg_Id': '1007', 'subctg_name':'API Key Expiry'}, {'subctg_Id': '1008', 'subctg_name':'Invalid API Request'}, {'subctg_Id': '1009', 'subctg_name':'Malformed Response'}, 
            {'subctg_Id': '2000', 'subctg_name':'API Versioning Issues'}
        ]}
    ]    
   
    category_list = []
    for category in categories:        
        for _, subcategory in enumerate(category['subcategories']):
            # print (subcategory)
            category_list.append({'category_Id': category['category_Id'] , 'category_name': category['category_name'], 'subcategory_Id': subcategory['subctg_Id'], 'subcategory_name': subcategory['subctg_name']})
    
    return pd.DataFrame(category_list)

incident_templates = [
    "User reported {subcategory} issue on the website, causing poor user experience.",
    "Website experienced {subcategory}, leading to a significant drop in performance.",
    "Frequent {subcategory} was observed, requiring immediate attention."
]

root_cause_templates = [
    "Root cause identified as {subcategory}-related configuration errors.",
    "Issue traced to a faulty {subcategory} system.",
    "Problem caused by an unexpected {subcategory} misconfiguration."
]

resolution_templates = [
    "Resolved the issue by optimizing {subcategory}-related settings.",
    "Fixed the problem by updating {subcategory} configurations.",
    "Patched the underlying {subcategory} component to restore functionality."
]

solution_templates = [
    "Implemented a new cache strategy for {subcategory} to reduce server load.",
    "Upgraded the {subcategory} system to handle increased traffic volume.",
    "Applied patches to the {subcategory} modules, improving stability and performance."
]

business_impact_templates = {    
    "HighImpact": [
        "Significant revenue loss as users are unable to complete transactions due to {subcategory} issue.",
        "High severity impact on business operations with core functions interrupted, affecting daily workflows.",
        "Critical client relationships are strained as {subcategory} issue delays critical project timelines.",
        "High-level impact on operational efficiency, with a 50% drop in system performance due to {subcategory} issue."        
    ],
    
    "ModImpact":[
        "Moderate disruption in service availability, causing delays in user access to key functionalities.",
        "Noticeable effect on user satisfaction, with an increase in support tickets related to {subcategory}.",
        "Impact on back-office productivity, as team members experience delays due to {subcategory} issues.",
        "Service quality impacted as {subcategory} issues lead to inconsistent user experiences."        
        
    ],
    
    "LowImpact": [
         "Minimal impact, limited to slower response times in certain functions due to {subcategory}.",
        "Low-level effect on non-essential services, with minor inconvenience for users encountering {subcategory} issues.",
        "Temporary issue resolved with minimal impact on business operations or user interactions.",
        "Low impact on business continuity, as the {subcategory} issue affects only a small subset of users."
    ]
}


def generate_user_queries(incidents_df):
    queries = []
    query_templates = [
        "What is the status of my incident related to {}?",
        "I need more information about the {} incident.",
        "Can you please update me on the incident regarding {}?",
        "Has the issue with {} been resolved?",
        "What steps are being taken to fix the {} issue?",
        "Why is the {} issue taking so long to resolve?",
        "Is there any progress on my {} incident?",
        "When can I expect the {} issue to be fixed?",
        "Can you escalate the {} issue to higher support?",
        "Why was my {} incident marked as closed?"
    ]
    
    for _, incident in incidents_df.iterrows():
        #print(incident)
        query = random.choice(query_templates).format(incident['Incident_Description'])
        #time.sleep(1)
        user_query = {
            'incident_id': incident['incident_id'],
            'user_id': incident['user_id'],
            'query': query,
            #'created_at': random_date(incident['created_at'], datetime.datetime.now())
        }
        queries.append(user_query)
        print(len(queries))
        if len(queries) > 100:
            break
    
    return pd.DataFrame(queries)

# Data for Users table
def generate_users(num_users=10):
    names = [
        'John Doe', 'Jane Smith', 'Mike Johnson', 'Emily Davis', 'Daniel Brown', 
        'Sarah Wilson', 'David Lee', 'Laura Taylor', 'James White', 'Olivia Green'
    ]
    roles = ['Admin', 'Support', 'Manager', 'Technician', 'Analyst']
    departments = ['IT', 'Customer Support', 'Sales', 'Data Analytics']
    
    users = []
    start_date = datetime.datetime(2024, 9, 1)
    end_date = datetime.datetime(2024, 9, 30)
    
    for i in range(num_users):
        user = {
            'Id': i,
            'name': names[i],
            'email': f"{names[i].replace(' ', '.').lower()}@example.com",
            'role': random.choice(roles),
            'phone': random_phone(),
            'department': random.choice(departments),
            'created_at': random_date(start_date, end_date),
            'last_login': random_date(start_date, datetime.datetime.now())
        }
        users.append(user)
    return pd.DataFrame(users)

# Precompute template-based lists for faster access
def precompute_templates(categories_df):
    templates = []
    for _,category in categories_df.iterrows():
        templates.append({
            'subcategory_name': category['subcategory_name'],
            'subcatery_Id': category['subcategory_Id'],
            'incident_templates': [t.format(subcategory=category['subcategory_name']) for t in incident_templates],
            'root_cause_templates': [t.format(subcategory=category['subcategory_name']) for t in root_cause_templates],
            'resolution_templates': [t.format(subcategory=category['subcategory_name']) for t in resolution_templates],
            'solution_templates': [t.format(subcategory=category['subcategory_name']) for t in solution_templates],
            'LowImpact': [t.format(subcategory=category['subcategory_name']) for t in business_impact_templates["LowImpact"]],
            'ModImpact': [t.format(subcategory=category['subcategory_name']) for t in business_impact_templates['ModImpact']],
            'HighImpact': [t.format(subcategory=category['subcategory_name']) for t in business_impact_templates['HighImpact']]
        })
    return templates

# Function to generate random incidents
def generate_random_incidents(num_incidents, users_df, categories_df):
    incident_list = []
    start_date = datetime.datetime(2024, 10, 1)
    end_date = datetime.datetime(2024, 10, 30)
    
    #category_list = []
    #for category in categories:        
     #   for _, subcategory in enumerate(category['subcategories']):
      #      category_list.append({'category_Id': category['category_Id'] , 'category_name': category['category_name'], 'subcategory_Id': subcategory['subctg_Id'], 'subcategory_name': subcategory['subctg_name']})
    #categories_df = pd.DataFrame(category_list)
    
    count = 0
    unique_descriptions = set()
    
    #Precompute templates to avoid repeated formatting
    precomputed_templates = precompute_templates(categories_df)
    
    while count < num_incidents:
        template = random.choice(precomputed_templates)
        
        #Generate fields based on precomputed templates
        incident_desc = random.choice(template['incident_templates'])
        
        if incident_desc in unique_descriptions:
            continue
        
        unique_descriptions.add(incident_desc)
        
        root_cause = random.choice(template['root_cause_templates'])
        resolution = random.choice(template['resolution_templates'])
        solution = random.choice(template['solution_templates'])
        severity = random_severity()
        
        # Select business impact based on severity
        if severity == 'Low':
            business_impact = random.choice(template['LowImpact'])
        elif severity == 'Medium':
            business_impact = random.choice(template['ModImpact'])
        else:
            business_impact = random.choice(template['HighImpact'])
            
        incident = {
            'incident_id': random.randint(1234, 100400300),
            'user_id' : random.choice(users_df.index.tolist()) + 1,
            'Incident_description': incident_desc,
            'Root_Cause': root_cause,
            'Resolution': resolution,
            'Solution': solution,
            'Business_Impact': business_impact,
            'Subcategory_Id': template['subcatery_Id'],
            'created_at': random_date(start_date, end_date),
            'updated_at': random_date(start_date, end_date) if random_status() != 'Open' else
            None,
            'severity' : severity
        }
        
        incident_list.append(incident)
        count += 1
        if count % 500 == 0:
            print(f"Incidents generated: {count}")

    return pd.DataFrame(incident_list)

# Main function to generate all tables and save as CSV
def main():
    # Generate Users, Categories, and Incidents Data
    users_df = generate_users()
    categories_df = generate_categories()
    incidents_df = generate_random_incidents(3000, users_df, categories_df)
    
    # Generate User Queries related to Incidents
    user_queries_df = generate_user_queries(incidents_df)
    
    # Save to CSV files
    users_df.to_csv('users_table.csv', index=False)
    categories_df.to_csv('categories_table.csv', index=False)
    incidents_df.to_csv('incidents_table.csv', index=False)
    user_queries_df.to_csv('user_queries_table.csv', index=False)
    
    print("Data saved to CSV files!")

# Run the script
if __name__ == "__main__":
    main()
    
    
