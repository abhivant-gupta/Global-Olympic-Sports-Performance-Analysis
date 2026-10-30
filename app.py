from flask import Flask, render_template

app = Flask(__name__)

# Replace these URLs/viz_names with your actual Tableau Server or Tableau Public details
TABLEAU_SERVER_URL = "https://public.tableau.com"
DASHBOARD_SITE_ROOT = "smartbridge_17931188449870"
DASHBOARD_VIZ_NAME = "OlympicDashboard"
STORY_VIZ_NAME = "Story1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template(
        'dashboard.html',
        tableau_url=TABLEAU_SERVER_URL,
        site_root=DASHBOARD_SITE_ROOT,
        viz_name=DASHBOARD_VIZ_NAME,
        title="Olympic Dashboard"
    )

@app.route('/story')
def story():
    return render_template(
        'story.html',
        tableau_url=TABLEAU_SERVER_URL,
        site_root=DASHBOARD_SITE_ROOT,
        viz_name=STORY_VIZ_NAME,
        title="Olympic Story"
    )

if __name__ == '__main__':
    app.run(debug=True)
