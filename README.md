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
![Alt text](<Data Ingetions.png>)
2. Data Validation
3. Model Trainer
4. Model Pusher