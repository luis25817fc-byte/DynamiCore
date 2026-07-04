async function sendMessage(message) {
  const res = await fetch("https://dynamicore-api.onrender.com/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer 9e4ed968-02fe-4027-ad91-dba303cbe437"
    },
    body: JSON.stringify({
      message: message,
      model: "gpt-4-turbo"
    })
  });

  return await res.json();
}
