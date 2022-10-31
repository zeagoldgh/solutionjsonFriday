# Job notifier 

# To notify you when there is a new job

1. Setup Fast api

Setup fastapi to return jobs with id, title and description
"/job" a list of jobs
"/job/:id" "single job matching the id
2. Upload Fast api to ec2

Upload your code to an ec2 instance and try to configure it that you can access the api from the internet (If you start the server on port 80 you may need sudo permissons)
Upload the source code to an s3 bucket and write a script that you can use as userdata to download the code and start your fast api
3. Add a Loadbalancer

Create a Terraform project to setup your ec2 instance with your fastapi
add a load balancer to your infrastructure
4. Add a Autoscaling

add autoscaling to your infrastructure that everytime an instance crash a new instance will start
5. CI CD

Add a pipeline that deploys your terraform infrastructure
Add a pipeline that uploads packs your source code and update the s3 package.
create a script that updates you instances by remove old instances
6. Load Job Data

Create a script that call the api arbeit now and save every job item as a single json file with id,title,description in a s3 bucket. Use the slug as id and id.json as filename.
Update your api to load job data from the s3 bucket and return it