#!/usr/bin/node

const req = require('request');

const apiUrl = process.argv[2];

req(apiUrl, (err, res, msg) => {
  if (err) {
    console.error(err);
    return;
  }
  if (res.statusCode !== 200) {
    console.error(`Failed to fetch data: Status ${res.statusCode}`);
    return;
  }
  const todos = JSON.parse(msg);
  const completedTasksByUser = {};
  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });
  console.log(completedTasksByUser);
});
