// Require the necessary modules
const express = require('express');
const path = require('path');

// Create a new Express application
const app = express();

// Define the path to the static files
const staticPath = path.join(__dirname, 'public');

// Set the static file directory
app.use(express.static(staticPath));

// Define the port number
const port = 3000;

// Start the server
app.listen(port, () => {
  console.log(`Server is listening on port ${port}...`);
});


// for html to play sound when event is triggered
function playClickSound() {
  var audio = new Audio('public/assets/clicksound.mp3');
  audio.play();
}

