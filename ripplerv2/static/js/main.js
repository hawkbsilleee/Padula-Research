
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  }

var texts = new Array();
texts.push(getRandomInt(10))
texts.push(" ");
texts.push(getRandomInt(10))
texts.push(" ");
texts.push(getRandomInt(10))
texts.push(" ");
texts.push(getRandomInt(10))
texts.push(" ");
texts.push(getRandomInt(10))
texts.push(" ");
texts.push(getRandomInt(10))
texts.push(" ");


var point = 0;

function changeText(){
  $('p').html(texts[point]);
  if(point < ( texts.length - 1 ) ){
    point++;
  }else{
    point = 0;
  }
  
}
 
setInterval(changeText, 1000); 
changeText();



// /**
//  * Self-adjusting interval to account for drifting
//  * 
//  * @param {function} workFunc  Callback containing the work to be done
//  *                             for each interval
//  * @param {int}      interval  Interval speed (in milliseconds)
//  * @param {function} errorFunc (Optional) Callback to run if the drift
//  *                             exceeds interval
//  */
// function AdjustingInterval(workFunc, interval, errorFunc) {
//   var that = this;
//   var expected, timeout;
//   this.interval = interval;

//   this.start = function() {
//       expected = Date.now() + this.interval;
//       timeout = setTimeout(step, this.interval);
//   }

//   this.stop = function() {
//       clearTimeout(timeout);
//   }

//   function step() {
//       var drift = Date.now() - expected;
//       if (drift > that.interval) {
//           // You could have some default stuff here too...
//           if (errorFunc) errorFunc();
//       }
//       workFunc();
//       expected += that.interval;
//       timeout = setTimeout(step, Math.max(0, that.interval-drift));
//   }
// }

// // For testing purposes, we'll just increment
// // this and send it out to the console.
// var justSomeNumber = 0;

// // Define the work to be done
// var doWork = function() {
//     console.log(++justSomeNumber);
// };

// // Define what to do if something goes wrong
// var doError = function() {
//     console.warn('The drift exceeded the interval.');
// };

// // (The third argument is optional)
// var ticker = new AdjustingInterval(doWork, 1000, doError);


// let start_button = document.querySelector('#start-button') 
// let stop_button = document.querySelector('#stop-button')

// function startFunction() {
//   console.log("started");
//   // ticker.start();
// }

// function stopFunction() {
//   console.log("ended");
//   // ticker.stop(); 
// }

// start_button.addEventListener("click", startFunction);
// stop_button.addEventListener("click", stopFunction);
