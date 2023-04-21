const request = require('supertest');
const app = require('./index');

describe('AI Bot endpoint', () => {
  it('responds with a 200 status code', async () => {
    const res = await request(app).get('/ai-bot');
    expect(res.status).toBe(200);
  });

  it('responds with a message from the AI bot', async () => {
    const res = await request(app).get('/ai-bot?query=hello');
    expect(res.body.message).toBeTruthy();
  });

  it('responds with an error message if no query is provided', async () => {
    const res = await request(app).get('/ai-bot');
    expect(res.body.error).toBeTruthy();
  });
});
