let root = document.documentElement;
let color = document.getElementsById("quad").getAttribute("data-value")
root.style.setProperty('--color', color);