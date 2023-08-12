# IndustrySafe: Industry Safety Monitoring Using AI

### What is the need for Industry Safety Monitoring/Detection Using AI?

- Industrial Accidents and Deaths have been recorded in 1000s in India and the US due to negligence regarding wearing of Safety Equipment while working in factories and construction sites etc. 
- These accidents can be overcome or prevented by using the appropriate safety gear during working.
- But we need some kind of monitoring to check whether the workers are wearing the appropriate geat or not.

### How can Industry Safety Monitoring be achieved?

- One way is continuous monitoring of the CCTV footage of workers and working area by a person, but there are drawbacks of this method such as fatigue and requirement of intermittent breaks for the person monitoring the footage.
- Another way is by implementing AI solutions, ie scanning the footage in realtime using AI and triggering alerts if the required safety protocols are breached.
- We shall be building such a basic solution using AI to detect whether the person is wearing the required safety equipment.
- While building our solution, we shall be using the YoloV7 Object Detection algorithm and will use MAP as the metric to detect the model performance.
- The objects that will will use to detect are: HELMETS, GOGGLES, SAFETY JACKET, HAND GLOVES, SAFETY SHOES.
- These AI based monitoring systems can be installed for detection before the worker enters the work site or the factories thus ensuring the worker safety and avoiding or reducing any safety lapses or hazards.

### How will we implement Industry Safety monitoring project?

- In our project, we have 150 images which consist of the objects to be detected namely: HELMETS, GOGGLES, SAFETY JACKET, HAND GLOVES, SAFETY SHOES.
- We will be labelling the above objects in the images using a tool called labelImg, we shall configure the tool settings to the object detection algorithm that we will be using.
- The algorithm that we will be using to detect the objects is YOLOV7, it has its own advantages and disadvantages.
- We shall train the model using GOOGLE COLAB because of its GPU capabilities, then we will create a WEB APP which can be run locally.
- We shall then create a DOCKER IMAGE(using Docker) of this app so that it can be run anywhere, this image will then be deployed using the AMAZON EC2 INSTANCE.

### STEPS INVOLVED IN THE PROJECT:

1. Data Ingestion
   ![Data Ingetions](https://github.com/therealabhishek/IndustrySafetyDetection_YoloV7_WebApp_Deployment/assets/18556069/93627efb-0594-4ad8-86f2-b071b8e581e0)
In the data ingestion stage, we shall import the data stored in the Amazon S3 bucket by making the required connection.

Here, we shall create the data ingestion config and the data ingestion artifacts which are the settings for importing the data and what will be the output of the data ingestion stage respectively.

Under the artifacts directory, the original zip files of the data will be imported from the S3 bucket into 'data ingestion' directory, the contents of the S3 bucket will then be extracted into the 'featurestore' directory.

3. Data Validation
   ![Data validation](https://github.com/therealabhishek/IndustrySafetyDetection_YoloV7_WebApp_Deployment/assets/18556069/3b418b3c-8eb4-43b6-9e65-f148e6d27de9)
In the data validation stage, we shall check if the required files and folders are available in the 'featurestore' directory. The validation status will be stored in 'status.txt' file in a boolean format.

5. Model Trainer
   ![Model trainer](https://github.com/therealabhishek/IndustrySafetyDetection_YoloV7_WebApp_Deployment/assets/18556069/8b569f1f-c873-48a4-9e1c-e235669bf6ba)
Based on the validation status True/False we shall proceed to either training or not training the model respectively in the Model Trainer stage.

7. Model Pusher
   ![Model Pusher](https://github.com/therealabhishek/IndustrySafetyDetection_YoloV7_WebApp_Deployment/assets/18556069/f86caa95-68c5-48a5-adbc-adf3b2d363d0)
In Model Pusher stage, we shall save the model created in the Model Trainer stage to an S3 bucket.

8. Model Deployment
   ![deployment](https://github.com/therealabhishek/IndustrySafetyDetection_YoloV7_WebApp_Deployment/assets/18556069/ae9cbdce-6f9b-435e-b0b9-a0c5e284e62a)
In the Deployment stage, we shall create a Docker image of the local project and deploy it using the AWS EC2 instance.


