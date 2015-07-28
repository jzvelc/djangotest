var server = require('http').createServer(handler);
var io = require('socket.io')(server);
var redis = require('redis');
var q = require('q');
var winston = require('winston');
var fs = require('fs');

function handler (req, res) {
  fs.readFile(__dirname + '/index.html',
  function (err, data) {
    if (err) {
      res.writeHead(500);
      return res.end('Error loading index.html');
    }
    res.writeHead(200);
    res.end(data);
  });
}

var logger = new (winston.Logger)({
  transports: [
    new (winston.transports.Console)({colorize: 'true', level: 'debug'}),
  ]
});


var deferred = q.defer();
var client = redis.createClient(
  '6379',
  '192.0.0.123'
);

var rclient = redis.createClient(
  '6379',
  '192.0.0.123'
);

var deferrers = [q.defer(), q.defer()];
var promises = [deferrers[0].promise, deferrers[1].promise];

rclient.select(5, function (err, res) {
  if (err) {
    deferrers[0].reject(err);
  } else {
    deferrers[0].resolve(res);
  }
});

client.select(5, function (err, res) {
  if (err) {
    deferrers[1].reject(err);
  } else {
    deferrers[1].resolve(res);
  }
});

q.all(promises).then(function () {
  client.psubscribe('ps:*');

  client.on('pmessage', function (pattern, channel, message) {
    logger.debug(channel + ' -> ' + message);
    io.sockets.emit(channel, message);
  });

  io.on('connection', function (socket) {
    socket.join('ps:public');

    socket.on('disconnect', function () {
      socket.disconnect();
    });
  });

  server.listen(8001, function () {
    console.log('Listening on port 8001 ...');
  });
});

