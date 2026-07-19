export async function sendMessage(message) {
  try {
    const res = await fetch("https://dynamicore.onrender.com/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer e22efa84-543b-459d-82d0-0f0147762451"
      },
      body: JSON.stringify({
        message,
        model: "gpt-4-turbo"
      })
    });

    const data = await res.json();

    return data;
  } catch (err) {
    return { response: "Error de conexión: " + err.message };
  }
}
