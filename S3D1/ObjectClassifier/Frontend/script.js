// Get video element from HTML
const webcamFeed = document.getElementById('webcam-feed');

// Check if user's browser supports getUserMedia
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Access the webcam
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            // Set the video stream as the source for the webcam feed
            webcamFeed.srcObject = stream;
        })
        .catch(error => {
            console.error('Error accessing webcam:', error);
        });
} else {
    console.error('getUserMedia is not supported by your browser');
}

// Load the pre-trained model
let model;
(async function () {
    model = await tf.loadLayersModel('path_to_your_exported_model/model.json');
    console.log('Model loaded');
})();

// ...

// Capture an image from the webcam and classify it
async function classifyImage() {
    const imageCapture = new ImageCapture(webcamFeed.srcObject.getVideoTracks()[0]);
    const imageBitmap = await imageCapture.grabFrame();
    
    // Preprocess the image (resize and normalize pixel values)
    const resizedImage = tf.image.resizeBilinear(tf.browser.fromPixels(imageBitmap), [224, 224]).toFloat();
    const normalizedImage = resizedImage.div(tf.scalar(255));
    const batchedImage = normalizedImage.expandDims(0);

    // Make predictions with the model
    const predictions = await model.predict(batchedImage).data();

    // Get the class label with the highest prediction score
    const topPrediction = Array.from(predictions).indexOf(Math.max(...predictions));
    
    // Display the result
    displayResult(topPrediction);
}

// ...

// Call the classifyImage function when the user clicks a button or at a regular interval
// For example, you can call it when the user clicks a "Classify" button
classifyButton.addEventListener('click', classifyImage);

function displayResult(predictionIndex) {
    const resultText = document.getElementById('result-text');
    
    // You can define an array of labels corresponding to the classes your model can classify
    const labels = ['Bottel', 'Cup', 'Label 3', /* ... */];
    
    // Update the result text
    resultText.textContent = `Classified as: ${labels[predictionIndex]}`;
}
