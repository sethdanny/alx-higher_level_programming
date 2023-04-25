#!/usr/bin/node
/* script to read files */

const fs = require('fs');

fs.readFile(process.argv[2], 'uft8', (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
