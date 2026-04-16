Title: Signal Snapshot - Generating visualizations of Signal Messenger data
Date: 2025-02-16
Category: Analytics
Author: Andrew Stewart
Summary: Exploring the use of computer audition and machine learning to detect faults in engines simply using the sound they produce.
Tags: Python, Machine Learning

# Question
Spotify Wrapped, and other similar products, are so fun for their audience because it provides *personalized* insights into something is used every day, but rarely analyzed. Chats, like music, are something we all interact with daily, which results in a ton of interesting data. But that data often isn't used for anything. It would be cool to build some analytics on top of someone's SIgnal conversations.

**Question**: How could an easy-to-use and shareable analytics tool be built for Signal users?

# Methodology
For those unfamiliar, Signal is a messenger app, similar to WhatsApp, but heavily focused on privacy with their end-to-end encryption.

I intiially started this project with the intention to build a bespoke, locally run dashboard that used my Signal Desktop database. I built a prototype of this in December 2024, which was a 100% Python app using the Dash/Plotly libraries to handle the data visualizations and Flask to serve it all up. 

It was rough, but it worked. I was able to fetch data from my local Signal database and create a few basic charts and KPIs. Things like: "Who sent the most messages in this conversation" and "what was every member's favorite emoji". Silly stuff to show the rest of the Signal peeps.

To share it with the others in my Signal conversations, I used a hosting service to serve up my Python app. I think I used Heroku? In any case, I used a free version of their hosting offerings which allowed me to share the app via the web.

All of this worked fine, but it wasn't scalable *at all*. And the farther I got into, the more I realized that other Signal users might like to build dashboards of their own.

So a few months later, I decided to turn this Python app into a legitimate single-page web app that would allow any Signal user to generate an analytics dashboard on their data. I have very little FE web experience, so I relied *heavily* on LLMs to build the foundations of the React app.


So here's what I have so far: signalsnapshot.com

It's still pretty raw, but maybe some of you will find it fun.

Important things to note:

    This only supports Signal Desktop at the moment

    In order to use the tool, you need to first decrypt your Signal database. I also wrote a program to handle that, and the app has the necessary documentation on how to use it

    The app is purely client-side, meaning that your uploaded data never leaves your browser. There is no server, this is a static web page. Nobody but you can see your data.

If you're a Signal user and interested in this stuff, check it out! If there's enough demand, I'll build out the analytics a little more, and maybe add support for Signal Android. There’s a ton of meat left on this bone, chat analytics is a cool world.

Here's the GitHub if you want to check out the code. https://github.com/ahstewart/signal-snapshot
### Background
### The Project
# Results
# Takeaways
# Looking Forward
# Resources
