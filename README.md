# Multi-agents architecture to produce newsletters and summaries on topics
This project is a project to learn how to create and managed agents using AI and how to orchestrate them. The summary provides the sources.

## Architecture
The architecture is quite simple : 
- A searcher to seek sources and elements according to keywords given by the user or inside the file `topics.yaml`
- An analyst to keep the better elements inside the results given by the searcher
- A writer to write the summary
- A critic to rewriter and express the sentences properly

## How to use it
### API key
After `git clone` the repository, you will need to create an API key from Anthropic. To make that, you must create an account on Claude and generate an API key (inside the settings).
You muste keep the key because you will lose the access whenever you will quit the webpage. You can create inside the project a `.env` file and put the key as it is in the `.env.example` file.
It is possible to take open source agents but you have to change the code part related to anthropic.
### Requirements
You have to have anthropic, ddgs, dotenv and pyyaml to execute the program.
### How to launch it
Two ways to use it :
`python main.py --topic key words search 2025` inside the console.
Here you search for your own topic. Avoid the link words like 'of', 'the' or 'or' and keep just the key words to have the best results.
You can add --output to name your produced markdown file.
`python main.py --topic key words search 2025 --output mynewsletter.md`

Edit the yaml file or choose a topic inside the yaml file and :
`python main.py --from-yaml drones` To have the summary about drones in 2025.

## How to improve it
You can connect this with an API to send the summary by mail and you can automatize the code process by coding a cron job or using n8n (or airflow).
