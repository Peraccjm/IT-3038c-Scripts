const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

const server = http.createServer((req, res) => {
    if (req.url === "/") {
        fs.readFile("./index.html", "UTF-8", (err, body) => {
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
      });
    } else if(req.url.match("/sysinfo")) {
      myHostName=os.hostname();
      const totalMem = os.totalmem() / 1000000
      const freeMem = os.freemem() / 1000000
      const upTime = process.uptime()
      const CPUs = os.cpus().length
      html=`
      <!DOCTYPE html>
      <html>
        <head>
          <title>Node JS Response</title>
        </head>
        <body>
          <p>Hostname: ${myHostName}</p>
          <p>IP: ${ip.address()}</p>
          <p>Server Uptime: ${upTime} </p>
          <p>Total Memory: ${totalMem} </p>
          <p>Free Memory: ${freeMem} </p>
          <p>Number of CPUs: ${CPUs} </p>
        </body>
      </html>`
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(html);
    } else {
      res.writeHead(404, {"Content-Type": "text/plain"});
      res.end(`404 File Not Found at ${req.url}`);
    }
  }).listen(3000);
  
  console.log("Server listening on port 3000");