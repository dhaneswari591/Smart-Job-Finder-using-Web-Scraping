import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from email_alert import send_email
from gui_alert import notify

with open('dataset/justjoinit_2021-2023.json', 'r', encoding='utf-8') as f:
    job_data = json.load(f)

def extract_salary_from(job):
    employment = job.get("employment_types", [])
    if employment and isinstance(employment[0], dict):
        salary_info = employment[0].get("salary")
        if salary_info and isinstance(salary_info, dict):
            return salary_info.get("from", 0)
    return 0

def find_matching_jobs(user_prefs):
    vectorizer = TfidfVectorizer(stop_words='english')

    job_texts = [
        job['title'] + ' ' + ' '.join(
            skill['name'] for skill in job.get('skills', [])
            if isinstance(skill, dict) and 'name' in skill
        )
        for job in job_data
    ]

    tfidf_matrix = vectorizer.fit_transform(job_texts)

    user_query = user_prefs['title'] + ' ' + user_prefs['skills']
    query_vec = vectorizer.transform([user_query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

    matches = []
    for i, sim in enumerate(similarities):
        job = job_data[i]
        salary_from = extract_salary_from(job)

        if sim > 0.3 and salary_from >= user_prefs['min_salary'] and user_prefs['location'].lower() in job.get('city', '').lower():
            matches.append({
                'title': job['title'],
                'company': job.get('company_name', 'Unknown'),
                'location': job.get('city', 'Unknown'),
                'skills': ', '.join(
                    skill['name'] for skill in job.get('skills', [])
                    if isinstance(skill, dict) and 'name' in skill
                ),
                'salary': salary_from,
                'url': job.get('company_url', '#')
            })

    if matches:
        # Email Alert
        body = ""
        for job in matches:
            body += f"{job['title']} at {job['company']}\nLocation: {job['location']}\nSkills: {job['skills']}\nSalary: {job['salary']}\nLink: {job['url']}\n\n"
        send_email('receiver_email@example.com', 'Job Alert: Matches Found', body)

        # Pop-up Notification
        notify("Jobs Found!", f"{len(matches)} job(s) match your criteria.")

    return matches
