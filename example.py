from ezprez.core import *
from ezprez.components import *

# CI/CD Pipelines
Slide("What is Continuous Integration/Continuous Deployment?", "Essentially it is a method for defining automated virtual computing processes. In laymens terms it typically means writing a configuration file or script that will spin up a 'virtual computer' (though sometimes it will run on the host computer) and run through a series of defined tasks.",background="gray")
Slide("What is CI/CD Used for?", "Any task that you might want a 'virtual computer' to run it on for example", ["Testing", "Building a distribution", "Automated updating", "etc."], background="gray")

## Definitions
Slide("Pipeline/Workflow vs jobs/steps", " A pipeline/workflow is the full definition of the task (can mean the file or the actions). Jobs/steps are the individual actions or group of actions that make up a pipeline/workflow", background="gray")
Slide("Environment", "The environment the pipeline/workflow runs in including the operating system, any configuration variables, and any included binaries/languages", background="gray")

## CI/CD Example
Slide("Strategy for making a pipeline", "Imagine you have someone you are training to do the task. They have a brand new laptop and you need to help them get setup and do the task", background="gray")
Slide("An example", "Last week we looked at using hugo with the ignite site, what are the steps needed to build the ignite site if you were given a brand new laptop?", background="gray")
Slide("Overview of steps for the example", "First we need to clone the site so we have the files, next we need to install hugo, then we need to build them (hugo -d), and finally we need to take the files and put them somewhere other people can access them", background="gray")
### Steps
Slide("Step 1: Clone the site so we have the files", "First we need to clone the site down, this means we will need some sort of OS and git along with a URL to clone the files down. So once we have an os we need to run:", Code("bash", "git clone https://github.com/Schulich-Ignite/website"), background="gray")
Slide("Step 2: We need to install hugo", "This means either installing go and installing hugo that way, or downloading a binary", background="gray")
Slide("Step 3: Build the files", "Need to run the hugo command over the files we downloaded", Code("bash", "hugo -d"), background="gray")
Slide("Step 4: Deploy the files", "Find a way to deploy those files so other people can access them (will cover this in detail tomorrow)", background="gray")

## Example systems
jenkins_example = """pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello world!' 
            }
        }
    }
}"""
Slide("Some example systems", background="gray")
Slide("Jenkins", "Example jenkinsfile (printing Hello world! at cli)", Code("jenkins", jenkins_example ), Link("Site", "https://www.jenkins.io/", color="#ff0000"), background="gray")

ansible_example ="""---
- name: This is a hello-world example
  hosts: ansibleclient01.local
  tasks:
    - name: Create a file called '/tmp/testfile.txt' with the content 'hello world'.
      copy:
        content: hello worldn
        dest: /tmp/testfile.txt"""
Slide("Ansible", Code("ansible", ansible_example),Link("Site", "https://www.ansible.com/", color="#ff0000"), background="gray")

gitlab_example ="""build-job:
  stage: build
  script:
    - echo \"Hello World!\"
"""

Slide("Gitlab CI/CD", Code("gitlab", gitlab_example),Link("Site", "https://docs.gitlab.com/ee/ci/", color="#ffff00"), background="gray")

### Extra examples
Slide("Travis CI", Link("Site", "https://www.travis-ci.com/", color="#0000ff"), background="gray")
Slide("Azure", Link("Site", "https://azure.microsoft.com/en-us/services/devops/pipelines/",color="#0000ff"), background="gray")

## More definitions
Slide("CI/CD is not always remote", "Some CI/CD processes are run locally on people's devices like local testing pipelines (some people say this isn't ci/cd some say it is)", background="gray")
Slide("CI/CD vs PaaS (platforms as a service)", "PaaS services like heroku are designed to be a one-stop shop for setting up a project, they tend to be more efficient but they are by design less flexible than standard CI/CD systems", Link("Heroku", "https://www.heroku.com/", color="#79589F"), background="gray")
Slide("CI/CD vs containers", "Containers are essentially a way to run code inside a 'mini computer' inside a computer. Some CI/CD systems use containers, but containers are not themselves CI/CD systems necessarily", Link("Docker", "https://www.docker.com/", color="#2496ed"), background="gray")

# Github Actions
Slide("Github Actions", "Github actions is a remote CI/CD system that is integrated with github directly", background="black")
Slide("Github Actions Files are YML/YAML", "Github actions files are written in YAML/YML", Link("YAML Syntax","https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html#yaml-basics"), background="black")

presentation_pipeline="""name: GH build for ezprez

on:
  push:
    branches:
      - master
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repo
      uses: actions/checkout@v2
    - name: Setup Python
      uses: actions/setup-python@v2
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install --upgrade setuptools wheel
        python -m pip install ezprez
    - name: build html files
      run: |
        mkdir ~/Downloads
        python example.py
        mv Presentation/* .
        rm -rf Presentation
    - name: Deploy Docs
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: .
"""

Slide("For example this presentation has a pipeline", Code("yaml", presentation_pipeline), background="black")

Slide("Github Actions File structure", "They go in a folder in your repository called /.github/workflows (you can have multiple pipelines)", background="black")

## Triggers
Slide("Triggers", "This configuration determines when an action pipeline runs. Note that multiple pipelines can be run off a single trigger, and pipelines finishing can trigger other pipelines to start", background="black") # On-dispatch, on-push, cron, on-event (release etc.) etc. include examples like ignite site or sws or ezcv themes

## Jobs
Slide("Jobs", "Each job is essentially a set of steps with some associated state",background="black") # On-dispatch, on-push, cron etc.

### Job Steps
Slide("Steps","This is where actual commands are run. Note that state is typically persistant across steps in the same job.", background="black") # Each bullet point is a task that runs steps defined, or runs action defined


Slide("Using pre-built actions", background="black")

### Environment definitions
Slide("Environment definitions", "The information used to configure all steps in a job", background="black") 
Slide("Strategy", "matrix",background="black")  # TODO: Strategy with matrix of options to run on https://github.com/Descent098/sws/blob/master/.github/workflows/test-suite.yml#L11-L13
Slide("Using with", "with can be used to define settings for each step in a job. There are some standard one's we will cover but keep in mind custom actions often have custom settings you can use alongside the with section",background="black") 
Slide("With options: token", "Tokens are used to authenticate an action and are what allows the action access to make changes or even just access content that is locked behind a password",background="black")  
Slide("With options: artifacts", background="black")  



# Github Pages
Slide("Github Pages", background="black-blue")

# Setup the presentation
presentation_title = "CI/CD Basics"
presentation_description = "The basics of CI/CD pipelines, github actions and github pages"
presentation_url = "https://kieranwood.ca/ci-cd-basics/"
prez = Presentation(presentation_title, presentation_description, presentation_url, background="gray")

# Export the files to the current directory at /Presentation, do not change this if you want to use the auto-deployment
prez.export(".", force=True, folder_name="Presentation")
