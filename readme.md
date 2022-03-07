<h1 align="center">Data Engineering final project</h1>

<div align="center">
   <strong> Dockerized web interface for toxicity analysis </strong>
</div>
<div align="center">
  Final Project of a group of 2 persons at EFREI Paris for the Data Engineering course.
</div>

<br />

<div align="center">
  <!-- Maintenance -->
    <img src="https://img.shields.io/maintenance/yes/2021?style=for-the-badge"
      alt="Maintenance" />
  <!-- Last Commit -->
  <a href="https://github.com/Duramann/Data_engineering_final_project/commit/release">
    <img src="https://img.shields.io/github/last-commit/Duramann/Data_engineering_final_project?style=for-the-badge"
      alt="Last Commit" />
  </a>
  <!-- Activity -->
  <a href="https://github.com/Duramann/Data_engineering_final_project/graphs/commit-activity">
    <img src="https://img.shields.io/github/commit-activity/w/Duramann/Data_engineering_final_project?style=for-the-badge"
      alt="Activity" />
  </a>
  <!-- PR -->
  <!--  <img src="https://img.shields.io/github/status/contexts/pulls/Duramann/Data_engineering_project/0?style=for-the-badge"-->
  <!--    alt="pulls" />-->
  <!-- Size -->
    <img src="https://img.shields.io/github/repo-size/Duramann/Data_engineering_final_project?style=for-the-badge"
      alt="size" />
</div>

<br />

### Project organization : <br />

<pre><code class="language-nohighlight">
├── README.md               &lt;- The top-level README for developers using this project. 
│
├── static                  &lt;- The folder containing the css files.
│      └── css       
│ 
├── templates               &lt;- The folder containing the html files.
│
├── docker-compose.yaml     &lt;- The docker compose properties to define the multi-container docker application. <strong> The port used is "5000" </strong>
│
├── Dockerfile.dockerfile   &lt;- The docker image for the application.
│
├── requirements.txt        &lt;- The requirements for the Docker image 
│
├── flask_app              &lt;- The folder with the app, its requirement, Dockerfile and the script for testing
│
├── JenkinsFile         &lt;- The file to configure the steps for our jenkins pipeline
│
└── Prometheus.yml & Rules.yml         &lt;- The two configuration file for monitoring.
</code></pre><br />

On Github, several branches were created during the project and were deleted when merged.

* __web_app__ : to design the html and css and render a first web application.
* __dockerization__ : to build the web app with docker.
* __testing__ : to do the testing parts.
* __monitoring__ : to monitor the application with prometheus and grafana.
* __automation__ : to automatically build and release the app with jenkins.
* __release__ : the final code.


### Demonstration : 

<p> To start the application, run <strong>docker-compose up</strong> at the root of the projet. The application is now running at <em>localhost:5000</em>

### Performed tests :

Here are the test that we performed in test_web_app.py : 

* Is the application working for "/" route and "/predict" post route.
* Is the get route for "/predict" redirecting corretly.
* Is the application rendering the correct html page.
* Several sentence were tested to see if the prediction was correct.
* Stress testing of the home page and the prediction page to see if they can handle 100 request a second.
* end-to-end testing to see if we can submit a prediction and hit predict.

### Monitoring :

Prometheus and Grafana were used to monitor our application.

We created a dashboard on Grafana (localhost:3000) with those insights:

* Disk Usage.
* Memory Usage.
* CPU Usage.
* Number of visit of the home page.
* Number of prediction made.
* Average prediction time.

### Project Management : <br />

A Trello was created to coordinate the tasks between the team members.

<div align="center">
  
  <a href="https://trello.com/b/X5G8QLou/data-engineering-project"><img width="300px" src="https://logos-world.net/wp-content/uploads/2021/02/Trello-Logo.png"/></a>
</div>

<div align="center">
<strong> Languages and Tools: </strong>
</div>
<br />
<div align="center">
<img align="center" width="60px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" />
<img align="center" width="60px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"/>
<img align="center" width="60px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/>
<img align="center" width="60px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" />
</div>

<br />


<div align="center">
  <sub>Project made by
  <a href="https://github.com/Duramann">Théo Dura</a>,
  <a href="https://github.com/plao1996">Philippe Lao</a>,
  </a>
</div>

