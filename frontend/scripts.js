async function register() {
    const user = document.getElementById('registerUser').value;
    const response = await fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user })
    });
    const result = await response.json();
    alert(result.message);
}

async function submitKnowledge() {
    const user = document.getElementById('knowledgeUser').value;
    const knowledge = document.getElementById('knowledgeText').value;
    const proof = document.getElementById('knowledgeProof').value;
    const response = await fetch('/submit_knowledge', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user, knowledge, proof })
    });
    const result = await response.json();
    alert(result.message);
}

async function viewBalance() {
    const user = document.getElementById('balanceUser').value;
    const response = await fetch(`/balance?user=${user}`);
    const result = await response.json();
    document.getElementById('balanceResult').innerText = `Balance: ${result.balance}`;
}
