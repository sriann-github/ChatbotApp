import pandas as pd

incidents_file_path = "D:\Learning-Valli\Azure\Data Files for Solutions\chatbot\incidents_table.csv"
incidents_df = pd.read_csv(incidents_file_path)

emails_sample = []
email_types = ['Notification', 'Escalation Alert', 'Closure Update']
oncall_emails = {
  'Critical': 'critical-oncall@company.com',
  'High': 'high-oncall@company.com',
  'Medium': 'medium-oncall@company.com',
  'Low': 'low-oncall@company.com'
}

# Generate email entries for each incident
for idx, row in incidents_df.iterrows():
  email_type = email_types[idx % len(email_types)] #Rotate through email types
  sent_to = oncall_emails.get(row['severity'], 'support@company.com')
  recipients = f"team-{row['severity'].lower()}@company.com, escalation@company.com"
  emails_sample.append({
    'incident_id' : row['incident_id'],
    'email_type': email_type,
    'sent_to': sent_to,
    'recipients': recipients
  })
  
  #Create a DataFrame for the Emails table
  emails_df = pd.DataFrame(emails_sample)
  
  # Save to a CSV file
  emails_file_path = 'emails_table_sample.csv'
  emails_df.to_csv(emails_file_path, index=False)
  
  print(f"Emails saved to {emails_file_path}")