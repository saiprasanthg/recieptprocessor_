






1️⃣ Build the Docker Image

docker build -t receiptprocessor .

2️⃣ Run the Container

docker run --name receiptprocessor-container -d -p 8080:8080 receiptprocessor

3️⃣ Stop the Running Container

docker stop receiptprocessor-container

4️⃣ Remove the Container

docker rm receiptprocessor-container
