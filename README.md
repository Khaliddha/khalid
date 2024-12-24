# Project Name

Weather Web Application 

# Project Structure

my_project/

├── app.py              # Main application file (Flask)

├── templates/          # HTML files

│   ├── index.html      # Main landing page

│   ├── weather.html    # Weather information page

├── requirements.txt    # Python dependencies

├── Dockerfile          # Containerization instructions

├── Vagrantfile         # Configuration for two virtual machines

├── deploy.yml          # Ansible playbook for deployment

# Prerequisites

- Python 3.9+

- Docker and Docker Hub account

- Jenkins (with Git, Docker, and Ansible plugins installed)

- Ansible

- Vagrant and VirtualBox

- GitHub account

# Steps to Deploy

# 1. Clone the Repository

Clone this repository to your local machine:

```
it clone https://github.com/yourusername/your-repo.git
cd your-repo
``` 

# 2. Test the Application Locally

Run the Flask app locally to ensure it works:

```
pip install -r requirements.txt
python app.py
```

# 3. Build and Test Docker Container

Build and run the Docker container locally:

```
docker build -t your-app-image-name .
docker run -d -p 5000:5000 your-app-image-name
```
Visit http://localhost:5000 to test the containerized application.

# 4. Push Code to GitHub

Push all project files to a private GitHub repository:

```
git add .
git commit -m "Initial commit"
git push origin main
```

# 5. Set Up Jenkins Pipeline

1. Create a Jenkins pipeline job.

2. Use the provided Jenkinsfile script to automate the build and deployment process.

# 6. Deploy Using Ansible

Run the deploy.yml playbook to install Docker, pull the image, and run the application on the Vagrant machines:

```
ansible-playbook deploy.yml
```

# 7. Access the Application

Visit the application on both Vagrant machines at:

- http://<machine1-ip>:5000

- http://<machine2-ip>:5000

# Expected Outputs

1. Two Accessible Web Pages:

- index.html: Landing page available at /.

- weather.html: Weather page available at /weather.

2. Automated CI/CD Pipeline:

- Jenkins automates code fetching, Docker image building, pushing, and deployment.


