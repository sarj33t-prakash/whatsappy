# WhatsApp Twilio Bot

There are few tech behind the scene when I posted the YouTube Link. Here’s a bit descriptive text to give an overall idea what actually have I done so far and how them things goes on:

Programming Language: Python3
I have coded a bot in pure Python language which accepts an input from end-user based on the query asked. Now there are few prefixes I have considered to differentiate between the end-user input queries.

For an instance, if you want to ask this bot an image response (using openAi Image Creation), you’re suppose to send him command in the below syntax:

!aimg YOUR QUERY - to lookup for an Image using using OpenAi Image Creation tool (needs an API Key)

!ask YOUR QUERY - Ask a normal chat-flow query to ChatGPT (basically returns text based conversation outputs, includes links to webpages, images, blogs, so on)

WhatsApp API : Twilio

Repository Hosted: Github (Dockerfile setup is need to build Docker Image - CI/CD) 

Application Deployment: Docker Container using back4app (I used to prefer *Heroku* but since it is now Paid Service, you need to link a credit card/ Payment method in your Account for purchasing Eco dynos)

WhatsApp WebApp (Bot) is up & serving: https://whatsapp-sarj33t.b4a.run

I luv to Python ! 🙏 
