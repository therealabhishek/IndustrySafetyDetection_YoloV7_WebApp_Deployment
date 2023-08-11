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