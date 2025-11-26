// Refactored JS: move calculation into a function and use concise arrow notation
const calculateSales = (price, quantity) => price * quantity;

let totalSales = 0;

totalSales += calculateSales(3, 100); // apples
totalSales += calculateSales(5, 50);  // oranges

console.log(`Total: ${totalSales}`);
