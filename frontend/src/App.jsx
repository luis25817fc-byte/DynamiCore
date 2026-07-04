export async function sendMessage(message) {
  try {
    const controller = new AbortController();

    // timeout de seguridad (15s)
    const timeout = setTimeout(() => {
      controller.abort();
    }, 15000);

    const res = await fetch("https://dynamicore-api.onrender.com/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer 9e4ed968-02fe-4027-ad91-dba303cbe437"
      },
      signal: controller.signal,
      body: JSON.stringify({
        message: message,
        model: "gpt-4-turbo"
      })
    });

    clearTimeout(timeout);

    if (!res.ok) {
      const errorText = await res.text();
      throw new Error(`API Error: ${res.status} - ${errorText}`);
    }

    const data = await res.json();

    return {
      success: true,
      data
    };

  } catch (error) {
    return {
      success: false,
      error: error.message || "Error desconocido en DynamiCore API"
    };
  }
}
