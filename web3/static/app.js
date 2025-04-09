document.getElementById("generate").addEventListener("click", async () => {
    document.getElementById("result").classList.add("hidden");
    document.getElementById("loading").classList.remove("hidden");

    try {
        const res = await fetch("/generate");
        const data = await res.json();

        document.getElementById("privateKey").textContent = data.private_key;

        const list = document.getElementById("addressList");
        list.innerHTML = "";
        for (const [coin, address] of Object.entries(data.addresses)) {
            const li = document.createElement("li");
            li.innerHTML = `<button onclick="copyTextFrom('${address}')">📋</button> <strong>${coin}:</strong> ${address}`;
            list.appendChild(li);
        }

        document.getElementById("loading").classList.add("hidden");
        document.getElementById("result").classList.remove("hidden");
        renderDonationCards();
    } catch (e) {
        console.error("Error:", e);
    }
});

function copyTextFrom(text) {
    navigator.clipboard.writeText(text);
    showCopiedToast("¡Copiado!");
}

function renderDonationCards() {
    const cards = {
        "Bitcoin": "17jrtsZ245v7M5f8Vv6ZdR3NowasZ9hELv",
        "Litecoin": "LRxpA5rr8kAAbtMHg45ruS7929x9gsnEsv",
        "Dogecoin": "DBsxS8VfMVpPt5qjEW68BBCyh5KAsCNYec",
        "BitcoinCash": "17jrtsZ245v7M5f8Vv6ZdR3NowasZ9hELv",
        "Dash": "XhRhj8Cv1o8hW2FiMoQnUwjAeHAZfvCAdp",
        "Clams": "xF3VnkPVKoQ9PTkzrPjE4bLA33t718KGLG",
        "Zcash": "t1QcTuCyA2Qhhwii2SLugmE9J4bmxMxwMZN",
        "Ethereum": "0xf2462aff5a801ed1c2d8da2c93a0ac81658e6252",
        "BNB": "0xf2462aff5a801ed1c2d8da2c93a0ac81658e6252"
    };

    const container = document.getElementById("donations");
    container.innerHTML = "";

    for (let [name, address] of Object.entries(cards)) {
        const div = document.createElement("div");
        div.className = "addr";
        div.innerHTML = `
            <button class="copy-btn" onclick="copyToClipboard('${address}')">📋</button>
            <strong>${name}</strong>: <code>${address}</code>
        `;
        container.appendChild(div);
    }
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text);
    showCopiedToast("Copiado al portapapeles");
}

function showCopiedToast(msg) {
    const toast = document.createElement("div");
    toast.textContent = msg;
    toast.style.position = "fixed";
    toast.style.bottom = "20px";
    toast.style.right = "20px";
    toast.style.background = "#33ff33";
    toast.style.color = "#000";
    toast.style.padding = "10px 15px";
    toast.style.borderRadius = "5px";
    toast.style.boxShadow = "0 0 10px #33ff33";
    toast.style.zIndex = "9999";
    toast.style.opacity = "0.95";
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 2000);
}

async function generateWallet() {
    const res = await fetch("/generate");
    const text = await res.text();
    renderFormattedOutput(text);
    document.getElementById("donations").classList.remove("hidden");
    renderDonationCards();
}

async function fromExistingKey() {
    const key = document.getElementById("existingKey").value.trim();
    const res = await fetch("/from_key", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ key })
    });
    const text = await res.text();
    renderFormattedOutput(text);
    document.getElementById("donations").classList.remove("hidden");
    renderDonationCards();
}

function renderFormattedOutput(jsonText) {
    const data = JSON.parse(jsonText);
    const outputDiv = document.getElementById("output");
    outputDiv.innerHTML = `<h2>🔐 Direcciones Generadas</h2><div class="wallet-grid"></div>`;

    const grid = outputDiv.querySelector(".wallet-grid");

    for (let [name, address] of Object.entries(data.addresses)) {
        const div = document.createElement("div");
        div.className = "wallet-card";
        div.innerHTML = `
            <button class="copy-btn" onclick="copyToClipboard('${address}')">📋</button>
            <strong>${name}</strong>: <code>${address}</code>
        `;
        grid.appendChild(div);
    }

    outputDiv.innerHTML += `
        <h2>🗝 Clave Privada</h2>
        <div class="private-key">
            <code>${data.private_key}</code>
            <button class="copy-btn" onclick="copyToClipboard('${data.private_key}')">📋 Copiar</button>
        </div>
    `;
}
