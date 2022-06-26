from ezprez.core import *
from ezprez.components import *

# CI/CD Pipelines
Slide("What is Continuous Integration/Continuous Deployment?", "Essentially it is a method for defining automated virtual computing processes. In laymens terms it typically means writing a configuration file or script that will spin up a 'virtual computer' (though sometimes it will run on the host computer) and run through a series of defined tasks.",background="gray")
Slide("What is CI/CD Used for?", "Any task that you might want a 'virtual computer' to run it on for example", ["Testing", "Building a distribution", "Automated updating", "etc."], background="gray")


Slide("Strategy for making a pipeline", "Imagine you have someone you are training to do the task. They have a brand new laptop and you need to help them get setup and do the task", background="gray")
Slide("An example", "Last week we looked at using hugo with the ignite site, what are the steps needed to build the ignite site if you were given a brand new laptop?", background="gray")
Slide("An example", "First we need to clone the site so we have the files, next we need to install hugo, then we need to build them (hugo -d), and finally we need to take the files and put them somewhere other people can access them", background="gray")

# Github Actions
Slide("Github Actions", background="black")

## Triggers
Slide("Triggers", background="black") # On-dispatch, on-push, cron, on-event (release etc.) etc. include examples like ignite site or sws or ezcv themes

## Jobs
Slide("Jobs", "Each job is essentially a set of steps with some associated state",background="black") # On-dispatch, on-push, cron etc.

### Job Steps
Slide("Steps","This is where actual commands are run. Note that state is typically persistant across steps in the same job.", background="black") # Each bullet point is a task that runs steps defined, or runs action defined


## TODO: Add note that multiple pipelines can run off single action i.e. build site, gh pages pipeline deploys


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
