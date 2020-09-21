# Easysize - Takehome Task

Hello,

this doc will guide you through the code written to complete the takehome task that was part of the interview process. Follow the steps, and you should be up and running in no time! :)


## Getting Started

By reading this doc, you will have most likely unzipped the package containing all the source code etc. In this case, a git step is not neccessary.

What is neccessary however, is Docker. Be sure that Docker installed and running by using:

    $ docker version

If you haven't installed it, head on over to: https://www.docker.com/get-started. Once installed, make sure you run the docker deamon (insalled as a application on your system, see guide). Once running, you should be able to get the app (emulating an API for real-time prediction), using:

    $ docker-compose up

This might take a little bit (as we need to build the image). Once built and up and running, you should start seeing "web_1   |" logging output in your console. That means the app is running! 

Open up a browser and put in the link directing you to the developement server (should be http://0.0.0.0:8000/). 

## Now what?

By going on the homepage you should notice the modest amount of endpoints. To navigate to any of them, use the built in docs provided by the rest framework.

You should notice that you will be getting 403s if you try to reach any endpoint. This is due to you not being logged in yet. To log in, just click the log in button (top right) of the base url homepage and use:

    username: admin
    password: admin

Now try navigating to the same endpoints you tried before. You should now be able send requests using the built in client. 

## Real-time API endpoint for regression model

To check out the realtime prediction, end on over to <code>/predictions</code>. Using the client, you can feed in your choice of inputs into the model (2 floats, 1 categorical /w lowercase english letters).

Please do try to be cheeky and put in something "unexpected" in the output. :)

On successful request (status_201), you will get back the generated output with the rest of the model that is the object representing the prediction.

## Disclaimers

Note that this is only a demo product and as such it is lacking a couple of things. Some things that immidetely spring to mind are:

1. Security. This is a demo app and should never be used in production. An example of how this manifests, is the whitelisting of all hosts (see <code>settings.py</code>). This should never be the case for any production app.

2. While saving a prediction is valuable as it is vital to evaluate model performance historically or catch data/model degredation, forcing a request to make a roundtrip from the DB is unnessecary (and would likely lead to latency issues in a real-system). A better solution would be to seperate the serving of the prediction and the save of the data model representing the prediction. A way of doing this would be to use a worker to handle the saving of the model (e.g. Celery or something similar).

3. Tests need to be expanded to cover the breath of the app. Right now they are only dealing the very core of the prediction (at a model level). True tests would be much more all-encompassing.

There's plenty more to be said about extension and productionizing a system like this. I'd gladly answer any questions and discuss the solution with you. I'd also love to hear about roughly what is already in place and what your planned next steps are! :)

Best regards,

Erik

