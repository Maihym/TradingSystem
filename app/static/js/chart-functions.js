//chart-functions.js
console.log("Page loaded and script running.");
// Initialize the chart with a default ticker
//let chart = initializeChart('DefaultTicker');  // Implement initializeChart function
let allTickers = [];

window.onload = function() {
    console.log("Fetching all tickers...");
    fetch('/get_all_tickers')  // Make sure this route exists in your Flask app
        .then(response => response.json())
        .then(data => {
            allTickers = data;
            console.log("Tickers fetched:", data);
        })
        .catch(error => console.error("Error fetching tickers:", error));
};