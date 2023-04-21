const express = require('express');
const app = express();

// AI bot related code here
const { PythonShell } = require('python-shell');
const express = require('express');
const router = express.Router();

router.post('/ai-bot', (req, res) => {
  // Get the user input from the request body
  const userInput = req.body.userInput;

  // Set up the options for the Python script
  const options = {
    scriptPath: path.join(__dirname, 'ai-bot'),
    args: [userInput]
  };

  // Run the Python script
  PythonShell.run('ai_bot.py', options, (err, result) => {
    if (err) {
      // Handle the error
      console.error(err);
      res.status(500).send('An error occurred');
    } else {
      // Send the result back to the client
      res.send(result);
    }
  });
});

module.exports = router;

// const userInput = // Get the user input
const response = await fetch('/ai-bot', {
  method: 'POST',
  body: JSON.stringify({ userInput }),
  headers: {
    'Content-Type': 'application/json'
  }
});

const result = await response.text();
// Do something with the result


module.exports = app;
