fetch("/menu")
    .then(response => response.json())
    .then(data => {
        const foodDiv = document.getElementById("food");
        foodDiv.innerHTML = "";

        data.forEach(item => {
            foodDiv.innerHTML += `
                <div class="card">
                    <img src="/static/${item.image}" alt="${item.name}">
                    <h3>${item.name}</h3>
                    <p>₹${item.price}</p>
                    <button onclick="orderFood('${item.name}')">Order Now</button>
                </div>
            `;
        });
    })
    .catch(err => console.error("Menu load error:", err));

function orderFood(item) {
    fetch(`/order/${item}`, { method: "POST" })
        .then(res => res.json())
        .then(data => alert(data.message))
        .catch(err => console.error("Order error:", err));
}
