const request = require('supertest');
const app = require('../index.js');

describe('GET /', function() {
  it('responds with 200 OK', function(done) {
    request(app)
      .get('/')
      .expect(200, done);
  });
});
