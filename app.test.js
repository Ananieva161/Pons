const request = require('supertest');
const app = require('./app');

describe('Express Server', () => {
  it('should respond with "Hello, World!" on the root route', async () => {
    const response = await request(app).get('/');
    expect(response.status).toBe(200);
    expect(response.text).toBe('Hello, World!');
  });
});
