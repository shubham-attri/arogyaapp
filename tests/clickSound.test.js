test('audio plays on span click', () => {
  const span = document.createElement('span');
  document.body.appendChild(span);

  const audio = new Audio('public/assets/clicksound.mp3');
  span.addEventListener('click', () => audio.play());

  // Simulate a click on the span element
  span.click();

  // Check if audio is playing
  expect(audio.paused).toBe(false);
});
