Welcome to my cloud-resume-challenge!

I'm Ignacio and i have made this "famous" cloud-resume-challenge (https://cloudresumechallenge.dev/) to get some hands-on experience with AWS and public cloud in general. 

I installed AWS CLI and started building my application using a CloudFormation template from the beginning to benefit from Infrastructure as Code

Front-End

- I then started to create my application by creating an S3 bucket configured as static Website
- For the HTTPS, I used a cloudfront distribution to which i attached a SSL certificate from ACM manager
- DNS: I purchased a custom domain https://ignaciolarranaga and created a hosted zone. 
- I added a Javascript that would contain the call to the lambda functions. 
- HTML & CSS: I used a template from the internet, because my focus was more on the architecture.
 
Back-end

- Created a DynamoDB table to store the number of visitors with an atomic counter 
- API gateway using Python: a get-function to retrieve the number of visitors and a put-function to update the dynamo-db database.
- I uploaded my project to Github and implemented CI|CD using Github Actions

Finally, on 27th october, I got my AWS Cloud Practitioner Certification. I chose to do it at the end so i would feel more confident facing the exam after having some hands-on experience. 
