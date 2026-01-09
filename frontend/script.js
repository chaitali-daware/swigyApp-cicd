fetch("http://localhost:5000/menu")
    .then(response => response.json())
    .then(data => {
        const foodDiv = document.getElementById("food");

        data.forEach(item => {
            foodDiv.innerHTML += `
                <div class="card">
                    <img src="${item.image}" alt="${item.name}">
                    <h3>${item.name}</h3>
                    <p>₹${item.price}</p>
                    <button onclick="orderFood('${item.name}')">Order Now</button>
                </div>
            `;
        });
    });

function orderFood(item) {
    fetch(`http://localhost:5000/order/${item}`, {
        method: "POST"
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}
