from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

responses = {
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "who are you": "I'm just a bot, for Zeotap",
    "bye": "Goodbye! Have a nice day!",
    "bye": "Thanks, It's My Job",
    "what is segment": "Segment is a customer data platform (CDP) that helps you collect, clean, and control your customer data, and send it to various tools for analytics, marketing, and data warehousing.",
    "what is mparticle": "mParticle is a customer data infrastructure that helps businesses collect, unify, and route customer data to various analytics and marketing tools.",
    "what is lytics": "Lytics is a customer data platform (CDP) that enables businesses to build and activate audience segments based on user behavior and attributes.",
    "what is zeotap": "Zeotap is a customer intelligence platform that helps businesses unify customer data, enrich it with third-party insights, and activate it for marketing campaigns.",
    "set up a new source in segment": "Go to the Sources tab, click Add Source, select the source type, and follow the setup steps. Copy the Write Key, integrate it into your app, and verify data in the Debug section.",
    "set up new source in segment": "Go to the Sources tab, click Add Source, select the source type, and follow the setup steps. Copy the Write Key, integrate it into your app, and verify data in the Debug section.",
    "create a user profile in particle": "Use the mParticle SDK’s identify event to create a profile with User ID and attributes. Verify the profile in the Live Stream or User Activity sections.",
    "create an user profile in particle": "Use the mParticle SDK’s identify event to create a profile with User ID and attributes. Verify the profile in the Live Stream or User Activity sections.",
    "create user profile in particle": "Use the mParticle SDK’s identify event to create a profile with User ID and attributes. Verify the profile in the Live Stream or User Activity sections.",
    "build an audience segment in lytics": "Navigate to Audiences, click 'Create New Audience', and set filters based on user attributes. Save and activate the segment for use in marketing campaigns.",
    "build audience segment in lytics": "Navigate to Audiences, click 'Create New Audience', and set filters based on user attributes. Save and activate the segment for use in marketing campaigns.",
    "integrate my data with zeotap": "Choose integration type (API, SFTP, or SDK), then send user data in JSON format. Validate data ingestion in the Data Dashboard.",
    "install segment": "Install Segment by adding the JavaScript snippet or SDK and configuring your source.",
    "track events": "Use analytics.track('Event Name', { properties }) to log events in Segment.",
    "add source": "Go to Sources, click 'Add Source,' select your source type, and configure it.",
    "connect destination": "Select a destination in the Destinations tab, configure settings, and enable it.",
    "transform data": "Use Functions to modify data before sending it to destinations.",
    "debug events": "View real-time event logs in the Debugger section of the Segment UI.",
    "forward data warehouse": "Enable warehouse destinations like BigQuery or Redshift to store event data.",
    "set user traits": "Use analytics.identify('userId', { traits }) to update user details.",
    "filter events": "Use Destination Filters to exclude, modify, or allow specific events.",
    "gdpr compliance": "Use Data Privacy controls to handle GDPR and data deletion requests.",
    "install mparticle": "Integrate the mParticle SDK and configure data sources in the dashboard.",
    "track events mparticle": "Use logEvent('Event Name', { attributes }) to track user actions.",
    "set user profile": "Use setUserAttribute('key', 'value') to update user profiles.",
    "send user identity": "Use Identity.login() with unique identifiers to sync user data.",
    "connect google analytics": "Add Google Analytics as an output and map events accordingly.",
    "transform data in segment": "Utilize 'Functions' within Segment to modify data before routing it to destinations.",
    "forward data to warehouse in segment": "Enable warehouse destinations such as BigQuery or Redshift in Segment to store and analyze event data.",
    "filter events in segment": "Apply 'Destination Filters' to include or exclude specific events from being sent to particular destinations.",
    "manage user identities in mparticle": "Leverage mParticle's IDSync feature to handle and synchronize user identities across various platforms.",
    "ensure data quality in mparticle": "Use the 'Data Master' tool in mParticle to monitor and enforce data quality standards.",
    "create journeys in zeotap": "Within Zeotap's 'Orchestrate' module, design personalized workflows to engage users based on their behavior and attributes.",
    "protect user data in zeotap": "Utilize the 'Protect' features in Zeotap to manage user consent and comply with data protection regulations.",

}

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("question", "").strip().lower()  # Normalize input
        
        # Find the best matching response
        for keyword, response in responses.items():
            if keyword in user_input:  # Check if any keyword is present in the input
                return jsonify({"answer": response})

        return jsonify({"answer": "I'm not sure I understand. Can you rephrase?"})
    
    except Exception as e:
        return jsonify({"answer": "An error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
